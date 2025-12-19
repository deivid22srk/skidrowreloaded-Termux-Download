#!/bin/bash

echo "🎮 Instalando Skidrow Game Downloader para Termux..."
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
pip install -r requirements.txt

echo ""
echo "🔧 Configurando permissões de execução..."
chmod +x skidrow_downloader.py

echo ""
echo "✅ Instalação concluída!"
echo ""
echo "🚀 Para executar o aplicativo, use:"
echo "   python skidrow_downloader.py"
echo ""
echo "   ou"
echo ""
echo "   ./skidrow_downloader.py"
echo ""
echo "📖 Leia o README.md para mais informações!"
echo ""
