import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os.path
import pickle
import nota as nt
import produto as pd
import cliente as cl





class janelaPrincipal:
    def __init__(self, raiz, controller):
        self.raiz = raiz
        self.raiz.title("App Açougue")
        self.controller = controller
        self.frame_height = 400
        self.frame_width = 400
        self.screen_width = self.raiz.winfo_screenwidth()
        self.screen_height = self.raiz.winfo_screenheight()
        coordenada_x = int((self.screen_width/2) - (self.frame_width/2))
        coordenada_y = int((self.screen_height/2) - (self.frame_height/2))
        self.raiz.geometry("{}x{}+{}+{}".format(self.frame_width, self.frame_height, coordenada_x, coordenada_y))

        self.barra_menu = tk.Menu(self.raiz)
        self.menu_produto = tk.Menu(self.barra_menu)
        self.menu_nota = tk.Menu(self.barra_menu)
        self.menu_cliente = tk.Menu(self.barra_menu)


        self.barra_menu.add_cascade(label="Cliente", menu=self.menu_cliente)
        self.barra_menu.add_cascade(label="Produto", menu=self.menu_produto)
        self.barra_menu.add_cascade(label="Nota Fiscal", menu=self.menu_nota)
        self.barra_menu.add_command(label="Sair", command= lambda: self.controller.fechar_janela(self.raiz))


        self.menu_produto.add_command(label="Cadastrar Produto")
        self.menu_produto.add_command(label="Consultar Produto")
        self.menu_produto.add_command(label="Alterar Produto")
        self.menu_produto.add_command(label="Excluir Produto")
        self.menu_produto.add_command(label="Ir para o carrinho")

        self.menu_cliente.add_command(label="Cadastrar Cliente", command=self.controller.cadastrar_cliente)
        self.menu_cliente.add_command(label="Consultar Cliente", command=self.controller.consultar_cliente)



        self.menu_nota.add_command(label="Consultar Nota Fiscal", command=self.controller.consultar_nota)
        self.menu_nota.add_command(label="Consultar Vendas por Cliente")
        self.menu_nota.add_command(label="Consultar Produtos mais vendidos")
        self.menu_nota.add_command(label="Consultar Faturamento por Produto")
        self.menu_nota.add_command(label="Consultar Faturamento por Cliente")
        self.menu_nota.add_command(label="Consultar Faturamento por Data")
        self.menu_nota.add_command(label="Consultar Faturamento por Período")

        
        self.raiz.config(menu=self.barra_menu)

        self.raiz.mainloop()

class ControlePrincipal:
    def __init__(self):
        self.raiz = tk.Tk()
        self.controle_cliente = cl.ControleCliente(self)
        self.controle_produto = pd.ControleProduto(self)
        self.controle_nota = nt.ControleNota(self)
        self.main_janela = janelaPrincipal(self.raiz, self)
        
    def fechar_janela(self, janela):
        janela.destroy()
        self.salvar_dados()
        print(self.controle_cliente.lista_de_clientes_cadastrados)
        print(self.controle_produto.lista_de_produtos_cadastrados)
    
    def salvar_dados(self):
        self.controle_cliente.salvar_clientes_cadastrados() 
        self.controle_produto.salvar_produtos_cadastrados()
        # self.controle_nota.salvar_notas_fiscais()

        pass
        
    def cadastrar_cliente(self):
        self.controle_cliente.cadastrar_cliente_handler()

    def consultar_cliente(self):
        self.controle_cliente.consultar_cliente_handler()

    def cadastrar_produto(self):
        pass
    def consultar_produto(self):
        pass
    def alterar_produto(self):
        pass
    def excluir_produto(self):
        pass
    def ir_para_carrinho(self):
        pass
    def consultar_nota(self):
        self.controle_nota.criar_janela_consultar_nota()
        pass
    def consultar_vendas_por_cliente(self):
        pass
    def consultar_produtos_mais_vendidos(self):
        pass
    def consultar_faturamento_por_produto(self):
        pass
    def consultar_faturamento_por_cliente(self):
        pass
    def consultar_faturamento_por_data(self):
        pass
    def consultar_faturamento_por_periodo(self):
        pass

        


if __name__ == "__main__":
    main = ControlePrincipal()

    