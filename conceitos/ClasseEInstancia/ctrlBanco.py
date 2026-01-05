"""
    Vamos iniciar um projeto de controle bancário!

O objetivo do projeto é o desenvolvimento orientado a objetos para a execução de tarefas do cotidiano bancário, como saque, consulta de saldo e depósito.

Durante esta aula, já desenvolvemos a classe Cliente e seus atributos. Agora, vamos desenvolver a classe Conta, que será definida recebendo o objeto Cliente, além dos atributos “número” e “saldo”.

Classe Conta

Para desenvolver a classe Conta, crie um novo arquivo Python, por meio do menu File-New. Na caixa de texto New, escolha a opção Python File. Digite o nome Conta e pressione a tecla Enter, para finalizar.

Logo após, adicione a codificação inicial para a classe:
"""

#criando objeto conta
class Conta():
        #construtor criador de variaveis
        def __init__(self,titular, numero, saldo):
            self.saldo = saldo
            self.numero = numero
            self.titular = titular
