import tkinter as tk

class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Bank System')
        self.config(bg='black')
        self.geometry('600x400')

        # cria um frame para info
        self.labelName = tk.Label(self, text='Nome: ', bg='black', fg='white')
        self.entryName = tk.Entry(self)

        self.labelCpf = tk.Label(self, text='CPF: ', bg='black', fg='white')
        self.entryCpf = tk.Entry(self)

        self.buttonAbreConta = tk.Button(self, text='Abrir Conta', bg='gray', fg='black', command=self.abrirConta)

        # posiciona os widgets
        self.labelName.pack()
        self.entryName.pack()
        self.labelCpf.pack()
        self.entryCpf.pack()
        self.buttonAbreConta.pack()

    def abrirConta(self):
        # obtém os valores dos campos
        nome = self.entryName.get()
        cpf = self.entryCpf.get()
        print(f'Nome: {nome}\nCPF: {cpf}')

        # cria novos labels
        labelInfo = tk.Label(self, text=f'Nome: {nome}\nCPF: {cpf}', bg='black', fg='white')
        labelInfo.pack()

        # remove o botão de abrir conta
        self.buttonAbreConta.pack_forget()

        # cria botões para criar conta corrente e poupança
        self.buttonContaCorrente = tk.Button(self, text='Conta Corrente', bg='gray', fg='black', command=self.criaContaCorrente)
        self.buttonContaPoupanca = tk.Button(self, text='Conta Poupança', bg='gray', fg='black', command=self.criaContaPoupanca)

        # posiciona os botões
        self.buttonContaCorrente.pack()
        self.buttonContaPoupanca.pack()

    def criaContaCorrente(self):
        self.buttonContaCorrente.pack_forget()
        self.buttonContaPoupanca.pack_forget()
        labelInfo = tk.Label(self, text=f'Conta Corrente criada', bg='black', fg='white')
        labelInfo.pack()

    def criaContaPoupanca(self):
        self.buttonContaCorrente.pack_forget()
        self.buttonContaPoupanca.pack_forget()
        labelInfo = tk.Label(self, text=f'Conta Poupança criada', bg='black', fg='white')
        labelInfo.pack()

if __name__ == '__main__':
    # cria uma instância da classe Interface
    app = Interface()
    # inicia o loop de eventos
    app.mainloop()
