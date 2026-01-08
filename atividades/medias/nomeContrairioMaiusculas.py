class MaiusculaInversa():
    def __init__(self):
        self.f = input("Digite sua frase: ")

    def processar(self):
        fraseinversa = ""
        for i in self.f:
            fraseinversa = i.upper() + fraseinversa
            
        print(fraseinversa)
    
MI = MaiusculaInversa()
MI.processar()