import sqlite3

def insert_professor(professor):
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()

    ddl_professor = """
    CREATE TABLE IF NOT EXISTS PROFESSOR(
        ID INT PRIMARY KEY,
        NOME VARCHAR(255)
    
    )

    """
    cursor.execute(ddl_professor)
    connection.commit()
    cursor.close()
    insert = f"INSERT INTO PROFESSOR (ID, NOME) VALUES({professor['id']}, '{professor['nome']}')"
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    cursor.execute(insert)
    connection.commit()
    return cursor.close()

def select_professor():
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    select_professor = '''
    SELECT ID, NOME FROM PROFESSOR
    '''
    professores = {}
    list_professsores = []
    select = cursor.execute(select_professor)
    select_professor = cursor.fetchall()
    cursor.close()
    for professor in select_professor:
        professores = {
            "id": professor[0],
            "nome": professor[1]
        }
        list_professsores.append(professores.copy())
    return list_professsores
