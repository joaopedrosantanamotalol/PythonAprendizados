"""
Faça um programa que converta metros para centímetros:
"""

def MetrosParaCentimetros():
    m = 0
    c = 0
    const = 1000
    decisao = ""
    cont = ""
    decisao = input("Voce quer começar o programa?: ").lower().strip()

    while decisao == "sim":
        deci = input("""
1- Voce quer converter metros para centimetros
2- ou centimetros para metros?
(1 ou 2)\n"""
        )
        
        if deci == "1":
            m = int(input("Digite quantos metros você tem\n"))
            print(f"O resultado é {m * const} centimetros")

            cont = input("deseja continuar? Sim / Não\n").lower().strip()
            if cont == "sim":
                pass
            else:
                decisao = "nao"

        if deci == "2":
            c = int(input("Digite quantos centimetrôs você tem\n"))
            print(f"O resultado é {c / const} metros")
            cont = input("deseja continuar? Sim / Não\n").lower().strip()
            if cont == "sim":
                pass
            else:
                decisao = "nao"
        else:
            decisao = "Não"

MetrosParaCentimetros()