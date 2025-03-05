import subprocess
import time
import os

def run_script(script_name):
    """Executa um script Python."""
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    result = subprocess.run(["python", script_path], capture_output=True, text=True)
    return result.stdout

def main():
    os.system("cls")

    resultados_finais = {}
    
    for i in range(1, 4):  
        print(f"Execução {i}...")
        run_script("netsh.py")  
        time.sleep(2)  
        resultado = run_script("read.py")  
        run_script("delete.py") 
        time.sleep(2)  
        
        dados = {}
        for linha in resultado.split("\n"):
            if ":" in linha:
                chave, valor = linha.split(":")
                dados[chave.strip()] = valor.strip()
        
        resultados_finais[f"Execução {i}"] = dados
    

    with open("resultados_finais.txt", "w", encoding="utf-8") as file:
        for execucao, dados in resultados_finais.items():
            file.write(f"{execucao}: {dados}\n")
    
    print("Resultados finais salvos em 'resultados_finais.txt'.")

if __name__ == "__main__":
    main()