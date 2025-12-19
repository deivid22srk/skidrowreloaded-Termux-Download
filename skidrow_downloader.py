#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import asyncio
from pathlib import Path
from typing import List, Dict, Optional

from textual.app import App, ComposeResult
from textual.containers import Container, Vertical, Horizontal, ScrollableContainer
from textual.widgets import Header, Footer, Input, Button, Static, Label, ListView, ListItem, DirectoryTree
from textual.binding import Binding
from textual.reactive import reactive
from textual.screen import Screen
from textual import events

import requests
from bs4 import BeautifulSoup
import re
import subprocess


class GameItem(ListItem):
    def __init__(self, title: str, url: str, date: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game_title = title
        self.game_url = url
        self.game_date = date


class SearchScreen(Screen):
    CSS = """
    SearchScreen {
        background: $surface;
        align: center middle;
    }
    
    #search_container {
        width: 90%;
        height: auto;
        background: $panel;
        border: heavy $primary;
        padding: 2;
    }
    
    #title {
        text-align: center;
        color: $accent;
        text-style: bold;
        margin-bottom: 1;
    }
    
    #subtitle {
        text-align: center;
        color: $text-muted;
        margin-bottom: 2;
    }
    
    Input {
        margin: 1 0;
        border: solid $primary;
    }
    
    Button {
        width: 100%;
        margin-top: 1;
    }
    
    #status {
        text-align: center;
        color: $warning;
        margin-top: 1;
        height: 3;
    }
    """
    
    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="search_container"):
            yield Static("🎮 SKIDROW GAME DOWNLOADER", id="title")
            yield Static("Busque seus jogos favoritos", id="subtitle")
            yield Input(placeholder="Digite o nome do jogo...", id="search_input")
            yield Button("🔍 BUSCAR", variant="primary", id="search_btn")
            yield Static("", id="status")
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "search_btn":
            self.search_game()
    
    def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.input.id == "search_input":
            self.search_game()
    
    def search_game(self) -> None:
        input_widget = self.query_one("#search_input", Input)
        query = input_widget.value.strip()
        
        if not query:
            self.query_one("#status", Static).update("⚠️  Digite o nome de um jogo!")
            return
        
        self.query_one("#status", Static).update("🔄 Buscando...")
        self.app.search_query = query
        self.app.push_screen("results")


class ResultsScreen(Screen):
    CSS = """
    ResultsScreen {
        background: $surface;
    }
    
    #results_header {
        height: 5;
        background: $panel;
        border-bottom: heavy $primary;
        padding: 1 2;
    }
    
    #results_title {
        color: $accent;
        text-style: bold;
    }
    
    #results_count {
        color: $text-muted;
        margin-top: 1;
    }
    
    ListView {
        height: 1fr;
        border: solid $primary;
        margin: 1;
    }
    
    ListItem {
        padding: 1 2;
        height: auto;
    }
    
    ListItem:hover {
        background: $primary 20%;
    }
    
    .game-title {
        color: $accent;
        text-style: bold;
    }
    
    .game-date {
        color: $text-muted;
    }
    
    #loading {
        text-align: center;
        color: $warning;
        margin: 2;
    }
    
    #error {
        text-align: center;
        color: $error;
        margin: 2;
    }
    
    #buttons {
        height: auto;
        dock: bottom;
        background: $panel;
        border-top: heavy $primary;
        padding: 1;
    }
    
    Button {
        width: 1fr;
        margin: 0 1;
    }
    """
    
    BINDINGS = [
        Binding("escape", "back", "Voltar"),
        Binding("enter", "select", "Selecionar"),
    ]
    
    results: reactive[List[Dict]] = reactive([], recompose=True)
    
    def compose(self) -> ComposeResult:
        yield Header()
        
        with Container(id="results_header"):
            yield Static("📋 Resultados da Busca", id="results_title")
            yield Static("", id="results_count")
        
        if not hasattr(self, '_loaded'):
            yield Static("🔄 Carregando resultados...", id="loading")
        elif len(self.results) == 0:
            yield Static("❌ Nenhum resultado encontrado", id="error")
        else:
            with ScrollableContainer():
                yield ListView(
                    *[
                        ListItem(
                            Static(f"🎮 {r['title']}", classes="game-title"),
                            Static(f"📅 {r['date']}", classes="game-date"),
                        )
                        for r in self.results
                    ],
                    id="results_list"
                )
        
        with Horizontal(id="buttons"):
            yield Button("⬅️  VOLTAR", variant="default", id="back_btn")
        
        yield Footer()
    
    async def on_mount(self) -> None:
        self._loaded = False
        await self.load_results()
    
    async def load_results(self) -> None:
        try:
            query = self.app.search_query
            results = await asyncio.to_thread(self.scrape_skidrow, query)
            self.results = results
            self._loaded = True
            
            count_widget = self.query_one("#results_count", Static)
            count_widget.update(f"Encontrados: {len(results)} jogos")
            
            self.refresh(recompose=True)
            
        except Exception as e:
            self._loaded = True
            self.results = []
            self.refresh(recompose=True)
    
    def scrape_skidrow(self, query: str) -> List[Dict]:
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
            
            for article in articles[:15]:
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
            return []
    
    def on_list_view_selected(self, event: ListView.Selected) -> None:
        if event.list_view.id == "results_list":
            index = event.list_view.index
            if 0 <= index < len(self.results):
                selected = self.results[index]
                self.app.selected_game = selected
                self.app.push_screen("details")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back_btn":
            self.action_back()
    
    def action_back(self) -> None:
        self.app.pop_screen()
    
    def action_select(self) -> None:
        list_view = self.query_one("#results_list", ListView)
        if list_view.index is not None:
            index = list_view.index
            if 0 <= index < len(self.results):
                selected = self.results[index]
                self.app.selected_game = selected
                self.app.push_screen("details")


