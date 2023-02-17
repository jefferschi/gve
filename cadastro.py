# bibliotecas nativas
from tkinter import *
from tkinter import ttk 
from datetime import *
import pymsgbox as pymb
from tkinter import messagebox

#variáveis globais de configurações
bt_lar = 60 #largura botões
bt_alt = 25 #altura botões
bt_bd = 1.5 #borda interna botões

class Categoria:
    def __init__(self):
        self.tl_categ = Tk()
        self.janela('Cadastro de Categorias','400x500+450+35')
        self.tl_categ.mainloop()

    def janela(self,titulo,dim_pos):
        #configuração das dimensões
        self.tl_categ.title(titulo)
        self.tl_categ.geometry(dim_pos)
        self.tl_categ.resizable(False,False)
        
        #quadro para as informações da categoria
        self.qd_dados_cat = Frame(self.tl_categ)
        self.qd_dados_cat.place(x=3,y=3, relheight=0.35, relwidth=0.99)

        # rotulos e entradas
        Label(self.qd_dados_cat, text='Código').place(x=0, y=1)
        self.ent_cod_cat = Entry(self.qd_dados_cat, width=10)
        self.ent_cod_cat.place(x=0,y=20)
        self.ent_cod_cat.focus()

        Label(self.qd_dados_cat, text='Descrição').place(x=0, y=45)
        self.ent_desc_cat = Entry(self.qd_dados_cat, width=30)
        self.ent_desc_cat.place(x=0,y=65)

        # labelframe e combobox para ordenação de colunas e ascedencia ou descendencia
        self.lf_ord_cat = LabelFrame(self.qd_dados_cat,text=' Ordenar lista por ', width=180, height=77)
        self.lf_ord_cat.place(x=0,y=98)

        self.cb_ord_col = ttk.Combobox(self.lf_ord_cat, width=19, values=('Código','Descrição'))
        self.cb_ord_col.place(x=1.5,y=0)
        self.cb_ord_an = ttk.Combobox(self.lf_ord_cat, width=8, values=('↓ Cresc.','↑ Decres.')) #alt + 24 ou 25
        self.cb_ord_an.place(x=1.5,y=25)
        
        self.botoes()
        self.lista_dados()

    def lista_dados(self):
        # quadro para a treeview categoria
        self.qd_lista_cat = Frame(self.tl_categ)

        #barra lateral da treeview
        self.barra_lt_cat = Scrollbar(self.qd_lista_cat)


        # lista treeview
        self.lt_cat = ttk.Treeview(self.qd_lista_cat, columns=('cod','desc'),
                        yscrollcommand=self.barra_lt_cat.set, show='headings')


        self.barra_lt_cat.config(command=self.lt_cat.yview)

        self.lt_cat.heading('#0',text='')
        self.lt_cat.heading('#1',text='Código')
        self.lt_cat.heading('#2',text='Descrição')

        self.lt_cat.column('#0',width=1)
        self.lt_cat.column('#1',width=5)
        self.lt_cat.column('#2',width=200)

        #empacotamento quadros, lista e barra de rolagem
        self.qd_lista_cat.place(relx=0.01, rely=0.37,relwidth=0.98, relheight=0.61)
        self.lt_cat.place(relwidth=0.96, relheight=0.98, relx=0, rely=0.01)
        self.barra_lt_cat.pack(side=RIGHT, fill=Y)

    def botoes(self):
        """colocar ícones na frente dos botões, em vez de cores, se possível"""

        # quadro para os botões
        self.qd_bt_cat = Frame(self.qd_dados_cat, width=200, height=150)
        self.qd_bt_cat.place(relx=0.7,y=7)
        
        # botões
        bt_novo = Button(self.qd_bt_cat,text='Novo', bd=bt_bd, command=None)
        bt_novo.place(x=1,y=1, width=bt_lar, height=bt_alt)

        bt_alterar = Button(self.qd_bt_cat,text='Alterar',bd=bt_bd, command=None)
        bt_alterar.place(x=1,y=36,width=bt_lar, height=bt_alt)
             
        bt_limpar = Button(self.qd_bt_cat,text='Limpar',bd=bt_bd, command=self.limpa_entrys)
        bt_limpar.place(x=1,y=70,width=bt_lar, height=bt_alt)

        bt_deletar = Button(self.qd_bt_cat,text='Deletar',bd=bt_bd, command=None)
        bt_deletar.place(x=1,y=105,width=bt_lar, height=bt_alt)
       
        # botão buscar temporário, colocar um ícone de lupa ao lado do código
        bt_buscar = Button(self.tl_categ,text='Buscar',bd=bt_bd, command=None)
        bt_buscar.place(relx=0.25,y=19,width=bt_lar, height=bt_alt)

        #botão ordenar dentro da labelframe ordenar por
        bt_ordenar = Button(self.lf_ord_cat,text='Ordenar',bd=bt_bd, command=None)
        bt_ordenar.place(relx=0.55, rely=0.45, width=bt_lar, height=bt_alt)

    # funções para os botões
    def limpa_entrys(self):
        # limpa entradas dos dados de categoria
        self.ent_cod_cat.delete(0,END)
        self.ent_desc_cat.delete(0,END)
        self.ent_cod_cat.focus()

