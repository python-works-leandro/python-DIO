import textwrap

def menu():
    menu = """
    ============== Bem vindo ao Banco, ==============
            Seu dinheiro é a minha felicidade !

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    """

    return input(textwrap.dedent(menu))

def depositar(saldo, valor_deposito, extrato, /):

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: {saldo:.2f}! \n"
        print("\n === Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou ! o valor informado é inválido. @@@")
                
    return saldo, extrato


def sacar(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saque):
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques >= limite_saque
        
        if excedeu_saldo:
            print("\n@@@ Operação Falhou ! Você não possui saldo suficiente. @@@")

        elif excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite diário @@@")
        
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@" )

        elif valor_saque > 0 :
            saldo -= valor_saque
            extrato += f"Saque : R$ {valor_saque:.2f}\n"
            numero_saques += 1
        else :
            print("\n@@@ Operação falhou ! o valor informado é inválido. @@@")

        return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):

    print("\n ============= EXTRATO ============= ")
    print("Não foram realizados movimentações." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo :.2f} ")
    print(" ===================================")

def criar_usuario(usuarios):

    cpf = input("informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_de_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidadde/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_de_nascimento": data_de_nascimento,
        "cpf": cpf,
        "endereco": endereco
         })

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]== cpf]

    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):

    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de  criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""
                Agência:\t{conta['agencia']}
                C/c\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES    = 3
    AGENCIA         = "0001"

    saldo           = 0 
    limite          = 500
    extrato         = ""
    numero_saques   = 0
    usuarios        = []
    contas          = []

    while True:
        opcao = menu()

        if opcao == "d":

            valor_deposito = float(input("Qual o valor deseja depositar ? "))

            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao == "s":
            print("Função Saque selecionado")

            valor_saque = float(input (" Qual valor deseja sacar ? "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite=limite, 
                numero_saques=numero_saques,
                limite_saque=LIMITE_SAQUES,
            )           

        elif opcao == "e":
            print("Função Extrato selecionado")

            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Função Sair selecionado")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desajada.")



main()



