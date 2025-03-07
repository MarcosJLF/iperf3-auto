import subprocess
import os
import time
import re
import json
from r_json import load_json

variaveis = load_json()

def run_script(script_name):
    """Executa um script Python e retorna a saída."""
    result = subprocess.run(["python", script_name], capture_output=True, text=True)
    return result.stdout

def delete_file(file_path):
    """Deleta um arquivo se ele existir."""
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Arquivo {file_path} deletado com sucesso.")
    else:
        print(f"Arquivo {file_path} não encontrado.")

def extract_bandwidth(file_path):
    """Extrai o maior valor de Bandwidth do arquivo iperf_output.txt."""
    with open(file_path, "r") as file:
        arquivo = file.read()
    bandwidths = re.findall(r'(\d+)\s*Mbits/sec', arquivo)
    if bandwidths:
        return max(map(int, bandwidths))
    else:
        return "Erro: Não foi possível encontrar o Bandwidth."

def run_iperf_test(ip, servidor, tempo):
    """Executa o comando iperf3 e salva a saída em iperf_output.txt."""
    command = f"iperf3 -c {servidor} -B {ip} -t{tempo} -R"
    output_file = "iperf_output.txt"
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        if result.returncode != 0:
            print("Erro ao executar o comando:", result.stderr)
            return False
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(result.stdout)
        print(f"Saída salva em '{output_file}'.")
        return True
    except Exception as e:
        print("Erro inesperado:", e)
        return False

def load_config():
    """Carrega as configurações do arquivo config.json."""
    caminho_config = 'config.json'
    if not os.path.exists(caminho_config):
        raise FileNotFoundError(f"Arquivo de configuração não encontrado: {caminho_config}")
    with open(caminho_config, "r", encoding="utf-8") as file:
        return json.load(file)

def main():
    os.system("cls")
    #config = load_config()
    ip = "10.0.0.5"
    servidor = "50.0.0.10"
    tempo = 30
    vezes = 3

    resultados = []

    for i in range(1, vezes + 1):
        print(f"Iniciando execução {i}...")
        
        if run_iperf_test(ip, servidor, tempo):
            bandwidth = extract_bandwidth("iperf_output.txt")
            resultados.append(bandwidth)
        
        delete_file("iperf_output.txt")
        time.sleep(5)

    print("\nResultados finais:")
    for i, resultado in enumerate(resultados, start=1):
        print(f"Execução {i}: {resultado}")

    with open("r_up.txt", "w", encoding="utf-8") as file:
        file.write("Resultados finais:\n")
        for i, resultado in enumerate(resultados, start=1):
            file.write(f"Execução {i}: {resultado}\n")

    print("\nResultados salvos em 'r_down.txt'.")

if __name__ == "__main__":
    main()