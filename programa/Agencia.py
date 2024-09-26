from Conta import Conta

class Agencia():
    def __init__(self):

        self.contas = []
        self.contador = 1

    def opcao(self):
        while True:
            print("------------------------------------------------------")
            print("         Bem-Vindo ao nosso Caixa Eletrônico          ")
            print("------------------------------------------------------")
            print("|   Opção 1 - Criar conta   |")
            print("|   Opção 2 - Depositar     |")
            print("|   Opção 3 - Sacar         |")
            print("|   Opção 4 - Transferir    |")
            print("|   Opção 5 - Listar Contas |")
            print("|   Opção 6 - Sair          |")
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                self.criar_conta()

            elif opcao == 2:
                self.depositar()

            elif opcao == 3:
                self.sacar()

            elif opcao == 4:
                self.transferir()

            elif opcao == 5: 
                self.listar_contas()

            elif opcao == 6:
                print("\nSaindo ...")
                break

            else:
                print("\nOpção inválida")
    
    def criar_conta(self):

        id = self.contador
        self.contador += 1
        nome = input("\nDigite seu nome: ")
        cpf = input("Digite seu CPF: ")
        email = input("Digite seu Email: ")
        saldo = 0

        nova_conta = Conta(id, nome, cpf, email, saldo)
        self.contas.append(nova_conta)

        print("\nConta criada com sucesso!")
    
    def depositar(self):

        id_conta = int(input("Número da conta: "))
        id_indice = id_conta - 1

        if (self.contas[id_indice] is not None):
             
             valor_deposito = float(input("Digite o valor a ser depositado: "))
             if valor_deposito > 0:
                  self.contas[id_indice].saldo += valor_deposito
                  print(f"\nDepósito de {valor_deposito} realizado com sucesso")
             else:
                  print("\nValor inválido")
        else:
             print("\nConta não encontrada")
    
    def sacar(self):

        id_conta = int(input("Número da conta: "))
        id_indice = id_conta - 1

        if (self.contas[id_indice] is not None):
             valor_saque = float(input("Digite o valor a ser sacado: "))
             if valor_saque > 0:
                  self.contas[id_indice].saldo -= valor_saque
                  print(f"\nSaque de {valor_saque} realizado com sucesso")
             else:
                  print("\nValor inválido")
        else:
             print("\nConta não encontrada")

    def transferir(self):
         
         id_conta_remetente = int(input("Digite o ID da conta remetente: "))
         id_indice_remetente = id_conta_remetente - 1

         id_conta_destinatario = int(input("Digite o ID da conta destinátario: "))
         id_indice_destinatario = id_conta_destinatario - 1

         valor_transferido = float(input("Digite o valor a ser transferido: "))

         if (self.contas[id_indice_destinatario] and self.contas[id_indice_remetente] is not None):
              if valor_transferido > 0:
                   self.contas[id_indice_remetente].saldo -= valor_transferido
                   self.contas[id_indice_destinatario].saldo += valor_transferido
              else:
                   print("\nValor inválido!")  
         else:
              print("\nConta não encontrada!")

    def listar_contas(self):

        if not self.contas:
             print("\nNenhum conta regristada!")

        else:
             print("-- Contas Cadastradas --")
             for conta in self.contas:
                  print(conta)

def main():
    agencia = Agencia()
    agencia.opcao()

if __name__ == '__main__':
    main()