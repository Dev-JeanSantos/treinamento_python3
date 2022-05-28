class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("Uso do @property para chamar um getter")
        return self.__nome.title()
 
    @nome.setter
    def nome(self, nome):
        print("Uso do @nome.setter para chamar um setter")
        self.__nome = nome
 