from tabulate import tabulate

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as file:
        return file.readlines()

def extrair_valores(linhas):
    valores = []
    for linha in linhas:
        if "Execução" in linha:
            partes = linha.split(":")
            if len(partes) > 1:
                valores.append(partes[1].strip())
    return valores

def extrair_dados_data(linhas):
    dados = []
    for linha in linhas:
        if "Execução" in linha:
            partes = linha.split("{")[1].split("}")[0]  
            partes = partes.replace("'Taxa de recepção'", "'T. Rec.'")
            partes = partes.replace("'Taxa de transmissão'", "'T. Tra.'")
            dados.append(partes)
    return dados

dados_down = ler_arquivo("r_down.txt")
dados_up = ler_arquivo("r_up.txt")
dados_data = ler_arquivo("resultados_finais.txt")

valores_down = extrair_valores(dados_down)
valores_up = extrair_valores(dados_up)
valores_data = extrair_dados_data(dados_data)


tabela = []
for i in range(len(valores_down)):
    rodada = i + 1
    up = valores_up[i] if i < len(valores_up) else "N/A"
    down = valores_down[i] if i < len(valores_down) else "N/A"
    data = valores_data[i] if i < len(valores_data) else "N/A"
    tabela.append([rodada, up, down, data])

cabecalho = ["Rodadas", "Up", "Down", "Data"]
tabela_formatada = tabulate(tabela, headers=cabecalho, tablefmt="pretty")

print("Tabela de Resultados:")
print(tabela_formatada)

with open("tabela_resultados.txt", "w", encoding="utf-8") as file:
    file.write("Tabela de Resultados:\n")
    file.write(tabela_formatada)

print("\nTabela salva em 'tabela_resultados.txt'.")