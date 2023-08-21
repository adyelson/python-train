import unittest
import sqlite3
from crud import listar_alunos, atualizar_aluno, deletar_aluno, cria_aluno


class TestCrud(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute('''CREATE TABLE IF NOT EXISTS alunos
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INT NOT NULL
            );''')
    def tearDown(self):
        self.conn.close()

    def test_listar_alunos(self):
        cria_aluno(self.conn, "josé", 66)
        cria_aluno(self.conn, "josé", 66)
        cria_aluno(self.conn, "josé", 66)
        alunos = listar_alunos(self.conn)     
        self.assertEqual(len(alunos),3)
       
        
    def test_atualizar_alunos(self):
        cria_aluno(self.conn, "josé", 66)
        atualizar_aluno(self.conn,1, "mario", 626)
        aluno = self.conn.execute("SELECT * FROM alunos WHERE id = 1").fetchone()
        self.assertEqual(aluno[1],"mario")
        

    def test_cria_aluno(self):
        cria_aluno(self.conn, "josé", 66)
        alunos = self.conn.execute("SELECT * FROM alunos").fetchall()
        self.assertEqual(len(alunos),1)
        self.assertEqual(alunos[0][1],"josé")

        

    def test_deletar_alunos(self):
        cria_aluno(self.conn, "josé", 66)
        cria_aluno(self.conn, "mario", 66)
        deletar_aluno(self.conn,1)
        alunos = self.conn.execute("SELECT * FROM alunos").fetchall()
        self.assertEqual(len(alunos),1)
        self.assertEqual(alunos[0][1], 'mario')
        
