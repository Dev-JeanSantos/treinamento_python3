
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Olá {} seu saldo atual é de R${}. Obrigado por utilizar os nossos serviços. ".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor
        print("Novo saldo R${}.".format(self.__saldo))

    
    def saca(self, valor):
        self.__saldo -= valor
        print("Novo saldo R${}.".format(self.__saldo))
    
    def transfere(self, valor, contaDestino):
        self.sacar(valor)
        contaDestino.depositar(valor)

    #Getters com OO no python
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    #Setters com OO no python
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
