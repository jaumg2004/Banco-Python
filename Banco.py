menu = """[d]-depositar
          [s]-sacar
          [e]-extrato
          [q]-sair
           """

saldo = 0
limite = 500
extrato = ""

numero_saques = 0
LIMIT_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Informe o valor do depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido")

    if opcao == 's':
        valor = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMIT_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente")

        elif excedeu_limite:
            print("Operação falhou! Você excedeu o limite de saque")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$: {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido")

    if opcao == 'e':
        print("Extrato:")
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}\n")

    if opcao == 'q':
        break
