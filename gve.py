# bibliotecas nativas
from tkinter import *
from tkinter import ttk 
from datetime import *
import pymsgbox as pymb
from tkinter import messagebox

#bibliotecas GVE
from cadastro import Produto, Categoria

#variáveis globais de configurações
bt_lar = 60 #largura botoes
bt_alt = 30 #altura botoes
bt_bd = 1.5 #borda interna  botoes

class Aplicativo:

    def __init__(self):
        self.raiz = Tk()
        self.janela()
        self.menu_raiz()
        self.raiz.mainloop()
    
    def janela(self):
        self.raiz.title('Gestão de Distribuição e Entrega')
        self.raiz.geometry('1000x600+150+30')

    def menu_raiz(self):
        #configurações para a tela e para o menu
        self.menu_barra = Menu(self.raiz)
        self.raiz.config(menu=self.menu_barra) #configurando a tela principal para este menu

        #menu cadastros
        self.menu_cad = Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(label='Cadastro',menu=self.menu_cad, underline=0)
        self.menu_cad.add_command(label='Cliente', command=None)
        self.menu_cad.add_command(label='Fornecedor', command=None)
        self.menu_cad.add_command(label='Produto', command=Produto, underline=0)
        self.menu_cad.add_command(label='Categoria', command=Categoria,underline=0)
        self.menu_cad.add_command(label='Forma de Pagamento', command=None)
        self.menu_cad.add_separator()
        self.menu_cad.add_command(label='Sair', command=self.raiz.quit)

        #menu movimento
        self.menu_mov = Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(label='Movimento',menu=self.menu_mov)
        self.menu_mov.add_command(label='Saída', command=None)
        self.menu_mov.add_command(label='Entregas', command=None)
        self.menu_mov.add_command(label='Entrada', command=None)

        #menu relatorio
        self.menu_rel = Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(label='Relatórios',menu=self.menu_rel)
        self.menu_rel.add_command(label='Venda', command=None)
        self.menu_rel.add_command(label='Compra', command=None)
        
        #menu utilitarios
        self.menu_uti = Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(label='Utilitários',menu=self.menu_uti)
        self.menu_uti.add_command(label='Usuários', command=Produto)
        self.menu_uti.add_command(label='Atualização', command=Produto)


if __name__ == '__main__':
   Aplicativo()
   