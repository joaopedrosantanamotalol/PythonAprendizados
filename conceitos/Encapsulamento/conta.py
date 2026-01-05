class Conta():
    def __init__(self,titular,numero,saldo, telefone):
        self.titular = titular
        self._numero = numero
        self._saldo = 0
        self.saldo = saldo
        self.phone = telefone

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
    #pega o valor de (saldo) e subtrai o valor de (saldo) em valor
    def saque(self,valor):
        if (self.saldo >= valor):
            self.saldo -=valor
            print(f"saque no valor de {valor} realizado")
    #pega o valor de (saldo) e adciona o valor de (saldo) em valor
    def depositar(self,deposito):
        self.saldo +=deposito
    #exibe no terminal todas as informações
    def extrato(self):
        print(f"Cliente {self.titular} saldo {self.saldo} telefone {self.phone}")