class DetailsScreen(Screen):
    CSS = """
    DetailsScreen {
        background: $surface;
    }
    
    #details_container {
        height: 1fr;
        background: $panel;
        border: heavy $primary;
        margin: 1;
        padding: 2;
    }
    
    .detail-title {
        color: $accent;
        text-style: bold;
        text-align: center;
        margin-bottom: 2;
    }
    
    .detail-label {
        color: $text;
        margin-top: 1;
    }
    
    .detail-info {
        color: $warning;
        margin-bottom: 1;
    }
    
    #loading {
        text-align: center;
        color: $warning;
        margin: 2;
    }
    
    #buttons {
        height: auto;
        dock: bottom;
        background: $panel;
        border-top: heavy $primary;
        padding: 1;
    }
    
    Button {
        width: 1fr;
        margin: 0 1;
    }
    """
    
    BINDINGS = [
        Binding("escape", "back", "Voltar"),
    ]
    
    torrent_links: List[str] = []
    magnet_links: List[str] = []
    
    def compose(self) -> ComposeResult:
        yield Header()
        
        with ScrollableContainer(id="details_container"):
            game = self.app.selected_game
            yield Static(f"🎮 {game['title']}", classes="detail-title")
            yield Static(f"📅 Data: {game['date']}", classes="detail-label")
            yield Static(f"🔗 URL: {game['url']}", classes="detail-label")
            yield Static("", id="loading")
        
        with Horizontal(id="buttons"):
            yield Button("⬅️  VOLTAR", variant="default", id="back_btn")
            yield Button("💾 BAIXAR", variant="success", id="download_btn", disabled=True)
        
        yield Footer()
    
    async def on_mount(self) -> None:
        await self.load_details()
    
    async def load_details(self) -> None:
        loading = self.query_one("#loading", Static)
        loading.update("🔄 Buscando links de download...")
        
        try:
            game = self.app.selected_game
            links = await asyncio.to_thread(self.scrape_download_links, game['url'])
            
            self.torrent_links = links['torrent']
            self.magnet_links = links['magnet']
            
            if self.torrent_links or self.magnet_links:
                info_text = f"\n\n✅ Links encontrados:\n"
                info_text += f"🧲 Torrents: {len(self.torrent_links)}\n"
                info_text += f"🔗 Magnets: {len(self.magnet_links)}"
                loading.update(info_text)
                
                download_btn = self.query_one("#download_btn", Button)
                download_btn.disabled = False
            else:
                loading.update("\n\n❌ Nenhum link de download encontrado")
                
        except Exception as e:
            loading.update(f"\n\n❌ Erro ao buscar links: {str(e)}")
    
    def scrape_download_links(self, url: str) -> Dict[str, List[str]]:
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
            return {'torrent': [], 'magnet': []}
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back_btn":
            self.action_back()
        elif event.button.id == "download_btn":
            self.app.download_links = {
                'torrent': self.torrent_links,
                'magnet': self.magnet_links
            }
            self.app.push_screen("download")
    
    def action_back(self) -> None:
        self.app.pop_screen()


