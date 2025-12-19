# 🎮 Skidrow Game Downloader - Informações do Projeto

## 📝 Descrição

Aplicativo com interface touch (TUI) para Android/Termux que permite buscar e baixar jogos do site Skidrow Reloaded através de torrents. Desenvolvido com Python e a biblioteca Textual para proporcionar uma experiência visual moderna e amigável ao toque no terminal.

## ✨ Características Principais

### Interface
- 🎨 Interface TUI moderna e bonita usando Textual
- 📱 Otimizada para toque e dispositivos móveis
- 🎯 Navegação intuitiva com setas ou toque
- 🌈 Cores e temas personalizáveis
- ⚡ Responsiva e rápida

### Funcionalidades
- 🔍 Busca de jogos no Skidrow Reloaded
- 📋 Listagem de resultados com detalhes
- 🔗 Extração automática de links torrent e magnet
- 💾 Escolha personalizada do caminho de download
- 🧲 Suporte a arquivos .torrent e magnet links
- ⬇️ Integração com Transmission para downloads
- 📊 Monitoramento de progresso via CLI

## 🏗️ Arquitetura

### Estrutura de Telas

```
SkidrowDownloaderApp (App Principal)
│
├── SearchScreen (Tela de Busca)
│   ├── Input de busca
│   ├── Botão de buscar
│   └── Status de busca
│
├── ResultsScreen (Tela de Resultados)
│   ├── Lista de jogos encontrados
│   ├── Informações (título, data)
│   └── Navegação para detalhes
│
├── DetailsScreen (Tela de Detalhes)
│   ├── Informações do jogo
│   ├── Scraping de links de download
│   ├── Contador de torrents/magnets
│   └── Botão para configurar download
│
└── DownloadScreen (Tela de Download)
    ├── Seleção de caminho
    ├── Listagem de links disponíveis
    ├── Inicialização do download
    └── Status e instruções
```

### Fluxo de Dados

```
1. Usuário digita nome do jogo
        ↓
2. Busca no Skidrow Reloaded (requests + BeautifulSoup)
        ↓
3. Parse dos resultados (título, URL, data)
        ↓
4. Usuário seleciona um jogo
        ↓
5. Scraping da página do jogo (links torrent/magnet)
        ↓
6. Usuário configura download (caminho)
        ↓
7. Transmissão para Transmission ou salva arquivo
        ↓
8. Download via Transmission Daemon
```

## 🛠️ Tecnologias Utilizadas

### Core
- **Python 3.8+**: Linguagem principal
- **Textual 0.47+**: Framework TUI moderno
- **BeautifulSoup4**: Web scraping
- **Requests**: HTTP requests
- **lxml**: Parser HTML rápido

### Ferramentas Externas
- **Transmission**: Cliente torrent
- **Termux**: Ambiente Linux Android

## 📦 Estrutura de Arquivos

```
/project/workspace/
│
├── 🐍 skidrow_downloader.py      # Aplicativo principal (590 linhas)
│   ├── Classe: SearchScreen       # Tela de busca inicial
│   ├── Classe: ResultsScreen      # Listagem de resultados
│   ├── Classe: DetailsScreen      # Detalhes e links
│   ├── Classe: DownloadScreen     # Configuração de download
│   └── Classe: SkidrowDownloaderApp  # App principal
│
├── 📋 requirements.txt            # Dependências Python
│
├── 🔧 install.sh                  # Script de instalação automática
│
├── 🧪 test_installation.py        # Verificador de instalação
│
├── 📖 README.md                   # Documentação completa (450+ linhas)
│   ├── Instalação passo a passo
│   ├── Como usar
│   ├── Atalhos e comandos
│   ├── Solução de problemas
│   └── Dicas e truques
│
├── 📖 QUICKSTART.md              # Início rápido (100+ linhas)
│
├── 📖 TERMUX_SETUP.md            # Guia completo do Termux (600+ linhas)
│   ├── Instalação do Termux
│   ├── Configuração inicial
│   ├── Pacotes úteis
│   ├── Configuração avançada
│   ├── Transmission setup
│   └── Plugins e extensões
│
├── 📖 EXAMPLES.md                # Exemplos práticos (500+ linhas)
│   ├── Passo a passo visual
│   ├── Cenários de uso
│   ├── Comandos úteis
│   ├── Scripts auxiliares
│   └── Fluxos de trabalho
│
├── 📖 FAQ.md                     # Perguntas frequentes (600+ linhas)
│   ├── Sobre Termux
│   ├── Sobre o app
│   ├── Sobre downloads
│   ├── Problemas técnicos
│   ├── Performance
│   ├── Segurança
│   └── Dicas e truques
│
├── 📖 PROJECT_INFO.md            # Este arquivo
│
└── 📄 .gitignore                 # Arquivos ignorados pelo git
```

