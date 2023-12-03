import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import os.path
import pickle

from datetime import datetime


class Produto:
    def __init__(self, codigo: int, descricao: str, preco_por_kg:float):
        self.codigo = codigo
        self.__descricao = descricao
        self.preco_por_kg = preco_por_kg 


    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        
        try:
            codigo = int(codigo)
            
        except ValueError:
            raise ValueError("Código deve ser um número inteiro!")
            
        self.__codigo = codigo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):         
            self.__descricao = descricao
    
    @property
    def preco_por_kg(self):
        return self.__preco_por_kg
    
    @preco_por_kg.setter
    def preco_por_kg(self, preco_por_kg):
        
        try:
            preco_por_kg = float(preco_por_kg)
            
        except ValueError:
            raise ValueError("Preço deve ser um número real!")
            
        self.__preco_por_kg = preco_por_kg
    
    
class ConjuntoProdutosCarrinho:
    def __init__(self, produto: Produto, quantidade: float):
        self.produto = produto
        self.quantidade = quantidade
        
    @property
    def produto(self):
        return self.__produto
    
    @produto.setter
    def produto(self, produto):
        self.__produto = produto
        
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        try:
            quantidade = float(quantidade)
        except ValueError:
            raise ValueError("Quantidade deve ser um número real!")
        self.__quantidade = quantidade
        
        
    def calcular_valor_total_do_conjunto(self):
        return self.quantidade * self.produto.preco_por_kg        

    
class JanelaSecondaria(tk.Toplevel):
    def __init__(self, controle):
        self.controle = controle
        tk.Toplevel.__init__(self)
        
        self.root_height = 300
        self.root_width = 300
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        x_cordinate = int((self.screen_width/2) - (self.root_width/2))
        y_cordinate = int((self.screen_height/2) - (self.root_height/2))
        self.title("Janela Secondária")   
        self.geometry("{}x{}+{}+{}".format(self.root_width, self.root_height, x_cordinate, y_cordinate))
        
        
        self.frame_01 = tk.Frame(self)
        self.frame_01.pack()

        self.label_01 = tk.Label(self.frame_01, text="Label 01")
        self.label_01.pack(side="left")

        self.entry_01 = tk.Entry(self.frame_01)
        self.entry_01.pack()

        self.button_01 = tk.Button(self, text="Cadastrar Instancias", command=self.controle.cadastrar_instancias) 
        self.button_01.pack(pady=20)
        
        self.button_02 = tk.Button(self, text="Mostrar Instancias", command=self.controle.mostrar_instancias)
        self.button_02.pack(pady=20)
        
        self.button_03 = tk.Button(self, text="Salvar Instancias", command=self.controle.salvar_instancias)
        self.button_03.pack(pady=20)
        
        self.button_fechar = tk.Button(self, text="Fechar", command=lambda:self.controle.fechar_janela(self))
        self.button_fechar.pack(pady=20)
        
        
class FecharCarrinhoView(tk.Toplevel):
    def __init__(self, controle):
        self.controle = controle
        tk.Toplevel.__init__(self)
        
        self.root_height = 300
        self.root_width = 300
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        x_cordinate = int((self.screen_width/2) - (self.root_width/2))
        y_cordinate = int((self.screen_height/2) - (self.root_height/2))
        self.title("Carrinho")   
        self.geometry("{}x{}+{}+{}".format(self.root_width, self.root_height, x_cordinate, y_cordinate))
        
        
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(pady=15)
        
        self.frame_01 = tk.Frame(self.main_frame)
        self.frame_01.pack()

        self.label_01 = tk.Label(self.frame_01, text="Código do produto:")
        self.label_01.pack(side="left")

        self.entry_codigo = tk.Entry(self.frame_01)
        self.entry_codigo.pack()
        
        self.frame_02 = tk.Frame(self.main_frame)
        self.frame_02.pack()
        
        self.label_02 = tk.Label(self.frame_02, text="Quantidade(em kg):")
        self.label_02.pack(side="left")
        
        self.entry_quantidade = tk.Entry(self.frame_02)
        self.entry_quantidade.pack()

        self.button_01 = tk.Button(self.main_frame, text="Adicionar Produto", command=self.controle.adicionar_produto_no_carrinho_handler)
        self.button_01.pack(pady=20)
        
        self.button_02 = tk.Button(self.main_frame, text="Emitir Nota", command=self.controle.emitir_nota_handler)
        self.button_02.pack(pady=20)
        
        self.button_fechar = tk.Button(self, text="Fechar", command=lambda:self.controle.fechar_janela(self))
        self.button_fechar.pack(pady=20)
        
        
