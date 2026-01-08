"""
Docstring for atividades.medias.nomeContrairioMaiusculas
Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o 
seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente 
letras maiúsculas. Dica: lembre−se 
que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
"""

class MaiusculaInversa():
    def __init__(self):
        print("Pode digitar em letras maiusculas e minusculas")
        self.f = input("Digite sua frase: ")


    def processar(self):
       
      """ Versão rápida utilizando Slice
      fraseInversa = self.f[::-1] # inverte a ordem da String
      print(fraseInversa)

      """

    """ Versão diática utilizando soma do indice na variavel
    fraseinversa = ""
    for i in self.f:
        fraseinversa = i.upper() + fraseinversa
            
        print(fraseinversa)
    """
        
MI = MaiusculaInversa()
MI.processar()