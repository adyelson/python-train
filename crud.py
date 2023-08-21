import sqlite3


conn = sqlite3.connect("aula.db")


conn.execute('''CREATE TABLE IF NOT EXISTS alunos
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INT NOT NULL
            );''')


def cria_aluno(conn,nome,idade):
    alunoCriado = conn.execute("INSERT INTO alunos(nome, idade) VALUES (?,?);", (nome,idade))
    conn.commit()
    print("Aluno criado com sucesso!")  
    return alunoCriado

def listar_alunos(conn):
    listaAlunos = conn.execute("SELECT * FROM alunos;").fetchall()
    for aluno in listaAlunos:
        print(aluno)
    return listaAlunos

def atualizar_aluno(conn, id, nome,idade):
    alunoAtualizado = conn.execute("UPDATE alunos SET nome = ?, idade = ? WHERE id = ?;", (nome, idade, id))
    conn.commit()
    return alunoAtualizado

def deletar_aluno(conn,id):
    alunoDeletado = conn.execute("DELETE FROM alunos WHERE id = ?;", (id,))
    conn.commit()
    return alunoDeletado

# cria_aluno("Mario", 20)
# cria_aluno("Maria", 60)
# cria_aluno("José", 10)
# cria_aluno("Pedro", 30)
# cria_aluno("Marta", 40)

# atualizar_aluno(9, 'Felix', 31)
# deletar_aluno(8)
# listar_alunos(conn)