class AlterarProdutoView(tk.Toplevel):
    def __init__(self, controle, codigo, descricao, preco):
        self.controle = controle
        
        self.controle = controle
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco
        
        tk.Toplevel.__init__(self)
        self.root_height = 300
        self.root_width = 300
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        x_cordinate = int((self.screen_width/2) - (self.root_width/2))
        y_cordinate = int((self.screen_height/2) - (self.root_height/2))
        self.title("Cadastro de Produtos")   
        self.geometry("{}x{}+{}+{}".format(self.root_width, self.root_height, x_cordinate, y_cordinate))
        
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(pady=15)
        
        self.frame_01 = tk.Frame(self.main_frame)
        self.frame_01.pack()
        self.label_01 = tk.Label(self.frame_01, text="Código: ")
        self.label_01.pack(side="left")
        
        self.entry_codigo = tk.Entry(self.frame_01)
        self.entry_codigo.delete(0, tk.END)
        self.entry_codigo.insert(0, self.codigo)
        self.entry_codigo.configure(state="readonly")
        self.entry_codigo.pack()
        
        
        self.frame_02 = tk.Frame(self.main_frame)
        self.frame_02.pack()
        self.label_02 = tk.Label(self.frame_02, text="Descrição: ")
        self.label_02.pack(side="left")
        
        self.entry_descricao = tk.Entry(self.frame_02)
        self.entry_descricao.pack()
        self.entry_descricao.delete(0, tk.END)
        self.entry_descricao.insert(0, self.descricao)
        
        self.frame_03 = tk.Frame(self.main_frame)
        self.frame_03.pack()
        
        self.label_03 = tk.Label(self.frame_03, text="Preço por quilo: ")
        self.label_03.pack(side="left")

        
        self.entry_preco = tk.Entry(self.frame_03, textvariable=self.preco)
        self.entry_preco.pack()
        self.entry_preco.delete(0, tk.END)
        self.entry_preco.insert(0, self.preco)
        
        self.button_01 = tk.Button(self.main_frame, text="Alterar Produto", command=self.controle.alterar_produto_handler)
        self.button_01.pack(pady=20)
        
        self.button_fechar = tk.Button(self, text="Fechar", command=lambda:self.controle.fechar_janela(self))
        self.button_fechar.pack(pady=20)
        
        
        
class CadastroProdutoView(tk.Toplevel):
    def __init__(self,controle):
        
        self.controle = controle
        
        tk.Toplevel.__init__(self)
        
        self.root_height = 300
        self.root_width = 300
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        x_cordinate = int((self.screen_width/2) - (self.root_width/2))
        y_cordinate = int((self.screen_height/2) - (self.root_height/2))
        self.title("Cadastro de Produtos")   
        self.geometry("{}x{}+{}+{}".format(self.root_width, self.root_height, x_cordinate, y_cordinate))
        
        
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(pady=15)
        self.frame_01 = tk.Frame(self.main_frame)
        self.frame_01.pack()
        self.label_01 = tk.Label(self.frame_01, text="Código:")
        self.label_01.pack(side="left")
        self.entry_codigo = tk.Entry(self.frame_01)
        self.entry_codigo.pack()
        
        self.frame_02 = tk.Frame(self.main_frame)
        self.frame_02.pack()
        self.label_02 = tk.Label(self.frame_02, text="Descrição:")
        self.label_02.pack(side="left")
        self.entry_decricao = tk.Entry(self.frame_02)
        self.entry_decricao.pack()
        
        
        self.frame_03 = tk.Frame(self.main_frame)
        self.frame_03.pack()
        self.label_03 = tk.Label(self.frame_03, text="Preço por quilo:")
        self.label_03.pack(side="left")
        self.entry_preco = tk.Entry(self.frame_03)
        self.entry_preco.pack()
        
    
        
        self.button_01 = tk.Button(self.main_frame, text="Cadastrar Produto", command=self.controle.cadastrar_produto_handler) 
        self.button_01.pack(pady=20)
    
        
        self.button_fechar = tk.Button(self, text="Fechar", command=lambda:self.controle.fechar_janela(self))
        self.button_fechar.pack(pady=20)


