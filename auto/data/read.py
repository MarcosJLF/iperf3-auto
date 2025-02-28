import re
import os

arquivo = "wifi_output.txt"

os.system("cls")

padroes = {
    "Taxa de recepção": r"Taxa de recep‡Æo \(Mbps\)\s*:\s*(\d+)",
    "Taxa de transmissão": r"Taxa de transmissÆo \(Mbps\)\s*:\s*(\d+)",
    "Sinal": r"Sinal\s*:\s*(\d+)%"
}

resultados = {}

with open(arquivo, "r", encoding="utf-8") as f:
    conteudo = f.read()
    for chave, padrao in padroes.items():
        match = re.search(padrao, conteudo)
        if match:
            resultados[chave] = match.group(1)

for chave, valor in resultados.items():
    print(f"{chave}: {valor}")
