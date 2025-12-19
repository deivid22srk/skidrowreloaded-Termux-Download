# ❓ Perguntas Frequentes (FAQ)

## 📱 Sobre o Termux

### O que é Termux?
Termux é um emulador de terminal Android e ambiente Linux. Permite executar comandos Linux e instalar pacotes diretamente no seu dispositivo Android, sem necessidade de root.

### Preciso de root para usar?
**Não!** O aplicativo funciona perfeitamente em dispositivos sem root.

### Funciona em qualquer Android?
Sim, funciona no Android 7.0 (Nougat) ou superior.

### Por que não instalar da Google Play Store?
A versão da Play Store está desatualizada e não recebe mais atualizações. Use F-Droid ou GitHub.

---

## 🎮 Sobre o Skidrow Downloader

### O que faz este aplicativo?
Busca jogos no site Skidrow Reloaded e facilita o download dos arquivos torrent encontrados.

### É seguro usar?
O aplicativo em si é seguro. No entanto:
- ⚠️ Downloads de torrents podem conter malware
- ⚠️ Verifique a fonte antes de executar qualquer arquivo
- ⚠️ Use antivírus quando extrair arquivos baixados

### É legal baixar jogos assim?
⚠️ **Importante**: Baixar jogos pirateados é ilegal na maioria dos países. Este aplicativo é apenas para fins educacionais. Use apenas para:
- Fazer backup de jogos que você possui
- Testar jogos antes de comprar
- Jogar games descontinuados/indisponíveis

### Precisa de internet?
Sim, precisa de internet para:
- Buscar jogos
- Baixar torrents
- Durante todo o processo de download

### Consome muitos dados móveis?
- **Busca**: ~1-5 MB por busca
- **Download de torrents**: Depende do tamanho do jogo (geralmente 2-50 GB)
- 💡 **Recomendação**: Use WiFi para downloads grandes

---

## 💾 Sobre Downloads

### Quanto espaço preciso?
Depende do jogo:
- Jogos indie: 500 MB - 5 GB
- Jogos médios: 5 GB - 30 GB
- Jogos AAA: 30 GB - 150 GB
- 💡 Sempre mantenha pelo menos 10 GB livres extras

### Quanto tempo demora para baixar?
Depende de:
1. **Tamanho do jogo**: 5 GB vs 50 GB
2. **Velocidade da internet**: 10 Mbps vs 100 Mbps
3. **Seeders do torrent**: Mais seeders = mais rápido

**Exemplos:**
```
Jogo de 10 GB com internet de 50 Mbps:
~30-40 minutos

Jogo de 50 GB com internet de 10 Mbps:
~10-12 horas
```

### Posso pausar e retomar downloads?
✅ Sim! Com transmission você pode:
- Pausar: `transmission-remote -t 1 -S`
- Retomar: `transmission-remote -t 1 -s`
- Downloads sobrevivem a reinicializações

### Downloads continuam se eu fechar o Termux?
Depende:
- ✅ **Com wake-lock ativo**: Sim
- ✅ **Com otimização de bateria desativada**: Sim
- ❌ **Sem configuração**: Pode parar

**Solução:**
```bash
# Ativar wake-lock
termux-wake-lock

# Desativar otimização de bateria:
# Configurações > Apps > Termux > Bateria > Sem restrições
```

### Onde ficam os arquivos baixados?
Caminho padrão: `~/storage/downloads`

Que corresponde a: `/storage/emulated/0/Download`

Você pode mudar o caminho na tela de download.

### Como abrir os jogos baixados?
1. Os jogos são baixados compactados (ZIP, RAR, ISO)
2. Você precisa extrair no PC
3. Instalar conforme instruções incluídas
4. **Importante**: Não é possível jogar direto no Android (são jogos de PC)

---

## 🔧 Problemas Técnicos

### "ModuleNotFoundError: No module named 'textual'"

**Solução:**
```bash
pip install --upgrade textual requests beautifulsoup4
```

### "Permission denied" ao executar

**Solução:**
```bash
chmod +x skidrow_downloader.py
```

### Interface aparece quebrada/distorcida

**Possíveis causas e soluções:**

1. **Termux desatualizado**
```bash
pkg update && pkg upgrade
```

2. **Terminal muito pequeno**
- Ajuste o tamanho da fonte
- Use o dispositivo em modo retrato
- Toque longo > Estilo > Fonte menor

