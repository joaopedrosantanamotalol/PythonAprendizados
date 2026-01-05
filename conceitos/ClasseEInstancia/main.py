#imports das classes
from ClasseEConstrutor import cliente
from ctrlBanco import Conta

#instancia das classes
cli = cliente("joao","999999999")
banco = Conta(cli.nome,cli.telefone,0)

#exibição das classes e seus dados com passagem de valor entre classes
print(f"dados cliente\nnome:{banco.titular} saldo:{banco.saldo} numero:{banco.numero}")

#declaração da classe principal, main
class main():
    pass

