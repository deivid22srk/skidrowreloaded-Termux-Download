# 📱 Guia de Configuração Completo para Termux

## 📥 Instalando o Termux

### 1. Baixar o Termux

**⚠️ IMPORTANTE**: Não instale o Termux da Google Play Store (está desatualizado)!

**Opções recomendadas:**

#### Opção A: F-Droid (Recomendado)
1. Baixe o F-Droid em: https://f-droid.org/
2. Instale o F-Droid no seu Android
3. Abra o F-Droid e busque por "Termux"
4. Instale o Termux oficial

#### Opção B: GitHub Releases
1. Acesse: https://github.com/termux/termux-app/releases
2. Baixe o arquivo APK mais recente (ex: `termux-app_vX.XXX.apk`)
3. Instale o APK no seu Android

## ⚙️ Configuração Inicial do Termux

### 1. Primeira Execução

Ao abrir o Termux pela primeira vez, aguarde a instalação inicial dos pacotes.

### 2. Atualizar Repositórios

```bash
pkg update && pkg upgrade -y
```

⏱️ Este processo pode demorar alguns minutos dependendo da conexão.

### 3. Conceder Permissões de Armazenamento

```bash
termux-setup-storage
```

✅ Clique em "Permitir" quando o Android solicitar permissão.

Isso criará a pasta `~/storage` com atalhos para:
- `downloads` - Pasta de downloads do Android
- `dcim` - Câmera
- `pictures` - Imagens
- `music` - Músicas
- `movies` - Vídeos
- `shared` - Armazenamento compartilhado

### 4. Instalar Pacotes Essenciais

```bash
pkg install wget curl git nano vim -y
```

## 🎮 Instalando o Skidrow Downloader

### Método 1: Instalação Automática

```bash
# Navegar para o diretório do projeto
cd /caminho/para/o/projeto

# Executar script de instalação
bash install.sh
```

### Método 2: Instalação Manual

```bash
# 1. Atualizar sistema
pkg update && pkg upgrade -y

# 2. Instalar Python
pkg install python python-pip -y

# 3. Instalar transmission
pkg install transmission -y

# 4. Instalar dependências Python
pip install textual requests beautifulsoup4 lxml

# 5. Dar permissão de execução
chmod +x skidrow_downloader.py

# 6. Executar
python skidrow_downloader.py
```

## 🔧 Configurações Avançadas do Termux

### Teclado Aprimorado

Ative a linha extra de teclas especiais:

1. Toque longo na tela do Termux
2. Selecione "More..."
3. Ative "Extra Keys"

Isso adiciona teclas como ESC, CTRL, ALT, TAB, etc.

### Atalhos de Teclado Úteis

| Atalho | Ação |
|--------|------|
| `Ctrl + C` | Interromper comando |
| `Ctrl + D` | Sair do shell |
| `Ctrl + L` | Limpar tela |
| `Volume + ↑/↓` | Rolar tela |
| `Volume + Q` | Mostrar teclas extras |

### Configurar Wake Lock

Evita que o Termux pare quando a tela desliga:

```bash
termux-wake-lock
```

Para desativar:
```bash
termux-wake-unlock
```

### Verificar Wake Lock

```bash
termux-wake-status
```

## 📦 Gerenciamento de Pacotes

### Comandos Básicos do pkg

```bash
# Buscar pacote
pkg search <nome>

# Instalar pacote
pkg install <nome>

# Remover pacote
pkg uninstall <nome>

# Listar pacotes instalados
pkg list-installed

# Atualizar tudo
pkg update && pkg upgrade
```

### Pacotes Úteis Adicionais

```bash
# Editor de texto avançado
pkg install nano vim

# Navegador web terminal
pkg install lynx

# Gerenciador de arquivos
pkg install mc

# Monitor de sistema
pkg install htop

# Compactação de arquivos
pkg install zip unzip

# Multiplexador de terminal (recomendado!)
pkg install tmux

# Download manager alternativo
pkg install aria2
```

## 🔐 Configurações de Segurança

### Habilitar Autenticação SSH (opcional)

```bash
# Instalar OpenSSH
pkg install openssh

# Gerar chave SSH
ssh-keygen

# Iniciar servidor SSH
sshd

# Ver endereço IP
ifconfig
```

## 📂 Estrutura de Diretórios do Termux

```
/data/data/com.termux/files/
├── home/           # Diretório home (~)
│   ├── storage/    # Links para armazenamento Android
│   └── ...
└── usr/            # Binários e bibliotecas do sistema
    ├── bin/        # Executáveis
    ├── lib/        # Bibliotecas
    └── ...
```

## 🌐 Configurar Transmission Daemon

### Configuração Básica

```bash
# Criar diretório de configuração
mkdir -p ~/.config/transmission-daemon

# Iniciar daemon (cria configuração padrão)
transmission-daemon

# Parar daemon
pkill transmission-daemon
```

### Editar Configuração

```bash
# Editar settings.json
nano ~/.config/transmission-daemon/settings.json
```

