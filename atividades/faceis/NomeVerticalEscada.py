"""
Docstring for atividades.faceis.NomeVerticalEscada
Nome na vertical em escada. Modifique o programa 
anterior de forma a mostrar o nome em formato de escada.
"""

class Escada():
    def __init__(self,Nome):
        self.nome = Nome

    def Processo(self):
        esc = ""
        for letra in self.nome:
            esc += letra
            print(esc)

es = Escada("Giovanna")
es.Processo()