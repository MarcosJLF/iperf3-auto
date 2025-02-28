import subprocess
import re
import os

def run_command(command):
    """Executa um comando no terminal e retorna a saída."""

    subprocess.run('cls', shell=True)
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    if result.returncode != 0:
        print("Erro ao executar o comando:", result.stderr)
        return None
    return result.stdout

def save_to_file(filename, content):
    """Salva o conteúdo em um arquivo."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Saída salva em '{filename}'.")

def extract_info(output, pattern):
    """Extrai informações usando expressões regulares."""
    match = re.search(pattern, output)
    return match.group(1).strip() if match else None  # Remove espaços em branco

def read_from_file(filename):
    """Lê o conteúdo de um arquivo."""
    if not os.path.exists(filename):
        print(f"Arquivo '{filename}' não encontrado.")
        return None
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def main():
    output_filename = "wifi_output.txt"  # Nome do arquivo para salvar a saída

    # Verifica se o arquivo já existe
    if os.path.exists(output_filename):
        print(f"Arquivo '{output_filename}' encontrado. Lendo a partir do arquivo...")
        file_content = read_from_file(output_filename)
    else:
        print(f"Arquivo '{output_filename}' não encontrado. Executando o comando...")
        command = "netsh wlan show interface"
        output = run_command(command)
        if output:
            save_to_file(output_filename, output)
            file_content = output
        else:
            print("Falha ao executar o comando.")
            return

if __name__ == "__main__":
    main()