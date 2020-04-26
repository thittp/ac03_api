import sqlite3


def inserir_disciplina(disciplina):
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()

    ddl_aluno = """
    CREATE TABLE IF NOT EXISTS DISCIPLINA(
        ID INT PRIMARY KEY,
        NOME VARCHAR(255),
        STATUS INT,
        PLANO_ENSINO VARCHAR(255),
        CARGA_HORARIA INT,
        ID_COORDENADOR INT,
        CONSTRAINT FK_COORDENADOR FOREIGN KEY(ID_COORDENADOR)
            REFERENCES PROFESSOR(ID)

    )

    """
    cursor.execute(ddl_aluno)
    connection.commit()

    insert = f"""
    INSERT INTO DISCIPLINA (ID, NOME, STATUS, PLANO_ENSINO, CARGA_HORARIA, ID_COORDENADOR)
    VALUES({disciplina['id']}, '{disciplina['nome']}', {disciplina['status']}, '{disciplina['plano_ensino']}',
    {disciplina['carga_horaria']}, {disciplina["id_coordenador"]}
    )
    """
    cursor.execute(insert)
    return connection.commit()

def select_disciplinas():
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()

    ddl_aluno = """
    CREATE TABLE IF NOT EXISTS DISCIPLINA(
        ID INT PRIMARY KEY,
        NOME VARCHAR(255),
        STATUS INT,
        PLANO_ENSINO VARCHAR(255),
        CARGA_HORARIA INT,
        ID_COORDENADOR INT,
        CONSTRAINT FK_COORDENADOR FOREIGN KEY(ID_COORDENADOR)
            REFERENCES PROFESSOR(ID)

    )

    """
    cursor.execute(ddl_aluno)
    connection.commit()
    cursor.close()
    select_disciplina = '''
    SELECT D.ID, D.NOME, D.STATUS, D.PLANO_ENSINO, D.CARGA_HORARIA, D.ID_COORDENADOR, P.NOME FROM DISCIPLINA AS D
    JOIN PROFESSOR AS P ON D.ID_COORDENADOR = P.ID
    '''
    disciplinas = {}
    list_disciplinas = []
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    cursor.execute(select_disciplina)
    select_disciplina = cursor.fetchall()
    cursor.close()
    print(select_disciplina)
    for disciplina in select_disciplina:
        
        disciplinas = {
            "id": disciplina[0],
            "nome_disciplina": disciplina[1],
            "status": disciplina[2],
            "plano_ensino": disciplina[3],
            "carga_horaria": disciplina[4],
            "nome_coordenador": disciplina[6]
        }
        list_disciplinas.append(disciplinas.copy())
    
    return list_disciplinas
