print('Rodadando Aplicação Principal')
#Importando Bibliotecas do Python
import sys
import os
import pandas as pd
from datetime import datetime
#Importando as bibliotecas do PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem, QColor
from PySide6.QtCore import Qt
#Importando as janelas criadas no QtDesigner
from Windows.MainWindow import Ui_MainWindow   # A janela criada no QtDesigner
from Windows.DarkMode import DarkPallete

import os
caminho = os.getcwd()


# Cria a classe da janela principal | Herda a classe QMainWindow e a classe Ui_MainWindow
class MainWindow(QMainWindow, Ui_MainWindow):   
    def __init__(self):
        super().__init__()
        self.setupUi(self)                      # Configura a janela principal
        self.show()                             # Mostra a janela principal
        self.carrega_dfs()
        self.prepara_dataframe()
        self.carrega_programa_tableview(self.new_df, self.TableView_QVV)          # Carrega o DataFrame na tabela
        self.carrega_programa_tableview(self.df_agr, self.TableView_Categoria_Agr)    # Carrega o DataFrame na tabela
        self.carrega_programa_tableview(self.df_AgrExp, self.TableView_Exp)    # Carrega o DataFrame na tabela
        self.largura_tableview()    
        self.colorir_colunas()                  # Define a largura das colunas da tabela   
        self.conectar_sinais()                  # Conecta os sinais aos slots
        QMessageBox.information(self, 'Informação', 'Dados Carregados com Sucesso!"')

    def carrega_dfs(self):
        # =========== LISTA DE QVV'S ==============
        self.df_qvvs = pd.read_excel(r'{}/Arquivos Usados/Lista_QVVs.xlsx'.format(caminho), sheet_name='Plan1')
        self.df_qvvs.fillna('',inplace=True)
        
        # =========== LISTA EXPORTAÇÃO ==============
        self.df_lista_exp = pd.read_excel(r'{}/Arquivos Usados/Lista_Exportação.xlsx'.format(caminho), sheet_name='Plan1')
        
                
        # =========== PROGRAMA DE VEICULOS ==============
        self.df_programas = pd.read_excel(r'{}/Arquivos Usados/Programa.xlsx'.format(caminho), sheet_name='Plan1')
        dict_datas = {'01': 'jan', '02': 'fev', '03': 'mar', '04': 'abr', '05': 'mai', '06': 'jun', '07': 'jul', '08': 'ago', '09': 'set', '10': 'out', '11': 'nov', '12': 'dez', 'Linha': 'Linha_Destino'}
        self.df_programas.rename(columns={'Variante':'QVV'}, inplace=True)
        for item in dict_datas:
            self.df_programas.rename(columns={item:dict_datas[item]}, inplace=True)
            
        self.df_programas['DataArquivo'] = pd.to_datetime(self.df_programas['DataArquivo']).dt.strftime('%d/%m/%Y %H:%M:%S')
            
        # =========== PROGRAMA DE AGREGADOS EXPORTAÇÃO ==============
        self.df_programas_exp = pd.read_csv(r'{}/Arquivos Usados/Programa_Exportacao.csv'.format(caminho),sep=';', encoding='latin-1')

        self.df_programas_exp = self.df_programas_exp.merge(self.df_lista_exp[['Variante', 'Tipo', 'Serie']], on='Variante', how='left', indicator=True)
        self.df_programas_exp.loc[self.df_programas_exp['_merge'] == 'left_only', 'Tipo'] = 'NotFound'
        self.df_programas_exp.loc[self.df_programas_exp['_merge'] == 'left_only', 'Serie'] = 'NotFound'
        # Alterar o tipo de  objeto para int nos campos de Jan a Dez
        meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov','Dez']

        for item in meses:
            self.df_programas_exp[item] = self.df_programas_exp[item].astype(int)
            
        #somar as colunas de Jan a Dez se o campo 'Variante' for igual
        self.df_programas_exp = self.df_programas_exp.groupby(['Variante', 'Tipo', 'Serie', 'Versão', 'DataArquivo', 'Ano']).sum().reset_index()

        self.df_programas_exp.rename(columns={'Variante':'QVV'}, inplace=True)
        dict_datas_exp = {'Jan': 'jan', 'Fev': 'fev', 'Mar': 'mar', 'Abr': 'abr', 'Mai': 'mai', 'Jun': 'jun', 'Jul': 'jul', 'Ago': 'ago', 'Set': 'set', 'Out': 'out', 'Nov': 'nov', 'Dez': 'dez'}
        for item in dict_datas_exp:
            self.df_programas_exp.rename(columns={item:dict_datas_exp[item]}, inplace=True)
        
        self.df_programas_exp['Linha_Destino'] = 'EXP'
        self.df_programas_exp['DataArquivo'] = self.df_programas['DataArquivo'].values.astype(str)[0]
                    
        #=========== Categoria_Agregados Exportação ==============
        self.df_cat_agr_exp = pd.read_excel(r'{}/Arquivos Usados/Categoria_Agregados Exportação.xlsx'.format(caminho), sheet_name='Plan1')
        
        # =========== JUNÇÃO DOS PROGRAMAS ==============
        self.df_programas = pd.concat([self.df_programas, self.df_programas_exp], axis=0)
        
        # =========== EXTRAÇÃO DA DATA PARA ARQUIVO ==============
        self.Data_arquivo = self.df_programas['DataArquivo'].values.astype(str)[0]
        self.Data_arquivo = self.Data_arquivo[:10]
        #self.Data_arquivo = datetime.strptime(self.Data_arquivo, '%Y-%m-%d').date()
        #self.Data_arquivo = self.Data_arquivo.strftime('%d/%m/%Y')
        self.Data_arquivo = self.Data_arquivo.replace('/','.')   
                 
        # =========== PROGRAMA FINAL ============== 
        self.new_df = self.df_programas.merge(self.df_qvvs, on='QVV', how='left')
        self.new_df.fillna('NotFound',inplace=True)
        #REMOVER AS DUPLICADAS DO DATAFRAME EM TODAS AS COLUNAS
        self.new_df = self.new_df.drop_duplicates()
        
        # =========== CATEGORIA DE AGREGADOS ==============
        self.df_agr = pd.read_excel(r'{}/Arquivos Usados/Categoria_Agregados.xlsx'.format(caminho), sheet_name='Plan1')
        self.df_AgrExp = pd.read_excel(r'{}/Arquivos Usados/Lista_Exportação.xlsx'.format(caminho), sheet_name='Plan1')
        self.df_AgrExp = self.df_AgrExp.sort_values(by=['Variante'])

    def conectar_sinais(self):
        self.TableView_QVV.clicked.connect(self.seleciona_linha_programa)
        self.TableView_Categoria_Agr.clicked.connect(self.seleciona_linha_agregados)
        self.TableView_Exp.clicked.connect(self.seleciona_linha_exportacao)
        self.TableView_QVV.verticalHeader().setVisible(False)
        self.TableView_Categoria_Agr.verticalHeader().setVisible(False)
        self.TableView_Exp.verticalHeader().setVisible(False)
        self.Button_Cadastrar.clicked.connect(self.atualiza_dados_programa)
        self.Button_Cadastrar_Agregado.clicked.connect(self.atualiza_dados_agregados)
        self.Button_Cadastrar_Agregado_Exp.clicked.connect(self.atualiza_dados_exportacao)
        self.TableView_QVV.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.RadioButton_NotFound.clicked.connect(self.filtrar_radiobutton)
        self.RadioButton_Tudo.clicked.connect(self.filtrar_radiobutton)
        self.TabAgregados.currentChanged.connect(self.redimensiona_janela)


    def prepara_dataframe(self):
        """
        Função para verificar se o valor do LineEdit corresponde a um valor na coluna 'BM' do DataFrame df_agr.
        Se corresponder, retorna o valor da coluna 'Modelo' e 'Linha' na mesma linha em que o valor foi encontrado.
        """

        lista_agr = ['M', 'G', 'H', 'J', 'V', 'W']
        
        for i in lista_agr:
            self.new_df = self.new_df.rename(columns={i: 'BM'})
            self.df_agr = self.df_agr.rename(columns={'Modelo': 'Modelo_{}'.format(i), 'Linha': 'Lin_{}'.format(i)})
            self.new_df = self.new_df.merge(self.df_agr, on='BM', how='left')
            self.new_df = self.new_df.rename(columns={'BM': i})
            self.df_agr = self.df_agr.rename(columns={'Modelo_{}'.format(i): 'Modelo', 'Lin_{}'.format(i): 'Linha'})

        self.new_df = self.new_df[['QVV','jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez',
                                   'M','Modelo_M','Lin_M','G','Modelo_G','Lin_G','H','Modelo_H','Lin_H',
                                   'J','Modelo_J','Lin_J','V','Modelo_V','Lin_V','W','Modelo_W','Lin_W', 'DataArquivo', 'Ano', 'Tipo', 'Serie', 'Linha_Destino', 'País']]

        self.new_df = self.new_df.rename(columns={'País': 'Pais'})
        def check_agregado(bm, modelo, linha):
            # Verifica se 'bm' é vazio ou igual a 'NotFound'
            if bm == '' or bm == 0:
                modelo = ''
                linha = ''
            elif bm == 'NotFound':
                modelo = 'NotFound'
                linha = 'NotFound'
            else:

                # Verifica se 'modelo' é um número (float) ou igual a 'nan'
                if isinstance(modelo, (float, int)):
                    modelo = 'NotFound'
                    linha = 'NotFound'
                elif isinstance(modelo, str) and modelo.lower() == 'nan':
                    modelo = 'NotFound'
                    linha = 'NotFound'
                else:
                    linha = linha  # Não é necessário modificar linha se modelo não for vazio, numérico ou 'nan'
            return (modelo, linha)

        # Aplica a função em cada linha do DataFrame e cria duas novas colunas com os valores retornados da função
        self.new_df[['Modelo_M', 'Lin_M']] = self.new_df.apply(lambda linha: pd.Series(check_agregado(linha['M'], linha['Modelo_M'], linha['Lin_M'])), axis=1)
        self.new_df[['Modelo_G', 'Lin_G']] = self.new_df.apply(lambda linha: pd.Series(check_agregado(linha['G'], linha['Modelo_G'], linha['Lin_G'])), axis=1)
        self.new_df[['Modelo_H', 'Lin_H']] = self.new_df.apply(lambda linha: pd.Series(check_agregado(linha['H'], linha['Modelo_H'], linha['Lin_H'])), axis=1)
        self.new_df[['Modelo_J', 'Lin_J']] = self.new_df.apply(lambda linha: pd.Series(check_agregado(linha['J'], linha['Modelo_J'], linha['Lin_J'])), axis=1)
        self.new_df[['Modelo_V', 'Lin_V']] = self.new_df.apply(lambda linha: pd.Series(check_agregado(linha['V'], linha['Modelo_V'], linha['Lin_V'])), axis=1)
        self.new_df[['Modelo_W', 'Lin_W']] = self.new_df.apply(lambda linha: pd.Series(check_agregado(linha['W'], linha['Modelo_W'], linha['Lin_W'])), axis=1)

    def carrega_programa_tableview(self, df, table_view = None):
        model = QStandardItemModel()                        # Cria um modelo de dados
        model.setRowCount(df.shape[0])                      # Define o número de linhas
        model.setColumnCount(df.shape[1])                   # Define o número de colunas
        model.setHorizontalHeaderLabels(df.columns)         # Define os rótulos das colunas (cabeçalhos)
        
        for i in range(df.shape[0]):                        # Itera através das linhas
            for j in range(df.shape[1]):                    # Itera através das colunas
                item = QStandardItem(str(df.iloc[i, j]))    # Obtém o valor do DataFrame na linha i e coluna j
                item.setTextAlignment(Qt.AlignCenter)       # Centraliza o texto
                model.setItem(i, j, item)                   # Define o item na linha i e coluna j
        table_view.setModel(model)
        return table_view


    def seleciona_linha_programa(self, index):
        """
        Função para selecionar a linha na tabela e definir os valores nos LineEdits
        """
        model = self.TableView_QVV.model()               # Obtém o modelo de dados da TableView
        row = index.row()                                # Obtém a linha selecionada
        # Define os valores nos LineEdits
        self.LineEdit_QVV.setText(model.index(row, 0).data())
        self.LineEdit_M.setText(model.index(row, 13).data())
        self.LineEdit_G.setText(model.index(row, 16).data())
        self.LineEdit_H.setText(model.index(row, 19).data())
        self.LineEdit_J.setText(model.index(row, 22).data())
        self.LineEdit_V.setText(model.index(row, 25).data())
        self.LineEdit_W.setText(model.index(row, 28).data())

    def atualiza_dados_programa(self):
        """
        Função para atualizar os valores na linha selecionada do DataFrame com os valores dos LineEdits
        """
        # Atualiza a linha selecionada do DataFrame com os novos valores
        self.new_df.loc[self.new_df['QVV'] == self.LineEdit_QVV.text(), 'M'] = self.LineEdit_M.text()
        self.new_df.loc[self.new_df['QVV'] == self.LineEdit_QVV.text(), 'G'] = self.LineEdit_G.text()
        self.new_df.loc[self.new_df['QVV'] == self.LineEdit_QVV.text(), 'H'] = self.LineEdit_H.text()
        self.new_df.loc[self.new_df['QVV'] == self.LineEdit_QVV.text(), 'J'] = self.LineEdit_J.text()
        self.new_df.loc[self.new_df['QVV'] == self.LineEdit_QVV.text(), 'V'] = self.LineEdit_V.text()
        self.new_df.loc[self.new_df['QVV'] == self.LineEdit_QVV.text(), 'W'] = self.LineEdit_W.text()
        #Aqui eu tenho que Atualizar o DataFrame 'df_qvvs' com os novos valores
        if self.df_qvvs.loc[self.df_qvvs['QVV'] == self.LineEdit_QVV.text()].empty:
            #adiciona o novo registro no DataFrame
            self.df_qvvs.loc[len(self.df_qvvs)] = [self.LineEdit_QVV.text(), self.LineEdit_M.text(), self.LineEdit_G.text(), 
                                                   self.LineEdit_H.text(), self.LineEdit_J.text(), self.LineEdit_V.text(), self.LineEdit_W.text()]
        else:
            self.df_qvvs.loc[self.df_qvvs['QVV'] == self.LineEdit_QVV.text(), 'M'] = self.LineEdit_M.text()
            self.df_qvvs.loc[self.df_qvvs['QVV'] == self.LineEdit_QVV.text(), 'G'] = self.LineEdit_G.text()
            self.df_qvvs.loc[self.df_qvvs['QVV'] == self.LineEdit_QVV.text(), 'H'] = self.LineEdit_H.text()
            self.df_qvvs.loc[self.df_qvvs['QVV'] == self.LineEdit_QVV.text(), 'J'] = self.LineEdit_J.text()
            self.df_qvvs.loc[self.df_qvvs['QVV'] == self.LineEdit_QVV.text(), 'V'] = self.LineEdit_V.text()
            self.df_qvvs.loc[self.df_qvvs['QVV'] == self.LineEdit_QVV.text(), 'W'] = self.LineEdit_W.text()
        
        # Adicionar tambem no Dataframe 'self.df_cat_agr_exp' mas somente se o incial começar com QVA
        if self.LineEdit_QVV.text()[:3] == 'QVA':
            if self.LineEdit_QVV.text()[:4] == 'QVAM':
                if self.df_cat_agr_exp.loc[self.df_cat_agr_exp['QVV'] == self.LineEdit_QVV.text()].empty:
                    #adiciona o novo registro no DataFrame
                    self.df_cat_agr_exp.loc[len(self.df_cat_agr_exp)] = [self.LineEdit_QVV.text(), self.LineEdit_M.text(), "M"]
                else:
                    self.df_cat_agr_exp.loc[self.df_cat_agr_exp['QVV'] == self.LineEdit_QVV.text(), 'BM'] = self.LineEdit_M.text()
                    self.df_cat_agr_exp.loc[self.df_cat_agr_exp['QVV'] == self.LineEdit_QVV.text(), 'AGREGADO'] = "M"
            elif self.LineEdit_QVV.text()[:4] == 'QVAG':
                if self.df_cat_agr_exp.loc[self.df_cat_agr_exp['QVV'] == self.LineEdit_QVV.text()].empty:
                    #adiciona o novo registro no DataFrame
                    self.df_cat_agr_exp.loc[len(self.df_cat_agr_exp)] = [self.LineEdit_QVV.text(), self.LineEdit_G.text(), "G"]
                else:
                    self.df_cat_agr_exp.loc[self.df_cat_agr_exp['QVV'] == self.LineEdit_QVV.text(), 'BM'] = self.LineEdit_G.text()
                    self.df_cat_agr_exp.loc[self.df_cat_agr_exp['QVV'] == self.LineEdit_QVV.text(), 'AGREGADO'] = "G"
        
        # Lista de chaves
        chaves = ['M', 'G', 'H', 'J', 'V', 'W']
        # Dicionário para armazenar os resultados
        dicionario_agr = {}

        # Loop sobre as chaves
        for chave in chaves:
            # Obtenha o texto do LineEdit correspondente à chave
            texto = getattr(self, f'LineEdit_{chave}').text()
            if texto == '':
                modelo = ''
                linha = ''
            else:
                # Verifique se o texto corresponde a um valor na coluna 'BM' do DataFrame df_agr
                try:
                    modelo = self.df_agr.loc[self.df_agr['BM'] == texto, 'Modelo'].values[0]
                    linha = self.df_agr.loc[self.df_agr['BM'] == texto, 'Linha'].values[0]
                # Se não houver correspondência, defina o modelo e a linha como 'NotFound'
                except:
                    modelo = 'NotFound'
                    linha = 'NotFound'

            # Armazene os resultados no dicionário
            dicionario_agr[f'Modelo_{chave}'] = modelo
            dicionario_agr[f'Lin_{chave}'] = linha

        # Atualize a linha selecionada do DataFrame com os novos valores
        self.new_df.loc[self.new_df['QVV'] == self.LineEdit_QVV.text(), 'Modelo_M'] = dicionario_agr['Modelo_M']
        self.new_df.loc[self.new_df['QVV'] == self.LineEdit_QVV.text(), 'Lin_M'] = dicionario_agr['Lin_M']
        self.new_df.loc[self.new_df['QVV'] == self.LineEdit_QVV.text(), 'Modelo_G'] = dicionario_agr['Modelo_G']
        self.new_df.loc[self.new_df['QVV'] == self.LineEdit_QVV.text(), 'Lin_G'] = dicionario_agr['Lin_G']
        self.new_df.loc[self.new_df['QVV'] == self.LineEdit_QVV.text(), 'Modelo_H'] = dicionario_agr['Modelo_H']
        self.new_df.loc[self.new_df['QVV'] == self.LineEdit_QVV.text(), 'Lin_H'] = dicionario_agr['Lin_H']
        self.new_df.loc[self.new_df['QVV'] == self.LineEdit_QVV.text(), 'Modelo_J'] = dicionario_agr['Modelo_J']
        self.new_df.loc[self.new_df['QVV'] == self.LineEdit_QVV.text(), 'Lin_J'] = dicionario_agr['Lin_J']
        self.new_df.loc[self.new_df['QVV'] == self.LineEdit_QVV.text(), 'Modelo_V'] = dicionario_agr['Modelo_V']
        self.new_df.loc[self.new_df['QVV'] == self.LineEdit_QVV.text(), 'Lin_V'] = dicionario_agr['Lin_V']
        self.new_df.loc[self.new_df['QVV'] == self.LineEdit_QVV.text(), 'Modelo_W'] = dicionario_agr['Modelo_W']
        self.new_df.loc[self.new_df['QVV'] == self.LineEdit_QVV.text(), 'Lin_W'] = dicionario_agr['Lin_W']


        self.filtrar_radiobutton()                  # Filtra os dados na tabela
        # Salva o DataFrame atualizado no arquivo CSV
        self.df_qvvs.to_excel(r'{}/Arquivos Usados/Lista_QVVs.xlsx'.format(caminho), sheet_name='Plan1', index=False)
        self.new_df.to_csv(r'{}/Arquivos Gerados/12MPP de Agregados.csv'.format(caminho), index=False, sep=';')
        self.df_cat_agr_exp.to_excel(r'{}/Arquivos Usados/Categoria_Agregados Exportação.xlsx'.format(caminho), sheet_name='Plan1', index=False)

        QMessageBox.information(self, 'Atualização do Programa', 'Baumuster Cadastrado na QVV!"')
        self.LineEdit_QVV.setText('')
        self.LineEdit_M.setText('')
        self.LineEdit_G.setText('')
        self.LineEdit_H.setText('')
        self.LineEdit_J.setText('')
        self.LineEdit_V.setText('')
        self.LineEdit_W.setText('')

    def seleciona_linha_agregados(self, index):
        """
        Função para selecionar a linha na tabela e definir os valores nos LineEdits
        """
        model = self.TableView_Categoria_Agr.model()                # Obtém o modelo de dados da TableView
        row = index.row()                                           # Obtém a linha selecionada
        self.LineEdit_BM.setText(model.index(row, 0).data())
        self.LineEdit_Tipo_agr.setText(model.index(row, 1).data())
        self.LineEdit_Linha_agr.setText(model.index(row, 2).data())

    #repetir o mesmo processo para a tabela de exportação
    def seleciona_linha_exportacao(self, index):
        """
        Função para selecionar a linha na tabela e definir os valores nos LineEdits
        """
        model = self.TableView_Exp.model()                # Obtém o modelo de dados da TableView
        row = index.row()                                           # Obtém a linha selecionada
        self.LineEdit_Exp_Variante.setText(model.index(row, 0).data())
        self.LineEdit_Exp_BM.setText(model.index(row, 1).data())
        self.LineEdit_Exp_Agregado.setText(model.index(row, 2).data())
        self.LineEdit_Exp_Tipo.setText(model.index(row, 3).data())
        self.LineEdit_Exp_Serie.setText(model.index(row, 4).data())

    def atualiza_dados_agregados(self):
        #Aqui eu tenho que Atualizar o DataFrame 'df_qvvs' com os novos valores
        if self.df_agr.loc[self.df_agr['BM'] == self.LineEdit_BM.text()].empty:
            #adiciona o novo registro no DataFrame
            self.df_agr.loc[len(self.df_agr)] = [self.LineEdit_BM.text(), self.LineEdit_Tipo_agr.text(), self.LineEdit_Linha_agr.text()]
        else:
            self.df_agr.loc[self.df_agr['BM'] == self.LineEdit_BM.text(), 'Modelo'] = self.LineEdit_Tipo_agr.text()
            self.df_agr.loc[self.df_agr['BM'] == self.LineEdit_BM.text(), 'Linha'] = self.LineEdit_Linha_agr.text()

        #Aqui eu tenho que Atualizar o DataFrame 'df_agr' com os novos valores
        self.carrega_programa_tableview(self.df_agr, self.TableView_Categoria_Agr)           # Carrega o DataFrame na tabela
        self.df_agr.to_excel(r'{}/Arquivos Usados/Categoria_Agregados.xlsx'.format(caminho), sheet_name='Plan1', index=False)            
        self.carrega_dfs()
        self.prepara_dataframe()
        self.filtrar_radiobutton()                  # Filtra os dados na tabela

        QMessageBox.information(self, 'Atualização da Categoria', 'Novo Baumuster Cadastrado!')
        self.LineEdit_BM.setText('')
        self.LineEdit_Tipo_agr.setText('')
        self.LineEdit_Linha_agr.setText('')

    # criar uma função com a mesma funcionalidade do "atualiza_dados_agregados" só que pro arquivo de exportação
    def atualiza_dados_exportacao(self):
        #Aqui eu tenho que Atualizar o DataFrame 'df_qvvs' com os novos valores
        if self.df_AgrExp.loc[self.df_AgrExp['Variante'] == self.LineEdit_Exp_Variante.text()].empty:
            #adiciona o novo registro no DataFrame
            self.df_AgrExp.loc[len(self.df_AgrExp)] = [self.LineEdit_Exp_Variante.text(), self.LineEdit_Exp_BM.text(), self.LineEdit_Exp_Agregado.text(), self.LineEdit_Exp_Tipo.text(), self.LineEdit_Exp_Serie.text()]
        else:
            self.df_AgrExp.loc[self.df_AgrExp['Variante'] == self.LineEdit_Exp_Variante.text(), 'BM'] = self.LineEdit_Exp_BM.text()
            self.df_AgrExp.loc[self.df_AgrExp['Variante'] == self.LineEdit_Exp_Variante.text(), 'AGREGADO'] = self.LineEdit_Exp_Agregado.text()
            self.df_AgrExp.loc[self.df_AgrExp['Variante'] == self.LineEdit_Exp_Variante.text(), 'Tipo'] = self.LineEdit_Exp_Tipo.text()
            self.df_AgrExp.loc[self.df_AgrExp['Variante'] == self.LineEdit_Exp_Variante.text(), 'Serie'] = self.LineEdit_Exp_Serie.text()

        #Aqui eu tenho que Atualizar o DataFrame 'df_agr' com os novos valores
        self.carrega_programa_tableview(self.df_AgrExp, self.TableView_Exp)           # Carrega o DataFrame na tabela
        self.df_AgrExp.to_excel(r'{}/Arquivos Usados/Lista_Exportação.xlsx'.format(caminho), sheet_name='Plan1', index=False)            
        self.carrega_dfs()
        self.prepara_dataframe()
        self.filtrar_radiobutton()                  # Filtra os dados na tabela

        QMessageBox.information(self, 'Atualização do Exportação', 'Novo Baumuster Cadastrado!')
        self.LineEdit_Exp_Variante.setText('')
        self.LineEdit_Exp_BM.setText('')
        self.LineEdit_Exp_Agregado.setText('')
        self.LineEdit_Exp_Tipo.setText('')
        self.LineEdit_Exp_Serie.setText('')

    def largura_tableview(self):
        self.TableView_QVV.setColumnWidth(0, 87)
        for i in range(1, 13):
            self.TableView_QVV.setColumnWidth(i, 25)
        for i in range(13, 30):
            self.TableView_QVV.setColumnWidth(i, 50)

        self.TableView_QVV.setColumnWidth(15, 34)
        self.TableView_QVV.setColumnWidth(18, 34)
        self.TableView_QVV.setColumnWidth(21, 34)
        self.TableView_QVV.setColumnWidth(24, 34)
        self.TableView_QVV.setColumnWidth(27, 34)
        self.TableView_QVV.setColumnWidth(30, 34)
        self.TableView_Categoria_Agr.setColumnWidth(0, 100)
        self.TableView_Categoria_Agr.setColumnWidth(1, 233)
        self.TableView_Categoria_Agr.setColumnWidth(2, 100)

        self.TableView_Exp.setColumnWidth(0, 100)
        self.TableView_Exp.setColumnWidth(1, 233)
        self.TableView_Exp.setColumnWidth(2, 100)
        self.TableView_Exp.setColumnWidth(3, 100)
        self.TableView_Exp.setColumnWidth(4, 100)

    def colorir_colunas(self):
        # Obtém o modelo de dados da TableView
        model = self.TableView_QVV.model()

        dicionario_cores = {'M': (13, QColor(70,130,180),), 
                            'G': (16, QColor(218,165,32)), 
                            'H': (19, QColor(210,180,140)), 
                            'J': (22, QColor(210,180,140)), 
                            'V': (25, QColor(144,238,144)), 
                            'W': (28, QColor(144,238,144)), 
                            }
        
        # Define as cores para as colunas M, G, H, J, V, W e A
        for item in dicionario_cores:
            coluna = dicionario_cores[item][0]
            cor = dicionario_cores[item][1]
            for row in range(model.rowCount()):
                item = QStandardItem(model.index(row, coluna).data())
                item.setForeground(cor)
                model.setItem(row, coluna, item)
                item = QStandardItem(model.index(row, coluna+1).data())
                item.setForeground(cor)
                model.setItem(row, coluna+1, item)
                item = QStandardItem(model.index(row, coluna+2).data())
                item.setForeground(cor)
                model.setItem(row, coluna+2, item)                                
  

        # Define a cor vermelha para as células que contêm o valor "NotFound"
        for row in range(model.rowCount()):
            for col in range(model.columnCount()):
                index = model.index(row, col)
                if index.data() == "NotFound":
                    item = QStandardItem(index.data())
                    item.setForeground(QColor(255, 0, 0))
                    model.setItem(row, col, item)

    def filtrar_radiobutton(self):
        if self.RadioButton_NotFound.isChecked():
            self.carrega_programa_tableview(self.new_df[(self.new_df['M'] == 'NotFound') | 
                                                        (self.new_df['Modelo_M'] == 'NotFound') |
                                                        (self.new_df['G'] == 'NotFound') |
                                                        (self.new_df['Modelo_G'] == 'NotFound') |
                                                        (self.new_df['H'] == 'NotFound') |
                                                        (self.new_df['Modelo_H'] == 'NotFound') |
                                                        (self.new_df['J'] == 'NotFound') |
                                                        (self.new_df['Modelo_J'] == 'NotFound') |
                                                        (self.new_df['V'] == 'NotFound') |
                                                        (self.new_df['Modelo_V'] == 'NotFound') |
                                                        (self.new_df['W'] == 'NotFound') |
                                                        (self.new_df['Modelo_W'] == 'NotFound') |
                                                        (self.new_df['Tipo'] == 'NotFound')], self.TableView_QVV)
        else:
            self.carrega_programa_tableview(self.new_df, self.TableView_QVV)
        self.largura_tableview()
        self.colorir_colunas()

    def redimensiona_janela(self):
        # Define a largura da janela com base no índice do TabWidget
        if self.TabAgregados.currentIndex() == 0:
            largura_window = 1350
            largura_tabwidget = 1330
        elif self.TabAgregados.currentIndex() == 1:
            largura_window = 500
            largura_tabwidget = 480
        else:
            largura_window = 700
            largura_tabwidget = 680

        # Define a largura da janela
        self.setFixedWidth(largura_window)
        self.TabAgregados.setFixedWidth(largura_tabwidget)
        
    def closeEvent(self, event):
        # Salva o DataFrame atualizado no arquivo CSV
        self.df_qvvs.to_excel(r'Arquivos Usados/Lista_QVVs.xlsx', sheet_name='Plan1', index=False)
        self.new_df.to_csv(r'Arquivos Gerados/12MPP de Agregados.csv', index=False, sep=';')
        print(f'Arquivos BI/12MPP de Agregados_{self.Data_arquivo}.csv')
        self.new_df.to_csv(f'Arquivos BI/12MPP de Agregados por Veiculos_{self.Data_arquivo}.csv', index=False, sep=';')
        ############# exportações adicionais do arquivo csv: #############
        #o Primeiro irá para Controw Tower
        #self.new_df.to_csv(f'C:/Users/ccavalh/OneDrive - Daimler Truck/12MPP_Agregados_ControlTower/12MPP de Agregados por Veiculos_{self.Data_arquivo}.csv', index=False, sep=';')
        #o Segundo irá para o FTP da TL (Raul quem usará)
        #self.new_df.to_csv(f'R:/TL - Comando de Montagem - Sistemas Internos/FTP/12MPP AGREGADOS BI/12MPP de Agregados.csv', index=False, sep=';')
        self.df_to_powerbi()
        event.accept() 
        
              
    def df_to_powerbi(self):
        df_powerbi = pd.DataFrame()         #Cria um Dataframe vazio
        self.new_df['Tipo_agr'] = ''             #Adiciona Coluna chamada Tipo
        Lista_agregados = ['M', 'G', 'H', 'J', 'V', 'W']
        tipo_atual = None
        
        for item in Lista_agregados:
            df = self.new_df
            df = df.rename(columns={item: 'BM'})
            df = df.rename(columns={f'Modelo_{item}': 'Modelo'})
            df = df.rename(columns={f'Lin_{item}': 'Linha'})
            try:
                df = df[['QVV', 'jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez', 'BM', 'Modelo', 'Linha', 'DataArquivo', 'Ano', 'Tipo_agr', 'Tipo', 'Serie', 'Linha_Destino', 'Pais']]            
            except:
                pass
            if tipo_atual is None or tipo_atual != item:
                # se o campo BM for vazio
                if df['BM'].empty or df['BM'].isnull().all():
                    pass
                else:
                    df['Tipo_agr'] = item
                    tipo_atual = item            
            df_powerbi = pd.concat([df_powerbi, df], axis=0)

        df_powerbi = df_powerbi.loc[df_powerbi['BM'] != '']
        df_powerbi.to_csv(r'Arquivos Gerados/12MPP de Agregados PowerBI.csv', index=False, sep=';')
        df_powerbi.to_csv(f'Arquivos BI/12MPP de Agregados por Agregados_{self.Data_arquivo}.csv', index=False, sep=';')
        print('finalizado')
        ############# exportações adicionais do arquivo csv: #############
        #o Primeiro irá para Controw Tower
        #df_powerbi.to_csv(f'C:/Users/ccavalh/OneDrive - Daimler Truck/12MPP_Agregados_ControlTower/12MPP de Agregados por Agregados_{self.Data_arquivo}.csv', index=False, sep=';')
        
    
app = QApplication(sys.argv)    # Configura a aplicação Qt
app.setStyle('Fusion')
app.setPalette(DarkPallete().darkPalette_color)
w = MainWindow()                # Cria a janela principal
app.exec()                      # Executa a aplicação

print('Fim da Aplicação Principal')