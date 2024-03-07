# sistema bancário com POO
# classes: Conta, Cliente, Extrato

# importando bibliotecas
import random
import datetime

# classe Cliente
class Cliente:
    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf
        self._contas = [] # lista de contas -> protected

    def abreConta(self, tipoConta, saldoInicial):
        if tipoConta == 'corrente':
            conta = ContaCorrente(saldoInicial) # criada embaixo
        elif tipoConta == 'poupanca':
            conta = ContaPoupanca(saldoInicial)
        else:
            raise ValueError('Tipo de conta inválido')

        self._contas.append(conta)
        return conta
    
    def __str__(self): # forma usual de printar em POO
        return f'Nome: {self.name}\nCPF: {self.cpf}'
    

# classe Conta
class Conta: # estrutura obrigatoria de todas as contas
    def __init__(self, saldoInicial=0): # metodo construtor pra criar conta
        self.numeroConta = random.randint(1000, 9999) # numero aleatorio de 4 digitos
        self._saldo = saldoInicial # pode iniciar com um valor diferente de zero -> saldo padrão depois das movimentações
        self._transacoes = [] # lista de transacoes -> protected

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._registraTransacao(f"Depósito de R$ {valor}")
        else:
            raise ValueError('Valor de depósito inválido')
        
    def sacar(self, valor):
        if valor > 0 and self._saldo >= valor:
            self._saldo -= valor
            self._registraTransacao(f"Saque de R$ {valor}")

    def _registraTransacao(self, descricao):
        time = datetime.datetime.now() # chama a biblioteca datetime, chama a funcao datetime e pega a hora atual
        self._transacoes.append((time, descricao)) # descricao eh o print

    def extrato(self):
        print(f"Extrato da conta {self.numeroConta}:")
        for time, descricao in self._transacoes:
            print(f"{time}: {descricao}")
        print(f"Saldo atual: R$ {self._saldo}") # encapsulamento de protected


# classe ContaCorrente
class ContaCorrente(Conta): # herda atributos da class conta
    def __init__(self, saldoInicial=0):
        super().__init__(saldoInicial) # chama o metodo construtor da classe mae
        self._tipo = 'corrente' # atributo especifico da classe

    def __str__(self):
        return f'Conta Corrente de número: {self.numeroConta} possui saldo de R$ {self._saldo}'
    

# classe ContaPoupanca
class ContaPoupanca(Conta):
    def __init__(self, saldoInicial=0):
        super().__init__(saldoInicial)
        self._tipo = 'poupanca'
        self._taxaJuros = 0.2 # taxa de juros de 20%
    
    def calculaJuros(self):
        juros = self._saldo * self._taxaJuros
        self._saldo += juros
        self._registraTransacao(f"Rendimento de juros de R$ {juros}")
    
    def __str__(self):
        return f'Conta Poupança de número {self.numeroConta} possui saldo de R$ {self._saldo}'
    

# main
if __name__ == '__main__':
    count = 0
    name = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    while cpf.__len__() != 11:
        print("CPF inválido")
        cpf = input("Digite um CPF valido: ")
        

    # cria cliente
    cliente1 = Cliente(name, cpf)
    print(cliente1)

    conta = input("Digite o tipo de conta (corrente ou poupanca): ")
    while conta != 'corrente' and conta != 'poupanca':
        print("Tipo de conta inválido")
        conta = input("Digite o tipo de conta (corrente ou poupanca): ")
    
    saldo = float(input("Digite o saldo inicial da conta: "))
    while saldo < 0:
        print("Saldo inválido")
        saldo = float(input("Digite o saldo inicial da conta: "))
    cliente1.abreConta(conta, saldo)

    # printa contas atuais
    print("\nContas atuais:")
    for conta in cliente1._contas:
        print(conta)

    while True:
        if count >= 1:
            question = input("\nDeseja fazer outra operação (s/n)? ")
        else:
            question = input("Deseja fazer alguma operação (s/n)? ")
        
        while question != 's' and question != 'n':
            print("Resposta inválida")
            question = input("Deseja fazer alguma operação (s/n)? ")

        if question == 's':
            count += 1
            operacao = input("Digite a operação (deposito ou saque): ")
            if operacao == 'deposito':
                value = input("Digite o valor do depósito: ")
                cliente1._contas[0].depositar(float(value))
                print("Depósito realizado com sucesso!")
                if conta == 'poupanca':
                    cliente1._contas[0].calculaJuros()
                else:
                    pass
                print(f"Novo saldo: R$ {cliente1._contas[0]._saldo}")
            elif operacao == 'saque':
                print(f"Saldo atual: R$ {cliente1._contas[0]._saldo}")
                value = input("Digite o valor do saque: ")
                cliente1._contas[0].sacar(float(value))
                print("Saque realizado com sucesso!")
                print(f"Novo saldo: R$ {cliente1._contas[0]._saldo}")
            else:
                while operacao != 'deposito' and operacao != 'saque':
                    print("Operação inválida")
                    operacao = input("Digite a operação (deposito ou saque): ")
        else:
            break


    print("\nFim das operações!")
    querExtrato = input("Deseja ver o extrato da conta (s/n)? ")
    if querExtrato == 's':
        cliente1._contas[0].extrato()
    else:
        print("Obrigado! Volte sempre!")


