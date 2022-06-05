class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title() #Inicia todas as letras como Maiuscula
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes
    
    @property
    def nome(self):
        return self._nome


    def dar_likes(self):
        self._likes += 1
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    
    def __str__(self) -> str:
        return f'Nome do Filme: {self._nome} - Ano de Lançamento: {self.ano} - Duração: {self.duracao} Minutos - Likes: {self._likes}'



class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self) -> str:
        return f'Nome do Filme: {self._nome} - Ano de Lançamento: {self.ano} - Duração: {self.duracao} Minutos - Likes: {self._likes}'
    

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self) -> str:
        return f'Nome do Filme: {self._nome} - Ano de Lançamento: {self.ano} - Temporadas: {self.temporadas} - Likes: {self._likes}'

gameOfThrones = Serie('game of thrones', 2015, 9)
vingadores = Filme('vingadores - guerra infinita', 2010, 60)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
gameOfThrones.dar_likes()
gameOfThrones.dar_likes()

#print(f'Nome da Série: {gameOfThrones.nome} - Ano: {gameOfThrones.ano} - Temporadas: {gameOfThrones.temporadas} - Likes: {gameOfThrones.likes} ') 

lista_programas = [vingadores, gameOfThrones]
for programa in lista_programas:
    print(programa)