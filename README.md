# 🎮 Skidrow Game Downloader para Termux

Aplicativo com interface touch para buscar e baixar jogos do Skidrow Reloaded diretamente no Termux.

## 📋 Características

- 🎨 Interface Touch Bonita (TUI) usando Textual
- 🔍 Busca de jogos no Skidrow Reloaded
- 📋 Lista de resultados navegável
- 💾 Download de arquivos torrent
- 🧲 Suporte a links magnet
- 📁 Escolha do caminho de download
- ⚡ Otimizado para Termux

## 📦 Requisitos

- Android com Termux instalado
- Acesso ao armazenamento do dispositivo
- Conexão com a internet

## 🚀 Instalação

### 1. Atualizar pacotes do Termux

```bash
pkg update && pkg upgrade -y
```

### 2. Instalar Python e dependências do sistema

```bash
pkg install python python-pip git -y
```

### 3. Instalar transmission-cli (opcional, mas recomendado)

```bash
pkg install transmission -y
```

### 4. Configurar acesso ao armazenamento

```bash
termux-setup-storage
```

Quando solicitado, conceda permissão de armazenamento ao Termux.

### 5. Instalar dependências Python

```bash
pip install textual requests beautifulsoup4 lxml
```

### 6. Baixar o aplicativo

Copie o arquivo `skidrow_downloader.py` para o Termux ou clone este repositório:

```bash
git clone <url-do-repositorio>
cd <nome-do-repositorio>
```

### 7. Dar permissão de execução

```bash
chmod +x skidrow_downloader.py
```

## 🎯 Como Usar

### Executar o aplicativo

```bash
python skidrow_downloader.py
```

ou

```bash
./skidrow_downloader.py
```

### Navegação

1. **Tela de Busca**
   - Digite o nome do jogo
   - Pressione "BUSCAR" ou ENTER
   - Use `q` para sair

2. **Tela de Resultados**
   - Use as **setas** ⬆️⬇️ ou **toque** para navegar
   - Pressione **ENTER** ou **toque** para selecionar
   - Pressione **ESC** para voltar

3. **Tela de Detalhes**
   - Aguarde carregar os links de download
   - Pressione "BAIXAR" quando disponível
   - Pressione **ESC** para voltar

4. **Tela de Download**
   - Edite o caminho de download se necessário
   - Padrão: `~/storage/downloads`
   - Pressione "INICIAR DOWNLOAD"

### Atalhos de Teclado

| Tecla | Ação |
|-------|------|
| `q` | Sair do aplicativo |
| `ESC` | Voltar para tela anterior |
| `ENTER` | Confirmar/Selecionar |
| `↑↓` | Navegar na lista |
| `TAB` | Alternar entre campos |

## 📁 Caminhos de Download Recomendados

```bash
# Downloads do Termux (padrão)
~/storage/downloads

# Armazenamento compartilhado
~/storage/shared

# Cartão SD (se disponível)
~/storage/external-1
```

## 🔧 Gerenciar Downloads (Transmission)

### Ver downloads ativos

```bash
transmission-remote -l
```

### Ver status detalhado

```bash
transmission-remote -t <ID> -i
```

### Pausar download

```bash
transmission-remote -t <ID> -S
```

### Retomar download

```bash
transmission-remote -t <ID> -s
```

### Remover download

```bash
transmission-remote -t <ID> -r
```

### Iniciar daemon do transmission

```bash
transmission-daemon
```

### Parar daemon do transmission

```bash
pkill transmission-daemon
```

## 🎨 Personalização

### Mudar tema

Edite o arquivo `skidrow_downloader.py` e modifique as seções CSS:

```python
CSS = """
SearchScreen {
    background: $surface;  # Mude para sua cor preferida
}
"""
```

### Cores disponíveis no Textual

- `$primary` - Cor primária
- `$secondary` - Cor secundária
- `$accent` - Cor de destaque
- `$warning` - Cor de aviso
- `$error` - Cor de erro
- `$success` - Cor de sucesso
- `$surface` - Cor de fundo
- `$panel` - Cor de painel

## 🐛 Solução de Problemas

### Erro: "ModuleNotFoundError: No module named 'textual'"

```bash
pip install --upgrade textual
```

### Erro: "Permission denied"

```bash
chmod +x skidrow_downloader.py
termux-setup-storage
```

### Transmission não inicia downloads

```bash
# Iniciar daemon manualmente
transmission-daemon

# Verificar se está rodando
pgrep transmission

# Ver logs
transmission-remote -l
```

### Interface não aparece corretamente

```bash
# Atualizar Termux
pkg update && pkg upgrade

# Reinstalar Python
pkg reinstall python
```

### Erro ao acessar armazenamento

```bash
# Reconfigurar permissões
termux-setup-storage

# Verificar permissões no Android:
# Configurações > Apps > Termux > Permissões > Armazenamento
```

## 📝 Notas Importantes

⚠️ **Aviso Legal**: Este aplicativo é apenas para fins educacionais. Certifique-se de ter o direito legal de baixar e usar qualquer conteúdo. O autor não se responsabiliza pelo uso indevido desta ferramenta.

- Use uma VPN se necessário
- Verifique as leis de direitos autorais do seu país
- Baixe apenas conteúdo que você possui legalmente

## 🔄 Atualizações

Para atualizar o aplicativo:

```bash
# Se instalou via git
git pull origin main

# Se copiou manualmente, substitua o arquivo
```

## 💡 Dicas

1. **Bateria**: Downloads grandes consomem bateria. Mantenha o dispositivo carregando.

2. **Termux não dormir**: Use `termux-wake-lock` para evitar que o Termux pare em segundo plano:
   ```bash
   termux-wake-lock
   ```

3. **Desativar wake-lock**:
   ```bash
   termux-wake-unlock
   ```

4. **Ver espaço em disco**:
   ```bash
   df -h ~/storage/downloads
   ```

5. **Background**: Para manter o download rodando, use `screen` ou `tmux`:
   ```bash
   pkg install tmux
   tmux new -s downloads
   # Seus comandos aqui
   # Ctrl+B, D para desanexar
   # tmux attach -t downloads para voltar
   ```

## 🌐 Recursos Adicionais

### Clientes Torrent Alternativos

```bash
# rtorrent (avançado)
pkg install rtorrent

# aria2 (leve)
pkg install aria2
```

### Usando aria2 para baixar

```bash
aria2c --seed-time=0 "magnet:?xt=urn:..."
```

## 👨‍💻 Desenvolvimento

### Estrutura do Código

```
skidrow_downloader.py
├── SearchScreen      # Tela de busca
├── ResultsScreen     # Tela de resultados
├── DetailsScreen     # Tela de detalhes
├── DownloadScreen    # Tela de download
└── SkidrowDownloaderApp  # App principal
```

### Adicionar novas funcionalidades

O código usa o framework Textual. Para adicionar novas telas ou widgets:

```python
class MinhaNovaScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Meu conteúdo")
        yield Footer()
```

## 📞 Suporte

Se encontrar problemas:

1. Verifique a seção "Solução de Problemas"
2. Atualize todas as dependências
3. Reinstale o aplicativo
4. Verifique as permissões do Termux no Android

## 📄 Licença

Este projeto é fornecido "como está", sem garantias de qualquer tipo.

---

**Desenvolvido para Termux** | **Interface Textual** | **Download de Jogos Skidrow**

🎮 Divirta-se jogando! 🎮
