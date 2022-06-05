class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao


vingadores = Filme('Vingadores - Guerra Infinita', 2010, 60)
print(vingadores.nome)


