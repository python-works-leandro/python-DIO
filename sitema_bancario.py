menu = """
    ============== Bem vindo ao Banco, ==============
            Seu dinheiro é a minha felicidade !

    Para começar escolha uma letra!

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
"""

saldo           = 0 
limite          = 500
extrato         = ""
numero_saques   = 0
LIMITE_SAQUE    = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Função Deposito selecionado")
        message = " Qual o valor deseja depositar ? "
        valor_deposito = float(input(message))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: {saldo:.2f}! \n"
            print(extrato)
        else:
            print("Operação falhou ! o valor informado é inválido")

    elif opcao == "s":
        print("Função Saque selecionado")

        message = " Qual valor deseja sacar ? "
        valor_saque = float(input (message))

        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE
        
        if excedeu_saldo:
            print("Operação Falhou ! Você não possui saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite diário ")
        
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido" )

        elif valor_saque > 0 :
            saldo -= valor_saque
            extrato += f"Saque : R$ {valor_saque:.2f}\n"
            numero_saques += 1
        else :
            print("Operação falhou ! o valor informado é inválido")

    elif opcao == "e":
        print("Função Extrato selecionado")

        print("\n ============= EXTRATO ============= ")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo :.2f} ")
        print(" ===================================")

    elif opcao == "q":
        print("Função Sair selecionado")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desajada.")


