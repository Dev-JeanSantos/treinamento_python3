
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Olá {} seu saldo atual é de R${}. Obrigado por utilizar os nossos serviços. ".format(self.titular, self.saldo))

    def deposito(self, valor):
        self.saldo += valor
        print("Novo saldo R${}.".format(self.saldo))

    
    def saque(self, valor):
        self.saldo -= valor
        print("Novo saldo R${}.".format(self.saldo))