class ControleProduto:
    def __init__(self, controle_principal):
        self.controle_principal = controle_principal
        

        if not os.path.isfile("produtos.pickle"):
            self.lista_de_produtos_cadastrados = []
            produto_01 = Produto(1, "Picanha", 50.00)
            produto_02 = Produto(2, "Contra Filé", 40.00)
            produto_03 = Produto(3, "Alcatra", 45.00)
            produto_04 = Produto(4, "Coxão Mole", 35.00)
            produto_05 = Produto(5, "Coxão Duro", 30.00)
            produto_06 = Produto(6, "Patinho", 25.00)
            produto_07 = Produto(7, "Maminha", 55.00)
            produto_08 = Produto(8, "Acém", 20.00)
            produto_09 = Produto(9, "Fraldinha", 15.00)
            produto_10 = Produto(10, "Costela", 10.00)
            produto_11 = Produto(11, "Paleta", 5.00)
            produto_12 = Produto(12, "Peito", 60.00)
            
            self.lista_de_produtos_cadastrados.append(produto_01)
            self.lista_de_produtos_cadastrados.append(produto_02)
            self.lista_de_produtos_cadastrados.append(produto_03)
            self.lista_de_produtos_cadastrados.append(produto_04)
            self.lista_de_produtos_cadastrados.append(produto_05)
            self.lista_de_produtos_cadastrados.append(produto_06)
            self.lista_de_produtos_cadastrados.append(produto_07)
            self.lista_de_produtos_cadastrados.append(produto_08)
            self.lista_de_produtos_cadastrados.append(produto_09)
            self.lista_de_produtos_cadastrados.append(produto_10)
            self.lista_de_produtos_cadastrados.append(produto_11)
            self.lista_de_produtos_cadastrados.append(produto_12)
            

        else:
            with open("produtos.pickle", "rb") as f:
                self.lista_de_produtos_cadastrados = pickle.load(f)
                
                
    def getProduto(self, codigo):

        for produto in self.lista_de_produtos_cadastrados:
            if produto.codigo == codigo:
                print("ACHOU O PRODUTO")
                return produto
        print("NÃO ACHOU O PRODUTO")
        return None
    
    def criar_tela_fechar_carrinho(self):
        cpf = simpledialog.askstring("Cliente", "Qual o CPF do cliente?") 
        
        cliente = self.controle_principal.controle_cliente.getCliente(cpf)
        
        if cliente == None:
            messagebox.showerror("Erro", "Cliente não encontrado! faça seu cadastro na aba 'Cliente'")
            return
        
        self.cliente_atual = cliente
        self.lista_de_produtos_temp = []
        messagebox.showinfo("Sucesso, Cliente encontrado!", f"Seja bem vindo {cliente.nome}, agora coloque os produtos no carrinho!")
        self.fechar_carrinho_view = FecharCarrinhoView(self)
        
    def adicionar_produto_no_carrinho_handler(self):
        codigo = self.fechar_carrinho_view.entry_codigo.get()
        quantidade = self.fechar_carrinho_view.entry_quantidade.get()
        
        try:
            codigo = int(codigo)
            quantidade = float(quantidade)
        except ValueError:
            messagebox.showerror("Erro", "Código deve ser um número inteiro e quantidade deve ser um número real!")
            return
        
        produto = self.getProduto(codigo)
        
        if produto == None:
            messagebox.showerror("Erro", "Produto não encontrado!")
            return
        
        produtos = ConjuntoProdutosCarrinho(produto, quantidade)
        self.lista_de_produtos_temp.append(produtos)
        messagebox.showinfo("Sucesso", "Produto adicionado ao carrinho!")
        self.fechar_carrinho_view.lift()
        
        
    def emitir_nota_handler(self):
        lista_de_produtos = self.lista_de_produtos_temp 
        
        if len(lista_de_produtos) == 0:
            messagebox.showerror("Erro", "Carrinho vazio!")
            self.fechar_carrinho_view.lift()
            return
        numero =len(self.controle_principal.controle_nota.lista_de_notas_fiscais_geradas()) + 1
        cliente = self.cliente_atual
        cpf_cliente = cliente.cpf
        data_string = simpledialog.askstring("Data", "Qual a data da compra? (dia/mês/ano)")
        formato_data = "%d/%m/%Y"
        
        try:
            data_formatada = datetime.strptime(data_string, formato_data)
        except ValueError:
            messagebox.showerror("Erro", "Data inválida!")
            return
        
        self.controle_principal.controle_nota.criar_instancia_nota(numero, data_formatada, cpf_cliente, lista_de_produtos)
        messagebox.showinfo("Sucesso", "Nota emitida com sucesso!")
        self.fechar_carrinho_view.lift()
        self.controle_principal.controle_nota.mostrar_ultima_nota_fiscal()
       
  
        
        
        
            
            
    def mostrar_produtos_cadastrados(self):
        str = ''
        str += "Código - Descrição - Preço por quilo\n"
        for produto in self.lista_de_produtos_cadastrados:
            str += f"{produto.codigo} - {produto.descricao} - {produto.preco_por_kg}\n"
            
        messagebox.showinfo("Produtos Cadastrados", str)
        
    def consultar_produto_handler(self):
        produto_codigo = simpledialog.askinteger("Consultar Cliente", "Qual o código do produto buscado?")
        
        if produto_codigo == None:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        
        produto = self.getProduto(produto_codigo)
        
        if produto == None:
            messagebox.showerror("Erro", "Produto não encontrado!")
            return
        
        for produto in self.lista_de_produtos_cadastrados:
            if produto.codigo == produto_codigo:
                messagebox.showinfo("Sucesso", f"Produto encontrado:\nCódgio: {produto.codigo}\nDescrição: {produto.descricao}\nPreço / kg: {produto.preco_por_kg}")
                return
        
    def alterar_produto_handler(self):
        codigo = self.alterar_produto_view.entry_codigo.get()
        nova_descricao = self.alterar_produto_view.entry_descricao.get()
        novo_preco = self.alterar_produto_view.entry_preco.get()
        
        try:
            codigo = int(codigo)
        except ValueError:
            messagebox.showerror("Erro", "Código deve ser um número inteiro!")
            return
        
        
        produto = self.getProduto(codigo)
        
        if produto == None:
            messagebox.showerror("Erro", "Produto não encontrado!")
            return

        
        try:
            produto.descricao = nova_descricao
            produto.preco_por_kg = novo_preco 
            
        except ValueError as error:
            messagebox.showwarning("Alerta", str(error))
            self.alterar_produto_view.lift()
            return
        
        messagebox.showinfo("Sucesso", "Produto alterado com sucesso!")
        self.alterar_produto_view.lift()
        
    def excluir_produto_handler(self):
        produto_codigo = simpledialog.askinteger("Consultar Cliente", "Qual o código do produto que deseja excluir?")
        produto = self.getProduto(produto_codigo)
        
        
        respota = messagebox.askyesno("Confirmação", f"Deseja excluir o produto {produto.descricao}?")
        
        if respota == True:
            self.lista_de_produtos_cadastrados.remove(produto)
            
            messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
    

         
         
    def criar_alterar_produto_view(self):
        produto_codigo = simpledialog.askinteger("Consultar Cliente", "Qual o código do produto buscado?")
        produto = self.getProduto(produto_codigo)
        
        
        
        if produto == None:
            messagebox.showerror("Erro", "Produto não encontrado!")
            return
        
        print(produto.codigo)
        print(produto.descricao)
        print(produto.preco_por_kg)
        
        self.alterar_produto_view = AlterarProdutoView(self, produto.codigo, produto.descricao, produto.preco_por_kg)
        
        
    def cadastrar_produto_handler(self):
        
        try:
            codigo = self.cadastro_produto_view.entry_codigo.get()
            descricao = self.cadastro_produto_view.entry_decricao.get()
            preco_por_kg = self.cadastro_produto_view.entry_preco.get()
            produto = Produto(codigo, descricao, preco_por_kg)
            self.lista_de_produtos_cadastrados.append(produto)
            
            if codigo == "" or descricao == "" or preco_por_kg == "":
                messagebox.showerror("Erro", "Preencha todos os campos!")
                return
            
        except ValueError as error:
            messagebox.showwarning("Alerta", str(error))
            self.cadastro_produto_view.lift()
            return
            
    
        
        messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        self.cadastro_produto_view.lift()
        
    def criar_tela_cadastro_produto(self):
        self.cadastro_produto_view = CadastroProdutoView(self)
        

    def fechar_janela(self, janela):
        self.salvar_produtos_cadastrados()
        janela.destroy()

    
    def salvar_produtos_cadastrados(self):
        
        if len(self.lista_de_produtos_cadastrados) != 0:
            with open("produtos.pickle", "wb") as f:
                pickle.dump(self.lista_de_produtos_cadastrados, f)

    def mostrar_instancias(self):
        os.system("cls")
        print("Produtos Cadastrados: ")
        for produto in self.lista_de_produtos_cadastrados:
            print(f"{produto.codigo} - {produto.descricao} - {produto.preco_por_kg}")
            

    


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

        self.bt1 = tk.Button(self.raiz, text="Cadastrar Produto", command=self.controller.criar_tela_cadastro_produto)
        self.bt1.pack()

        
        self.bt2 = tk.Button(self.raiz, text="Consultar Produto", command="")
        self.bt2.pack()
  

        self.bt3 = tk.Button(self.raiz, text="Alterar Produto", command="")
        self.bt3.pack()


        self.bt4= tk.Button(self.raiz, text="Excluir Produto", command="")
        self.bt4.pack()
    

        self.bt5 = tk.Button(self.raiz, text="Ir para o carrinho", command="")
        self.bt5.pack()
   

        self.bt6 = tk.Button(self.raiz, text="Mostrar Instâncias", command=self.controller.mostrar_instancias)
        self.bt6.pack()



        self.fechar_button = tk.Button(self.raiz, text="Fechar", command= lambda: self.controller.fechar_janela(self.raiz))
        self.fechar_button.pack()



        self.raiz.mainloop()

        
    def fechar_janela(self, janela):

        janela.destroy()

    

if __name__ == "__main__":

    produto_controle = ControleProduto(None)
    janela_auxiliar = JanelaAuxiliar(produto_controle)