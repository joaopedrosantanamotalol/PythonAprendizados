"""
Docstring for atividades.faceis.EscadaNomeInversa

Nome na vertical em escada invertida. 
Altere o programa anterior de modo que a escada seja invertida.
"""

class Escada():
    def __init__(self,Nome):
        self.nome = Nome

    def Processo(self):
        esc = self.nome
        while esc:
            print(esc)
            esc = esc[:-1]

es = Escada("Giovanna")
es.Processo()