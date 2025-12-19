# 📖 Guia de Uso com Exemplos

## 🎬 Passo a Passo Completo

### Exemplo 1: Buscar e Baixar "GTA"

#### 1️⃣ Tela Inicial
```
┌────────────────────────────────────────┐
│   🎮 SKIDROW GAME DOWNLOADER          │
│                                        │
│   Busque seus jogos favoritos         │
│                                        │
│   ┌──────────────────────────────┐   │
│   │ Digite o nome do jogo...     │   │
│   │ GTA                          │   │
│   └──────────────────────────────┘   │
│                                        │
│   ┌──────────────────────────────┐   │
│   │      🔍 BUSCAR               │   │
│   └──────────────────────────────┘   │
│                                        │
└────────────────────────────────────────┘
```

**Ação:** Digite "GTA" e pressione BUSCAR ou ENTER

#### 2️⃣ Tela de Resultados
```
┌────────────────────────────────────────┐
│   📋 Resultados da Busca              │
│   Encontrados: 15 jogos                │
├────────────────────────────────────────┤
│                                        │
│ ➤ 🎮 GTA V Premium Edition            │
│   📅 December 19, 2025                │
│                                        │
│   🎮 GTA San Andreas Remastered       │
│   📅 December 15, 2025                │
│                                        │
│   🎮 GTA IV Complete Edition          │
│   📅 December 10, 2025                │
│                                        │
│   🎮 GTA Vice City Definitive         │
│   📅 December 05, 2025                │
│                                        │
├────────────────────────────────────────┤
│   [⬅️  VOLTAR]                        │
└────────────────────────────────────────┘
```

**Ação:** Use setas ou toque para navegar, ENTER para selecionar

#### 3️⃣ Tela de Detalhes
```
┌────────────────────────────────────────┐
│   🎮 GTA V Premium Edition            │
│                                        │
│   📅 Data: December 19, 2025          │
│   🔗 URL: https://www.skidrow...      │
│                                        │
│   🔄 Buscando links de download...    │
│                                        │
│   ✅ Links encontrados:               │
│   🧲 Torrents: 2                      │
│   🔗 Magnets: 3                       │
│                                        │
├────────────────────────────────────────┤
│   [⬅️  VOLTAR]  [💾 BAIXAR]          │
└────────────────────────────────────────┘
```

**Ação:** Pressione BAIXAR quando disponível

#### 4️⃣ Tela de Download
```
┌────────────────────────────────────────┐
│   💾 Configurar Download              │
│                                        │
│   📁 Caminho de Download:             │
│   ┌──────────────────────────────┐   │
│   │ /storage/emulated/0/Download │   │
│   └──────────────────────────────┘   │
│                                        │
│   🧲 Links Torrent (2)                │
│   ┌──────────────────────────────┐   │
│   │ 1. https://torrent1.com...   │   │
│   │ 2. https://torrent2.com...   │   │
│   └──────────────────────────────┘   │
│                                        │
│   🔗 Links Magnet (3)                 │
│   ┌──────────────────────────────┐   │
│   │ 1. magnet:?xt=urn:btih:...   │   │
│   │ 2. magnet:?xt=urn:btih:...   │   │
│   │ 3. magnet:?xt=urn:btih:...   │   │
│   └──────────────────────────────┘   │
│                                        │
│   [⬅️  VOLTAR]  [⬇️  INICIAR DOWNLOAD]│
│                                        │
│   ✅ Download iniciado com            │
│      transmission!                    │
│   📁 Local: /storage/.../Download     │
│                                        │
│   Use 'transmission-remote -l'        │
│   para ver o progresso                │
│                                        │
└────────────────────────────────────────┘
```

**Ação:** Pressione INICIAR DOWNLOAD

---

## 🎮 Exemplos de Buscas Comuns

### Busca: "Resident Evil"
```bash
# Resultados típicos:
- Resident Evil 4 Remake
- Resident Evil Village
- Resident Evil 2 Remake
- Resident Evil 7 Biohazard
```

### Busca: "Assassins Creed"
```bash
# Resultados típicos:
- Assassin's Creed Valhalla
- Assassin's Creed Odyssey
- Assassin's Creed Origins
- Assassin's Creed Mirage
```

### Busca: "FIFA"
```bash
# Resultados típicos:
- FC 24
- FIFA 23
- FIFA 22
```

---

## 💻 Comandos Úteis Durante o Uso

### Monitorar Downloads Ativos

```bash
# Em outra sessão do Termux (use tmux)
transmission-remote -l
```

