class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.sobrenome = sobrenome
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} {self.sobrenome} tem {self.idade} anos"


class Cachorro:
    def __init__(self, nome, raca, idade):
        self.raca = raca
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} é da raça {self.raca} e tem {self.idade} anos"

    def is_cachorro(self):
        return True

moyses = Pessoa(nome='MOyses', sobrenome='Santos', idade=31)
print(moyses)

scooby = Cachorro(nome='Scooby', raca='dane dog', idade=5.9)
print(scooby)
print(scooby.is_cachorro())


class EngenheiroDeDados(Pessoa):
    def __init__(self, nome, sobrenome, idade, experiencia):
        super().__init__(nome, sobrenome, idade)
        self.experiencia = experiencia

    def __str__(self):
        return f"{self.nome} {self.sobrenome} tem {self.idade} anos, " \
               f"é Engenheiro de Dados e tem {self.experiencia} anos de experiencia"

moyses = EngenheiroDeDados(nome='Moyses', sobrenome='Santos', idade=31, experiencia=2)
print(moyses)