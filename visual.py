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

if __name__ == '__main__':
    # cria uma instância da classe Interface
    app = Interface()
    # inicia o loop de eventos
    app.mainloop()
