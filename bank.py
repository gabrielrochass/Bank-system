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
        return f'Nome: {self.name}, CPF: {self.cpf}'
    

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
        self._taxaJuros = 0.02 # taxa de juros de 2%
    
    def __str__(self):
        return f'Conta Poupança de número: {self.numeroConta} possui saldo de R$ {self._saldo}'
    
    def juros(self):
        self._saldo *= self._taxaJuros
        self._registraTransacao(f"Saldo total (Salado iniial + rendimentos): R$ {self._saldo * self._taxaJuros}")

    
# main
if __name__ == '__main__':
    name = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    cliente1 = Cliente(name, cpf)
    print(cliente1)

    conta = input("Digite o tipo de conta (corrente ou poupanca): ")
    saldo = float(input("Digite o saldo inicial da conta: "))
    cliente1.abreConta(conta, saldo)
    print(cliente1._contas[0]) # acessa a primeira conta do cliente

    while True:
        question = input("Deseja fazer alguma operação (s/n)? ")
        if question == 's':
            operacao = input("Digite a operação (deposito ou saque): ")
            if operacao == 'deposito':
                value = input("Digite o valor do depósito: ")
                cliente1._contas[0].depositar(float(value))
                print(f"Novo saldo: R$ {cliente1._contas[0]._saldo}")
            elif operacao == 'saque':
                print(ContaPoupanca.juros())
                value = input("Digite o valor do saque: ")

                cliente1._contas[0].sacar(float(value))
            else:
                print("Operação inválida")
        else:
            break


    print("\nFim das operações\n")
    querExtrato = input("Deseja ver o extrato da conta (s/n)? ")
    if querExtrato == 's':
        cliente1._contas[0].extrato()
    else:
        print("Obrigado! Volte sempre!")
