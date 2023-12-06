import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import os.path
import pickle

class Cliente:
    def __init__(self, nome: str, email: str, cpf: str):
        self.__nome = nome
        self.email = email
        self.cpf = cpf 
        self.__lista_de_notas = [] # armazena as instâncias de NotaFiscal

    @property
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        if '@' not in email:
            raise ValueError("Email inválido!")
        self.__email = email
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        try:
            int(cpf)
            
        except ValueError:
            raise ValueError("Cpf inválido!")
        
        if len(cpf) != 11:
            raise ValueError("Cpf inválido!")
        self.__cpf = str(cpf)
    
    @property
    def lista_de_notas(self):
        return self.__lista_de_notas
    
    def adicionar_nota_a_cliente(self, nota):
        self.__lista_de_notas.append(nota)
    

class LimiteCadastraCliente(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)

        self.frame_height = 100
        self.frame_width = 250
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        coordenada_x = int((self.screen_width/2) - (self.frame_width/2))
        coordenada_y = int((self.screen_height/2) - (self.frame_height/2))
        self.geometry("{}x{}+{}+{}".format(self.frame_width, self.frame_height, coordenada_x, coordenada_y))
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
      
        self.button_submit = tk.Button(self.frame_button ,text="Enter", command=self.controle.enter_handler)      
        self.button_submit.pack(side="left")

      
        self.button_clear = tk.Button(self.frame_button ,text="Clear", command=self.controle.clear_handler)      
        self.button_clear.pack(side="left")


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
    def __init__(self, controle_principal):
        self.controle_principal = controle_principal

        if not os.path.isfile("clientes.pickle"):
            self.clientes_cadastrados = []
            cliente_01 = Cliente("João", "joao@gmail.com",'50639457112')
            cliente_02 = Cliente("Maria", "maria@gmail.com",'12345678901')
            cliente_03 = Cliente("Pedro", "pedro@gmail.com",'98765432109')
            cliente_04 = Cliente("Ana", "ana@gmail.com",'45678912345')
            cliente_05 = Cliente("Lucas", "lucas@gmail.com",'78912345678')

            self.clientes_cadastrados.append(cliente_01)
            self.clientes_cadastrados.append(cliente_02)
            self.clientes_cadastrados.append(cliente_03)
            self.clientes_cadastrados.append(cliente_04)
            self.clientes_cadastrados.append(cliente_05)

        else:
            with open("clientes.pickle", "rb") as f:
                self.clientes_cadastrados = pickle.load(f)
                


    @property
    def lista_de_clientes_cadastrados(self):
        return self.clientes_cadastrados
    
    def getCliente(self, cpf):
        cliente = None
        for cliente in self.clientes_cadastrados:
            if cliente.cpf == cpf:
                return cliente
        return None
    
    def mostrar_clientes_cadastrados(self):

        str = ''
        for cliente in self.clientes_cadastrados:
            str += 'Nome: ' + cliente.nome + '\n'
            str += 'Email: ' + cliente.email + '\n'
            str += 'Cpf: ' + cliente.cpf + '\n'
            str += '------------------------\n'

        messagebox.showinfo('Clientes Cadastrados', str)

    def salvar_clientes_cadastrados(self):
        
        if len(self.clientes_cadastrados) != 0:    
            with open("clientes.pickle", "wb") as f:
                pickle.dump(self.clientes_cadastrados, f)

    def cadastrar_cliente_handler(self):
        self.limiteCad = LimiteCadastraCliente(self)

    def consultar_cliente_handler(self):
        self.limite_consulta = LimiteConsultaCliente()
        str = ''
        cliente_buscado = self.limite_consulta.consulta()
        if cliente_buscado == None:
            return
        
        for cliente in self.clientes_cadastrados:
            if cliente_buscado == cliente.cpf:
                str += 'Nome: ' + cliente.nome + '\n'
                str += 'Email: ' + cliente.email + '\n'
                str += 'Cpf: ' + cliente.cpf + '\n'
                self.limite_consulta.mostra('Encontrado', str)
        if str == '':
            self.limite_consulta.mostra('Não encontrado', 'Cliente não foi encontrado!')

    def mostrar_instancias(self):
        os.system("cls")

    def enter_handler(self):
        nome = self.limiteCad.input_nome.get()
        email = self.limiteCad.input_email.get()
        cpf = self.limiteCad.input_cpf.get()
        
        if nome == '' or email == '' or cpf == '':
            messagebox.showinfo('Erro', 'Preencha todos os campos!')
            self.limiteCad.lift()
            return
        
        
        try:
            cliente = Cliente(nome, email, cpf)

        except ValueError as error:
            messagebox.showinfo('Erro', error)
            self.limiteCad.lift()
            return
        
        
        self.clientes_cadastrados.append(cliente)
        self.limiteCad.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
        self.limiteCad.lift()
        self.clear_handler()

    def clear_handler(self):
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

        self.cadastrar_button = tk.Button(self.raiz, text="Cadastrar Cliente", command=controle.cadastrar_cliente_handler)
        self.cadastrar_button.pack()


        self.consultar_button = tk.Button(self.raiz, text="Consultar Cliente", command=controle.consultar_cliente_handler)
        self.consultar_button.pack()
    

        self.mostar_button = tk.Button(self.raiz, text="Mostrar Instâncias", command=self.controle.mostrar_instancias)
        self.mostar_button.pack()

        self.fechar_button = tk.Button(self.raiz, text="Fechar", command= lambda: self.controle.fechar_janela(self.raiz))
        self.fechar_button.pack()



        self.raiz.mainloop()

        


if __name__ == "__main__":
    

    cliente_controle = ControleCliente(None)
    janela_aux = JanelaAuxiliar(cliente_controle)


# 2023006500 Pedro Nogueira Barboza
# 2023003517 Pedro de Paula Gonçalves
# 2023001577 João Henrique Flauzino