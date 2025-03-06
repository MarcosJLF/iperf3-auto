import subprocess
import time
import sys
import os

pwd = [
    "./down/main.py",
    "./up/main.py",
    "./data/main.py",
    "./r.py"
]

def run_script(script):
    script_path = os.path.join(os.path.dirname(__file__), script)
    result = subprocess.run(["python", script_path], capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"\nErro ao executar {script}: {result.stderr}")
    else:
        print(f"\n{script} executado com sucesso.")
    
    time.sleep(1)  

def update_progress_bar(progress):
    """
    Atualiza a barra de carregamento no terminal.
    :param progress: Porcentagem do progresso (0 a 100).
    """
    bar_length = 30  
    block = int(round(bar_length * progress / 100))
    progress_bar = f"[{'|' * block}{' ' * (bar_length - block)}] {progress:.1f}%"
    sys.stdout.write("\r" + progress_bar)  
    sys.stdout.flush()  

def main():
    print("Iniciando execução dos scripts...")
    total_scripts = len(pwd)
    for i, script in enumerate(pwd):
        progress = (i + 1) / total_scripts * 100
        update_progress_bar(progress)
        run_script(script)
    print("\nTodos os scripts foram executados!")

if __name__ == "__main__":
    main()