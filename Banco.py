from datetime import datetime

class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.limite = 500
        self.limite_personalizado = 1000
        self.extrato = ""
        self.numero_saques = 0
        self.LIMIT_SAQUES = 10

    def depositar(self, valor):
        try:
            if valor > 0:
                self.saldo += valor
                self.extrato += f"Depósito: R$ {valor:.2f}\n"
                print(f"Horário do depósito: {datetime.now().strftime('%d/%m/%Y %H:%M:%S ')}")
            else:
                raise ValueError("Operação falhou! O valor informado é inválido")
        except ValueError as e:
            print(e)

    def sacar(self, valor):
        try:
            excedeu_saldo = valor > self.saldo
            excedeu_limite = valor > self.limite
            excedeu_limite_personalizado = valor > self.limite_personalizado
            excedeu_saques = self.numero_saques >= self.LIMIT_SAQUES

            if excedeu_saldo:
                raise ValueError("Operação falhou! Você não tem saldo suficiente")
            elif excedeu_limite_personalizado:
                raise ValueError("Operação falhou! Você excedeu o limite de saque personalizado")
            elif excedeu_limite:
                raise ValueError("Operação falhou! Você excedeu o limite de saque")
            elif excedeu_saques:
                raise ValueError("Operação falhou! Número máximo de saques excedido")
            elif valor <= 0:
                raise ValueError("Operação falhou! O valor informado é inválido")
            else:
                self.saldo -= valor
                self.extrato += f"Saque R$: {valor:.2f}\n"
                self.numero_saques += 1
                print(f"Horário do saque: {datetime.now().strftime('%d/%m/%Y %H:%M:%S ')}")
        except ValueError as e:
            print(e)

    def ver_extrato(self):
        print("Extrato:")
        print(self.extrato)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print(f"Horário: {datetime.now().strftime('%d/%m/%Y %H:%M:%S ')}")

    def autenticar(self, senha):
        if senha == self.senha:
            return True
        else:
            print("Senha incorreta!")
            return False

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
        senha = input("Digite sua senha: ")
        if conta.autenticar(senha):
            valor = float(input("Informe o valor do saque:"))
            conta.sacar(valor)

    elif opcao == 'e':
        conta.ver_extrato()

    elif opcao == 'q':
        break
    else:
        print("Opção inválida!")
