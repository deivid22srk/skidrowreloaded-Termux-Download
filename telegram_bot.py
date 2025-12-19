#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import asyncio
import subprocess
from pathlib import Path
from typing import List, Dict

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

import requests
from bs4 import BeautifulSoup


# Token do bot
BOT_TOKEN = "7718948467:AAGhVsQyiJFsht4f8Kc4YJd6ReA9BTN5v_o"

# Armazenamento temporário de dados do usuário
user_data_storage = {}


def search_games(query: str) -> List[Dict]:
    """Busca jogos no Skidrow Reloaded"""
    search_url = f"https://www.skidrowreloaded.com/?s={query.replace(' ', '+')}"
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(search_url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        
        articles = soup.find_all('article', class_='post')
        
        for article in articles[:10]:
            title_elem = article.find('h2')
            if title_elem and title_elem.find('a'):
                title = title_elem.get_text(strip=True)
                url = title_elem.find('a')['href']
                
                date_elem = article.find('time')
                date = date_elem.get_text(strip=True) if date_elem else "Data desconhecida"
                
                results.append({
                    'title': title,
                    'url': url,
                    'date': date
                })
        
        return results
        
    except Exception as e:
        print(f"Erro ao buscar: {str(e)}")
        return []


def get_download_links(url: str) -> Dict[str, List[str]]:
    """Extrai links de download da página do jogo"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        torrent_links = []
        magnet_links = []
        
        for link in soup.find_all('a', href=True):
            href = link['href']
            if '.torrent' in href.lower():
                torrent_links.append(href)
            elif href.startswith('magnet:'):
                magnet_links.append(href)
        
        return {
            'torrent': torrent_links,
            'magnet': magnet_links
        }
        
    except Exception as e:
        print(f"Erro ao buscar links: {str(e)}")
        return {'torrent': [], 'magnet': []}


def check_transmission() -> bool:
    """Verifica se transmission está instalado"""
    try:
        subprocess.run(['transmission-remote', '--version'], 
                     capture_output=True, check=True)
        return True
    except:
        return False


def download_with_transmission(link: str, download_path: str) -> tuple[bool, str]:
    """Inicia download usando transmission"""
    try:
        Path(download_path).mkdir(parents=True, exist_ok=True)
        
        if link.startswith('magnet:'):
            cmd = f"transmission-remote -a '{link}' -w '{download_path}'"
            subprocess.Popen(cmd, shell=True)
            return True, f"✅ Download iniciado!\n📁 Local: {download_path}"
        else:
            torrent_file = Path(download_path) / "download.torrent"
            response = requests.get(link, timeout=30)
            with open(torrent_file, 'wb') as f:
                f.write(response.content)
            
            cmd = f"transmission-remote -a '{torrent_file}' -w '{download_path}'"
            subprocess.Popen(cmd, shell=True)
            return True, f"✅ Download iniciado!\n📁 Local: {download_path}"
        
    except Exception as e:
        return False, f"❌ Erro: {str(e)}"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start"""
    welcome_text = """
🎮 <b>BEM-VINDO AO SKIDROW DOWNLOADER BOT!</b>

Busque e baixe jogos do Skidrow Reloaded diretamente no Telegram!

<b>📋 Comandos disponíveis:</b>

/buscar &lt;nome do jogo&gt; - Buscar jogos
/caminho &lt;caminho&gt; - Definir caminho de download
/caminho_ver - Ver caminho atual
/ajuda - Mostrar ajuda
/sobre - Sobre o bot

<b>🎯 Exemplo:</b>
/buscar GTA V

<b>📁 Caminho padrão:</b>
/data/data/com.termux/files/home/storage/downloads

⚠️ <b>Importante:</b> Use apenas para fins legais!
"""
    
    await update.message.reply_text(
        welcome_text,
        parse_mode='HTML'
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /ajuda"""
    help_text = """
📖 <b>AJUDA - COMO USAR</b>

<b>1️⃣ Buscar Jogos:</b>
/buscar &lt;nome do jogo&gt;

Exemplo: /buscar GTA V

<b>2️⃣ Definir Caminho:</b>
/caminho /seu/caminho/aqui

Exemplo: /caminho /storage/emulated/0/Download

<b>3️⃣ Ver Caminho Atual:</b>
/caminho_ver

<b>4️⃣ Fluxo Completo:</b>

1. Defina o caminho (opcional)
2. Busque um jogo com /buscar
3. Clique no jogo desejado
4. Escolha o link de download
5. Confirme o download

<b>🔧 Comandos do Transmission:</b>
(No Termux)

• transmission-remote -l - Ver downloads
• transmission-remote -t 1 -S - Pausar
• transmission-remote -t 1 -s - Retomar

⚠️ <b>Nota:</b> Certifique-se que o Transmission está instalado no Termux!
"""
    
    await update.message.reply_text(
        help_text,
        parse_mode='HTML'
    )


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /sobre"""
    about_text = """
ℹ️ <b>SOBRE O BOT</b>

<b>Nome:</b> Skidrow Downloader Bot
<b>Versão:</b> 1.0.0
<b>Desenvolvido para:</b> Termux + Telegram

<b>Funcionalidades:</b>
✅ Busca de jogos no Skidrow Reloaded
✅ Listagem interativa com botões
✅ Download via Transmission
✅ Configuração de caminho
✅ Interface completa no Telegram

<b>Tecnologias:</b>
• Python 3.10+
• python-telegram-bot
• BeautifulSoup4
• Requests
• Transmission

⚠️ <b>Aviso Legal:</b>
Este bot é apenas para fins educacionais.
Use apenas para jogos que você possui legalmente.

<b>📞 Suporte:</b>
Reddit: r/termux
GitHub: termux/termux-app
"""
    
    await update.message.reply_text(
        about_text,
        parse_mode='HTML'
    )


async def set_path(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /caminho"""
    user_id = update.effective_user.id
    
    if not context.args:
        await update.message.reply_text(
            "❌ Uso correto: /caminho /seu/caminho\n\n"
            "Exemplo: /caminho /storage/emulated/0/Download"
        )
        return
    
    path = ' '.join(context.args)
    
    # Validar caminho
    try:
        path_obj = Path(path)
        if not path_obj.is_absolute():
            await update.message.reply_text("❌ Use um caminho absoluto (começando com /)")
            return
    except Exception as e:
        await update.message.reply_text(f"❌ Caminho inválido: {str(e)}")
        return
    
    # Salvar caminho
    if user_id not in user_data_storage:
        user_data_storage[user_id] = {}
    
    user_data_storage[user_id]['download_path'] = path
    
    await update.message.reply_text(
        f"✅ Caminho definido!\n\n📁 {path}\n\n"
        f"Agora você pode buscar jogos com /buscar &lt;nome&gt;",
        parse_mode='HTML'
    )


async def view_path(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /caminho_ver"""
    user_id = update.effective_user.id
    
    default_path = "/data/data/com.termux/files/home/storage/downloads"
    current_path = user_data_storage.get(user_id, {}).get('download_path', default_path)
    
    await update.message.reply_text(
        f"📁 <b>Caminho Atual:</b>\n\n{current_path}\n\n"
        f"Para mudar, use: /caminho /novo/caminho",
        parse_mode='HTML'
    )


async def search_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /buscar"""
    user_id = update.effective_user.id
    
    if not context.args:
        await update.message.reply_text(
            "❌ Uso correto: /buscar &lt;nome do jogo&gt;\n\n"
            "Exemplo: /buscar GTA V",
            parse_mode='HTML'
        )
        return
    
    query = ' '.join(context.args)
    
    # Enviar mensagem de busca
    search_msg = await update.message.reply_text(
        f"🔍 Buscando por: <b>{query}</b>\n\n"
        f"⏳ Aguarde...",
        parse_mode='HTML'
    )
    
    # Buscar jogos
    results = search_games(query)
    
    if not results:
        await search_msg.edit_text("❌ Nenhum resultado encontrado!\n\nTente outro nome.")
        return
    
    # Salvar resultados
    if user_id not in user_data_storage:
        user_data_storage[user_id] = {}
    
    user_data_storage[user_id]['search_results'] = results
    
    # Criar botões
    keyboard = []
    for i, game in enumerate(results):
        # Truncar título se muito longo
        title = game['title']
        if len(title) > 60:
            title = title[:57] + "..."
        
        keyboard.append([
            InlineKeyboardButton(
                f"🎮 {title}",
                callback_data=f"game_{i}"
            )
        ])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await search_msg.edit_text(
        f"📋 <b>Resultados da Busca</b>\n\n"
        f"Encontrados: <b>{len(results)} jogos</b>\n\n"
        f"Selecione um jogo:",
        parse_mode='HTML',
        reply_markup=reply_markup
    )


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Callback para botões inline"""
    query = update.callback_query
    user_id = update.effective_user.id
    
    await query.answer()
    
    data = query.data
    
    # Seleção de jogo
    if data.startswith('game_'):
        game_idx = int(data.split('_')[1])
        
        user_games = user_data_storage.get(user_id, {}).get('search_results', [])
        
        if game_idx >= len(user_games):
            await query.edit_message_text("❌ Jogo não encontrado!")
            return
        
        selected_game = user_games[game_idx]
        
        # Salvar jogo selecionado
        user_data_storage[user_id]['selected_game'] = selected_game
        
        # Buscar links
        await query.edit_message_text(
            f"🎮 <b>{selected_game['title']}</b>\n\n"
            f"📅 {selected_game['date']}\n\n"
            f"🔗 {selected_game['url']}\n\n"
            f"🔄 Buscando links de download...",
            parse_mode='HTML'
        )
        
        links = get_download_links(selected_game['url'])
        
        if not links['torrent'] and not links['magnet']:
            await query.edit_message_text(
                f"🎮 <b>{selected_game['title']}</b>\n\n"
                f"❌ Nenhum link de download encontrado!",
                parse_mode='HTML'
            )
            return
        
        # Salvar links
        user_data_storage[user_id]['download_links'] = links
        
        # Criar botões de links
        keyboard = []
        all_links = []
        
        for i, link in enumerate(links['torrent'][:5]):
            short_link = link[:40] + "..." if len(link) > 40 else link
            keyboard.append([
                InlineKeyboardButton(
                    f"🧲 Torrent {i+1}",
                    callback_data=f"link_{len(all_links)}"
                )
            ])
            all_links.append(link)
        
        for i, link in enumerate(links['magnet'][:5]):
            keyboard.append([
                InlineKeyboardButton(
                    f"🔗 Magnet {i+1}",
                    callback_data=f"link_{len(all_links)}"
                )
            ])
            all_links.append(link)
        
        user_data_storage[user_id]['all_links'] = all_links
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            f"🎮 <b>{selected_game['title']}</b>\n\n"
            f"📅 {selected_game['date']}\n\n"
            f"✅ Links encontrados:\n"
            f"🧲 Torrents: {len(links['torrent'])}\n"
            f"🔗 Magnets: {len(links['magnet'])}\n\n"
            f"Selecione um link:",
            parse_mode='HTML',
            reply_markup=reply_markup
        )
    
    # Seleção de link
    elif data.startswith('link_'):
        link_idx = int(data.split('_')[1])
        
        all_links = user_data_storage.get(user_id, {}).get('all_links', [])
        
        if link_idx >= len(all_links):
            await query.edit_message_text("❌ Link não encontrado!")
            return
        
        selected_link = all_links[link_idx]
        user_data_storage[user_id]['selected_link'] = selected_link
        
        # Confirmar download
        keyboard = [
            [
                InlineKeyboardButton("✅ CONFIRMAR DOWNLOAD", callback_data="confirm_download"),
                InlineKeyboardButton("❌ CANCELAR", callback_data="cancel_download")
            ]
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        default_path = "/data/data/com.termux/files/home/storage/downloads"
        current_path = user_data_storage.get(user_id, {}).get('download_path', default_path)
        
        link_type = "Magnet" if selected_link.startswith('magnet:') else "Torrent"
        link_preview = selected_link[:80] + "..." if len(selected_link) > 80 else selected_link
        
        await query.edit_message_text(
            f"💾 <b>CONFIRMAR DOWNLOAD</b>\n\n"
            f"🔗 Tipo: {link_type}\n"
            f"📁 Caminho: {current_path}\n\n"
            f"Link: {link_preview}\n\n"
            f"⚠️ O download será iniciado no Termux via Transmission.\n\n"
            f"Deseja continuar?",
            parse_mode='HTML',
            reply_markup=reply_markup
        )
    
    # Confirmar download
    elif data == 'confirm_download':
        selected_link = user_data_storage.get(user_id, {}).get('selected_link')
        
        if not selected_link:
            await query.edit_message_text("❌ Nenhum link selecionado!")
            return
        
        default_path = "/data/data/com.termux/files/home/storage/downloads"
        download_path = user_data_storage.get(user_id, {}).get('download_path', default_path)
        
        # Verificar transmission
        if not check_transmission():
            await query.edit_message_text(
                "❌ <b>Transmission não está instalado!</b>\n\n"
                "Instale no Termux:\n"
                "pkg install transmission\n\n"
                "Depois inicie o daemon:\n"
                "transmission-daemon",
                parse_mode='HTML'
            )
            return
        
        # Iniciar download
        await query.edit_message_text(
            "⏳ Iniciando download..."
        )
        
        success, message = download_with_transmission(selected_link, download_path)
        
        if success:
            game_title = user_data_storage.get(user_id, {}).get('selected_game', {}).get('title', 'Jogo')
            
            await query.edit_message_text(
                f"🎮 <b>{game_title}</b>\n\n"
                f"{message}\n\n"
                f"📊 <b>Ver progresso no Termux:</b>\n"
                f"transmission-remote -l\n\n"
                f"⏸️ <b>Pausar:</b>\n"
                f"transmission-remote -t 1 -S\n\n"
                f"▶️ <b>Retomar:</b>\n"
                f"transmission-remote -t 1 -s\n\n"
                f"🎉 Buscar outro jogo: /buscar &lt;nome&gt;",
                parse_mode='HTML'
            )
        else:
            await query.edit_message_text(
                f"❌ <b>Erro ao iniciar download</b>\n\n"
                f"{message}",
                parse_mode='HTML'
            )
    
    # Cancelar download
    elif data == 'cancel_download':
        await query.edit_message_text(
            "❌ Download cancelado.\n\n"
            "Busque novamente com /buscar &lt;nome&gt;",
            parse_mode='HTML'
        )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para mensagens de texto simples"""
    text = update.message.text
    
    await update.message.reply_text(
        f"❓ Não entendi '{text}'\n\n"
        f"Use /buscar &lt;nome do jogo&gt; para buscar.\n"
        f"Ou /ajuda para ver todos os comandos.",
        parse_mode='HTML'
    )


def main():
    """Função principal"""
    print("🤖 Iniciando Skidrow Downloader Bot...")
    print(f"📱 Token: {BOT_TOKEN[:20]}...")
    
    # Criar aplicação
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Adicionar handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ajuda", help_command))
    application.add_handler(CommandHandler("sobre", about_command))
    application.add_handler(CommandHandler("caminho", set_path))
    application.add_handler(CommandHandler("caminho_ver", view_path))
    application.add_handler(CommandHandler("buscar", search_command))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    
    # Iniciar bot
    print("✅ Bot iniciado!")
    print("📡 Aguardando mensagens...\n")
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️ Bot interrompido pelo usuário")
    except Exception as e:
        print(f"❌ Erro: {str(e)}")
