import os

caminho_arquivo = "wifi_output.txt"

if os.path.exists(caminho_arquivo):
    os.remove(caminho_arquivo)
    print(f"O arquivo {caminho_arquivo} foi deletado com sucesso.")
else:
    print(f"O arquivo {caminho_arquivo} não foi encontrado.")
