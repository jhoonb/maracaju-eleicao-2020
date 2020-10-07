#####################################################
# script.py 
# Jhonathan P. Banczek
# https://jhoonb.github.io/maracaju-eleicao-2020
# https://github.com/jhoonb/maracaju-eleicao-2020
#####################################################

import sys 
from pathlib import Path
import sqlite3

from PIL import Image, ImageDraw, ImageFont


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

############################################################
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


#################################################################
def js_objeto_candidato():

    strjs = ""
    line = 'cargo: "{}", numeroCandidato: {}, nomeCandidato: "{}", nomeUrna: "{}", partido: "{}", sqCandidato: {}'

    conn = sqlite3.connect('candidatos.sqlite')
    with conn:
        c = conn.cursor()
        sql = """select c.cargo, c.NUMERO_CANDIDATO, c.NOME_CANDIDATO, 
        c.NOME_URNA, c.SIGLA_PARTIDO, c.SQ_CANDIDATO from candidato c"""
        c.execute(sql)
        sq_candidatos = [i for i in c.fetchall()]
    
    for i in sq_candidatos:
        strjs += "{" + line.format(*i) + "}, \n"

    with open("teste.txt", "w") as f:
        f.write(strjs)


#######################################
def escrever_foto():
    
    conn = sqlite3.connect('candidatos.sqlite')
    with conn:
        c = conn.cursor()
        c.execute("SELECT nome_urna, numero_candidato, sigla_partido, sq_candidato FROM candidato")
        candidatos = [i for i in c.fetchall()]

    def f_dados(candidatos, foto):
        for i in candidatos:
            if i[3] in foto:
                return i[:3]
        raise ValueError('não encontrado')

    fonte = ImageFont.truetype('Ubuntu-R.ttf', 16)

    # pasta local das fotos - sobrescreve
    p = Path("fotos/")

    lista_fotos = [i for i in p.iterdir() if i.is_file()]

    for foto in lista_fotos:
        
        print('editando... ', foto)
        
        img = Image.open(str(foto))
        
        
        d1 = ImageDraw.Draw(img)
        d1.fontmode = "L"

        # captura infos do candidado 
        nome_urna, numero_urna, partido = f_dados(candidatos, foto.stem)

        # adiciona um retangulo cinza
        x, y = 0, int(img.height/1.3) 
        d1.rectangle((x, y, img.width, img.height), fill='grey')
        # se o nome for grande, coloca quebra de linha
        if len(nome_urna) >= 17:
            nome_urna = nome_urna[:16] + "\n" + nome_urna[16:]
        # add nome
        d1.multiline_text((0, int(img.height/1.3)), nome_urna, 
        font=fonte, fill=(255, 255, 0))

        # add numero - partido
        d1.multiline_text((0, int(img.height/1.1)), numero_urna + "-" + partido, 
        font=fonte, fill=(255, 255, 0))

        img.save(str(foto))

    print("ok!")


#######################################################
def gerar_mosaico():

    img = Image.new("RGB", (900, 7700), "#FFFFFF")

    p = Path("fotos/")

    lista_fotos = [str(i) for i in p.iterdir() if i.is_file()]
    lista_fotos.sort()

    x, y, = 0, 0
    cont, col = 1, 5

    for foto in lista_fotos:
        img2 = Image.open(foto)
        if cont <= col:
            img.paste(img2, (x, y))
            x += 175
            cont += 1
        else:
            x = 0
            y += 240
            img.paste(img2, (x, y))
            x = 175
            cont = 2

    # add texto fonte entre as linhas
    x = 240
    ddimg = ImageDraw.Draw(img)
    img.fontmode = "L"
    fonte = ImageFont.truetype('Ubuntu-R.ttf', 12)
    for i in range(1, 31):
        ddimg.text((300, x*i), "fonte: jhoonb.github.io/maracaju-eleicao-2020", 
        font=fonte, fill=(77,77,255))

    img.save("mosaico_candidatos.jpg")
    # melhor qualidade 
    img.save("mosaico_candidatos.PNG")
    print(len(lista_fotos))


###########################################################
# [TODO] eu sei, tá um bagunça isso aqui, depois arrumo.
###########################################################
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
    elif arg == "js":
        js_objeto_candidato()
    elif arg == "escrever":
        escrever_foto()
    elif arg == "mosaico":
        gerar_mosaico()
    else:
        print("python script.py [fotos, insert, js, escrever, mosaico, fonte] ")