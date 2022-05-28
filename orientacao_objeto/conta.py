
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Olá {} seu saldo atual é de R${}. Obrigado por utilizar os nossos serviços. ".format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor
        print("Novo saldo R${}.".format(self.__saldo))

    
    def sacar(self, valor):
        self.__saldo -= valor
        print("Novo saldo R${}.".format(self.__saldo))
    
    def transferir(self, valor, contaDestino):
        self.sacar(valor)
        contaDestino.depositar(valor)