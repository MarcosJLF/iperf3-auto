import os

caminho_arquivo = [
    "r_down.txt",
    "r_up.txt",
    "resultados_finais.txt",
    "tabela_resultados.txt"
]


for i in range(0, 3):
    if os.path.exists(caminho_arquivo[i]):
        os.remove(caminho_arquivo[i])
        print(f"O arquivo {caminho_arquivo[i]} foi deletado com sucesso.")
    else:
        print(f"O arquivo {caminho_arquivo[i]} não foi encontrado.")
