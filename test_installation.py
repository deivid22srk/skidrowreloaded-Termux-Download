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
    
    if major >= 3 and minor >= 8:
        print(f"   ✅ Python {version} - OK")
        return True
    else:
        print(f"   ❌ Python {version} - Precisa Python 3.8+")
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
    
    print(f"   ⚠️  {command} - NÃO instalado (opcional)")
    print(f"      Instale com: pkg install {command}")
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

def check_app_file():
    print("📄 Verificando arquivo do aplicativo...")
    
    app_file = Path("skidrow_downloader.py")
    
    if app_file.exists():
        print(f"   ✅ skidrow_downloader.py encontrado")
        
        if app_file.stat().st_mode & 0o111:
            print(f"   ✅ Permissão de execução OK")
        else:
            print(f"   ⚠️  Sem permissão de execução")
            print(f"      Execute: chmod +x skidrow_downloader.py")
        
        return True
    else:
        print(f"   ❌ skidrow_downloader.py NÃO encontrado")
        return False

def check_internet():
    print("🌐 Verificando conexão com internet...")
    
    try:
        import requests
        response = requests.get("https://www.google.com", timeout=5)
        if response.status_code == 200:
            print(f"   ✅ Conexão com internet OK")
            return True
        else:
            print(f"   ⚠️  Conexão instável")
            return False
    except:
        print(f"   ❌ Sem conexão com internet")
        return False

def main():
    print_header("🎮 TESTE DE INSTALAÇÃO")
    print("Verificando se tudo está pronto para usar o Skidrow Downloader...\n")
    
    results = {
        "Python": check_python(),
        "Internet": check_internet(),
    }
    
    print("\n📦 Verificando módulos Python necessários...")
    results["textual"] = check_module("textual")
    results["requests"] = check_module("requests")
    results["bs4"] = check_module("bs4", "beautifulsoup4")
    results["lxml"] = check_module("lxml")
    
    print("\n🔧 Verificando ferramentas opcionais...")
    results["transmission"] = check_command("transmission-remote")
    
    print()
    results["storage"] = check_storage()
    
    print()
    results["app"] = check_app_file()
    
    print_header("📊 RESULTADO")
    
    total = len(results)
    passed = sum(results.values())
    failed = total - passed
    
    print(f"Total: {total}")
    print(f"✅ Passou: {passed}")
    print(f"❌ Falhou: {failed}")
    
    print("\n" + "="*50)
    
    if passed == total:
        print("✅ TUDO OK! Você pode usar o aplicativo!")
        print("\nPara executar:")
        print("   python skidrow_downloader.py")
        print("\nou:")
        print("   ./skidrow_downloader.py")
    else:
        print("⚠️  ALGUMAS VERIFICAÇÕES FALHARAM")
        print("\nProblemas encontrados:")
        
        for item, status in results.items():
            if not status:
                print(f"   ❌ {item}")
        
        print("\n🔧 Soluções:")
        
        if not results.get("Python"):
            print("   • Atualize o Termux: pkg update && pkg upgrade")
        
        if not any([results.get("textual"), results.get("requests"), 
                   results.get("bs4"), results.get("lxml")]):
            print("   • Instale dependências: pip install -r requirements.txt")
        
        if not results.get("transmission"):
            print("   • Instale transmission: pkg install transmission")
        
        if not results.get("storage"):
            print("   • Configure storage: termux-setup-storage")
        
        if not results.get("app"):
            print("   • Certifique-se de estar no diretório correto")
        
        if not results.get("Internet"):
            print("   • Verifique sua conexão WiFi/dados móveis")
    
    print("="*50)
    print("\n📚 Para mais informações, leia:")
    print("   • README.md - Instruções completas")
    print("   • TERMUX_SETUP.md - Configuração do Termux")
    print("   • FAQ.md - Perguntas frequentes")
    print("   • EXAMPLES.md - Exemplos de uso")
    print()

if __name__ == "__main__":
    main()
