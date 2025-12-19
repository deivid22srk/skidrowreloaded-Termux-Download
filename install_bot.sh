#!/bin/bash

echo "🤖 Instalando Skidrow Telegram Bot para Termux..."
echo ""

echo "📦 Atualizando pacotes do Termux..."
pkg update -y && pkg upgrade -y

echo ""
echo "🐍 Instalando Python e ferramentas..."
pkg install python python-pip git -y

echo ""
echo "⚡ Instalando transmission-cli (cliente torrent)..."
pkg install transmission -y

echo ""
echo "📁 Configurando acesso ao armazenamento..."
echo "⚠️  Você precisará conceder permissão quando solicitado!"
termux-setup-storage

echo ""
echo "📚 Instalando dependências Python..."
pip install --upgrade pip
pip install -r requirements_bot.txt

echo ""
echo "🔧 Configurando permissões de execução..."
chmod +x telegram_bot.py

echo ""
echo "🔥 Iniciando daemon do Transmission..."
transmission-daemon

echo ""
echo "✅ Instalação concluída!"
echo ""
echo "🚀 Para iniciar o bot, use:"
echo "   python telegram_bot.py"
echo ""
echo "   ou"
echo ""
echo "   ./telegram_bot.py"
echo ""
echo "⚠️  IMPORTANTE: Mantenha o Termux aberto enquanto o bot estiver rodando!"
echo "💡 DICA: Use 'termux-wake-lock' para evitar que o Termux durma"
echo ""
