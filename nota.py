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
    def __init__(self):
        self.__lista_de_notas_fiscais = []

    

    def fechar_janela(self, janela):
        janela.destroy()
    

class JanelaAuxiliar:
    def __init__(self, controller):
        self.raiz = tk.Tk()
        self.raiz.title("janela Auxiliar")
        self.controller = controller
        self.frame_height = 400
        self.frame_width = 400
        self.screen_width = self.raiz.winfo_screenwidth()
        self.screen_height = self.raiz.winfo_screenheight()
        coordenada_x = int((self.screen_width/2) - (self.frame_height/2))
        coordenada_y = int((self.screen_height/2) - (self.frame_width/2))
        self.raiz.geometry("{}x{}+{}+{}".format(self.frame_width, self.frame_height, coordenada_x, coordenada_y)) # configura a janela para abrir no centro da tela


        self.bt1 = tk.Button(self.raiz, text="Consultar Nota Fiscal")
        self.bt1.pack()
        # self.btn.bind("<Button>", controle.enterHandler)
        
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
