import subprocess

def run_command(command, output_file):
    """Executa um comando e salva a saída em um arquivo."""
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        if result.returncode != 0:
            print("Erro ao executar o comando:", result.stderr)
            return False
        
        # Salva a saída em um arquivo
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(result.stdout)
        print(f"Saída salva em '{output_file}'.")
        return True
    except Exception as e:
        print("Erro inesperado:", e)
        return False

# Comando a ser executado
command = "iperf3 -c 50.0.0.10 -B 10.0.0.5 -t30 -R"
output_file = "iperf_output.txt"

# Executa o comando e salva a saída
if run_command(command, output_file):
    print("Comando executado com sucesso.")
else:
    print("Falha ao executar o comando.")