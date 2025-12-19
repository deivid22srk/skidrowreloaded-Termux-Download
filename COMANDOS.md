# 🖥️ LISTA COMPLETA DE COMANDOS

## 📦 INSTALAÇÃO

### Atualizar Termux
```bash
pkg update
pkg upgrade -y
pkg update && pkg upgrade -y
```

### Instalar Python
```bash
pkg install python
pkg install python-pip
pkg install python python-pip -y
```

### Instalar Git
```bash
pkg install git -y
```

### Instalar Transmission
```bash
pkg install transmission -y
```

### Configurar Armazenamento
```bash
termux-setup-storage
```

### Instalar Dependências Python
```bash
pip install textual
pip install requests
pip install beautifulsoup4
pip install lxml
pip install textual requests beautifulsoup4 lxml
pip install -r requirements.txt
```

### Instalação Automática Completa
```bash
bash install.sh
```

---

## 🚀 EXECUÇÃO

### Executar Aplicativo
```bash
python skidrow_downloader.py
./skidrow_downloader.py
```

### Testar Instalação
```bash
python test_installation.py
./test_installation.py
```

### Dar Permissão de Execução
```bash
chmod +x skidrow_downloader.py
chmod +x test_installation.py
chmod +x install.sh
```

---

## 🧲 TRANSMISSION

### Daemon

#### Iniciar Daemon
```bash
transmission-daemon
```

#### Parar Daemon
```bash
pkill transmission-daemon
killall transmission-daemon
```

#### Verificar se Está Rodando
```bash
pgrep transmission
ps aux | grep transmission
```

#### Verificar Versão
```bash
transmission-remote --version
transmission-daemon --version
```

### Downloads

#### Listar Todos os Downloads
```bash
transmission-remote -l
transmission-remote --list
```

#### Informações Detalhadas de um Download
```bash
transmission-remote -t 1 -i
transmission-remote -t 1 --info
```

#### Adicionar Torrent
```bash
transmission-remote -a "arquivo.torrent"
transmission-remote -a "magnet:?xt=..."
transmission-remote --add "arquivo.torrent"
```

#### Adicionar com Caminho Específico
```bash
transmission-remote -a "arquivo.torrent" -w "/caminho/download"
```

#### Pausar Download
```bash
transmission-remote -t 1 -S
transmission-remote -t 1 --stop
transmission-remote -t all -S
```

#### Retomar Download
```bash
transmission-remote -t 1 -s
transmission-remote -t 1 --start
transmission-remote -t all -s
```

#### Remover Download (mantém arquivo)
```bash
transmission-remote -t 1 -r
transmission-remote -t 1 --remove
```

#### Remover Download e Arquivo
```bash
transmission-remote -t 1 -rad
transmission-remote -t 1 --remove-and-delete
```

#### Ver Arquivos de um Torrent
```bash
transmission-remote -t 1 -f
transmission-remote -t 1 --files
```

### Limites de Velocidade

#### Definir Limite de Download (KB/s)
```bash
transmission-remote -d 500
transmission-remote --downlimit 500
```

#### Remover Limite de Download
```bash
transmission-remote -d 0
transmission-remote -D
```

#### Definir Limite de Upload (KB/s)
```bash
transmission-remote -u 50
transmission-remote --uplimit 50
```

#### Remover Limite de Upload
```bash
transmission-remote -u 0
transmission-remote -U
```

### Configuração

#### Editar Configuração
```bash
nano ~/.config/transmission-daemon/settings.json
vim ~/.config/transmission-daemon/settings.json
```

#### Ver Configuração de Porta
```bash
transmission-remote -pt
transmission-remote --port-test
```

---

## 📁 GERENCIAMENTO DE ARQUIVOS

### Navegar Diretórios
```bash
cd ~
cd ~/storage/downloads
cd /caminho/especifico
pwd
ls
ls -la
```

### Criar Diretórios
```bash
mkdir pasta
mkdir -p pasta/subpasta
mkdir ~/storage/downloads/Jogos
```

### Mover Arquivos
```bash
mv origem destino
mv arquivo.torrent ~/storage/downloads/
```

### Copiar Arquivos
```bash
cp origem destino
cp -r pasta_origem pasta_destino
```

### Remover Arquivos
```bash
rm arquivo
rm -f arquivo
rm -rf pasta
```

### Ver Espaço em Disco
```bash
df -h
df -h ~/storage/downloads
du -h
du -sh *
du -h --max-depth=1 | sort -hr
```

### Listar Arquivos Grandes
```bash
du -h | sort -hr | head -10
find . -type f -size +1G
```

---

## 🔧 SISTEMA

### Informações do Sistema
```bash
uname -a
cat /proc/version
```

### Uso de Memória
```bash
free -h
cat /proc/meminfo
```

### Uso de CPU
```bash
top
htop
```

