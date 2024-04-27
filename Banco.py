from datetime import datetime

class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMIT_SAQUES = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Horário do deposito: {datetime.now()}")
            return True
        else:
            print("Operação falhou! O valor informado é inválido")
            return False

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.LIMIT_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente")
            return False
        elif excedeu_limite:
            print("Operação falhou! Você excedeu o limite de saque")
            return False
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido")
            return False
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque R$: {valor:.2f}\n"
            self.numero_saques += 1
            print(f"Horário do saque: {datetime.now()}")
            return True
        else:
            print("Operação falhou! O valor informado é inválido")
            return False

    def ver_extrato(self):
        print("Extrato:")
        print(self.extrato)
        print(f"Saldo atual: R$ {self.saldo:.2f}\n")
        print(datetime.now())

conta = ContaBancaria()
menu = """[d]-depositar
[s]-sacar
[e]-extrato
[q]-sair
"""

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Informe o valor do depósito:"))
        conta.depositar(valor)

    elif opcao == 's':
        valor = float(input("Informe o valor do saque:"))
        conta.sacar(valor)

    elif opcao == 'e':
        conta.ver_extrato()

    elif opcao == 'q':
        break