class DownloadScreen(Screen):
    CSS = """
    DownloadScreen {
        background: $surface;
    }
    
    #download_container {
        width: 90%;
        height: auto;
        background: $panel;
        border: heavy $primary;
        padding: 2;
        margin: 2;
        align: center middle;
    }
    
    .section-title {
        color: $accent;
        text-style: bold;
        margin-top: 2;
        margin-bottom: 1;
    }
    
    Input {
        width: 100%;
        margin: 1 0;
    }
    
    #link_container {
        height: auto;
        border: solid $primary;
        padding: 1;
        margin: 1 0;
    }
    
    .link-item {
        color: $text;
        margin: 0 0 1 0;
    }
    
    #buttons {
        height: auto;
        margin-top: 2;
    }
    
    Button {
        width: 1fr;
        margin: 0 1;
    }
    
    #status {
        text-align: center;
        color: $warning;
        margin-top: 1;
        height: auto;
    }
    """
    
    BINDINGS = [
        Binding("escape", "back", "Voltar"),
    ]
    
    def compose(self) -> ComposeResult:
        yield Header()
        
        with ScrollableContainer():
            with Container(id="download_container"):
                yield Static("💾 Configurar Download", classes="section-title")
                
                yield Static("📁 Caminho de Download:", classes="section-title")
                default_path = str(Path.home() / "storage" / "downloads")
                yield Input(
                    value=default_path,
                    placeholder="Caminho onde será salvo o download",
                    id="path_input"
                )
                
                links = self.app.download_links
                
                if links['torrent']:
                    yield Static(f"🧲 Links Torrent ({len(links['torrent'])})", classes="section-title")
                    with Container(id="link_container"):
                        for i, link in enumerate(links['torrent'][:5], 1):
                            short_link = link[:60] + "..." if len(link) > 60 else link
                            yield Static(f"{i}. {short_link}", classes="link-item")
                
                if links['magnet']:
                    yield Static(f"🔗 Links Magnet ({len(links['magnet'])})", classes="section-title")
                    with Container(id="link_container"):
                        for i, link in enumerate(links['magnet'][:5], 1):
                            short_link = link[:60] + "..." if len(link) > 60 else link
                            yield Static(f"{i}. {short_link}", classes="link-item")
                
                with Horizontal(id="buttons"):
                    yield Button("⬅️  VOLTAR", variant="default", id="back_btn")
                    yield Button("⬇️  INICIAR DOWNLOAD", variant="success", id="start_btn")
                
                yield Static("", id="status")
        
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back_btn":
            self.action_back()
        elif event.button.id == "start_btn":
            self.start_download()
    
    def action_back(self) -> None:
        self.app.pop_screen()
    
    def start_download(self) -> None:
        path_input = self.query_one("#path_input", Input)
        download_path = path_input.value.strip()
        
        if not download_path:
            self.query_one("#status", Static).update("⚠️  Digite um caminho válido!")
            return
        
        path_obj = Path(download_path)
        try:
            path_obj.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            self.query_one("#status", Static).update(f"❌ Erro ao criar diretório: {str(e)}")
            return
        
        links = self.app.download_links
        
        if links['torrent']:
            link = links['torrent'][0]
        elif links['magnet']:
            link = links['magnet'][0]
        else:
            self.query_one("#status", Static).update("❌ Nenhum link disponível!")
            return
        
        status = self.query_one("#status", Static)
        
        try:
            if link.startswith('magnet:'):
                if self.check_transmission():
                    cmd = f"transmission-remote -a '{link}' -w '{download_path}'"
                    subprocess.Popen(cmd, shell=True)
                    status.update(f"✅ Download iniciado com transmission!\n📁 Local: {download_path}\n\nUse 'transmission-remote -l' para ver o progresso")
                else:
                    with open(path_obj / "magnet_link.txt", "w") as f:
                        f.write(link)
                    status.update(f"✅ Link magnet salvo em:\n{path_obj / 'magnet_link.txt'}\n\nInstale transmission-cli para baixar automaticamente")
            else:
                if self.check_transmission():
                    torrent_file = path_obj / "download.torrent"
                    response = requests.get(link, timeout=30)
                    with open(torrent_file, 'wb') as f:
                        f.write(response.content)
                    
                    cmd = f"transmission-remote -a '{torrent_file}' -w '{download_path}'"
                    subprocess.Popen(cmd, shell=True)
                    status.update(f"✅ Download iniciado com transmission!\n📁 Local: {download_path}\n\nUse 'transmission-remote -l' para ver o progresso")
                else:
                    torrent_file = path_obj / "download.torrent"
                    response = requests.get(link, timeout=30)
                    with open(torrent_file, 'wb') as f:
                        f.write(response.content)
                    status.update(f"✅ Arquivo torrent salvo em:\n{torrent_file}\n\nInstale transmission-cli para baixar automaticamente")
                    
        except Exception as e:
            status.update(f"❌ Erro: {str(e)}")
    
    def check_transmission(self) -> bool:
        try:
            subprocess.run(['transmission-remote', '--version'], 
                         capture_output=True, check=True)
            return True
        except:
            return False


class SkidrowDownloaderApp(App):
    CSS = """
    Screen {
        background: $surface;
    }
    """
    
    TITLE = "Skidrow Game Downloader"
    BINDINGS = [
        Binding("q", "quit", "Sair"),
    ]
    
    search_query: str = ""
    selected_game: Dict = {}
    download_links: Dict = {}
    
    def on_mount(self) -> None:
        self.install_screen(SearchScreen(), name="search")
        self.install_screen(ResultsScreen(), name="results")
        self.install_screen(DetailsScreen(), name="details")
        self.install_screen(DownloadScreen(), name="download")
        self.push_screen("search")
    
    def action_quit(self) -> None:
        self.exit()


if __name__ == "__main__":
    app = SkidrowDownloaderApp()
    app.run()
