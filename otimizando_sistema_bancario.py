import textwrap

# Função em torno de uma classe 
class Banco:
    def __init__(self):
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0
        self.limite = 500
        self.limite_saques = 3
        self.usuarios = []
        self.contas = []
        self.agencia = "0001"
    
    # Menu de opções
    def menu(self):
        menu = """\n
        ================ MENU ===================
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova Conta
        [lc]\tListar Contas
        [nu]\tNovo Usuário
        [q]\tSair
        => """
        return input(textwrap.dedent(menu))
    
    # Função de depósito
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    # Função de saque
    def sacar(self, valor):
        if valor <= 0:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        elif valor > self.saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif valor > self.limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif self.numero_saques >= self.limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        else:
            self.saldo -= valor
            self.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            self.numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
    
    # Função de exibição do extrato
    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("=========================================")

    # Função para filtrar usuário
    def filtrar_usuario(self, cpf):
        return next((usuario for usuario in self.usuarios if usuario["cpf"] == cpf), None)
    
    # Função para criar um novo usuário
    def criar_usuario(self):
        cpf = input("Informe o CPF (somente número): ")
        if self.filtrar_usuario(cpf):
            print("\n@@@ Já existe usuário com esse CPF! @@@")
            return

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

        self.usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("=== Usuário criado com sucesso! ===")

    # Função para criar nova conta
    def criar_conta(self):
        cpf = input("Informe o CPF do usuário: ")
        usuario = self.filtrar_usuario(cpf)
        if usuario:
            numero_conta = len(self.contas) + 1
            self.contas.append({"agencia": self.agencia, "numero_conta": numero_conta, "usuario": usuario})
            print("\n=== Conta criada com sucesso! ===")
        else:
            print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    
    # Função para listar contas
    def listar_contas(self):
        if not self.contas:
            print("\n@@@ Não há contas cadastradas. @@@")
        else:
            for conta in self.contas:
                print("=" * 100)
                print(f"Agência: {conta['agencia']}")
                print(f"C/c: {conta['numero_conta']}")
                print(f"Titular: {conta['usuario']['nome']}")
    
    # Função que organiza o fluxo
    def rodar(self):
        while True:
            opcao = self.menu()

            if opcao == "d":
                valor = float(input("Informe o valor do depósito: "))
                self.depositar(valor)

            elif opcao == "s":
                valor = float(input("Informe o valor do saque: "))
                self.sacar(valor)

            elif opcao == "e":
                self.exibir_extrato()

            elif opcao == "nu":
                self.criar_usuario()

            elif opcao == "nc":
                self.criar_conta()

            elif opcao == "lc":
                self.listar_contas()

            elif opcao == "q":
                print("Saindo do sistema...")
                break

            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")


# Rodando o sistema bancário
banco = Banco()
banco.rodar()
