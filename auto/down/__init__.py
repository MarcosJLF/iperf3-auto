import subprocess
import os
import time

def run_script(script_name):
    """
    Executa um script Python e aguarda sua conclusão.
    Retorna a saída do script.
    """
    result = subprocess.run(["python", script_name], capture_output=True, text=True)
    return result.stdout

def main():
    # Limpa a tela (funciona no Windows)
    os.system("cls")

    # Lista para armazenar os resultados de cada execução
    resultados = []

    for i in range(1, 4):  # Executa três vezes
        print(f"Iniciando execução {i}...")

        # Executa o script i.py (inserir dados)
        print("Executando i.py... (pode demorar cerca de 30 segundos)")
        run_script("i.py")  # Aguarda a conclusão automática

        # Executa o script r.py (ler dados)
        print("Executando r.py...")
        resultado = run_script("r.py")
        time.sleep(5)  # Aguarda 5 segundos

        # Executa o script d.py (deletar arquivo)
        print("Executando d.py...")
        run_script("d.py")

        # Processa a saída do script r.py
        try:
            # Converte a saída (um número) para inteiro
            maior_bandwidth = int(resultado.strip())
            resultados.append(maior_bandwidth)  # Adiciona o resultado à lista
        except ValueError:
            # Caso a saída não seja um número válido
            resultados.append("Erro: Não foi possível obter o valor de Bandwidth.")

    # Exibe os resultados finais
    print("\nResultados finais:")
    for i, resultado in enumerate(resultados, start=1):
        print(f"Execução {i}: {resultado}")

if __name__ == "__main__":
    main()