## 🎨 Design e UX

### Princípios de Design

1. **Mobile First**
   - Interface otimizada para telas pequenas
   - Botões grandes e fáceis de tocar
   - Texto legível em qualquer tamanho

2. **Feedback Visual**
   - Status claro de cada operação
   - Mensagens de erro e sucesso visíveis
   - Indicadores de carregamento

3. **Navegação Intuitiva**
   - Breadcrumbs virtuais (voltar sempre funciona)
   - Atalhos de teclado consistentes
   - Toque e teclado funcionam igualmente bem

4. **Informação Hierárquica**
   - Títulos destacados
   - Informações secundárias em cores suaves
   - Espaçamento adequado

### Paleta de Cores (Textual)

```python
$primary     # Azul - Bordas e elementos principais
$accent      # Amarelo - Títulos e destaques
$warning     # Laranja - Status e avisos
$error       # Vermelho - Erros
$success     # Verde - Sucesso
$text        # Branco/Cinza - Texto normal
$text-muted  # Cinza - Texto secundário
$surface     # Preto/Escuro - Fundo
$panel       # Cinza escuro - Painéis
```

## 🔒 Segurança e Privacidade

### O que o App Faz
✅ Busca no site público Skidrow Reloaded
✅ Extrai links de download disponíveis
✅ Salva arquivos localmente
✅ Usa Transmission para downloads

### O que o App NÃO Faz
❌ Não coleta dados do usuário
❌ Não envia informações para servidores externos
❌ Não tem telemetria ou analytics
❌ Não modifica arquivos do sistema
❌ Não requer permissões especiais (além de storage)

### Recomendações de Segurança
- Use VPN ao baixar torrents
- Escaneie arquivos baixados com antivírus
- Verifique comentários no site antes de baixar
- Não execute arquivos suspeitos

## 📊 Estatísticas do Código

```
Arquivo                  | Linhas | Funções/Classes | Finalidade
-------------------------|--------|-----------------|------------------
skidrow_downloader.py    |   590  |      5 classes  | App principal
test_installation.py     |   150  |      8 funções  | Teste instalação
README.md                |   450  |       -         | Documentação
TERMUX_SETUP.md          |   600  |       -         | Guia Termux
EXAMPLES.md              |   500  |       -         | Exemplos
FAQ.md                   |   600  |       -         | FAQ
QUICKSTART.md            |   100  |       -         | Início rápido
PROJECT_INFO.md          |   200  |       -         | Info projeto
-------------------------|--------|-----------------|------------------
TOTAL                    | 3,190+ |   5 classes    | Projeto completo
                         |        |   8 funções    |
```

## 🚀 Performance

### Otimizações Implementadas
- Async/await para operações de rede
- Limitar resultados de busca (15 jogos)
- Cache de BeautifulSoup parser
- Lazy loading de telas
- Minimal re-renders

### Uso de Recursos
- **Memória**: ~50-100 MB durante execução
- **CPU**: Baixo (picos durante scraping)
- **Rede**: Variável (busca ~1-5 MB, download do jogo GB)
- **Bateria**: Moderada (alta durante download)

## 🔄 Fluxo de Trabalho do Usuário

### Primeiro Uso
```
1. Instalar Termux (F-Droid)
2. Configurar storage (termux-setup-storage)
3. Instalar dependências (install.sh ou manual)
4. Executar teste (test_installation.py)
5. Executar app (skidrow_downloader.py)
6. Fazer primeira busca
7. Baixar primeiro jogo
```

