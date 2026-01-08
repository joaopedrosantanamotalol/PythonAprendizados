"""
Docstring for atividades.faceis.quantasVezesDigitar
Escreva um algoritmo que pergunte ao usuário quantos números ele quer digitar. Após isto, o
algoritmo deve ir lendo os números que o usuário digitar e armazenar a 
soma total dos números lidos.
Após a leitura dos números, escrever na tela a soma calculada.
"""

class VezesDigitar():
    def __init__(self):
        self.v = 0

    def processo(self):
        self.v = int(input("Digite quantos numeros você quer digitar: "))
        resultado = 0
        
        for _ in range(self.v):
            valor = int(input("Digite seu numero: "))
            resultado += valor
        print(f"a soma dos numeros é {resultado}")

vezes = VezesDigitar()
vezes.processo()