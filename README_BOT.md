# 🤖 Skidrow Telegram Bot

Bot do Telegram para buscar e baixar jogos do Skidrow Reloaded diretamente via chat!

## ✨ Características

- 🤖 Interface completa no Telegram
- 🔍 Busca de jogos com comando `/buscar`
- 📋 Resultados com botões interativos
- 🧲 Suporte a torrents e magnet links
- 💾 Configuração de caminho via comando
- ⬇️ Download automático via Transmission
- 📱 Funciona perfeitamente no Termux
- 🌐 Acesse de qualquer lugar

## 📦 Requisitos

- **Termux** instalado (F-Droid ou GitHub)
- **Python 3.10+**
- **Transmission** (para downloads)
- **Conexão com internet**
- **Conta no Telegram** (obviamente!)

## 🚀 Instalação

### Passo 1: Baixar e Extrair

```bash
# Extrair arquivos
cd ~
unzip ~/storage/downloads/skidrow-telegram-bot.zip
cd skidrow-telegram-bot
```

### Passo 2: Instalar Dependências

#### Instalação Automática (Recomendado)

```bash
bash install_bot.sh
```

#### Instalação Manual

```bash
# Atualizar sistema
pkg update && pkg upgrade -y

# Instalar Python e Transmission
pkg install python python-pip transmission git -y

# Configurar armazenamento
termux-setup-storage

# Instalar dependências Python
pip install -r requirements_bot.txt

# Dar permissão
chmod +x telegram_bot.py

# Iniciar transmission daemon
transmission-daemon
```

### Passo 3: Iniciar o Bot

```bash
# Ativar wake-lock (recomendado)
termux-wake-lock

# Iniciar bot
python telegram_bot.py
```

**Você verá:**
```
🤖 Iniciando Skidrow Downloader Bot...
📱 Token: 7718948467:AAGhVsQ...
✅ Bot iniciado!
📡 Aguardando mensagens...
```

## 🎯 Como Usar

### 1. Encontrar o Bot

Abra o Telegram e busque pelo nome do bot ou inicie uma conversa com ele.

### 2. Comandos Disponíveis

#### `/start`
Mostra mensagem de boas-vindas e informações básicas

#### `/buscar <nome do jogo>`
Busca jogos no Skidrow Reloaded

**Exemplo:**
```
/buscar GTA V
/buscar Resident Evil
/buscar FIFA 24
```

#### `/caminho <caminho>`
Define o caminho onde os jogos serão baixados

**Exemplo:**
```
/caminho /storage/emulated/0/Download
/caminho /data/data/com.termux/files/home/Jogos
```

**Padrão:** `/data/data/com.termux/files/home/storage/downloads`

#### `/caminho_ver`
Mostra o caminho atual configurado

#### `/ajuda`
Mostra ajuda completa com todos os comandos

#### `/sobre`
Informações sobre o bot

### 3. Fluxo de Uso Completo

```
1. Abrir Telegram
   ↓
2. Iniciar conversa com o bot
   ↓
3. /start (conhecer o bot)
   ↓
4. /caminho /seu/caminho (opcional)
   ↓
5. /buscar GTA V
   ↓
6. Clicar no jogo desejado (botão)
   ↓
7. Clicar no link de download (botão)
   ↓
8. Confirmar download (botão)
   ↓
9. Download inicia no Termux!
```

## 📱 Exemplo de Conversa

