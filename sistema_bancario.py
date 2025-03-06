# Menu de opções
def exibir_menu():
    menu = """\n
    =============== MENU ================
    [d] Depósito
    [s] Saque
    [e] Extrato
    [q] Sair
    => """
    return input(menu)

# Função de depósito
def realizar_deposito(saldo, extrato):
    valor = float(input("Digite o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

# Função de saque
def realizar_saque(saldo, extrato, limite_saque, limite_diario, saques_realizados):
    valor = float(input("Digite o valor do saque: "))
    if valor <= 0:
        print("Valor inválido para saque.")
    elif valor > saldo:
        print("Saldo insuficiente para o saque.")
    elif valor > limite_saque:
        print(f"O valor excede o limite máximo de saque de R$ {limite_saque}.")
    elif saques_realizados >= limite_diario:
        print("Limite diário de saques atingido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        saques_realizados += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato, saques_realizados

# Função de extrato
def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        print(extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=========================================")

# Função que organiza o fluxo
def iniciar_banco():
    saldo = 0
    extrato = ""
    limite_saque = 500
    limite_diario = 3
    saques_realizados = 0

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            saldo, extrato = realizar_deposito(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, saques_realizados = realizar_saque(saldo, extrato, limite_saque, limite_diario, saques_realizados)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "q":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida, por favor escolha novamente.")

# Iniciando o sistema bancário
iniciar_banco()
