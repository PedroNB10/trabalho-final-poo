import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import os.path
import pickle

from collections import OrderedDict
from datetime import datetime

import cliente as cl # lembrar de remover


class NotaFiscal:
    def __init__(self, numero, data, cpf_cliente, produtos):
        self.__numero = numero
        self.__data = data
        self.cpf_cliente = cpf_cliente
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
    
    @cpf_cliente.setter
    def cpf_cliente(self, cpf):
  
        if len(cpf) != 11:
            raise ValueError("CPF inválido")
        self.__cpf_cliente = cpf
            
    @property
    def produtos(self):
        return self.__produtos
    

class ControleNota:
    def __init__(self, controle_principal = None): # lembrar de remover
        self.controle_principal = controle_principal

        if not os.path.isfile("notas.pickle"):
            self.__lista_de_notas_fiscais = []

        else:
            with open("notas.pickle", "rb") as f:
                self.__lista_de_notas_fiscais = pickle.load(f)
                
                
    def salvar_notas_fiscais(self):
        
        if len(self.__lista_de_notas_fiscais) != 0:
            with open("notas.pickle", "wb") as f:
                pickle.dump(self.__lista_de_notas_fiscais, f)
            
            
    def mostrar_ultima_nota_fiscal(self):
        lista_de_notas = self.__lista_de_notas_fiscais
        ultima_nota = lista_de_notas[-1]
        print(ultima_nota)
        print(ultima_nota.cpf_cliente)
        print(ultima_nota.data)
        print(ultima_nota.numero)
        str = ''
        str += f'Número da Nota: {ultima_nota.numero}\n'
        str += f'Data: {ultima_nota.data.day}/{ultima_nota.data.month}/{ultima_nota.data.year}\n'
        str += f'CPF do Cliente: {ultima_nota.cpf_cliente}\n\n'
        str += 'Produtos: \n'
        c = 1
        for produto in ultima_nota.produtos:
            str += f'{c} - {produto.produto.descricao} - '
            str += f'Quantidade: {produto.quantidade} kg - '
            str += f'Preço por kg: R$ {produto.produto.preco_por_kg} \n'
            c += 1
        str += f'\nValor Total: R$ {self.calcular_valor_total_de_uma_nota(ultima_nota.numero)}\n'
        str += '-------------------------------------------------------------------------\n\n'
            
        messagebox.showinfo('Nota Fiscal Gerada', str)
            
    def mostrar_notas_fiscais(self):
        lista_de_notas = self.__lista_de_notas_fiscais
        
        if len(lista_de_notas) == 0:
            messagebox.showinfo("Notas Fiscais", "Não há notas fiscais cadastradas")
            return
        
        str = ''
        for nota in lista_de_notas:
            str += f'Número da Nota: {(nota.numero)}\n'
            str += f'Data: {nota.data.day}/{nota.data.month}/{nota.data.year}\n'
            str += f'CPF do Cliente: {nota.cpf_cliente}\n\n'
            str += 'Produtos: \n'
            c = 1
            for produto in nota.produtos:
                str += f'{c} - {produto.produto.descricao} - '
                str += f'Quantidade: {produto.quantidade} kg - '
                str += f'Preço por kg: R$ {produto.produto.preco_por_kg} \n'
                c += 1
            str += f'\nValor Total: R$ {self.calcular_valor_total_de_uma_nota(nota.numero)}\n'
            str += '-------------------------------------------------------------------------\n\n'
            
        messagebox.showinfo('Notas Fiscais', str)
        
    def calcular_valor_total_de_uma_nota(self, numero_nota):
        lista_de_notas = self.__lista_de_notas_fiscais
        for nota in lista_de_notas:
            if nota.numero == numero_nota:
                valor_total = 0
                for produto in nota.produtos:
                    valor_total += produto.produto.preco_por_kg * produto.quantidade
                return valor_total
        return None
    
    
    def mostrar_nota_unica(self, numero_nota):
        lista_de_notas = self.__lista_de_notas_fiscais
        str = ''
        
        for nota in lista_de_notas:
            if nota.numero == numero_nota:
                
                str += f'Número da Nota: {(nota.numero)}\n'
                str += f'Data: {nota.data.day}/{nota.data.month}/{nota.data.year}\n'
                str += f'Nome do Cliente: {self.controle_principal.controle_cliente.getCliente(nota.cpf_cliente).nome}\n\n'
                str += f'CPF do Cliente: {nota.cpf_cliente}\n\n'
                
                str += 'Produtos: \n'
                c = 1
                for produto in nota.produtos:
                    str += f'{c} - {produto.produto.descricao} - '
                    str += f'Quantidade: {produto.quantidade} kg - '
                    str += f'Preço por kg: R$ {produto.produto.preco_por_kg} \n'
                    c += 1
                str += f'\nValor Total: R$ {self.calcular_valor_total_de_uma_nota(nota.numero)}\n'
                str += '-------------------------------------------------------------------------\n\n'
                messagebox.showinfo('Nota Fiscal', str)
                return
        messagebox.showinfo('Nota Fiscal', 'Nota fiscal não encontrada')
            
        
    def criar_instancia_nota(self, numero, data, cpf_cliente, produtos):
        
        try:
            
            nota = NotaFiscal(numero, data, cpf_cliente, produtos)
            self.__lista_de_notas_fiscais.append(nota)
            cliente = self.controle_principal.controle_cliente.getCliente(cpf_cliente)
            
            if cliente == None:
                raise ValueError("Cliente não encontrado")
            print("Antes")
            print(cliente.lista_de_notas)
            cliente.lista_de_notas.append(nota)
            print("Depois")
            print(cliente.lista_de_notas)
            
            print("Total de notas")
            print(self.__lista_de_notas_fiscais)
        except ValueError as error:
            messagebox.showwarning("Alerta", str(error))
            
    def lista_de_notas_fiscais_geradas(self):
        return self.__lista_de_notas_fiscais
    
    def criar_janela_consultar_nota(self):
        self.limite_consultar_nota = LimiteConsultarNota(self)

    def consultar_nota_handler(self):

        
        try:
            numero_da_nota = int(self.limite_consultar_nota.input_numero_nota.get())

        except ValueError:
            messagebox.showwarning("Alerta", "Digite um número inteiro")
            return
        notas = self.__lista_de_notas_fiscais
        
        for nota in notas:
            if nota.numero == numero_da_nota:
                self.mostrar_nota_unica(numero_da_nota)
                self.limite_consultar_nota.lift()
                return
        
        messagebox.showinfo("Nota Fiscal", "Não há notas fiscais com esse código")
        self.limite_consultar_nota.lift()
        
        
    def consultar_faturamento_por_produto(self):
        codigo_produto = simpledialog.askinteger("Faturamento por Produto", "Digite o código do produto: ")
        produto = self.controle_principal.controle_produto.getProduto(codigo_produto)
        
        if produto == None:
            messagebox.showinfo("Faturamento por Produto", "Produto não encontrado")
            return

        notas = self.__lista_de_notas_fiscais
        valor_total = 0
        for nota in notas:
            for produto_nota in nota.produtos:
                if produto_nota.produto.codigo == codigo_produto:
                    valor_total += produto_nota.produto.preco_por_kg * produto_nota.quantidade
                    
        messagebox.showinfo("Faturamento por Produto", f"O faturamento total do produto {produto.descricao} foi de R$ {valor_total}")
        
    def criar_janela_consultar_periodo(self):
        self.limite_consultar_periodo = ConsultarPeriodoView(self)
        
    def consultar_faturamento_por_periodo_handler(self):
        data_inicial = self.limite_consultar_periodo.input_data_inicial.get()
        data_final = self.limite_consultar_periodo.input_data_final.get()

        if data_inicial.count('/') != 2 or data_final.count('/') != 2:
            messagebox.showwarning("Alerta", "Digite a data no formato dd/mm/aaaa")
            self.limite_consultar_periodo.lift()
            return
        
        data_inicial_formatada = datetime.strptime(data_inicial, '%d/%m/%Y')
        data_final_formatada = datetime.strptime(data_final, '%d/%m/%Y')

        notas = self.__lista_de_notas_fiscais
        valor_total = 0
        str = ''
        str += 'Notas Fiscais Geradas no período de ' + data_inicial + ' a ' + data_final + '\n\n'
        for nota in notas:
            if data_inicial_formatada <= nota.data <= data_final_formatada:
                str += f'Número da Nota: {(nota.numero)}\n'
                str += f'Data: {nota.data.day}/{nota.data.month}/{nota.data.year}\n'
                str += f'CPF do Cliente: {nota.cpf_cliente}\n\n'
                str += 'Produtos: \n'
                c = 1
                for produto in nota.produtos:
                    str += f'{c} - {produto.produto.descricao} - '
                    str += f'Quantidade: {produto.quantidade} kg - '
                    str += f'Preço por kg: R$ {produto.produto.preco_por_kg} \n'
                    c += 1
                str += f'\nValor Total: R$ {self.calcular_valor_total_de_uma_nota(nota.numero)}\n'
                str += '-------------------------------------------------------------------------\n\n'
                valor_total += self.calcular_valor_total_de_uma_nota(nota.numero)
                
        str += f'Fatutamento Total: R$ {valor_total}\n'     
        
        messagebox.showinfo("Faturamento por Período", str)
        self.limite_consultar_periodo.lift()        
        
        
    def mostrar_notas_fiscais_por_cliente(self, cpf):
        notas = self.__lista_de_notas_fiscais
        str = ''
        for nota in notas:
            if nota.cpf_cliente == cpf:
                str += f'Número da Nota: {(nota.numero)}\n'
                str += f'Data: {nota.data.day}/{nota.data.month}/{nota.data.year}\n'
                str += f'CPF do Cliente: {nota.cpf_cliente}\n\n'
                str += 'Produtos: \n'
                c = 1
                for produto in nota.produtos:
                    str += f'{c} - {produto.produto.descricao} - '
                    str += f'Quantidade: {produto.quantidade} kg - '
                    str += f'Preço por kg: R$ {produto.produto.preco_por_kg} \n'
                    c += 1
                str += f'\nValor Total: R$ {self.calcular_valor_total_de_uma_nota(nota.numero)}\n'
                str += '-------------------------------------------------------------------------\n\n'
        str += '-------------------------------------------------------------------------\n'        
        str += f'Fatutamento Total: R$ {self.calcular_faturamento_por_cliente(cpf)}\n'
        str += '-------------------------------------------------------------------------\n\n'
        messagebox.showinfo('Notas Fiscais', str)
        
        
        
    
        
    def calcular_faturamento_por_cliente(self, cpf):
        notas = self.__lista_de_notas_fiscais
        valor_total = 0
        for nota in notas:
            if nota.cpf_cliente == cpf:
                valor_total += self.calcular_valor_total_de_uma_nota(nota.numero)
        return valor_total
        
    def consultar_faturamento_por_cliente(self):
        cpf = simpledialog.askstring("Faturamento por Cliente", "Digite o CPF do cliente: ")
        cliente = self.controle_principal.controle_cliente.getCliente(cpf)
        
        if cliente == None:
            messagebox.showinfo("Faturamento por Cliente", "Cliente não encontrado")
            return
        
        if len(cliente.lista_de_notas) == 0:
            messagebox.showinfo("Faturamento por Cliente", "Cliente não possui notas fiscais")
            return
        
        print(cliente.nome)
        print(cliente.email)
        print(cliente.cpf)
        print(cliente.lista_de_notas)
        

        self.mostrar_notas_fiscais_por_cliente(cpf)
        
    
    def consultar_produtos_mais_vendidos(self):
        if len(self.__lista_de_notas_fiscais) == 0:
            messagebox.showinfo("Produtos mais vendidos", "Não houve nenhum produto vendido!")
            return
        lista_de_produtos_vendidos = []
        dicionario_produtos_vendidos = {}
        for nota in self.__lista_de_notas_fiscais:
            for conjunto_produto in nota.produtos:
                if conjunto_produto.produto not in lista_de_produtos_vendidos:
                    lista_de_produtos_vendidos.append(conjunto_produto.produto)
                    
                    
        for produto in lista_de_produtos_vendidos:
            dicionario_produtos_vendidos[produto.descricao] = 0
                    
        # lista_de_produtos_vendidos.sort(key=lambda x: x.descricao)
        dicionario_em_ordem_decrescente = {}
        
        if len(lista_de_produtos_vendidos) < 5:
            for produto in lista_de_produtos_vendidos:
                for nota in self.__lista_de_notas_fiscais:
                    for conjunto_produto in nota.produtos:
                        if conjunto_produto.produto == produto:
                            print(conjunto_produto.calcular_valor_total_do_conjunto())
                            dicionario_produtos_vendidos[conjunto_produto.produto.descricao] += conjunto_produto.calcular_valor_total_do_conjunto()
            dicionario_em_ordem_decrescente = OrderedDict(sorted(dicionario_produtos_vendidos.items(), key=lambda x: x[1], reverse=True))
            str = ''
            str += 'Produtos mais vendidos: \n\n'
            print(dicionario_em_ordem_decrescente)
            c = 1
            for produto in dicionario_em_ordem_decrescente:
                
                str += f'{c}º - {produto} - R$ {dicionario_produtos_vendidos[produto]}\n'
                c += 1
            messagebox.showinfo("Produtos mais vendidos", str)
            
        else:
            for produto in lista_de_produtos_vendidos:
                    for nota in self.__lista_de_notas_fiscais:
                        for conjunto_produto in nota.produtos:
                            if conjunto_produto.produto == produto:
                                print(conjunto_produto.calcular_valor_total_do_conjunto())
                                dicionario_produtos_vendidos[conjunto_produto.produto.descricao] += conjunto_produto.calcular_valor_total_do_conjunto()
            dicionario_em_ordem_decrescente = OrderedDict(sorted(dicionario_produtos_vendidos.items(), key=lambda x: x[1], reverse=True))
            str = ''
            str += 'Produtos mais vendidos: \n\n'
            c = 1
            for produto in dicionario_em_ordem_decrescente:
                str += f'{c}º - {produto} - R$ {dicionario_em_ordem_decrescente[produto]}\n'
                c += 1
                if c == 6:
                    break
                
            messagebox.showinfo("Produtos mais vendidos", str)                    

    
    def fechar_janela(self, janela):
        janela.destroy()
    
