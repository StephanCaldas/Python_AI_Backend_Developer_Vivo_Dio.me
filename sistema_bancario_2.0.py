def menu():

    menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Listar contas
    [6] Novo usuário
    [0] Sair

    """
    print(menu)
    opcao = int(input("Digite a operação desejada: "))
    print()

    return opcao


def depositar(saldo, extrato):

    valor = float(input("Digite o valor do depósito: "))

    if valor > 0:
        saldo += valor
        resultado = f"+ Depósito   = R${valor:.2f}"
        extrato.append(resultado)
        print()
        print("Depósito realizado com sucesso!")
        return saldo, extrato

    elif valor <= 0:
        print()
        return "O valor mínimo para depósito é de R$1.00!"

    else:
        print()
        return "Opção inválida!"


def sacar(limite, saldo, extrato, limite_saques, numero_saques):

    valor = float(input("Digite o valor do saque: "))

    if valor > saldo:
        print()
        print("Não há saldo suficiente na conta!")

    elif valor <= 0:
        print()
        print("Valor para saque inválido!")

    elif valor > 0 and valor <= limite:
        if numero_saques < limite_saques:
            saldo -= valor
            resultado = f"- Saque      = R${valor:.2f}"
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

    return saldo, extrato, numero_saques


def exibir_extrato(extrato, saldo):

    print()
    print("======== Extrato ========")
    for i, e in enumerate(extrato):
        print(e)
    print()
    print(f"* Saldo      = R${saldo:.2f}")
    print("=" * 25)


def criar_usuario(usuarios):

    cpf = int(input("Informe o CPF (somente números): "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print()
        print("Já existe usuário com esse CPF!")
        return

    nome = str(input("Informe o nome completo: "))
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): "
    )

    usuarios.append(
        {
            "nome": nome,
            "cpf": cpf,
            "data_nascimento": data_nascimento,
            "endreco": endereco,
        }
    )

    print()
    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):

    cpf = int(input("Informe o CPF do usuário: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print()
        print("=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print()
    print("Usuário não encontrado. Não é possivel criar uma conta sem usuário!")


def listar_contas(contas):

    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


def main():

    DEPOSITAR = 1
    SACAR = 2
    EXTRATO = 3
    NOVA_CONTA = 4
    LISTAR_CONTAS = 5
    NOVO_USUARIO = 6
    SAIR = 0

    saldo = 0
    limite = 500
    extrato = list()
    numero_saques = 0
    usuarios = list()
    contas = list()
    numero_conta = 1

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:

        opcao = menu()

        if opcao == DEPOSITAR:

            saldo, extrato = depositar(saldo, extrato)

        elif opcao == SACAR:

            saldo, extrato, numero_saques = sacar(
                limite=limite,
                saldo=saldo,
                extrato=extrato,
                limite_saques=LIMITE_SAQUES,
                numero_saques=numero_saques,
            )

        elif opcao == EXTRATO:

            exibir_extrato(extrato, saldo)

        elif opcao == NOVO_USUARIO:

            criar_usuario(usuarios)

        elif opcao == NOVA_CONTA:

            # numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == LISTAR_CONTAS:

            listar_contas(contas)

        elif opcao == SAIR:

            print("Obrigado por utilizar nosso sistema! Até logo!!!")
            break

        else:
            print()
            print(
                "Opção inválida," " por favor selecione novamente a operação desejada."
            )


main()