**Exemplo de saída:**
```
ID   Done  Have    ETA    Up     Down   Ratio  Status       Name
 1   45%   2.1 GB  1:30   50 KB  1.5 MB  0.03  Downloading  GTA V Premium Edition
Sum:        2.1 GB         50 KB  1.5 MB
```

### Ver Detalhes de um Download

```bash
transmission-remote -t 1 -i
```

**Exemplo de saída:**
```
NAME
  GTA V Premium Edition
  Id: 1
  Hash: abc123def456...
  
TRANSFER
  State: Downloading
  Progress: 45%
  Downloaded: 2.1 GB of 4.5 GB
  Ratio: 0.03
  
SPEEDS
  Download: 1.5 MB/s
  Upload: 50 KB/s
  
DATES
  Added: Thu Dec 19 10:30:00 2025
  Started: Thu Dec 19 10:30:05 2025
```

### Pausar um Download

```bash
transmission-remote -t 1 -S
```

### Retomar um Download

```bash
transmission-remote -t 1 -s
```

### Remover Download Completo

```bash
# Remove apenas do transmission, mantém arquivo
transmission-remote -t 1 -r

# Remove do transmission E apaga arquivo
transmission-remote -t 1 -rad
```

---

## 🔧 Usando tmux para Múltiplas Tarefas

### Criar Sessão com App + Monitor

```bash
# Iniciar tmux
tmux new -s gaming

# Janela 1: App principal
python skidrow_downloader.py

# Nova janela (Ctrl+B, C)
# Janela 2: Monitor de downloads
watch -n 5 transmission-remote -l

# Alternar entre janelas (Ctrl+B, N)
# Desanexar sessão (Ctrl+B, D)
# Reanexar sessão
tmux attach -t gaming
```

---

## 📊 Cenários de Uso

### Cenário 1: Download Rápido
```bash
1. Abrir app
2. Buscar jogo
3. Selecionar primeiro resultado
4. Iniciar download
5. Sair do app (download continua no background)
6. Verificar: transmission-remote -l
```

### Cenário 2: Download Múltiplo
```bash
1. Abrir app em tmux
2. Buscar primeiro jogo
3. Iniciar download
4. VOLTAR para busca (ESC várias vezes)
5. Buscar segundo jogo
6. Iniciar download
7. Verificar ambos: transmission-remote -l
```

### Cenário 3: Download com Escolha de Local
```bash
1. Buscar jogo
2. Selecionar resultado
3. Na tela de download, EDITAR caminho:
   - Padrão: ~/storage/downloads
   - Cartão SD: ~/storage/external-1
   - Pasta customizada: ~/storage/shared/Jogos
4. Iniciar download
```

---

## 🎯 Fluxo de Trabalho Recomendado

### Para Downloads Longos

```bash
# 1. Iniciar tmux
tmux new -s downloads

# 2. Ativar wake-lock
termux-wake-lock

# 3. Iniciar transmission daemon
transmission-daemon

# 4. Verificar status do daemon
pgrep transmission

# 5. Executar app
python skidrow_downloader.py

# 6. Configurar downloads

# 7. Criar janela de monitoramento (Ctrl+B, C)
watch -n 10 'transmission-remote -l && df -h ~/storage/downloads'

# 8. Desanexar tmux (Ctrl+B, D)

# 9. Pode fechar o Termux (downloads continuam)

# 10. Reanexar depois
tmux attach -t downloads
```

---

## 📱 Interface Touch - Gestos

### Navegação Touch

```
┌─────────────────────────────────────┐
│  Toque único      → Selecionar      │
│  Arrastar         → Scroll          │
│  Deslizar esq.    → Voltar (ESC)   │
│  Toque longo      → Menu contexto   │
└─────────────────────────────────────┘
```

### Teclado Virtual

Use a linha extra de teclas do Termux:
```
[ESC] [TAB] [CTRL] [ALT] [/] [-] [↑] [↓] [←] [→]
```

**Habilitar:**
1. Toque longo no Termux
2. More...
3. ✓ Extra Keys

---

## 🎨 Personalização de Interface

### Temas do Termux

```bash
# Instalar ferramenta de temas
pkg install termux-styling

# Executar
termux-style

# Escolher:
# - Tema: Dark, Light, Solarized, etc.
# - Fonte: monospace, cascadia, etc.
```

### Cores Recomendadas

**Para melhor visualização do app:**
- Tema: Dark ou Solarized Dark
- Fonte: Cascadia Code ou Fira Code
- Tamanho: 12-14pt

---

## 📈 Gerenciamento de Espaço

### Verificar Espaço Antes de Baixar

