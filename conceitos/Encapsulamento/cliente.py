#classe cliente
class cliente():
    #construtor
    def __init__(self,n, fone):
        self.nome = n
        self.phone = fone

    #pega o nome
    def get_nome(self):
        return self.nome
    
    #define o nome
    def set_nome(self, nome):
        self.nome = nome

    #pega o telefone
    def get_telefone(self):
        return self.phone
