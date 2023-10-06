from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem 
from PyQt5 import  QtWidgets
import sys
from PyQt5.QtCore import QTimer, QTime, QDate
from cronometro import Ui_MainWindow
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label_vazia.setText('00:00:00')
        self.ui.btn_iniciar.clicked.connect(self.iniciar_tempo)
        self.ui.btn_finalizar.clicked.connect(self.finalizar)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.atualizar_tempo)
        self.horas = 0
        self.segundos = 0
        self.tempo_trabalho = 0
        self.pausa_descanso = 0
        self.pausa_banheiro = 0
        self.pausa_almoco = 0
        self.pausa_servico_domestico = 0
        self.start_time = False
        self.banco = sqlite3.connect('sistema_de_ponto.db')
        self.cursor = self.banco.cursor()
        data_atual = QDate.currentDate().toString('yyyy-MM-dd')
        self.cursor.execute("CREATE TABLE IF NOT EXISTS banco (data DATE PRIMARY KEY, tempo_trabalho TEXT, pausa_descanso TEXT, pausa_banheiro TEXT, pausa_almoco TEXT, pausa_servico_domestico TEXT)")
        self.cursor.execute("SELECT * FROM banco WHERE data = ?", (data_atual,))
        registro = self.cursor.fetchone()

        # checa se a data atual já existe no banco, caso não exista será criada uma nova linha
        if registro is None:
            # Se não existe, insira os dados
            self.cursor.execute("INSERT INTO banco (data, tempo_trabalho, pausa_descanso, pausa_banheiro, pausa_almoco, pausa_servico_domestico) VALUES (?, ?, ?, ?, ?, ?)",
                        (data_atual, "00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:00:00"))
            
            # Salvar as alterações no banco de dados
            self.banco.commit()
        
        # coloca todos os dados de banco na tabela de relatorios
        self.cursor.execute("SELECT * FROM banco")
        dados = self.cursor.fetchall()
        if dados:
            self.ui.tabela.setRowCount(len(dados))
            self.ui.tabela.setColumnCount(len(dados[0])) 

            # Preencha a tabela com os dados da consulta SQL
            for linha, registro in enumerate(dados):
                for coluna, valor in enumerate(registro):
                    item = QTableWidgetItem(str(valor))
                    self.ui.tabela.setItem(linha, coluna, item)

            self.ui.tabela.update()
            self.ui.tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        

    def finalizar(self):
        if self.start_time == True:
            self.start_time = False
            self.timer.stop()
            index = self.ui.combo.currentIndex()
            opcao = self.ui.combo.itemText(index)
            tempo_atual = self.ui.label_vazia.text()

            data_atual = QDate.currentDate().toString('yyyy-MM-dd')
            
            
            coluna = None
            if opcao == 'Trabalho':
                coluna = 'tempo_trabalho'
            elif opcao == 'Pausa Descanso':
                coluna = 'pausa_descanso'
            elif opcao == 'Pausa Banheiro':
                coluna = 'pausa_banheiro'
            elif opcao == 'Pausa Almoço':
                coluna = 'pausa_almoco'
            elif opcao == 'Pausa Serviço doméstico':
                coluna = 'pausa_servico_domestico'

            tempo_atual_objeto = QTime.fromString(tempo_atual)
            segundos = tempo_atual_objeto.second() + (tempo_atual_objeto.minute() * 60) + (tempo_atual_objeto.hour() * 3600)

            # pegando dados da data atual
            self.cursor.execute(f'SELECT * FROM banco WHERE data = "{data_atual}"')
            registro = self.cursor.fetchone()
            
            
            # Obtém o tempo atual na coluna
            if coluna == "tempo_trabalho":           
                tempo_atual_na_coluna = QTime.fromString(registro[1])

                # Soma o tempo atual ao novo tempo
                novo_tempo = tempo_atual_na_coluna.addSecs(segundos)
            
                # Formata o novo tempo no formato "00:00:00"
                novo_tempo_formatado = novo_tempo.toString("hh:mm:ss")
                
                # Atualiza o registro existente com o novo tempo
                self.cursor.execute(f'UPDATE banco SET {coluna} = "{novo_tempo_formatado}" WHERE data = "{data_atual}"')
                self.banco.commit()

            if coluna == "pausa_descanso":
                tempo_atual_na_coluna = QTime.fromString(registro[2])

                # Soma o tempo atual ao novo tempo
                novo_tempo = tempo_atual_na_coluna.addSecs(segundos)
            
                # Formata o novo tempo no formato "00:00:00"
                novo_tempo_formatado = novo_tempo.toString("hh:mm:ss")
                
                # Atualiza o registro existente com o novo tempo
                self.cursor.execute(f'UPDATE banco SET {coluna} = "{novo_tempo_formatado}" WHERE data = "{data_atual}"')
                self.banco.commit()
                
            if coluna == "pausa_banheiro":
                tempo_atual_na_coluna = QTime.fromString(registro[3])

                # Soma o tempo atual ao novo tempo
                novo_tempo = tempo_atual_na_coluna.addSecs(segundos)
            
                # Formata o novo tempo no formato "00:00:00"
                novo_tempo_formatado = novo_tempo.toString("hh:mm:ss")
                
                # Atualiza o registro existente com o novo tempo
                self.cursor.execute(f'UPDATE banco SET {coluna} = "{novo_tempo_formatado}" WHERE data = "{data_atual}"')
                self.banco.commit()
            if coluna == "pausa_almoco":
                tempo_atual_na_coluna = QTime.fromString(registro[4])

                # Soma o tempo atual ao novo tempo
                novo_tempo = tempo_atual_na_coluna.addSecs(segundos)
            
                # Formata o novo tempo no formato "00:00:00"
                novo_tempo_formatado = novo_tempo.toString("hh:mm:ss")
                
                # Atualiza o registro existente com o novo tempo
                self.cursor.execute(f'UPDATE banco SET {coluna} = "{novo_tempo_formatado}" WHERE data = "{data_atual}"')
                self.banco.commit()
            if coluna == "pausa_servico_domestico":
                tempo_atual_na_coluna = QTime.fromString(registro[5])

                # Soma o tempo atual ao novo tempo
                novo_tempo = tempo_atual_na_coluna.addSecs(segundos)
            
                # Formata o novo tempo no formato "00:00:00"
                novo_tempo_formatado = novo_tempo.toString("hh:mm:ss")
                
                # Atualiza o registro existente com o novo tempo
                self.cursor.execute(f'UPDATE banco SET {coluna} = "{novo_tempo_formatado}" WHERE data = "{data_atual}"')
                self.banco.commit()
            

            self.banco.commit()

            # atualiza o registro existente com novos dados
            self.cursor.execute("SELECT * FROM banco")
            dados = self.cursor.fetchall()

            self.ui.tabela.setRowCount(len(dados))
            self.ui.tabela.setColumnCount(len(dados[0])) 

            # Preencha a tabela com os dados da consulta SQL
            for linha, registro in enumerate(dados):
                for coluna, valor in enumerate(registro):
                    item = QTableWidgetItem(str(valor))
                    self.ui.tabela.setItem(linha, coluna, item)

            self.ui.tabela.update()
            self.ui.tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


            mensagem_box = QMessageBox()
            mensagem_box.setWindowTitle('Pausa Finalizada')
            mensagem_box.setText(f"Pausa {opcao} Finalizada, pode trocar de pausa agora")
            mensagem_box.exec_()
        else:
            mensagem_box = QMessageBox()
            mensagem_box.setWindowTitle('Erro')
            mensagem_box.setText("Você precisa estar em uma pausa para finalizar")
            mensagem_box.exec_()

    def formatar_tempo(self, segundos):
        horas = segundos // 3600
        minutos = (segundos % 3600) // 60
        segundos = segundos % 60
        return f"{horas:02}:{minutos:02}:{segundos:02}"

    def pausar_tempo(self):
        self.timer.stop()

    def iniciar_tempo(self):
        if self.start_time == False:
            self.start_time = True
            self.timer.stop()
            self.segundos = 0
            self.atualizar_tempo()
            self.timer.start(1000)
            mensagem_box = QMessageBox()
            mensagem_box.setWindowTitle('Tempo iniciado')
            mensagem_box.setText("Tempo iniciado com sucesso")
            mensagem_box.exec_()
        else:
            mensagem_box = QMessageBox()
            mensagem_box.setWindowTitle('Tempo já iniciado')
            mensagem_box.setText("O tempo já foi iniciado")
            mensagem_box.exec_()
        

    def atualizar_tempo(self):
        self.segundos += 1
        minutos = self.segundos // 60
        segundos = self.segundos % 60
        horas = minutos // 60
        minutos %= 60
        
        tempo_formatado = f"{horas:02}:{minutos:02}:{segundos:02}"
        self.ui.label_vazia.setText(tempo_formatado)
    

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
