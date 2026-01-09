"""
Docstring for atividades.medias.lerdeznumeros
Escreva um algoritmo para ler 10 numeros e escrever quantos desses numeros lidos são
NEGATIVOS.
"""

class LerNumerosENegativos():
    def __init__(self, n1):
        self.vezes = n1

    def processo(self):
        numeros = []
        negativos = []
        valores = 0

        for i in range(self.vezes):
            valores = int(input(f"Digite o {i + 1 } numero: "))
            numeros.append(valores)
        print(f"todos os numeros que temos são: {numeros}")
            
        for numero in numeros:
            if numero < 0:
                negativos.append(numero)
        print(f"nossos numeros negativos são {negativos}")

        if len(negativos) > 0:
            print(f"existem {len(negativos)} numero(s) negativos, ele(s) são {negativos}")
        else:
            print("Não existem")


entr = LerNumerosENegativos(10)
entr.processo()