3. **Problema com renderização**
```bash
pkg reinstall python
pip install --force-reinstall textual
```

### "Cannot connect to skidrowreloaded.com"

**Verificações:**

1. **Internet funcionando?**
```bash
ping -c 3 google.com
```

2. **Site está no ar?**
```bash
curl -I https://www.skidrowreloaded.com
```

3. **DNS funcionando?**
```bash
nslookup skidrowreloaded.com
```

**Soluções:**
```bash
# Usar DNS alternativo
echo "nameserver 8.8.8.8" > $PREFIX/etc/resolv.conf

# Aguardar se site estiver fora do ar
# Tentar mais tarde
```

### "No space left on device"

**Solução:**
```bash
# Verificar espaço
df -h

# Limpar cache
pkg clean
pip cache purge

# Limpar downloads antigos
cd ~/storage/downloads
rm -rf arquivos_antigos

# Mover para cartão SD se disponível
```

### Transmission não inicia

**Verificações:**

1. **Está instalado?**
```bash
which transmission-remote
# Se não aparecer nada:
pkg install transmission
```

2. **Daemon rodando?**
```bash
pgrep transmission
# Se não mostrar número, iniciar:
transmission-daemon
```

3. **Porta bloqueada?**
```bash
# Matar processo antigo
pkill transmission-daemon
# Aguardar 5 segundos
sleep 5
# Reiniciar
transmission-daemon
```

4. **Arquivo de config corrompido?**
```bash
# Backup config antiga
mv ~/.config/transmission-daemon ~/.config/transmission-daemon.bak
# Reiniciar daemon (cria nova config)
transmission-daemon
```

### Download fica em 0%

**Causas comuns:**

1. **Torrent morto (sem seeders)**
```bash
transmission-remote -t 1 -i | grep Seeders
# Se mostrar "Seeders: 0", escolha outro link
```

2. **Porta não está aberta**
```bash
# Verificar status de porta
transmission-remote -pt
```

3. **Falta de espaço**
```bash
df -h ~/storage/downloads
```

**Soluções:**
- Tentar outro link do mesmo jogo
- Aguardar alguns minutos (às vezes demora para conectar)
- Verificar se não está pausado: `transmission-remote -t 1 -s`

---

## 🎨 Interface e Usabilidade

### Não consigo tocar nos botões

**Soluções:**
1. Use teclas de navegação (setas + ENTER)
2. Ative "Extra Keys" no Termux
3. Ajuste tamanho da fonte
4. Use toque longo para seleção

### Texto muito pequeno/grande

```bash
# Ajustar no Termux:
# Toque longo > Estilo > Selecionar tamanho de fonte
```

### Cores estão estranhas

```bash
# Instalar ferramenta de temas
pkg install termux-styling

# Executar e escolher tema
termux-style
```

### Teclado cobre o app

- Use teclado flutuante do Android
- Configure teclado para modo compacto
- Esconda teclado quando não precisar (botão voltar)

---

## 📊 Performance

### App está lento

**Otimizações:**

1. **Fechar outros apps**
```bash
# Ver uso de memória
free -h
```

2. **Limpar cache**
```bash
# Cache do Python
find ~ -type d -name __pycache__ -exec rm -rf {} +

# Cache do pip
pip cache purge
```

3. **Reiniciar Termux**
- Feche e abra novamente o Termux

4. **Verificar CPU**
```bash
pkg install htop
htop
# Pressione F10 para sair
```

### Bateria acaba rápido

**Normal durante downloads!** Mas você pode:

1. **Limitar velocidade de upload**
```bash
transmission-remote -u 50  # 50 KB/s
```

2. **Reduzir peers**
```bash
# Editar config
nano ~/.config/transmission-daemon/settings.json
# Alterar "peer-limit-global": 200 para 50
```

3. **Baixar com dispositivo carregando**

### Esquenta muito durante download

**Normal!** Downloads intensivos usam rede constantemente.

**Dicas:**
- Remova capa do celular
- Coloque perto de ventilador
- Não use o celular enquanto baixa
- Ative modo avião + WiFi (desliga dados móveis)

---

## 🔐 Segurança

### É seguro baixar torrents?

⚠️ **Riscos:**
- Arquivos podem conter vírus/malware
- ISP pode detectar torrents (use VPN)
- Jogos crackeados podem ter trojans