##############################################        
    newCount = 0
    querNovaConta = input("\nAgora que você já realizou suas operações, deseja abrir uma nova conta?")
    while True:
        if querNovaConta == 's':
            newCount += 1
            conta = input("Digite o tipo de conta (corrente ou poupanca): ")
            saldo = float(input("Digite o saldo inicial da conta: "))
            cliente1.abreConta(conta, saldo)

            # printa contas atuais
            print("\nContas atuais:")
            for conta in cliente1._contas:
                print(conta)
            
            
            # querNovaConta = input("Deseja abrir uma nova conta (s/n)? ")
        elif querNovaConta == 'n':
            print("Obrigado! Volte sempre!")
            break
        while querNovaConta != 's' and querNovaConta != 'n':
            print("Resposta inválida")
            querNovaConta = input("Deseja abrir uma nova conta (s/n)? ")
        
        novaConta = input("Digite o tipo de conta (corrente ou poupanca): ")
        saldo = float(input("Digite o saldo inicial da conta: "))
        while saldo < 0:
            print("Saldo inválido")
            saldo = float(input("Digite o saldo inicial da conta: "))
        cliente1.abreConta(conta, saldo)


        while True:
            if newCount >= 1:
                question = input("\nDeseja fazer outra operação (s/n)? ")
            else:
                question = input("Deseja fazer alguma operação (s/n)? ")
            
            while question != 's' and question != 'n':
                print("Resposta inválida")
                question = input("Deseja fazer alguma operação (s/n)? ")

            if question == 's':
                count += 1
                print("\nContas atuais:")
                for conta in cliente1._contas:
                    print(conta)
                
            # especificar em qual conta vai fazer a operação    
            numConta = input("Em qual conta você deseja realizar a operação? (Digite o número da conta):")

            # Procurar a conta com o número especificado
            conta_especifica = None
            for conta in cliente1._contas:
                if str(conta.numeroConta) == numConta:
                    conta_especifica = conta
                
            if conta_especifica is not None:
                operacao = input("Digite a operação (deposito ou saque): ")
                if operacao == 'deposito':
                    value = input("Digite o valor do depósito: ")
                    alue = input("Digite o valor do depósito: ")
                    cliente1._contas[0].depositar(float(value))
                    print("Depósito realizado com sucesso!")
                    if conta == 'poupanca':
                        cliente1._contas[0].calculaJuros()
                    else:
                        pass
                    print(f"Novo saldo: R$ {cliente1._contas[0]._saldo}")
                elif operacao == 'saque':
                    print(f"Saldo atual: R$ {conta_especifica._saldo}")
                    value = input("Digite o valor do saque: ")
                    conta_especifica.sacar(float(value))
                    print("Saque realizado com sucesso!")
                    print(f"Novo saldo: R$ {conta_especifica._saldo}")
                else:
                    print("Operação inválida")
                    while operacao != 'deposito' and operacao != 'saque':
                        operacao = input("Digite a operação (deposito ou saque): ")
            else:
                while conta_especifica is None:
                    print("Conta não encontrada. Verifique o número da conta digitado.")
                    numConta = input("Em qual conta você deseja realizar a operação? (Digite o número da conta):")

                
                
                
                

