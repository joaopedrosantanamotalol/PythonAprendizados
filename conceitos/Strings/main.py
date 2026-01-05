from cliente import cliente
from conta import Conta

cli = cliente("joao", "7373-7373")
conta = Conta(cli.get_nome(),222,333)

conta.depositar(300)
conta.saque(100)
conta.extrato()


class main():
    pass