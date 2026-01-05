"""
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas 
seguido do seu comprimento. Informe também se as duas strings possuem o mesmo 
comprimento e são iguais ou diferentes no conteúdo.
"""

class CompStrings():
    def __init__(self,st1, st2):
        self.str1 = st1
        self.str2 = st2
    
    def VerSeSaoIguais(self):
        if self.str1 == self.str2:
            print("São iguais")
        else:
            print("diferentes")

    def VerSeMesmoTamanho(self):
        tm1 = len(self.str1)
        tm2 = len(self.str2)
        print(f"o tamanho da 1° string é: {tm1}\ne o tamamnho da 2° string é: {tm2}")
        
    def ConteudoString(self):
        cont1 = self.str1
        cont2 = self.str2
        print(f"as string dizem {cont1} e {cont2}")

comp = CompStrings("AA","AA")
comp.VerSeSaoIguais()
comp.VerSeMesmoTamanho()
comp.ConteudoString()
