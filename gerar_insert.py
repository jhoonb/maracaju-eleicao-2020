#####################################################
# le os dados do arquivo candidatos.csv
# e gera o arquivo sql_inser.sql para 
# ser executado no banco Sqlite
#####################################################


sql_insert = '''
INSERT INTO candidato (CARGO, NUMERO_CANDIDATO,
NOME_CANDIDATO, NOME_URNA, CPF, 
EMAIL, TIPO_AGREMIACAO, NUMERO_PARTIDO, 
SIGLA_PARTIDO, NOME_PARTIDO, NOME_COLIGACAO, 
COMPOSICAO_COLIGACAO, DATA_NASCIMENTO, IDADE_POSSE, 
SEXO, GRAU_INSTRUCAO, ESTADO_CIVIL, 
COR_RACA, OCUPACAO, DESPESA, REELEICAO) 

VALUES ("{}", "{}", "{}", "{}", "{}", 
"{}", "{}", "{}", "{}", "{}",  
"{}", "{}", "{}", {}, "{}",
"{}", "{}", "{}", "{}", {}, "{}");\n'''


def form(d):
    dd = [i.strip() for i in d]
    return dd


def lista_candidatos(arquivo):
    with open(arquivo, "r") as f:
        data = f.readlines()
    data = [form(i.split(";")) for i in data]
    return data


def gerar_insert(data):
    n = [sql_insert.format(*i) for i in data]
    with open('sql_insert.sql', 'w') as f:
        f.writelines(n)
    

#######################################
if __name__ == "__main__":
    dados = lista_candidatos("candidatos.csv")
    gerar_insert(dados)