**Proteções:**
1. Use VPN sempre
2. Escaneie arquivos com antivírus
3. Não execute arquivos suspeitos
4. Leia comentários no site antes de baixar

### Preciso de VPN?

**Recomendado!** Especialmente se seu ISP ou país monitora torrents.

**VPNs para Termux:**
```bash
# OpenVPN
pkg install openvpn

# WireGuard
pkg install wireguard-tools
```

### Alguém pode ver o que estou baixando?

**Sem VPN**: Sim, seu ISP pode ver
**Com VPN**: Não, tráfego é criptografado

### O app coleta meus dados?

**Não!** O aplicativo:
- ✅ É código aberto
- ✅ Roda localmente
- ✅ Não envia dados para servidores externos
- ✅ Não tem telemetria

Apenas acessa:
- Site do Skidrow (necessário para busca)
- Trackers de torrent (necessário para download)

---

## 💡 Dicas e Truques

### Como baixar mais rápido?

1. **Use WiFi 5GHz** (se disponível)
2. **Escolha torrents com mais seeders**
3. **Abra portas no roteador** (avançado)
4. **Configure transmission**:
```bash
transmission-remote -d 0  # Remove limite de download
transmission-remote -u 50  # Limita upload (ajuda download)
```

### Como economizar dados móveis?

1. **Baixe apenas em WiFi**
2. **Configure firewall** para bloquear Termux em dados móveis:
   - Apps > Termux > Dados móveis > Desativar

### Posso baixar vários jogos ao mesmo tempo?

✅ **Sim!** Transmission suporta múltiplos downloads.

**Recomendações:**
- Não baixe mais de 2-3 jogos grandes simultaneamente
- Isso divide a velocidade de download
- Pode deixar sistema lento

### Como organizar downloads?

```bash
# Criar estrutura de pastas
mkdir -p ~/storage/downloads/Jogos/{Acao,RPG,Esporte,Aventura}

# Mover jogos após download
mv ~/storage/downloads/GTA* ~/storage/downloads/Jogos/Acao/
```

### Como saber se um torrent é bom?

**Verifique:**
1. **Seeders**: Quanto mais, melhor (mínimo 5)
2. **Data**: Postagens recentes são melhores
3. **Comentários**: Leia antes de baixar
4. **Grupo**: Torrents de grupos conhecidos (SKIDROW, CODEX, etc.)

---

## 🆘 Ainda com Problemas?

### Onde conseguir ajuda?

1. **Documentação**: Leia README.md e TERMUX_SETUP.md
2. **Exemplos**: Veja EXAMPLES.md
3. **Comunidade Termux**:
   - Reddit: r/termux
   - GitHub Issues: github.com/termux/termux-app
4. **Re-instale**: Às vezes resolver tudo:
```bash
pip uninstall textual requests beautifulsoup4
pip install textual requests beautifulsoup4
```

### Como reportar bugs?

Se encontrou um bug:
1. Anote a mensagem de erro completa
2. Anote o que estava fazendo quando aconteceu
3. Verifique versões:
```bash
python --version
pip show textual
pkg show termux-app
```

### Reset completo

Se nada funcionar:
```bash
# Backup de dados importantes primeiro!

# Remover instalação
rm skidrow_downloader.py
pip uninstall textual requests beautifulsoup4 lxml

# Reinstalar tudo
pkg update && pkg upgrade
pip install textual requests beautifulsoup4 lxml

# Baixar app novamente
# Executar
```

---

## 📚 Glossário

**Termux**: Emulador de terminal para Android
**TUI**: Text User Interface (Interface de texto)
**Torrent**: Protocolo P2P para compartilhamento de arquivos
**Magnet Link**: Link que identifica torrent sem arquivo .torrent
**Seeder**: Usuário compartilhando arquivo completo
**Leecher**: Usuário baixando arquivo
**Daemon**: Processo que roda em segundo plano
**Wake Lock**: Impede dispositivo de dormir
**tmux**: Multiplexador de terminal
**VPN**: Virtual Private Network (Rede privada virtual)

---

✅ **Essas são as dúvidas mais comuns!**

Se sua pergunta não está aqui, consulte a documentação completa ou comunidade Termux.

🎮 Boa sorte com seus downloads!
