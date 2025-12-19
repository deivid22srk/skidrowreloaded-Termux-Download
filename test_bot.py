#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
from pathlib import Path

def print_header(text):
    print(f"\n{'='*50}")
    print(f"  {text}")
    print(f"{'='*50}\n")

def check_python():
    print("🐍 Verificando Python...")
    version = sys.version.split()[0]
    major, minor = sys.version_info[:2]
    
    if major >= 3 and minor >= 10:
        print(f"   ✅ Python {version} - OK")
        return True
    else:
        print(f"   ❌ Python {version} - Precisa Python 3.10+")
        return False

def check_module(module_name, package_name=None):
    if package_name is None:
        package_name = module_name
    
    try:
        __import__(module_name)
        print(f"   ✅ {package_name} - Instalado")
        return True
    except ImportError:
        print(f"   ❌ {package_name} - NÃO instalado")
        print(f"      Instale com: pip install {package_name}")
        return False

def check_command(command):
    try:
        result = subprocess.run(
            [command, '--version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            version = result.stdout.split('\n')[0] if result.stdout else "version unknown"
            print(f"   ✅ {command} - {version}")
            return True
    except:
        pass
    
    print(f"   ⚠️  {command} - NÃO instalado (necessário)")
    print(f"      Instale com: pkg install {command}")
    return False

def check_transmission_daemon():
    print("🔥 Verificando Transmission daemon...")
    try:
        result = subprocess.run(
            ['pgrep', 'transmission'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0 and result.stdout.strip():
            print(f"   ✅ Transmission daemon rodando (PID: {result.stdout.strip()})")
            return True
        else:
            print(f"   ⚠️  Transmission daemon NÃO está rodando")
            print(f"      Inicie com: transmission-daemon")
            return False
    except:
        print(f"   ❌ Erro ao verificar daemon")
        return False

def check_storage():
    print("📁 Verificando acesso ao armazenamento...")
    
    storage_path = Path.home() / "storage"
    downloads_path = storage_path / "downloads"
    
    if storage_path.exists():
        print(f"   ✅ Pasta storage existe")
        if downloads_path.exists():
            print(f"   ✅ Pasta downloads acessível")
            return True
        else:
            print(f"   ⚠️  Pasta downloads não encontrada")
            return False
    else:
        print(f"   ❌ Pasta storage não encontrada")
        print(f"      Execute: termux-setup-storage")
        return False

def check_bot_file():
    print("📄 Verificando arquivo do bot...")
    
    bot_file = Path("telegram_bot.py")
    
    if bot_file.exists():
        print(f"   ✅ telegram_bot.py encontrado")
        
        # Verificar token
        content = bot_file.read_text()
        if 'BOT_TOKEN = "7718948467:' in content:
            print(f"   ✅ Token do bot configurado")
        else:
            print(f"   ⚠️  Token pode estar incorreto")
        
        if bot_file.stat().st_mode & 0o111:
            print(f"   ✅ Permissão de execução OK")
        else:
            print(f"   ⚠️  Sem permissão de execução")
            print(f"      Execute: chmod +x telegram_bot.py")
        
        return True
    else:
        print(f"   ❌ telegram_bot.py NÃO encontrado")
        return False

def check_internet():
    print("🌐 Verificando conexão com internet...")
    
    try:
        import requests
        response = requests.get("https://api.telegram.org", timeout=5)
        if response.status_code in [200, 401, 404]:
            print(f"   ✅ Conexão com Telegram API OK")
            return True
        else:
            print(f"   ⚠️  Conexão instável")
            return False
    except:
        print(f"   ❌ Sem conexão com internet")
        return False

def main():
    print_header("🤖 TESTE DE INSTALAÇÃO DO BOT")
    print("Verificando se tudo está pronto para usar o Telegram Bot...\n")
    
    results = {
        "Python": check_python(),
        "Internet": check_internet(),
    }
    
    print("\n📦 Verificando módulos Python necessários...")
    results["requests"] = check_module("requests")
    results["bs4"] = check_module("bs4", "beautifulsoup4")
    results["lxml"] = check_module("lxml")
    results["telegram"] = check_module("telegram", "python-telegram-bot")
    
    print("\n🔧 Verificando ferramentas necessárias...")
    results["transmission"] = check_command("transmission-remote")
    results["transmission_daemon"] = check_transmission_daemon()
    
    print()
    results["storage"] = check_storage()
    
    print()
    results["bot_file"] = check_bot_file()
    
    print_header("📊 RESULTADO")
    
    total = len(results)
    passed = sum(results.values())
    failed = total - passed
    
    print(f"Total: {total}")
    print(f"✅ Passou: {passed}")
    print(f"❌ Falhou: {failed}")
    
    print("\n" + "="*50)
    
    if passed == total:
        print("🎉 TUDO OK! Você pode usar o bot!")
        print("\nPara executar:")
        print("   1. termux-wake-lock")
        print("   2. python telegram_bot.py")
        print("\nDepois:")
        print("   3. Abrir Telegram")
        print("   4. Buscar seu bot")
        print("   5. Enviar /start")
    else:
        print("⚠️  ALGUMAS VERIFICAÇÕES FALHARAM")
        print("\nProblemas encontrados:")
        
        for item, status in results.items():
            if not status:
                print(f"   ❌ {item}")
        
        print("\n🔧 Soluções:")
        
        if not results.get("Python"):
            print("   • Atualize o Termux: pkg update && pkg upgrade")
        
        if not any([results.get("requests"), results.get("bs4"), 
                   results.get("lxml"), results.get("telegram")]):
            print("   • Instale dependências: pip install -r requirements_bot.txt")
        
        if not results.get("transmission"):
            print("   • Instale transmission: pkg install transmission")
        
        if not results.get("transmission_daemon"):
            print("   • Inicie daemon: transmission-daemon")
        
        if not results.get("storage"):
            print("   • Configure storage: termux-setup-storage")
        
        if not results.get("bot_file"):
            print("   • Certifique-se de estar no diretório correto")
        
        if not results.get("Internet"):
            print("   • Verifique sua conexão WiFi/dados móveis")
    
    print("="*50)
    print("\n📚 Para mais informações, leia:")
    print("   • README_BOT.md - Instruções completas")
    print("   • FAQ.md - Perguntas frequentes")
    print("   • COMANDOS.md - Lista de comandos")
    print()

if __name__ == "__main__":
    main()
