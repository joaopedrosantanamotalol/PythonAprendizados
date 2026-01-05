class cliente():
    def __init__(self,n, fone):
        self._nome = n
        self._fone = fone

    #metodo de verificação e captura de dados
    @property
    def nome(self):
        return self.nome
    
    #metodo de verificação e manipulação de dados
    @nome.setter
    def nome(self,nome):
        if (len(nome)) < 2 :
            print("O nome precisa ter mais de 2 caracteres")
        else:
            self.nome = nome
