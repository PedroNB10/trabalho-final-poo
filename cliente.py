import tkinter as tk
from tkinter import messagebox
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
    


class ControleCliente:
    def __init__(self):
        self.clientes_cadastrados = []


        if os.path.isfile("clientes.pickle"):
           with open("clientes.pickle", "rb") as f:
                self.clientes_cadastrados = pickle.load(f)
        else:
            cliente_01 = Cliente("João", "joao@gmail.com",'1234120558')
            cliente_02 = Cliente("Maria", "maria@gmail.com", "1234120558")
            cliente_03 = Cliente("José", "jose@gmail.com", "1234120558")
            self.clientes_cadastrados.append(cliente_01)
            self.clientes_cadastrados.append(cliente_02)
            self.clientes_cadastrados.append(cliente_03)


            


    def salvar_clientes_cadastrados(self):
        with open("clientes.pickle", "wb") as f:

            pickle.dump(self.clientes_cadastrados, f)

    def mostrar_instancias(self):
        os.system("cls")
        print("Clientes Cadastrados: ")
        for cliente in self.clientes_cadastrados:
            print(cliente.nome)
            print(cliente.email)
            print(cliente.cpf)
            print("")

    def fechar_janela(self, janela):
        self.salvar_clientes_cadastrados()
        janela.destroy()


class ViewAuxiliar:
    def __init__(self, controller):
        self.root = tk.Tk()
        self.root.title("View Auxiliar")
        self.controller = controller
        self.frame_height = 400
        self.frame_width = 400
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        coordenada_x = int((self.screen_width/2) - (self.frame_height/2))
        coordenada_y = int((self.screen_height/2) - (self.frame_width/2))
        self.root.geometry("{}x{}+{}+{}".format(self.frame_width, self.frame_height, coordenada_x, coordenada_y)) # configura a janela para abrir no centro da tela

        self.cadastrar_button = tk.Button(self.root, text="Cadastrar Cliente", command="")
        self.cadastrar_button.pack()
        # self.btn.bind("<Button>", controle.enterHandler)

        self.consultar_button = tk.Button(self.root, text="Consultar Cliente", command="")
        self.consultar_button.pack()
        # self.btn.bind("<Button>", controle.enterHandler)

        self.mostar_button = tk.Button(self.root, text="Mostrar Instâncias", command=self.controller.mostrar_instancias)
        self.mostar_button.pack()

        self.fechar_button = tk.Button(self.root, text="Fechar", command= lambda: self.controller.fechar_janela(self.root))
        self.fechar_button.pack()



        self.root.mainloop()

        


if __name__ == "__main__":
    

    cliente_controle = ControleCliente()
    view_aux = ViewAuxiliar(cliente_controle)


