import os
import shutil
import subprocess

src_dir = "/storage/emulated/0/Download/wunderbaum-main/digital-library"
dest_dir = os.path.expanduser("~/digital-library")

print("Iniciando cópia limpa via Python...")

# Garante que o diretório de destino existe
os.makedirs(dest_dir, exist_ok=True)

# Copia os itens da pasta de download para o repositório, ignorando o que é pesado
for item in os.listdir(src_dir):
    s = os.path.join(src_dir, item)
    d = os.path.join(dest_dir, item)
    
    # Ignora pastas pesadas ou desnecessárias
    if item in ["node_modules", ".next", ".git"]:
        print(f"Ignorado com segurança: {item}")
        continue
        
    if os.path.isdir(s):
        if os.path.exists(d):
            shutil.rmtree(d)
        shutil.copytree(s, d, ignore=shutil.ignore_patterns("node_modules", ".next"))
        print(f"Diretório copiado: {item}")
    else:
        shutil.copy2(s, d)
        print(f"Arquivo copiado: {item}")

# Atualiza o .gitignore para garantir que o git nunca pegue lixo
gitignore_path = os.path.join(dest_dir, ".gitignore")
with open(gitignore_path, "w", encoding="utf-8") as f:
    f.write("node_modules/\n.next/\n*.log\n")
print(".gitignore atualizado e blindado.")

# Executa os comandos Git de forma automatizada
os.chdir(dest_dir)
print("Executando rotina do Git...")
subprocess.run(["git", "add", "-A"], check=True)
subprocess.run(["git", "commit", -m "Estrutura Wunderbaum enviada via script Python limpo"], check=True)
subprocess.run(["git", "push", "-u", "origin", "main"], check=True)

print("Processo concluído com sucesso total pelo Python!")

