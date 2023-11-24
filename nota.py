import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os.path
import pickle

class NotaFiscal:
    def __init__(self, numero:int, data: str, cpf_cliente: str, produtos: list):
        self.__numero = numero
        self.__data = data
        self.__cpf_cliente = cpf_cliente
        self.__produtos = produtos

    
    @property
    def numero(self):
        return self.__numero

    @property
    def data(self):
        return self.__data
    
    @property
    def cpf_cliente(self):
        return self.__cpf_cliente
    
    @property
    def produtos(self):
        return self.__produtos
    

class ControleNota:
    def __init__(self, controle_principal = None):
        self.__controle_principal = controle_principal
        self.__lista_de_notas_fiscais = []

    def lista_de_notas_fiscais_geradas(self):
        return self.__lista_de_notas_fiscais
    
    def criar_janela_consultar_nota(self, event):
        self.__limite_consultar_nota = LimiteConsultarNota(self)

    def consultar_nota_handler(self, event):
        cpf = self.__limite_consultar_nota.input_cpf.get()
        clientes = self.__controle_principal.controle_cliente.lista_de_clientes_cadastrados()
        for cliente in clientes:
            if cliente.cpf == cpf:
                notas = cliente.lista_de_notas
                for nota in notas:
                    if nota.cpf_cliente == cpf:
                        messagebox.showinfo("Nota Fiscal", "Número da Nota: " + str(nota.numero) + "\nData: " + nota.data + "\nCPF do Cliente: " + nota.cpf_cliente)
                        break
                break
        messagebox.showinfo("Nota Fiscal", "Não há notas fiscais para este cliente")
    def fechar_janela(self, janela):
        janela.destroy()
    
    
class LimiteConsultarNota(tk.Toplevel):
    def __init__(self, controle):
        self.controle = controle
        tk.Toplevel.__init__(self)
        self.title("Consultar Nota Fiscal")
        self.geometry('300x100')
        self.frame_nota = tk.Frame(self)
        self.label_nota = tk.Label(self.frame_nota, text="Digite o número do CPF: ")
        self.label_nota.pack(side="left")
        self.input_cpf = tk.Entry(self.frame_nota, width=20)
        self.input_cpf.pack(side="left")
        self.frame_nota.pack()
        self.botao_consultar = tk.Button(self, text="Consultar")
        self.botao_consultar.pack()
        self.botao_consultar.bind("<Button>", controle.consultar_nota_handler)


    
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


        self.bt1 = tk.Button(self.raiz, text="Consultar Nota Fiscal")
        self.bt1.pack()
        self.bt1.bind("<Button>", controle.criar_janela_consultar_nota)
        
        self.bt2 = tk.Button(self.raiz, text="Consultar Vendas por Cliente")
        self.bt2.pack()
        # self.btn.bind("<Button>", controle.enterHandler)

        self.bt3 = tk.Button(self.raiz, text="Consultar Produtos mais vendidos")
        self.bt3.pack()
        # self.btn.bind("<Button>", controle.enterHandler)

        self.bt4= tk.Button(self.raiz, text="Consultar Faturamento por Produto")
        self.bt4.pack()
        # self.btn.bind("<Button>", controle.enterHandler)

        self.bt5 = tk.Button(self.raiz, text="Consultar Faturamento por Cliente")
        self.bt5.pack()
        # self.btn.bind("<Button>", controle.enterHandler)

        self.bt6 = tk.Button(self.raiz, text="Consultar Faturamento por Data")
        self.bt6.pack()
        # self.btn.bind("<Button>", controle.enterHandler)

        self.bt7 = tk.Button(self.raiz, text="Consultar Faturamento por Período")
        self.bt7.pack()
        # self.btn.bind("<Button>", controle.enterHandler)



        self.fechar_button = tk.Button(self.raiz, text="Fechar", command= lambda: self.controller.fechar_janela(self.raiz))
        self.fechar_button.pack()




        self.raiz.mainloop()

    

        
    

if __name__ == "__main__":
    nota_controle = ControleNota()
    janela_aux = JanelaAuxiliar(nota_controle)
