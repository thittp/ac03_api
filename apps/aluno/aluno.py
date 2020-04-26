import sqlite3

def insert_aluno(aluno):
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()

    ddl_aluno = """
    CREATE TABLE IF NOT EXISTS ALUNO(
        ID INT PRIMARY KEY,
        NOME VARCHAR(255)
    
    )

    """
    cursor.execute(ddl_aluno)
    connection.commit()
    cursor.close()
    insert = f"INSERT INTO ALUNO (ID, NOME) VALUES({aluno['id']}, '{aluno['nome']}')"
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    cursor.execute(insert)
    connection.commit()
    return cursor.close()

def select_aluno():
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()

    select_aluno = '''
    SELECT ID, NOME FROM ALUNO
    '''
    alunos = {}
    list_alunos = []
    select = cursor.execute(select_aluno)
    select_aluno = cursor.fetchall()
    cursor.close()
    for aluno in select_aluno:
        alunos = {
            "id": aluno[0],
            "nome": aluno[1]
        }
        list_alunos.append(alunos.copy())
    return list_alunos