#
class Produto:
    def __init__(self):
        self.tl_prod = Tk()
        self.janela('Cadastro de Produtos','800x550+410+45')
        self.tl_prod.mainloop()

    def janela(self,titulo,dim_pos):
        #configuração das dimensões
        self.tl_prod.title(titulo)
        self.tl_prod.geometry(dim_pos)
        self.tl_prod.resizable(True,True)
        self.tl_prod.sizefrom('user')
        

        #quadro para as informações dos produtos
        self.qd_dados_prod = Frame(self.tl_prod, bg='white')
        self.qd_dados_prod.place(x=3,y=3, height=575, width=750)
        

        #subquadro para os dados gerais de cadastro do produto
        self.lf_dd_ger_prod = LabelFrame(self.qd_dados_prod, text='Dados Principais')
        self.lf_dd_ger_prod.place(x=0,y=0, height=120, relwidth=1)

        # rotulos, entradas, check buttons, combobox
        Label(self.lf_dd_ger_prod, text='Código').place(x=0, y=1)
        self.ent_cod_prod = Entry(self.lf_dd_ger_prod, width=10)
        self.ent_cod_prod.place(x=0,y=20)
        self.ent_cod_prod.focus()

        Label(self.lf_dd_ger_prod, text='Código de barras').place(x=125, y=1)
        self.ent_cod_br_prod = Entry(self.lf_dd_ger_prod, width=15)
        self.ent_cod_br_prod.place(x=125,y=20)

        Label(self.lf_dd_ger_prod, text='Descrição').place(x=0, y=45)
        self.ent_desc_prod = Entry(self.lf_dd_ger_prod, width=45)
        self.ent_desc_prod.place(x=0,y=65)

         # variável para o check button campo Ativo igual a 1 ou 0
        self.v_ativo = IntVar(self.lf_dd_ger_prod,1)
        self.ch_bt_ativo = Checkbutton(self.lf_dd_ger_prod,text='Ativo',variable=self.v_ativo, 
                            onvalue=1, offvalue=0)
        self.ch_bt_ativo.place(x=670, y=10)

        
        #temporário para as combos
        self.lt_combo = ['REFRIGERANTE','CX']   
        """exemplo para usar quando conectar as combobox a um banco de dados"""
        #self.dados = self.cursor.execute(""" SELECT DISTINCT(categoria) as categoria FROM categorias""")
        #self.lista_combo = [r for r, in self.dados]
        

        Label(self.lf_dd_ger_prod, text='Categoria').place(x=450, y=1)   
        self.cb_cat = ttk.Combobox(self.lf_dd_ger_prod, width=18, values=self.lt_combo)
        self.cb_cat.place(x=450, y=20)

        Label(self.lf_dd_ger_prod, text='Marca').place(x=450, y=45)
        self.cb_marca = ttk.Combobox(self.lf_dd_ger_prod,width=18, values=self.lt_combo)
        self.cb_marca.place(x=450,y=65)
        

        #subquadro para os dados COMERCIAIS do produto
        self.lf_dd_com_prod = LabelFrame(self.qd_dados_prod,text='Comerciais')
        self.lf_dd_com_prod.place(x=0,y=121, height=120, relwidth=1)


        Label(self.lf_dd_com_prod, text='Und. Venda').place(x=0, y=1)
        self.cb_und_vda = ttk.Combobox(self.lf_dd_com_prod,width=3, values=self.lt_combo)
        self.cb_und_vda.place(x=0,y=21)

        Label(self.lf_dd_com_prod, text='Preço de Venda').place(x=125, y=1)
        self.ent_pr_vda = Entry(self.lf_dd_com_prod, width=10)
        self.ent_pr_vda.place(x=125, y=21)

        Label(self.lf_dd_com_prod,text='Und. Compra').place(x=0,y=46)
        self.cb_und_cmp = ttk.Combobox(self.lf_dd_com_prod,width=3, values=self.lt_combo)
        self.cb_und_cmp.place(x=0,y=66)

        Label(self.lf_dd_com_prod,text='Preço de Custo').place(x=125,y=46)
        self.ent_pr_custo = Entry(self.lf_dd_com_prod, width=10)
        self.ent_pr_custo.place(x=125, y=66)

        Label(self.lf_dd_com_prod, text='Fator conversão').place(x=280, y=1) 
        self.ent_ft_conv = Entry(self.lf_dd_com_prod, width=5)
        self.ent_ft_conv.place(x=280, y=21)


        #subquadro para as CARACTERÍSTICAS do produto
        self.lf_carac_prod = LabelFrame(self.qd_dados_prod,text='Características')
        self.lf_carac_prod.place(x=0,y=242, height=120, relwidth=1)
        
        Label(self.lf_carac_prod, text='Peso(kg)').place(x=0, y=1)
        self.ent_peso = Entry(self.lf_carac_prod, width=10)
        self.ent_peso.place(x=0,y=21)

        Label(self.lf_carac_prod, text='Volume(lt)').place(x=0, y=46)
        self.ent_volume = Entry(self.lf_carac_prod, width=10)
        self.ent_volume.place(x=0,y=66)

        #subquadro para informações gerais
        # label estoque
        # entry estoque (não editável)
      