Configurações importantes:

```json
{
    "download-dir": "/data/data/com.termux/files/home/storage/downloads",
    "incomplete-dir": "/data/data/com.termux/files/home/storage/downloads/.incomplete",
    "rpc-enabled": true,
    "rpc-whitelist-enabled": false,
    "speed-limit-down": 1000,
    "speed-limit-down-enabled": false,
    "speed-limit-up": 100,
    "speed-limit-up-enabled": true
}
```

### Comandos Úteis do Transmission

```bash
# Listar torrents
transmission-remote -l

# Adicionar torrent
transmission-remote -a "link_magnet_ou_torrent"

# Remover torrent
transmission-remote -t <ID> -r

# Remover torrent e dados
transmission-remote -t <ID> -rad

# Ver informações
transmission-remote -t <ID> -i

# Pausar
transmission-remote -t <ID> -S

# Retomar
transmission-remote -t <ID> -s

# Definir limite de velocidade (KB/s)
transmission-remote -d 500  # Download
transmission-remote -u 50   # Upload
```

## 🎨 Personalizar Termux

### Mudar Cores e Fontes

```bash
# Instalar pacote de personalização
pkg install termux-styling

# Executar ferramenta de estilo
termux-style
```

### Configurar .bashrc

```bash
# Editar .bashrc
nano ~/.bashrc

# Adicionar aliases úteis:
alias ll='ls -la'
alias update='pkg update && pkg upgrade'
alias c='clear'

# Salvar: Ctrl+O, Enter, Ctrl+X
```

Recarregar configuração:
```bash
source ~/.bashrc
```

## 💾 Backup e Restauração

### Backup do Termux

```bash
# Backup completo
cd ~
tar -czf termux-backup.tar.gz .

# Mover para armazenamento compartilhado
mv termux-backup.tar.gz ~/storage/downloads/
```

### Restaurar Backup

```bash
cd ~
tar -xzf ~/storage/downloads/termux-backup.tar.gz
```

## 📱 Plugins Úteis do Termux

### Termux:API

Permite acessar recursos do Android via terminal.

**Instalação:**
1. Instalar "Termux:API" da F-Droid
2. No Termux: `pkg install termux-api`

**Exemplos de uso:**

```bash
# Tirar foto
termux-camera-photo ~/photo.jpg

# Fazer toast (notificação)
termux-toast "Olá, mundo!"

# Vibrar
termux-vibrate -d 1000

# Ver bateria
termux-battery-status

# Obter localização
termux-location

# Ligar/desligar WiFi
termux-wifi-enable true
termux-wifi-enable false
```

### Termux:Widget

Crie widgets na tela inicial para executar scripts.

**Instalação:**
1. Instalar "Termux:Widget" da F-Droid
2. Criar pasta: `mkdir -p ~/.shortcuts`
3. Adicionar scripts na pasta `.shortcuts`

**Exemplo de script:**

```bash
# Criar script
nano ~/.shortcuts/download_monitor.sh

# Conteúdo:
#!/bin/bash
transmission-remote -l | termux-toast
```

```bash
chmod +x ~/.shortcuts/download_monitor.sh
```

## 🐛 Solução de Problemas Comuns

### Problema: "Repository is under maintenance"

```bash
pkg update
# Se falhar, tente:
termux-change-repo
# Selecione um mirror diferente
```

### Problema: "Permission denied"

```bash
chmod +x <arquivo>
```

### Problema: "Cannot connect to the internet"

```bash
# Verificar conectividade
ping -c 3 google.com

# Verificar DNS
nslookup google.com

# Redefinir cache DNS
pkg reinstall resolv-conf
```

### Problema: "Storage not accessible"

```bash
# Reconfigurar storage
termux-setup-storage

# Verificar no Android:
# Configurações > Apps > Termux > Permissões > Armazenamento (ativar)
```

### Problema: App para de funcionar em segundo plano

```bash
# Usar wake-lock
termux-wake-lock

# Usar tmux para manter sessões
pkg install tmux
tmux new -s mysession

# Desativar otimização de bateria do Android:
# Configurações > Apps > Termux > Bateria > Sem restrições
```

## 📚 Recursos Adicionais

### Documentação Oficial
- https://wiki.termux.com/

### Comunidade
- Reddit: r/termux
- GitHub: https://github.com/termux/termux-app

### Tutoriais
- https://wiki.termux.com/wiki/Main_Page
- https://termux.com/

## 🎯 Dicas Finais

1. **Sempre use `pkg` ao invés de `apt`** no Termux
2. **Não tente usar `sudo`** - você já tem acesso total no ambiente Termux
3. **Mantenha o Termux atualizado** regularmente
4. **Use tmux** para manter processos rodando quando você fecha o app
5. **Configure wake-lock** para downloads longos
6. **Faça backups** regularmente de scripts e configurações importantes

---

✅ **Agora você está pronto para usar o Skidrow Game Downloader no Termux!**

Execute:
```bash
python skidrow_downloader.py
```

🎮 Divirta-se!
