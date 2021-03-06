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

#Aqui utilizamos essa estrategia para herdar tudo que vem do list (Desnecessário o uso de todos os metodos do list nesse caso) 
# class Playlist(list):
#     def __init__(self, nome, programas):
#         self.nome = nome
#         super().__init__(programas)



#Aqui utilizamos essa estrategia de utilizar apenas o necessario de um list (duck typing - mas performático pro caso) 
class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    #metodo que gera o duck typing
    def __getitem__(self, items):
        return self._programas[items]

    @property
    def listagem(self):
        return self._programas

    # @property
    # def tamanho(self):
    #     return len(self._programas)

    #metodo que gera o o tamanho de uma lista
    def __len__(self):
        return len(self._programas)

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
playlist_fim_de_semana = Playlist('lista_programas', lista_programas)

tamanho_lista = print(f'tamanho da lista: {len(playlist_fim_de_semana)}')

print(titanic in playlist_fim_de_semana)
print(f'Ultimo programa da Playlist: {playlist_fim_de_semana[7]}')


for programa in playlist_fim_de_semana:
    print(programa)