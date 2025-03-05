import os
import subprocess
import json

def carregar_configuracao(caminho_config):
    """Carrega as configurações de um arquivo JSON."""
    if not os.path.exists(caminho_config):
        raise FileNotFoundError(f"Arquivo de configuração não encontrado: {caminho_config}")
    
    with open(caminho_config, "r", encoding="utf-8") as file:
        return json.load(file)

def salvar_configuracao(caminho_config, config):
    """Salva as configurações em um arquivo JSON."""
    with open(caminho_config, "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)

def coletar_variaveis(config):
    """Coleta as variáveis do usuário, mostrando os valores atuais como padrão."""
    print("Por favor, insira as novas configurações. Pressione Enter para manter os valores atuais.")

    novo_ip = input(f"IP [{config['ip']}]: ").strip()
    novo_servidor = input(f"Servidor [{config['servidor']}]: ").strip()
    novoTempo = input(f"Tempo [{config['tempo']}]: ").strip()
    novoVezes = input(f"Vezes [{config['vezes']}]: ").strip()

    if novo_ip:
        config["ip"] = novo_ip
    if novo_servidor:
        config["servidor"] = novo_servidor
    if novoTempo:
        config["tempo"] = int(novoTempo)
    if novoVezes:
        config["vezes"] = int(novoVezes)

    return config

def main():
    caminho_config = "config.json"

    try:
        config = carregar_configuracao(caminho_config)
    except FileNotFoundError as e:
        print(e)
        return

    config = coletar_variaveis(config)

    salvar_configuracao(caminho_config, config)

    print("\nValores configurados:")
    print(f"IP: {config['ip']}")
    print(f"Servidor: {config['servidor']}")
    print(f"Tempo: {config['tempo']}")
    print(f"Vezes: {config['vezes']}")

    # Iniciar os scripts Python
    print("\nIniciando start.py e r.py...")
    subprocess.run(["python",  " .\auto\start.py"])
    subprocess.run(["python", "./auto/r.py"])

if __name__ == "__main__":
    main()