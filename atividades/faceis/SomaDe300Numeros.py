"""
Docstring for atividades.faceis.SomaDe300Numeros

Escreva um algoritmo para ler 300 números e escrever a soma total dos 300 
números lidos (usando a estrutura de repetição for)
"""

class SomaDeNumeros():
    def __init__(self,vezes):
        try:
            self.v = int(vezes)
        except ValueError:
             print("tipo de dados errado boy, loop não vai rodar")
             self.v = 0

    def op(self):
        resultado = 0
        for _ in range(self.v):
            n = int(input("Digite o numero para realizar a soma: "))
            resultado += n

        print(f"o resultado da soma é: {resultado}")

a = SomaDeNumeros(300)
a.op()