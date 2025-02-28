import re
import os

os.system("cls")


# Abrir o arquivo e ler o conteúdo
with open("iperf_output.txt", "r") as file:
    arquivo = file.read()

# Usando regex para extrair todos os valores de Bandwidth (Mbits/sec)
bandwidths = re.findall(r'(\d+)\s*Mbits/sec', arquivo)

# Verificando se encontramos algum valor de Bandwidth
if bandwidths:
    # Convertendo os valores para inteiros e pegando o maior
    maior_bandwidth = max(map(int, bandwidths))
    print(maior_bandwidth)
else:
    print("Não foi possível encontrar o Bandwidth.")
