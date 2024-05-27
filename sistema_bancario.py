menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

saldo = 0
limite = 500
extrato = list()
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(menu)
    opcao = int(input("Digite a operação desejada: "))
    print()

    if opcao == 1:
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            resultado = (f"+ Depósito   = R${valor:.2f}")
            extrato.append(resultado)
            print()
            print("Depósito realizado com sucesso!")

        elif valor <= 0:
            print()
            print("O valor mínimo para depósito é de R$1.00!")

        else:
            print()
            print("Opção inválida!")

    elif opcao == 2:
        valor = float(input("Digite o valor do saque: "))

        if valor > saldo:
            print()
            print("Não há saldo suficiente na conta!")

        elif valor <= 0:
            print()
            print("Valor para saque inválido!")

        elif valor > 0 and valor <= limite:
            if numero_saques < LIMITE_SAQUES:
                saldo -= valor
                resultado = (f"- Saque      = R${valor:.2f}")
                extrato.append(resultado)
                numero_saques += 1
                print()
                print("Saque realizado com sucesso!")

            elif numero_saques >= 3:
                print()
                print("O limite de 3 saques diários foi atingido!")

            else:
                print()
                print("Opção inválida!")

        elif valor > limite:
            print()
            print("Valor máximo para saque é de R$500.00!")

        else:
            print()
            print("Operação inválida!")

    elif opcao == 3:
        print()
        print("======== Extrato ========")
        for i, e in enumerate(extrato):
            print(e)
        print()
        print(f"* Saldo      = R${saldo:.2f}")
        print("=" * 25)

    elif opcao == 0:
        break

    else:
        print()
        print("Opção inválida,"
              " por favor selecione novamente a operação desejada.")

print("Obrigado por utilizar nosso sistema! Até logo!!!")
