import subprocess
from r_json import main

variaveis = main()

def run_command(command, output_file):
    """Executa um comando e salva a saída em um arquivo."""
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

ip = variaveis['ip']
servidor = variaveis['servidor']
tempo = variaveis['tempo']
vezes = variaveis['vezes']

command = f"iperf3 -c {servidor} -B {ip} -t{tempo} -R"
output_file = "iperf_output.txt"


if run_command(command, output_file):
    print("Comando executado com sucesso.")
else:
    print("Falha ao executar o comando.")