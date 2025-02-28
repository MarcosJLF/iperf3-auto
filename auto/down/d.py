import os

# Caminho do arquivo que você deseja deletar
caminho_arquivo = "iperf_output.txt"

# Verifica se o arquivo existe antes de tentar deletá-lo
if os.path.exists(caminho_arquivo):
    os.remove(caminho_arquivo)
    print(f"O arquivo {caminho_arquivo} foi deletado com sucesso.")
else:
    print(f"O arquivo {caminho_arquivo} não foi encontrado.")