class ConsultarPeriodoView(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.controle = controle
        self.title("Consultar Faturamento por Período")
    
        self.frame_height = 150
        self.frame_width = 300
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        coordenada_x = int((self.screen_width/2) - (self.frame_width/2))
        coordenada_y = int((self.screen_height/2) - (self.frame_height/2))
        self.geometry("{}x{}+{}+{}".format(self.frame_width, self.frame_height, coordenada_x, coordenada_y))
        
        self.main_frame = tk.Frame(self)
        self.main_frame.pack()        

        self.frame_data_inicial = tk.Frame(self.main_frame)
        self.frame_data_inicial.pack()
        self.label_data_inicial = tk.Label(self.frame_data_inicial, text="Data Inicial: ")
        self.label_data_inicial.pack(side="left")
        self.input_data_inicial = tk.Entry(self.frame_data_inicial, width=20)
        self.input_data_inicial.pack()
        
        self.frame_data_final = tk.Frame(self.main_frame)
        self.frame_data_final.pack()
        self.label_data_final = tk.Label(self.frame_data_final, text="Data Final: ")
        self.label_data_final.pack(side="left")
        self.input_data_final = tk.Entry(self.frame_data_final, width=20)
        self.input_data_final.pack()
        
        
        self.botao_consultar = tk.Button(self, text="Consultar", command=self.controle.consultar_faturamento_por_periodo_handler)
        self.botao_consultar.pack()
        
        self.botao_fechar = tk.Button(self, text="Fechar", command= lambda: self.controle.fechar_janela(self))
        self.botao_fechar.pack(pady=15)
    
class LimiteConsultarNota(tk.Toplevel):
    def __init__(self, controle):
        self.controle = controle
        tk.Toplevel.__init__(self)
        self.title("Consultar Nota Fiscal")
    
        self.frame_height = 150
        self.frame_width = 300
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        coordenada_x = int((self.screen_width/2) - (self.frame_width/2))
        coordenada_y = int((self.screen_height/2) - (self.frame_height/2))
        self.geometry("{}x{}+{}+{}".format(self.frame_width, self.frame_height, coordenada_x, coordenada_y))
        

        self.frame_nota = tk.Frame(self)
        self.label_nota = tk.Label(self.frame_nota, text="Digite o número da nota: ", pady=30)
        self.label_nota.pack(side="left")
        self.input_numero_nota = tk.Entry(self.frame_nota, width=20)
        self.input_numero_nota.pack(side="left")
        self.frame_nota.pack()
        self.botao_consultar = tk.Button(self, text="Consultar", command=self.controle.consultar_nota_handler)
        self.botao_consultar.pack()
        
        self.botao_fechar = tk.Button(self, text="Fechar", command= lambda: self.controle.fechar_janela(self))
        self.botao_fechar.pack(pady=15)



    
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


        self.bt1 = tk.Button(self.raiz, text="Consultar Nota Fiscal", command=controle.criar_janela_consultar_nota)
        self.bt1.pack()

        
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
    nota_controle = ControleNota(None)
    janela_aux = JanelaAuxiliar(nota_controle)