### Processos
```bash
ps
ps aux
ps aux | grep python
pgrep python
pkill python
killall python
```

### Limpar Tela
```bash
clear
```

---

## 🌐 REDE

### Testar Conexão
```bash
ping google.com
ping -c 3 google.com
ping www.skidrowreloaded.com
```

### Ver Endereço IP
```bash
ifconfig
ip addr
```

### Testar DNS
```bash
nslookup google.com
nslookup skidrowreloaded.com
```

### Download com Curl
```bash
curl -O https://exemplo.com/arquivo
curl -L -O https://exemplo.com/arquivo
```

### Download com Wget
```bash
wget https://exemplo.com/arquivo
wget -c https://exemplo.com/arquivo
```

---

## ⚡ TERMUX ESPECÍFICOS

### Wake Lock

#### Ativar Wake Lock
```bash
termux-wake-lock
```

#### Desativar Wake Lock
```bash
termux-wake-unlock
```

#### Ver Status
```bash
termux-wake-status
```

### Notificações
```bash
termux-toast "Mensagem"
termux-notification --title "Título" --content "Conteúdo"
termux-notification --sound
```

### Vibração
```bash
termux-vibrate
termux-vibrate -d 1000
```

### Bateria
```bash
termux-battery-status
```

### WiFi
```bash
termux-wifi-enable true
termux-wifi-enable false
termux-wifi-connectioninfo
termux-wifi-scaninfo
```

### Localização
```bash
termux-location
```

### Câmera
```bash
termux-camera-photo foto.jpg
```

---

## 📦 GERENCIAMENTO DE PACOTES

### pkg (Gerenciador de Pacotes)

#### Buscar Pacote
```bash
pkg search nome
```

#### Instalar Pacote
```bash
pkg install nome
pkg install nome1 nome2 nome3
```

#### Remover Pacote
```bash
pkg uninstall nome
pkg remove nome
```

#### Atualizar Lista de Pacotes
```bash
pkg update
```

#### Atualizar Pacotes Instalados
```bash
pkg upgrade
```

#### Listar Pacotes Instalados
```bash
pkg list-installed
pkg list-all
```

#### Informações de um Pacote
```bash
pkg show nome
```

#### Limpar Cache
```bash
pkg clean
```

#### Reinstalar Pacote
```bash
pkg reinstall nome
```

#### Mudar Repositório
```bash
termux-change-repo
```

### pip (Python)

#### Instalar Pacote Python
```bash
pip install nome
pip install nome==1.0.0
```

#### Desinstalar Pacote Python
```bash
pip uninstall nome
```

#### Atualizar pip
```bash
pip install --upgrade pip
```

#### Atualizar Pacote
```bash
pip install --upgrade nome
```

#### Listar Pacotes Instalados
```bash
pip list
pip freeze
```

#### Ver Informações de Pacote
```bash
pip show nome
```

#### Buscar Pacote
```bash
pip search nome
```

#### Instalar de requirements.txt
```bash
pip install -r requirements.txt
```

#### Criar requirements.txt
```bash
pip freeze > requirements.txt
```

#### Limpar Cache
```bash
pip cache purge
```

---

## 🖥️ TMUX (Multiplexador de Terminal)

### Instalação
```bash
pkg install tmux
```

### Sessões

#### Nova Sessão
```bash
tmux
tmux new
tmux new -s nome
```

#### Listar Sessões
```bash
tmux ls
tmux list-sessions
```

#### Anexar Sessão
```bash
tmux attach
tmux attach -t nome
tmux a -t nome
```

#### Desanexar Sessão
```
Ctrl+B, D
```

#### Matar Sessão
```bash
tmux kill-session -t nome
```

### Janelas

#### Nova Janela
```
Ctrl+B, C
```

#### Próxima Janela
```
Ctrl+B, N
```

#### Janela Anterior
```
Ctrl+B, P
```

#### Listar Janelas
```
Ctrl+B, W
```

#### Renomear Janela
```
Ctrl+B, ,
```

#### Fechar Janela
```
Ctrl+B, &
ou
exit
```

### Painéis

#### Dividir Horizontalmente
```
Ctrl+B, "
```

#### Dividir Verticalmente
```
Ctrl+B, %
```

#### Navegar entre Painéis
```
Ctrl+B, Setas
```

#### Fechar Painel
```
Ctrl+B, X
ou
exit
```

---

## 📝 EDITORES DE TEXTO

### nano

#### Abrir Arquivo
```bash
nano arquivo.txt
nano ~/.bashrc
```

#### Salvar
```
Ctrl+O, Enter
```

#### Sair
```
Ctrl+X
```

#### Buscar
```
Ctrl+W
```

### vim

#### Abrir Arquivo
```bash
vim arquivo.txt
```

#### Modo Inserção
```
I
```

#### Sair do Modo Inserção
```
ESC
```

#### Salvar e Sair
```
:wq
```

#### Sair sem Salvar
```
:q!
```

