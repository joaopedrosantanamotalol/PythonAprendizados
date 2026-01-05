class Conta():
    def __init__(self,titular,numero,saldo):
        self.titular = titular
        self._numero = numero
        self._saldo = 0
        self.saldo = saldo

    #metodo de verificação e captura de dados
    @property
    def saldo(self):
        return self._saldo
    
    #metodo de verificação e manipulação de dados
    @saldo.setter
    def saldo(self,valor):
        if valor < 0 :
            print("valor negativo paizão?")
        else:
            self._saldo = valor

    def saque(self,valor):
        if (self.saldo >= valor):
            self.saldo -=valor
            print(f"saque no valor de {valor} realizado")

    def depositar(self,deposito):
        self.saldo +=deposito

    def extrato(self):
        print(f"Cliente {self.titular} saldo {self.saldo} ")