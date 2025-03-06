import json
import os

def carregar_configuracao(caminho_config):
    """Carrega as configurações de um arquivo JSON."""
    if not os.path.exists(caminho_config):
        raise FileNotFoundError(f"Arquivo de configuração não encontrado: {caminho_config}")
    
    with open(caminho_config, "r", encoding="utf-8") as file:
        return json.load(file)

def load_json():
    caminho_config = "..//config.json"

    config = carregar_configuracao(caminho_config)

    IP = os.getenv("IP", config.get("ip", "192.168.1.1"))
    SERVIDOR = os.getenv("SERVIDOR", config.get("servidor", "meu_servidor"))
    TEMPO = int(os.getenv("TEMPO", config.get("tempo", 10)))
    VEZES = int(os.getenv("VEZES", config.get("vezes", 3)))

    return {'ip':IP,'servidor': SERVIDOR, 'tempo':TEMPO, 'vezes':VEZES}
