"""
Docstring for atividades.faceis.InputFatorial

Escreva um algoritmo que pergunte ao usuário um número e após, escreva na 
tela o fatorial do
número lido. Exemplo: Número lido é o 5. Fatorial: 1*2*3*4*5 = 120
"""

class NumeroFatorial():
    def __init__(self):
        self.n = 0

    def processo(self):
       self.n = int(input("Digite o numero para torna-lo fatorial: "))
       fatorial = 1

       """ 
       o (1, self.n + 1) diz que vai do numero 1 até o indice em escala 
       numerica de self.n utilizando o +1 para ir de 1 até o valor final de self.n
       assim não conta de 0 -> 5 e sim de 1 -> 5
       """
       
       for numero in range(1, self.n + 1): 
           fatorial *= numero
       print(f"O numero {self.n} em fatorial é {fatorial}")

fato = NumeroFatorial()
fato.processo()