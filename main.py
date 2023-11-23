import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os.path
import pickle
import nota as nt


class ViewPrincipal:
    def __init__(self, root, controller):
        self.root = root
        self.root.title("App Açougue")
        self.controller = controller
        self.frame_height = 400
        self.frame_width = 400
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        coordenada_x = int((self.screen_width/2) - (self.frame_height/2))
        coordenada_y = int((self.screen_height/2) - (self.frame_width/2))
        self.root.geometry("{}x{}+{}+{}".format(self.frame_width, self.frame_height, coordenada_x, coordenada_y))

        self.menu_bar = tk.Menu(self.root)
        self.menu_produto = tk.Menu(self.menu_bar)
        self.menu_nota = tk.Menu(self.menu_bar)
        self.menu_cliente = tk.Menu(self.menu_bar)


        self.menu_bar.add_cascade(label="Cliente", menu=self.menu_cliente)
        self.menu_bar.add_cascade(label="Produto", menu=self.menu_produto)
        self.menu_bar.add_cascade(label="Nota Fiscal", menu=self.menu_nota)
        self.menu_bar.add_command(label="Sair", command= lambda: self.controller.fechar_janela(self.root))


        self.menu_produto.add_command(label="Cadastrar Produto")
        self.menu_produto.add_command(label="Consultar Produto")
        self.menu_produto.add_command(label="Alterar Produto")
        self.menu_produto.add_command(label="Excluir Produto")
        self.menu_produto.add_command(label="Ir para o carrinho")

        self.menu_cliente.add_command(label="Cadastrar Cliente")
        self.menu_cliente.add_command(label="Consultar Cliente")



        self.menu_nota.add_command(label="Consultar Nota Fiscal")
        self.menu_nota.add_command(label="Consultar Vendas por Cliente")
        self.menu_nota.add_command(label="Consultar Produtos mais vendidos")
        self.menu_nota.add_command(label="Consultar Faturamento por Produto")
        self.menu_nota.add_command(label="Consultar Faturamento por Cliente")
        self.menu_nota.add_command(label="Consultar Faturamento por Data")
        self.menu_nota.add_command(label="Consultar Faturamento por Período")

        
        self.root.config(menu=self.menu_bar)

        self.root.mainloop()

class ControlePrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.main_view = ViewPrincipal(self.root, self)



    def fechar_janela(self, janela):
        janela.destroy()


if __name__ == "__main__":
    main  = ControlePrincipal()
    