---

## 🔍 BUSCA E FILTROS

### grep (Buscar em Texto)
```bash
grep "texto" arquivo
grep -r "texto" pasta/
grep -i "texto" arquivo
ps aux | grep python
```

### find (Buscar Arquivos)
```bash
find . -name "*.txt"
find . -type f -size +1G
find . -name "jogo*"
```

### Pipes e Redirecionamento
```bash
comando | grep filtro
comando > arquivo.txt
comando >> arquivo.txt
comando1 && comando2
comando1 ; comando2
```

---

## 📊 MONITORAMENTO

### Ver Downloads em Loop
```bash
watch -n 5 transmission-remote -l
```

### Monitor de Sistema
```bash
htop
top
```

### Ver Logs
```bash
tail -f arquivo.log
tail -100 arquivo.log
```

---

## 🔐 PERMISSÕES

### Ver Permissões
```bash
ls -la
```

### Mudar Permissões
```bash
chmod +x arquivo
chmod 755 arquivo
chmod -R 755 pasta/
```

### Tornar Arquivo Executável
```bash
chmod +x arquivo.sh
chmod +x arquivo.py
```

---

## 🎨 CUSTOMIZAÇÃO

### Editar .bashrc
```bash
nano ~/.bashrc
```

### Recarregar .bashrc
```bash
source ~/.bashrc
```

### Aliases Úteis
```bash
# Adicionar ao ~/.bashrc
alias ll='ls -la'
alias update='pkg update && pkg upgrade'
alias c='clear'
alias downloads='transmission-remote -l'
alias skidrow='python ~/skidrow_downloader.py'
```

### Termux Styling
```bash
pkg install termux-styling
termux-style
```

---

## 🔄 BACKUP E RESTAURAÇÃO

### Backup do Termux
```bash
cd ~
tar -czf termux-backup.tar.gz .
mv termux-backup.tar.gz ~/storage/downloads/
```

### Restaurar Backup
```bash
cd ~
tar -xzf ~/storage/downloads/termux-backup.tar.gz
```

---

## 🐛 DEBUG E TROUBLESHOOTING

### Ver Versões
```bash
python --version
pip --version
transmission-remote --version
termux-info
```

### Ver Logs de Erro Python
```bash
python arquivo.py 2>&1 | tee erro.log
```

### Limpar Cache Python
```bash
find . -type d -name __pycache__ -exec rm -rf {} +
find . -name "*.pyc" -delete
```

### Reinstalar Dependências
```bash
pip uninstall textual requests beautifulsoup4 lxml -y
pip install textual requests beautifulsoup4 lxml
```

---

## 🌐 ARIA2 (Cliente Download Alternativo)

### Instalação
```bash
pkg install aria2
```

### Download de Arquivo
```bash
aria2c https://exemplo.com/arquivo
```

### Download de Torrent
```bash
aria2c arquivo.torrent
aria2c "magnet:?xt=..."
```

### Download com Limite de Velocidade
```bash
aria2c --max-download-limit=1M arquivo
```

---

## 📱 TERMUX:API (Comandos Extras)

### Instalação
```bash
pkg install termux-api
```

### Comandos Disponíveis
```bash
termux-battery-status
termux-brightness
termux-camera-info
termux-camera-photo
termux-clipboard-get
termux-clipboard-set
termux-contact-list
termux-dialog
termux-download
termux-fingerprint
termux-infrared-frequencies
termux-infrared-transmit
termux-location
termux-media-player
termux-media-scan
termux-notification
termux-notification-remove
termux-sensor
termux-share
termux-sms-inbox
termux-sms-send
termux-storage-get
termux-telephony-call
termux-telephony-cellinfo
termux-telephony-deviceinfo
termux-toast
termux-torch
termux-tts-speak
termux-usb
termux-vibrate
termux-volume
termux-wallpaper
termux-wifi-connectioninfo
termux-wifi-enable
termux-wifi-scaninfo
```

---

## 🚀 COMANDOS RÁPIDOS ÚTEIS

### Executar App e Monitorar Downloads
```bash
# Terminal 1 (em tmux)
python skidrow_downloader.py

# Terminal 2 (Ctrl+B, C no tmux)
watch -n 10 transmission-remote -l
```

### Verificar Espaço e Downloads
```bash
df -h ~/storage/downloads && echo "---" && transmission-remote -l
```

### Limpeza Completa
```bash
pkg clean && pip cache purge && find ~ -type d -name __pycache__ -exec rm -rf {} +
```

### Reiniciar Transmission
```bash
pkill transmission-daemon && sleep 2 && transmission-daemon && sleep 1 && transmission-remote -l
```

---

✅ **Esta é a lista completa de todos os comandos úteis!**

💡 **Dica**: Salve os comandos mais usados como aliases no ~/.bashrc

📖 **Para mais informações**, consulte os outros arquivos de documentação!
