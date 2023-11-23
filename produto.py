import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os.path
import pickle

class Produto:
    def __init__(self, codigo: int, descricao: str, preco_por_kg: float):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco_por_kg = preco_por_kg

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def preco_por_kg(self):
        return self.__preco_por_kg
    




class ControleProduto:
    def __init__(self):
        self.__lista_de_produtos_cadastrados = []

        if os.path.isfile("produtos.pickle"):
            with open("produtos.pickle", "rb") as f:
                self.__lista_de_produtos_cadastrados = pickle.load(f)

        else:
            produto_01 = Produto(1, "Picanha", 50.00)
            produto_02 = Produto(2, "Contra Filé", 40.00)
            produto_03 = Produto(3, "Alcatra", 45.00)
            self.__lista_de_produtos_cadastrados.append(produto_01)
            self.__lista_de_produtos_cadastrados.append(produto_02)
            self.__lista_de_produtos_cadastrados.append(produto_03)

    def fechar_janela(self, janela):
        self.salvar_produtos_cadastrados()
        janela.destroy()

    @property
    def lista_de_produtos_cadastrados(self):
        return self.__lista_de_produtos_cadastrados
    
    def salvar_produtos_cadastrados(self):
        with open("produtos.pickle", "wb") as f:
            pickle.dump(self.__lista_de_produtos_cadastrados, f)

    def mostrar_instancias(self):
        os.system("cls")
        print("Produtos Cadastrados: ")
        for produto in self.__lista_de_produtos_cadastrados:
            print(produto.codigo)
            print(produto.descricao)
            print(produto.preco_por_kg)
            print("")
    

class JanelaAuxiliar:
    def __init__(self, controller):
        self.root = tk.Tk()
        self.root.title("janela Auxiliar")
        self.controller = controller
        self.frame_height = 400
        self.frame_width = 400
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        coordenada_x = int((self.screen_width/2) - (self.frame_height/2))
        coordenada_y = int((self.screen_height/2) - (self.frame_width/2))
        self.root.geometry("{}x{}+{}+{}".format(self.frame_width, self.frame_height, coordenada_x, coordenada_y)) # configura a janela para abrir no centro da tela

        self.bt1 = tk.Button(self.root, text="Cadastrar Produto", command="")
        self.bt1.pack()
        # self.btn.bind("<Button>", controle.enterHandler)
        
        self.bt2 = tk.Button(self.root, text="Consultar Produto", command="")
        self.bt2.pack()
        # self.btn.bind("<Button>", controle.enterHandler)

        self.bt3 = tk.Button(self.root, text="Alterar Produto", command="")
        self.bt3.pack()
        # self.btn.bind("<Button>", controle.enterHandler)

        self.bt4= tk.Button(self.root, text="Excluir Produto", command="")
        self.bt4.pack()
        # self.btn.bind("<Button>", controle.enterHandler)

        self.bt5 = tk.Button(self.root, text="Ir para o carrinho", command="")
        self.bt5.pack()
        # self.btn.bind("<Button>", controle.enterHandler)

        self.bt6 = tk.Button(self.root, text="Mostrar Instâncias", command=self.controller.mostrar_instancias)
        self.bt6.pack()



        self.fechar_button = tk.Button(self.root, text="Fechar", command= lambda: self.controller.fechar_janela(self.root))
        self.fechar_button.pack()



        self.root.mainloop()

        
    def fechar_janela(self, janela):

        janela.destroy()

    

if __name__ == "__main__":
    produto_controle = ControleProduto()
    janela_auxiliar = JanelaAuxiliar(produto_controle)