```
Você: /start

Bot: 🎮 BEM-VINDO AO SKIDROW DOWNLOADER BOT!
     
     Busque e baixe jogos do Skidrow Reloaded...
     [mensagem completa]

─────────────────────────────────────

Você: /buscar GTA

Bot: 🔍 Buscando por: GTA
     
     ⏳ Aguarde...

Bot: 📋 Resultados da Busca
     
     Encontrados: 10 jogos
     
     Selecione um jogo:
     
     [🎮 GTA V Premium Edition]
     [🎮 GTA San Andreas Remastered]
     [🎮 GTA IV Complete Edition]
     [...]

─────────────────────────────────────

Você: [Clica em "GTA V Premium Edition"]

Bot: 🎮 GTA V Premium Edition
     
     📅 December 19, 2025
     🔗 https://www.skidrow...
     
     🔄 Buscando links de download...

Bot: 🎮 GTA V Premium Edition
     
     ✅ Links encontrados:
     🧲 Torrents: 2
     🔗 Magnets: 3
     
     Selecione um link:
     
     [🧲 Torrent 1]
     [🧲 Torrent 2]
     [🔗 Magnet 1]
     [🔗 Magnet 2]
     [🔗 Magnet 3]

─────────────────────────────────────

Você: [Clica em "🔗 Magnet 1"]

Bot: 💾 CONFIRMAR DOWNLOAD
     
     🔗 Tipo: Magnet
     📁 Caminho: /storage/.../downloads
     
     Link: magnet:?xt=urn:btih:...
     
     ⚠️ O download será iniciado...
     
     Deseja continuar?
     
     [✅ CONFIRMAR] [❌ CANCELAR]

─────────────────────────────────────

Você: [Clica em "✅ CONFIRMAR"]

Bot: ⏳ Iniciando download...

Bot: 🎮 GTA V Premium Edition
     
     ✅ Download iniciado!
     📁 Local: /storage/.../downloads
     
     📊 Ver progresso no Termux:
     transmission-remote -l
     
     ⏸️ Pausar:
     transmission-remote -t 1 -S
     
     ▶️ Retomar:
     transmission-remote -t 1 -s
     
     🎉 Buscar outro jogo: /buscar <nome>
```

## 🔧 Gerenciar o Bot

### Iniciar Bot

```bash
# Com wake-lock (recomendado)
termux-wake-lock
python telegram_bot.py
```

### Parar Bot

```
Ctrl+C no Termux
```

### Rodar em Background

```bash
# Instalar tmux
pkg install tmux

# Criar sessão
tmux new -s bot

# Iniciar bot
python telegram_bot.py

# Desanexar (Ctrl+B, D)
# Bot continua rodando

# Reanexar depois
tmux attach -t bot
```

### Rodar como Serviço (Avançado)

```bash
# Usar nohup
nohup python telegram_bot.py > bot.log 2>&1 &

# Ver log
tail -f bot.log

# Matar processo
pkill -f telegram_bot.py
```

## 📊 Monitorar Downloads

### No Termux

```bash
# Ver todos os downloads
transmission-remote -l

# Ver detalhes
transmission-remote -t 1 -i

# Pausar
transmission-remote -t 1 -S

# Retomar
transmission-remote -t 1 -s

# Remover
transmission-remote -t 1 -r
```

### Monitor em Tempo Real

```bash
# Em outra janela tmux ou sessão
watch -n 5 transmission-remote -l
```

## 💡 Dicas Importantes

### 1. Manter Bot Ativo

O bot precisa que o Termux esteja rodando:

```bash
# Ativar wake-lock
termux-wake-lock

# Desativar otimização de bateria no Android:
# Configurações > Apps > Termux > Bateria > Sem restrições
```

### 2. Usar tmux

```bash
# Instalar
pkg install tmux

# Iniciar sessão
tmux new -s bot

# Iniciar bot
python telegram_bot.py

# Desanexar (Ctrl+B, D)
# Bot continua rodando em background

# Reanexar quando quiser ver
tmux attach -t bot
```

### 3. Ver Logs

```bash
# Se rodou com nohup
tail -f bot.log

# Se rodou normal
# Logs aparecem no terminal do Termux
```

### 4. Transmission Daemon

```bash
# Sempre certifique-se que está rodando
pgrep transmission

# Se não estiver, iniciar:
transmission-daemon

# Verificar status
transmission-remote -l
```

## 🐛 Solução de Problemas

### Bot não inicia

```bash
# Verificar token
# Editar telegram_bot.py e confirmar token

# Verificar dependências
pip install -r requirements_bot.txt

# Verificar Python
python --version  # Deve ser 3.10+
```

### Bot não responde no Telegram

