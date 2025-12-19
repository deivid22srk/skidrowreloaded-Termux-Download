# ⚡ Guia Rápido de Início

## 🚀 Instalação em 3 Passos

### 1️⃣ Prepare o Termux

```bash
pkg update && pkg upgrade -y
pkg install python python-pip transmission git -y
termux-setup-storage
```

### 2️⃣ Instale as Dependências

```bash
pip install textual requests beautifulsoup4 lxml
```

### 3️⃣ Execute o App

```bash
chmod +x skidrow_downloader.py
python skidrow_downloader.py
```

---

## 🎮 Uso Básico

1. **Digite o nome do jogo** na tela inicial
2. **Pressione BUSCAR** ou ENTER
3. **Selecione um resultado** da lista (setas + ENTER)
4. **Aguarde** carregar os links de download
5. **Pressione BAIXAR**
6. **Confirme o caminho** de download
7. **Pressione INICIAR DOWNLOAD**

---

## 📋 Comandos Essenciais

```bash
# Executar o aplicativo
python skidrow_downloader.py

# Ver downloads ativos
transmission-remote -l

# Pausar download
transmission-remote -t 1 -S

# Retomar download
transmission-remote -t 1 -s

# Remover download
transmission-remote -t 1 -r

# Verificar instalação
python test_installation.py
```

---

## ⌨️ Atalhos do App

| Tecla | Ação |
|-------|------|
| `q` | Sair |
| `ESC` | Voltar |
| `ENTER` | Selecionar |
| `↑↓` | Navegar |
| `TAB` | Próximo campo |

---

## 📁 Estrutura de Arquivos

```
skidrow-downloader/
├── 📄 skidrow_downloader.py     # Aplicativo principal ⭐
├── 📄 requirements.txt           # Dependências Python
├── 📄 install.sh                 # Script de instalação
├── 📄 test_installation.py       # Teste de instalação
├── 📖 README.md                  # Documentação completa
├── 📖 QUICKSTART.md             # Este arquivo
├── 📖 TERMUX_SETUP.md           # Guia do Termux
├── 📖 EXAMPLES.md               # Exemplos de uso
├── 📖 FAQ.md                    # Perguntas frequentes
└── 📄 .gitignore                # Arquivos ignorados
```

---

## 🔧 Solução Rápida de Problemas

### Erro de módulo não encontrado
```bash
pip install textual requests beautifulsoup4 lxml
```

### Permission denied
```bash
chmod +x skidrow_downloader.py
```

### Transmission não funciona
```bash
pkg install transmission
transmission-daemon
```

### Sem espaço
```bash
df -h ~/storage/downloads
pkg clean
```

---

## 💡 Dicas Rápidas

✅ **Use WiFi** para downloads grandes
✅ **Ative wake-lock** para downloads longos: `termux-wake-lock`
✅ **Use tmux** para múltiplas tarefas: `pkg install tmux`
✅ **Escolha torrents** com mais seeders
✅ **Leia comentários** antes de baixar

---

## 📚 Precisa de Mais Ajuda?

- **Instalação completa**: Leia @README.md
- **Configurar Termux**: Leia @TERMUX_SETUP.md
- **Exemplos práticos**: Leia @EXAMPLES.md
- **Perguntas comuns**: Leia @FAQ.md

---

## 🎯 Exemplo Completo

```bash
# 1. Instalar (só uma vez)
pkg update && pkg upgrade -y
pkg install python python-pip transmission -y
pip install textual requests beautifulsoup4 lxml
termux-setup-storage

# 2. Configurar downloads longos (recomendado)
termux-wake-lock
transmission-daemon

# 3. Executar app
python skidrow_downloader.py

# 4. No app:
#    - Digite: "GTA"
#    - Pressione: BUSCAR
#    - Selecione: Primeiro resultado
#    - Pressione: BAIXAR
#    - Pressione: INICIAR DOWNLOAD

# 5. Monitorar (em outra sessão)
transmission-remote -l

# 6. Quando terminar
termux-wake-unlock
```

---

✅ **Pronto! Você está pronto para usar!**

🎮 Divirta-se baixando seus jogos favoritos!

⚠️ **Lembre-se**: Use apenas para fins legais e educacionais!
