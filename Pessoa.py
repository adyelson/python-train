class Pessoa():
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
    def saudacao(self):
        return(f"Meu nome é {self.nome}")


pessoa = Pessoa("josé", 20)

print(pessoa.saudacao())


class Professor (Pessoa):
    def __init__(self,nome,idade ,salario):
        super().__init__(nome,idade)
        self.salario = salario
    def info(self):
        print(f"Meu salario é {self.salario}")

professor = Professor("joão",20, 3300)

print(professor.salario)

professor.info()