```bash
# Verificar se bot está rodando
ps aux | grep telegram_bot

# Verificar internet
ping -c 3 telegram.org

# Verificar logs (se usando nohup)
tail -50 bot.log
```

### Erro ao iniciar download

```bash
# Verificar transmission
pgrep transmission

# Se não estiver rodando
transmission-daemon

# Aguardar 5 segundos
sleep 5

# Tentar novamente no Telegram
```

### "Transmission não instalado"

```bash
pkg install transmission
transmission-daemon
```

### Bot desconecta

```bash
# Ativar wake-lock
termux-wake-lock

# Desativar otimização de bateria:
# Android > Configurações > Apps > Termux > Bateria > Sem restrições

# Usar tmux
tmux new -s bot
python telegram_bot.py
# Ctrl+B, D para desanexar
```

## ⚙️ Configurações Avançadas

### Mudar Token do Bot

Edite `telegram_bot.py`:

```python
BOT_TOKEN = "SEU_NOVO_TOKEN_AQUI"
```

### Limitar Número de Resultados

Edite `telegram_bot.py`, linha ~28:

```python
for article in articles[:10]:  # Mudar 10 para o número desejado
```

### Caminho Padrão

Edite `telegram_bot.py`, procure por:

```python
default_path = "/seu/caminho/preferido"
```

## 🔐 Segurança

### Proteger Token

❌ **Não compartilhe** o token do bot
❌ **Não faça commit** do token em repositórios públicos
✅ **Guarde** o token em local seguro

### Revogar Token

Se o token vazou:
1. Fale com @BotFather no Telegram
2. Use `/revoke` para revogar token
3. Gere novo token com `/newbot`
4. Atualize `telegram_bot.py`

## 📊 Estatísticas

```
Linhas de código: ~450
Comandos: 6
Callbacks: 3 tipos
Dependências: 4 pacotes
Tamanho: ~15 KB
```

## 🆚 Comparação de Versões

| Recurso | Bot Telegram | CLI | TUI |
|---------|--------------|-----|-----|
| Interface | Telegram | Terminal | Terminal |
| Uso remoto | ✅ Sim | ❌ Não | ❌ Não |
| Botões | ✅ Sim | ❌ Não | ✅ Sim |
| Múltiplos usuários | ✅ Sim | ❌ Não | ❌ Não |
| Requer Termux ativo | ✅ Sim | ✅ Sim | ✅ Sim |
| Complexidade | Média | Baixa | Média |

## 📖 Comandos Rápidos

```bash
# Instalar tudo
bash install_bot.sh

# Iniciar bot
termux-wake-lock
python telegram_bot.py

# Em outro terminal (tmux):
watch -n 10 transmission-remote -l

# Parar bot
Ctrl+C

# Ver downloads
transmission-remote -l
```

## 🎓 Fluxo Técnico

```
Usuário envia /buscar
    ↓
Bot busca no Skidrow (requests + BeautifulSoup)
    ↓
Bot mostra resultados (InlineKeyboardButtons)
    ↓
Usuário clica em jogo
    ↓
Bot extrai links de download
    ↓
Bot mostra links (InlineKeyboardButtons)
    ↓
Usuário escolhe link
    ↓
Bot confirma download
    ↓
Bot executa transmission-remote
    ↓
Download inicia no Termux
```

## ⚠️ Avisos Importantes

1. **Bot precisa estar rodando** no Termux
2. **Transmission precisa estar ativo** (daemon)
3. **Termux não pode dormir** (use wake-lock)
4. **Internet precisa estar ativa**
5. **Use apenas para fins legais**

## 🎉 Pronto para Usar!

```bash
# 1. Instalar
bash install_bot.sh

# 2. Iniciar
termux-wake-lock
python telegram_bot.py

# 3. Abrir Telegram e buscar o bot

# 4. Enviar /start

# 5. Divertir-se! 🎮
```

---

**🤖 Bot do Telegram** | **🎮 Skidrow Downloader** | **📱 Use de Qualquer Lugar**

**Versão:** 1.0.0
**Desenvolvido para:** Termux + Telegram
