import os
import importlib.util

# Função para executar um script e capturar a saída
def run_script(script_path):
    spec = importlib.util.spec_from_file_location("module.name", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Diretórios e scripts a serem executados
directories = ['down', 'up', 'data']
results = []

# Executar os scripts na ordem especificada
for dir_name in directories:
    script_path = os.path.join(dir_name, '__init__.py')
    if os.path.exists(script_path):
        print(f"Executando {dir_name}...")
        module = run_script(script_path)
        # Supondo que o script retorna um dicionário com os resultados
        if hasattr(module, 'get_results'):
            results.append(module.get_results())

# Processar os resultados para a tabela
table = []
for result in results:
    if 'data' in result:
        data = result['data']
        sinal = result.get('Sinal', 'N/A')
        table.append([data['Taxa de recepção'], data['Taxa de transmissão'], sinal])

# Exibir a tabela
print("\n| Vezes | up    | down   | sinal  | data |")
print("|---|---|---|---|---|")
for i, row in enumerate(table, start=1):
    print(f"| {i} | {row[0]} | {row[1]} | {row[2]} | {row[0]} |")