class Conta():
    def __init__(self,titular,numero,saldo):
        self.titular = titular
        self._numero = numero
        self.saldo = saldo

    #metodo de verificação e captura de dados
    @property
    def numero(self):
        return self._numero
    
    #metodo de verificação e manipulação de dados
    @numero.setter
    def numero(self,numero):
        if numero < 0 :
            print("valor negativo paizão?")
        else:
            self._numero = numero