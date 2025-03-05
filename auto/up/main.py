import subprocess
import os
import time

def run_script(script_name):
    """
    Executa um script Python e aguarda sua conclusão.
    Retorna a saída do script.
    """
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    result = subprocess.run(["python", script_path], capture_output=True, text=True)
    return result.stdout

def main():
    os.system("cls")

    resultados = []

    for i in range(1, 4):  
        print(f"Iniciando execução {i}...")
        
        print("Executando i.py... (pode demorar cerca de 30 segundos)")
        run_script("i.py")  

        print("Executando r.py...")
        resultado = run_script("r.py")
        time.sleep(5) 

        print("Executando d.py...")
        run_script("d.py")

        try:
            maior_bandwidth = int(resultado.strip())
            resultados.append(maior_bandwidth)  
        except ValueError:
            resultados.append("Erro: Não foi possível obter o valor de Bandwidth.")

    print("\nResultados finais:")
    for i, resultado in enumerate(resultados, start=1):
        print(f"Execução {i}: {resultado}")

    with open("r_up.txt", "w", encoding="utf-8") as file:
        file.write("Resultados finais:\n")
        for i, resultado in enumerate(resultados, start=1):
            file.write(f"Execução {i}: {resultado}\n")

    print("\nResultados salvos em 'r_up.txt'.")

if __name__ == "__main__":
    main()