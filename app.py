import os
import json

BLACKLIST = {
    'LICENSE', '.gitignore', '.gitattributes',
    '.venv', 'venv', 'env', '__pycache__', 'node_modules', '.git'
}

ALLOWED_EXTENSIONS = {
    '.py', '.c', '.cpp', '.h', '.hpp', '.js',
    '.html', '.css', '.java', '.php', '.rb',
    '.go', '.rs', '.ts', '.json', '.txt', '.md', '.ipynb', '.pdf'
}

# Extensões que serão ignoradas (por exemplo, .csv)
IGNORED_EXTENSIONS = {'.csv','.xlsx','.docx','.png', '.mp4'}

# Pasta onde os arquivos TXT serão salvos
OUTPUT_FOLDER = "relatorios"

def main(local):
    """Processa arquivos de código em diretórios e gera um relatório."""
    current_dir = local
    dir_name = os.path.basename(current_dir)
    
    # Cria a pasta de saída, se não existir
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    
    output_file = os.path.join(OUTPUT_FOLDER, f"{dir_name}.txt")

    auto_processar = input(
        "Deseja processar todos os arquivos de código automaticamente? [Y/n] "
    ).lower() in ('', 'y', 'yes')

    processar_ocultos = input(
        "Deseja incluir arquivos/diretórios ocultos? [y/N] "
    ).lower() in ('y', 'yes')

    with open(output_file, 'w', encoding='utf-8') as f_out:

        def processar_arquivo(caminho, rel_path):
            """Lê o conteúdo do arquivo e escreve no relatório."""
            _, extensao = os.path.splitext(caminho)
            # Ignora arquivos com extensões indesejadas
            if extensao in IGNORED_EXTENSIONS:
                return
            try:
                # Tratamento especial para notebooks: ignora os outputs
                if extensao == '.ipynb':
                    with open(caminho, 'r', encoding='utf-8') as f_in:
                        nb = json.load(f_in)
                    for cell in nb.get('cells', []):
                        if cell.get('cell_type') == 'code':
                            cell['outputs'] = []
                            cell['execution_count'] = None
                    conteudo = json.dumps(nb, indent=2, ensure_ascii=False)
                    f_out.write(f"--- ARQUIVO: {rel_path} (sem output) ---\n")
                    f_out.write(conteudo + "\n\n")
                else:
                    with open(caminho, 'r', encoding='utf-8') as f_in:
                        conteudo = f_in.read()
                    f_out.write(f"--- ARQUIVO: {rel_path} ---\n")
                    f_out.write(conteudo + "\n\n")
            except UnicodeDecodeError:
                try:
                    with open(caminho, 'r', encoding='latin-1') as f_in:
                        conteudo = f_in.read()
                    f_out.write(f"--- ARQUIVO: {rel_path} (latin-1) ---\n")
                    f_out.write(conteudo + "\n\n")
                except Exception as e:
                    f_out.write(f"--- ARQUIVO: {rel_path} ---\n")
                    f_out.write(f"(Erro ao ler arquivo: {e})\n\n")
            except Exception as e:
                f_out.write(f"--- ARQUIVO: {rel_path} ---\n")
                f_out.write(f"(Erro ao ler arquivo: {e})\n\n")

        def processar_diretorio(path, rel_path, nivel=0):
            """
            Processa recursivamente um diretório, perguntando ao usuário
            quais arquivos e subdiretórios devem ser processados.
            """
            nonlocal auto_processar
            try:
                itens = sorted(os.listdir(path))
            except PermissionError:
                return

            prefixo = "  " * nivel
            f_out.write(f"\n=== DIRETÓRIO: {rel_path} ===\n\n")

            for item in itens:
                if item in BLACKLIST and not processar_ocultos:
                    continue

                item_path = os.path.join(path, item)
                item_rel = os.path.join(rel_path, item)

                # Ignora arquivos/diretórios ocultos
                if item.startswith('.') and not processar_ocultos:
                    continue

                if os.path.isfile(item_path):
                    _, ext = os.path.splitext(item)
                    
                    # Se a extensão estiver na lista de ignorados, pula o arquivo
                    if ext in IGNORED_EXTENSIONS:
                        continue

                    if auto_processar and ext in ALLOWED_EXTENSIONS:
                        processar_arquivo(item_path, item_rel)
                        continue

                    if not auto_processar:
                        resposta = input(
                            f"{prefixo}Processar arquivo '{item}'? [Y/n/a] "
                        ).lower()
                        if resposta == 'a':
                            auto_processar = True
                        if resposta not in ('', 'y', 'yes') and not auto_processar:
                            continue

                    processar_arquivo(item_path, item_rel)

                elif os.path.isdir(item_path):
                    resposta = input(
                        f"{prefixo}Entrar no diretório '{item}'? [Y/n] "
                    ).lower()
                    if resposta in ('', 'y', 'yes'):
                        processar_diretorio(item_path, item_rel, nivel + 1)

        processar_diretorio(current_dir, dir_name)

    print(f"\nRelatório gerado em: {output_file}")


if __name__ == "__main__":
    local = r'C:\Users\jonat\Documents\GitHub\Sprints\Sprint 12'
    main(local)