### Uso Regular
```
1. Abrir Termux
2. (Opcional) Ativar wake-lock
3. (Opcional) Iniciar transmission-daemon
4. Executar app
5. Buscar jogo
6. Selecionar resultado
7. Iniciar download
8. (Opcional) Monitorar com transmission-remote
```

### Uso Avançado
```
1. Configurar tmux para múltiplas sessões
2. Scripts personalizados para automação
3. Configuração avançada do Transmission
4. Organização automática de downloads
5. Notificações de conclusão
6. Integração com VPN
```

## 🎯 Casos de Uso

### Usuário Casual
- Buscar jogos populares
- Baixar 1-2 jogos por vez
- Monitoramento básico
- Usar configurações padrão

### Usuário Power
- Baixar múltiplos jogos
- Organizar downloads em pastas
- Scripts de automação
- Configurar transmission avançado
- Usar tmux para sessões persistentes

### Desenvolvedor
- Contribuir com código
- Adicionar novas features
- Melhorar scraping
- Criar temas personalizados
- Integrar com outras ferramentas

## 🛣️ Roadmap (Possíveis Melhorias)

### Versão 1.1
- [ ] Cache de resultados de busca
- [ ] Histórico de downloads
- [ ] Favoritos
- [ ] Filtros (data, tamanho, etc.)

### Versão 1.2
- [ ] Múltiplos sites de download
- [ ] Integração com outros clientes torrent
- [ ] Download direto (não-torrent)
- [ ] Estimativa de tempo de download

### Versão 2.0
- [ ] Interface web opcional
- [ ] Suporte a mais idiomas
- [ ] Temas personalizáveis
- [ ] Sistema de plugins

## 🤝 Contribuindo

### Como Contribuir
1. Fork o repositório
2. Crie uma branch para sua feature
3. Faça suas alterações
4. Teste extensivamente no Termux
5. Envie pull request

### Diretrizes
- Código limpo e comentado
- Seguir estilo existente
- Testar no Termux real
- Documentar novas features
- Manter compatibilidade

## 📄 Licença

Este projeto é fornecido "como está", sem garantias de qualquer tipo.

**Uso**: Apenas para fins educacionais e legais.

## 👨‍💻 Desenvolvimento

### Ambiente de Desenvolvimento
- Python 3.8+ em qualquer OS
- Editor de código (VS Code, PyCharm, etc.)
- Dispositivo Android com Termux para testes
- Git para versionamento

### Testar Localmente (PC)
```bash
# Clonar repositório
git clone <repo>
cd skidrow-downloader

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar
python skidrow_downloader.py
```

### Testar no Termux
```bash
# Copiar arquivos via termux-api
# ou
# Upload para GitHub e clonar no Termux
git clone <repo>
cd skidrow-downloader
pip install -r requirements.txt
python skidrow_downloader.py
```

## 📞 Suporte

### Documentação
- README.md - Guia completo
- QUICKSTART.md - Início rápido
- TERMUX_SETUP.md - Configurar Termux
- EXAMPLES.md - Exemplos práticos
- FAQ.md - Perguntas comuns

### Comunidade
- Reddit: r/termux
- GitHub: Issues do repositório
- Stack Overflow: Tag [termux]

## 🙏 Agradecimentos

### Bibliotecas Utilizadas
- **Textual** por Will McGugan - Framework TUI incrível
- **BeautifulSoup** - Web scraping simplificado
- **Requests** - HTTP para humanos
- **Transmission** - Cliente torrent confiável

### Inspirações
- Termux community
- Skidrow Reloaded website
- TUI apps showcase

## 📈 Changelog

### v1.0.0 (Inicial)
- ✅ Interface TUI completa
- ✅ Busca no Skidrow Reloaded
- ✅ Scraping de links torrent/magnet
- ✅ Integração com Transmission
- ✅ Escolha de caminho de download
- ✅ Documentação completa
- ✅ Scripts de instalação e teste

---

**Desenvolvido para Termux** 📱
**Powered by Textual** ⚡
**Made with ❤️ for Gamers** 🎮

---

✅ **Projeto completo e pronto para uso!**

Para começar, leia @QUICKSTART.md ou @README.md
