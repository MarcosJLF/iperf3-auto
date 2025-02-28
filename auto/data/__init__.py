import subprocess
import time
import os

def run_script(script_name):
    """Executa um script Python."""
    result = subprocess.run(["python", script_name], capture_output=True, text=True)
    return result.stdout

def main():

    os.system("cls")

    resultados_finais = {}
    
    for i in range(1, 4):  # Executar três vezes
        print(f"Execução {i}...")
        run_script("netsh.py")  # Executa o primeiro script
        time.sleep(2)  # Aguarda um pouco para garantir a escrita
        resultado = run_script("read.py")  # Executa o segundo script
        run_script("delete.py")  # Executa o terceiro script
        time.sleep(2)  # Aguarda um pouco para garantir a exclusão
        
        # Processa a saída do segundo script
        dados = {}
        for linha in resultado.split("\n"):
            if ":" in linha:
                chave, valor = linha.split(":")
                dados[chave.strip()] = valor.strip()
        
        resultados_finais[f"Execução {i}"] = dados
        
    print("Resultados finais:")
    for execucao, dados in resultados_finais.items():
        print(execucao, dados)

if __name__ == "__main__":
    main()
