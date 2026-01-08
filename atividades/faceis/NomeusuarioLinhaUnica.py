"""
Docstring for atividades.faceis.NomeusuarioLinhaUnica
Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
"""

class NomeVertical():
    def __init__(self,nome : str):
        self.nome = nome

    def Processo(self):
        for letra in self.nome:
            print(letra)

proc = NomeVertical("Paulo")
proc.Processo()