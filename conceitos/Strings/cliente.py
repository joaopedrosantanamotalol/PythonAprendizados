class cliente():
    def __init__(self,n, fone):
        self.nome = n
        self.phone = fone

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome
