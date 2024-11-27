import pandas as pd
from pathlib import Path
from utilities import get_file_by_partial_name
import openpyxl

class GerarExcel():

    def ler_arquivo_txt(self, diretorio: Path, arquivo_parcial: str):
        arquivo_txt = get_file_by_partial_name(diretorio, arquivo_parcial)
        if not arquivo_txt:
            raise FileNotFoundError(f"Arquivo '{arquivo_parcial}' não encontrado em {diretorio}")
        
        with open(arquivo_txt, "r", encoding="utf-8") as txt_lido:
            dados = txt_lido.readlines()
            print("\nConteúdo do arquivo:")
            print(dados)
            df_dados = pd.DataFrame(dados)
            print(df_dados)

        # Retorna o conteúdo lido (opcional)
        return dados
    
def run():
    # Configura o diretório e o nome do arquivo
    diretorio = Path("./data")
    arquivo_parcial = "tabela-pessoas.txt"

    # Instancia a classe e executa o método
    gerador = GerarExcel()
    try:
        gerador.ler_arquivo_txt(diretorio, arquivo_parcial)
    except FileNotFoundError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"erro inesperado: {e}")


if __name__ == "__main__":
    run()