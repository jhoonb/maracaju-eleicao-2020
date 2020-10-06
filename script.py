#####################################################
# script.py 
# Jhonathan P. Banczek
#####################################################

import sys 
from pathlib import Path
import sqlite3


# str do insert
sql_insert = '''
INSERT INTO candidato (CARGO, NUMERO_CANDIDATO,
NOME_CANDIDATO, NOME_URNA, CPF, 
EMAIL, TIPO_AGREMIACAO, NUMERO_PARTIDO, 
SIGLA_PARTIDO, NOME_PARTIDO, NOME_COLIGACAO, 
COMPOSICAO_COLIGACAO, DATA_NASCIMENTO, IDADE_POSSE, 
SEXO, GRAU_INSTRUCAO, ESTADO_CIVIL, 
COR_RACA, OCUPACAO, DESPESA, REELEICAO, SQ_CANDIDATO) 

VALUES ("{}", "{}", "{}", "{}", "{}", 
"{}", "{}", "{}", "{}", "{}",  
"{}", "{}", "{}", {}, "{}",
"{}", "{}", "{}", "{}", {}, "{}", "{}");\n'''


def lista_candidatos(arquivo):

    f_form = lambda d: [i.strip() for i in d] 

    with open(arquivo, "r") as f:
        data = f.readlines()
    data = [f_form(i.split(";")) for i in data]
    return data


def gerar_insert(data):
    """gera o arquivo insert.sql para 
    ser executado no banco Sqlite"""

    n = [sql_insert.format(*i) for i in data]
    with open('insert.sql', 'w') as f:
        f.writelines(n)
    

################################################################
def fotos():
    """remove as fotos dos candidatos que não são de Maracaju.
    origem das fotos: Repositório de dados eleitorais - TSE
    - mantem apenas as fotos dos canditados de Maracaju.
    """
    # todos os sq_candidatos da base sqlite
    conn = sqlite3.connect('candidatos.sqlite')
    with conn:
        c = conn.cursor()
        c.execute("SELECT sq_candidato FROM candidato")
        sq_candidatos = [i[0] for i in c.fetchall()] 
    

    def existe_sq(item):
        for i in sq_candidatos:
            if i in item:
                return True
        return False

    # captura dos os arquivos de fotos (no diretório) 
    # que não tem na base sqlite
    p = Path("fotos/")
    lista_fotos = [i for i in p.iterdir() if i.is_file() and not existe_sq(i.stem)]
    print("removendo: ", len(lista_fotos), " fotos")
    for i in lista_fotos:
        i.unlink()
    print("ok")


#######################################
if __name__ == "__main__":
    try:
        arg = sys.argv[1]
    except:
        arg = None
    
    if arg == "fotos":
        fotos()
    elif arg == "insert":
        dados = lista_candidatos("candidatos.csv")
        gerar_insert(dados)
    else:
        print("python script.py [fotos, insert] ")