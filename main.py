import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os.path
import pickle
import nota as nt
import produto as pd
import cliente as cl





class janelaPrincipal:
    def __init__(self, raiz, controle):
        self.raiz = raiz
        self.raiz.title("App Açougue")
        self.controle = controle
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
        self.barra_menu.add_command(label="Sair", command= lambda: self.controle.fechar_janela(self.raiz))


        self.menu_produto.add_command(label="Cadastrar Produto", command=self.controle.controle_produto.criar_tela_cadastro_produto)
        self.menu_produto.add_command(label="Consultar Produto", command=self.controle.controle_produto.consultar_produto_handler)
        self.menu_produto.add_command(label="Alterar Produto", command=self.controle.controle_produto.criar_alterar_produto_view)
        self.menu_produto.add_command(label="Excluir Produto", command=self.controle.controle_produto.excluir_produto_handler)
        self.menu_produto.add_command(label="Ir para o carrinho", command=self.controle.controle_produto.criar_tela_fechar_carrinho)
        self.menu_produto.add_command(label="Mostrar Produtos cadastrados (EXTRA)", command=self.controle.controle_produto.mostrar_produtos_cadastrados)

        self.menu_cliente.add_command(label="Cadastrar Cliente", command=self.controle.controle_cliente.cadastrar_cliente_handler)
        self.menu_cliente.add_command(label="Consultar Cliente", command=self.controle.controle_cliente.consultar_cliente_handler)
        self.menu_cliente.add_command(label="Mostrar Clientes cadastrados (EXTRA)", command=self.controle.controle_cliente.mostrar_clientes_cadastrados)



        self.menu_nota.add_command(label="Consultar Nota Fiscal", command=self.controle.controle_nota.criar_janela_consultar_nota)
        self.menu_nota.add_command(label="Consultar Produtos mais vendidos", command=self.controle.controle_nota.consultar_produtos_mais_vendidos)
        self.menu_nota.add_command(label="Consultar Faturamento por Produto", command=self.controle.controle_nota.consultar_faturamento_por_produto)
        self.menu_nota.add_command(label="Consultar Faturamento por Cliente", command=self.controle.controle_nota.consultar_faturamento_por_cliente)
        self.menu_nota.add_command(label="Consultar Faturamento por Cliente em um Período", command=self.controle.controle_nota.consultar_faturamento_por_cliente_por_periodo_handler)
        self.menu_nota.add_command(label="Consultar Faturamento por Período", command=self.controle.controle_nota.criar_janela_consultar_periodo)
        self.menu_nota.add_command(label="Mostrar Notas Fiscais cadastradas (EXTRA)", command=self.controle.controle_nota.mostrar_notas_fiscais)

        
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
        resposta = messagebox.askyesno("Confirmação", "Deseja salvar os novos dados antes de sair?")
        
        if resposta == True:
            self.salvar_dados()    
        janela.destroy()    

    
    def salvar_dados(self):
        self.controle_cliente.salvar_clientes_cadastrados() 
        self.controle_produto.salvar_produtos_cadastrados()
        self.controle_nota.salvar_notas_fiscais()
        
        
if __name__ == "__main__":
    main = ControlePrincipal()

# 2023006500 Pedro Nogueira Barboza
# 2023003517 Pedro de Paula Gonçalves
# 2023001577 João Henrique Flauzino