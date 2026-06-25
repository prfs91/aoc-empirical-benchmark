from pathlib import Path 
from nbformat import v4 as nbf
import nbformat
import traceback

def criar_notebooks_faltantes():
    raiz_projeto = Path(__file__).resolve().parent.parent

    pasta_md = raiz_projeto / "docs" / "fichamentos" / "md"
    pasta_ipynb = raiz_projeto / "docs" / "fichamentos" / "ipynb"

    pasta_ipynb.mkdir(parents=True, exist_ok=True)

    if not pasta_md.exists:
        print(f"Erro: Pasta não encontrada em: {pasta_md}")
        return
    
    arquivos_md = list(pasta_md.glob("*.md"))

    if not arquivos_md:
        print(f"Nenhum arquivo .md encontrado em: {pasta_md}")
        return
    
    criados = 0

    for arquivo_md in arquivos_md:
        arquivo_ipynb = pasta_ipynb / f"{arquivo_md.stem}.ipynb"

        with open(arquivo_md, "r", encoding="utf-8") as f_md:
            conteudo_markdown = f_md.read()

        #nbformat.write(notebook, f)

        notebook_novo = nbf.new_notebook()
        celula_md = nbf.new_markdown_cell(conteudo_markdown)
        notebook_novo["cells"].append(celula_md)
        
        if not arquivo_ipynb.exists():

            with open(arquivo_ipynb, "w", encoding="utf-8") as f_ipynb:
                nbformat.write(notebook_novo, f_ipynb)
            
            print(f"Criado: {arquivo_ipynb.name}")
            criados =+ 1
        else:
            try:
                with open(arquivo_ipynb, "r", encoding="utf-8") as f_ipynb:
                    notebook_atual = nbformat.read(f_ipynb, as_version=4)
                
                texto_atual = ""
                '''if len(notebook_atual.cells) > 0:
                    primeira_celula = notebook_atual.cells[0]
                    if primeira_celula.cell_type == "markdown":
                        texto_atual = primeira_celula.get("source", "")'''

                if notebook_atual.get("cells"):
                    primeira_celula = notebook_atual["cells"][0]
                    if primeira_celula.get("cell_type") == "markdown":
                        texto_atual = primeira_celula.get("source", "")

                #if notebook_atual["cells"] and notebook_atual["cells"][0][cell_type] == "markdown":
                    #texto_atual = notebook_atual["cells"][0]["source"]
                
                if conteudo_markdown != texto_atual:
                    with open(arquivo_ipynb, "w", encoding="utf-8") as f_ipynb:
                        nbformat.write(notebook_novo, f_ipynb)
                    print(f"Atualizado: {arquivo_ipynb.name}")
                    criados =+ 1

            except Exception as erro:
                with open(arquivo_ipynb, "w", encoding="utf-8") as f_ipynb:
                    #print(f"Erro ao ler {arquivo_ipynb.name}: {erro}")
                    nbformat.write(notebook_novo, f_ipynb)
                print(f"Atualizado (forçado): {arquivo_ipynb.name}")
                #criados =+ 1

    if criados == 0:
        print("Todos os notebooks já existiam. Nenhum arquivo novo foi criado.")
    else:
        print(f"Sucesso! {criados} novos notebooks foram gerados.")

if __name__ == "__main__":
    criar_notebooks_faltantes()
