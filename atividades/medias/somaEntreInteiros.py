"""
Escreva um algoritmo para ler 2 números e escrever a soma 
dos inteiros existentes entre os 2
números lidos (incluindo os números lidos na soma). E
xemplo: Números lidos: 2 e 5 Resultado:
2+3+4+5 = 14. Observação: Considere que o segundo valor lido 
será sempre maior que o primeiro
valor lido.
"""

class EntreNumeros():
    def __init__(self, n1 = 0, n2 = 0):
        self.num1 = n1
        self.num2 = n2

    def processo(self):
        soma = 0
        inicio = min(self.num1, self.num2)
        fim = max(self.num1,self.num2)

        for i in range(inicio, fim + 1):
            soma += i
        print(f"o resultado da soma dos numeros entre {self.num1} e {self.num2} é {soma}")
entr = EntreNumeros(1,5)
entr.processo()