```bash
# Ver espaço disponível
df -h ~/storage/downloads

# Exemplo de saída:
# Filesystem      Size  Used Avail Use% Mounted on
# /storage/emul   64G   32G   32G  50% /storage/downloads
```

### Limpar Downloads Antigos

```bash
# Listar arquivos grandes
cd ~/storage/downloads
du -h --max-depth=1 | sort -hr | head -10

# Remover arquivo específico
rm "nome_do_jogo.iso"

# Remover torrents completos do transmission
transmission-remote -t all -r
```

---

## 🔍 Troubleshooting em Uso

### Problema: "Nenhum resultado encontrado"

**Possíveis causas:**
1. Nome do jogo muito específico
2. Ortografia incorreta
3. Jogo muito antigo/novo

**Soluções:**
```bash
# Tente buscas mais genéricas:
❌ "Grand Theft Auto V Premium Edition 2024"
✅ "GTA V"

❌ "The Legend of Zelda Breath Wild"
✅ "Zelda"
```

### Problema: "Erro ao buscar links"

**Soluções:**
```bash
# 1. Verificar internet
ping -c 3 www.skidrowreloaded.com

# 2. Tentar outro resultado
# Voltar e selecionar outra opção

# 3. Atualizar dependências
pip install --upgrade requests beautifulsoup4
```

### Problema: "Download não inicia"

**Verificações:**
```bash
# 1. Transmission rodando?
pgrep transmission
# Se não, iniciar:
transmission-daemon

# 2. Espaço disponível?
df -h ~/storage/downloads

# 3. Permissões?
ls -la ~/storage/downloads

# 4. Porta bloqueada?
transmission-remote -l
# Se erro, reiniciar daemon:
pkill transmission-daemon
transmission-daemon
```

---

## 💡 Dicas Avançadas

### 1. Alias para Comandos Rápidos

Adicione ao `~/.bashrc`:

```bash
# Aliases para o app
alias skidrow='python ~/skidrow_downloader.py'
alias downloads='transmission-remote -l'
alias downloadinfo='transmission-remote -t'
alias pauseall='transmission-remote -t all -S'
alias resumeall='transmission-remote -t all -s'

# Recarregar
source ~/.bashrc
```

Agora pode usar:
```bash
skidrow          # Inicia o app
downloads        # Lista downloads
downloadinfo 1   # Info do download 1
```

### 2. Script de Monitoramento Automático

Crie `~/monitor_downloads.sh`:

```bash
#!/bin/bash
while true; do
    clear
    echo "=== DOWNLOADS ATIVOS ==="
    transmission-remote -l
    echo ""
    echo "=== ESPAÇO EM DISCO ==="
    df -h ~/storage/downloads | tail -1
    echo ""
    echo "=== HORA: $(date) ==="
    sleep 10
done
```

Executar:
```bash
chmod +x ~/monitor_downloads.sh
./monitor_downloads.sh
```

### 3. Notificações de Download Completo

Crie `~/check_complete.sh`:

```bash
#!/bin/bash
while true; do
    COMPLETE=$(transmission-remote -l | grep "100%" | wc -l)
    if [ $COMPLETE -gt 0 ]; then
        termux-notification \
            --title "Download Completo!" \
            --content "$COMPLETE jogo(s) pronto(s)" \
            --sound
    fi
    sleep 60
done
```

Executar em background:
```bash
chmod +x ~/check_complete.sh
nohup ./check_complete.sh &
```

---

## 🎓 Recursos de Aprendizado

### Praticar Comandos

```bash
# Exercício 1: Buscar e listar
# 1. Busque "Mario"
# 2. Anote quantos resultados apareceram
# 3. Volte sem selecionar nenhum

# Exercício 2: Explorar detalhes
# 1. Busque "Sonic"
# 2. Selecione primeiro resultado
# 3. Veja quantos links foram encontrados
# 4. Volte sem baixar

# Exercício 3: Testar caminhos
# 1. Busque qualquer jogo
# 2. Na tela de download, teste diferentes caminhos:
#    - ~/storage/downloads
#    - ~/storage/shared
#    - ~/Jogos (criar antes: mkdir ~/Jogos)
```

### Entender Estrutura de Torrents

```bash
# Ver estrutura de um torrent
transmission-remote -t 1 -f

# Exemplo de saída:
# GTA V Premium Edition/
# ├── game.iso (45 GB)
# ├── crack/ (250 MB)
# ├── readme.txt (5 KB)
# └── instructions.pdf (2 MB)
```

---

✅ **Você agora domina o Skidrow Game Downloader!**

🎮 Divirta-se baixando seus jogos favoritos!
