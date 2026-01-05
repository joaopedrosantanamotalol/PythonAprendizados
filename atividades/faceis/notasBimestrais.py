"""
Faça um programa que peça as 4 notas bimestrais e mostre a média. 
"""

def notas_bimestrais():
    soma = 0
    for i in range(4):
        nota = float(input (f"Digite a nota do {i+1}° bimestre: "))
        soma += nota
        media = soma / 4
    print(f"a media das notas é {media}")

notas_bimestrais()