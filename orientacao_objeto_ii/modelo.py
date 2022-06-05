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

class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)
        
#SERIES
gameOfThrones = Serie('game of thrones', 2015, 9)
breakingBad = Serie('breaking Bad', 2008, 5)
missaDaMeiaNoite = Serie('missa da meia noite', 2022, 1)
strangerThings = Serie('stranger tThings', 2016, 4)

#FILMES
vingadores = Filme('vingadores - guerra infinita', 2010, 180)
titanic = Filme('titanic', 1998, 160)
eduardoEMonica = Filme('eduardo e monica', 2022, 150)
tropaDeElite = Filme('tropa de elite', 2008, 200)

#LIKES
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
gameOfThrones.dar_likes()
gameOfThrones.dar_likes()



lista_programas = [gameOfThrones, vingadores, titanic, eduardoEMonica,tropaDeElite,breakingBad,missaDaMeiaNoite,strangerThings]
fim_de_semana = Playlist('lista_programas', lista_programas)

tamanho_lista = print(f'tamanho da lista: {len(fim_de_semana)} ')

for programa in fim_de_semana:
    print(programa)