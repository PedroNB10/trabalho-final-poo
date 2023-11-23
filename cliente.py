import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import os.path
import pickle

class Cliente:
    def __init__(self, nome: str, email: str, cpf: str):
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf 
        self.__lista_de_notas = [] # armazena as instâncias de NotaFiscal

    @property
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def lista_de_notas(self):
        return self.__lista_de_notas
    

class LimiteCadastraCliente(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Cadastra Cliente")
        self.controle = controle

        self.frame_nome = tk.Frame(self)
        self.frame_email = tk.Frame(self)
        self.frame_cpf = tk.Frame(self)
        self.frame_button = tk.Frame(self)
        self.frame_nome.pack()
        self.frame_email.pack()
        self.frame_cpf.pack()
        self.frame_button.pack()
      
        self.label_nome = tk.Label(self.frame_nome,text="Nome: ")
        self.label_email = tk.Label(self.frame_email,text="Email: ")
        self.label_cpf = tk.Label(self.frame_cpf,text="Cpf: ")
        self.label_nome.pack(side="left")
        self.label_email.pack(side="left")
        self.label_cpf.pack(side="left")

        self.input_nome = tk.Entry(self.frame_nome, width=20)
        self.input_email = tk.Entry(self.frame_email, width=20)
        self.input_cpf = tk.Entry(self.frame_cpf, width=20)
        self.input_nome.pack(side="left")
        self.input_email.pack(side="left")
        self.input_cpf.pack(side="left")
      
        self.button_submit = tk.Button(self.frame_button ,text="Enter")      
        self.button_submit.pack(side="left")
        self.button_submit.bind("<Button>", controle.enter_handler)
      
        self.button_clear = tk.Button(self.frame_button ,text="Clear")      
        self.button_clear.pack(side="left")
        self.button_clear.bind("<Button>", controle.clear_handler)  

        self.fechar_button = tk.Button(self.frame_button, text="Fechar", command= lambda: self.controle.fechar_janela(self))
        self.fechar_button.pack()

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaCliente():
    def __init__(self):
        pass
        
    def consulta(self):
        answer = simpledialog.askstring("Consultar Cliente", "Qual o cpf do cliente buscado?")
        return answer
    
    def mostra(self, nome, str):
        messagebox.showinfo(nome, str)

class ControleCliente:
    def __init__(self, controle_principal = None):
        self.__controle_principal = controle_principal
        self.__clientes_cadastrados = []


        if os.path.isfile("clientes.pickle"):
           with open("clientes.pickle", "rb") as f:
                self.__clientes_cadastrados = pickle.load(f)
        else:
            cliente_01 = Cliente("João", "joao@gmail.com",'1234120558')
            cliente_02 = Cliente("Maria", "maria@gmail.com", "1234120558")
            cliente_03 = Cliente("José", "jose@gmail.com", "1234120558")
            self.__clientes_cadastrados.append(cliente_01)
            self.__clientes_cadastrados.append(cliente_02)
            self.__clientes_cadastrados.append(cliente_03)


    def lista_de_clientes_cadastrados(self):
        return self.__clientes_cadastrados


    def salvar_clientes_cadastrados(self):
        with open("clientes.pickle", "wb") as f:

            pickle.dump(self.__clientes_cadastrados, f)

    def cadastrar_cliente_handler(self, event):
        self.limiteCad = LimiteCadastraCliente(self)

    def consultar_cliente_handler(self, event):
        self.limite_consulta = LimiteConsultaCliente()
        str = ''
        cliente_buscado = self.limite_consulta.consulta()
        for cliente in self.__clientes_cadastrados:
            if cliente_buscado == cliente.cpf:
                str += 'Nome: ' + cliente.nome + '\n'
                str += 'Email: ' + cliente.email + '\n'
                str += 'Cpf: ' + cliente.cpf + '\n'
                self.limite_consulta.mostra('Encontrado', str)
        if str == '':
            self.limite_consulta.mostra('Nao encontrado', 'Cliente nao foi encontrado!')

    def mostrar_instancias(self):
        os.system("cls")
        print("Clientes Cadastrados: ")
        for cliente in self.__clientes_cadastrados:
            print(cliente.nome)
            print(cliente.email)
            print(cliente.cpf)
            print("")

    def enter_handler(self, event):
        nome = self.limiteCad.input_nome.get()
        email = self.limiteCad.input_email.get()
        cpf = self.limiteCad.input_cpf.get()
        cliente = Cliente(nome, email, cpf)
        self.__clientes_cadastrados.append(cliente)
        self.limiteCad.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
        self.clear_handler(event)

    def clear_handler(self, event):
        self.limiteCad.input_nome.delete(0, len(self.limiteCad.input_nome.get()))
        self.limiteCad.input_email.delete(0, len(self.limiteCad.input_email.get()))
        self.limiteCad.input_cpf.delete(0, len(self.limiteCad.input_cpf.get()))

    def fechar_janela(self, janela):
        self.salvar_clientes_cadastrados()
        janela.destroy()


class JanelaAuxiliar:
    def __init__(self, controle):
        self.raiz = tk.Tk()
        self.raiz.title("janela Auxiliar")
        self.controle = controle
        self.frame_height = 400
        self.frame_width = 400
        self.screen_width = self.raiz.winfo_screenwidth()
        self.screen_height = self.raiz.winfo_screenheight()
        coordenada_x = int((self.screen_width/2) - (self.frame_height/2))
        coordenada_y = int((self.screen_height/2) - (self.frame_width/2))
        self.raiz.geometry("{}x{}+{}+{}".format(self.frame_width, self.frame_height, coordenada_x, coordenada_y)) # configura a janela para abrir no centro da tela

        self.cadastrar_button = tk.Button(self.raiz, text="Cadastrar Cliente", command="")
        self.cadastrar_button.pack()
        self.cadastrar_button.bind("<Button>", controle.cadastrar_cliente_handler)

        self.consultar_button = tk.Button(self.raiz, text="Consultar Cliente", command="")
        self.consultar_button.pack()
        self.consultar_button.bind("<Button>", controle.consultar_cliente_handler)

        self.mostar_button = tk.Button(self.raiz, text="Mostrar Instâncias", command=self.controle.mostrar_instancias)
        self.mostar_button.pack()

        self.fechar_button = tk.Button(self.raiz, text="Fechar", command= lambda: self.controle.fechar_janela(self.raiz))
        self.fechar_button.pack()



        self.raiz.mainloop()

        


if __name__ == "__main__":
    

    cliente_controle = ControleCliente()
    janela_aux = JanelaAuxiliar(cliente_controle)


