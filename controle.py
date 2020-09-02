import sqlite3
from PyQt5 import uic,QtWidgets,QtGui

conexão = sqlite3.connect('campo.bd')


def agendawindow():
	agendainte.show()

def cadastrowindow():
	cadastrointe.show()

def sair():
	agendainte.close()
	cadastrointe.close()
	interfacepri.close()
	entradareserva.close()

def saircadastro():
	cadastrointe.close()

def sair_agenda():
	agendainte.close()

def data_selecionada():
	print (agendainte.calendarWidget.selectedDate())

def nova_entrada():
	entradareserva.show()


app = QtWidgets.QApplication([])
interfacepri = uic.loadUi('interface.ui')
agendainte = uic.loadUi('agendainterface.ui')
cadastrointe = uic.loadUi('cadastrointerface.ui')
entradareserva = uic.loadUi('entradaereservas.ui')
interfacepri.show()


interfacepri.pushButtonagenda.clicked.connect(agendawindow)
interfacepri.pushButtoncadastro.clicked.connect(cadastrowindow)
interfacepri.pushButtonsair.clicked.connect(sair)
cadastrointe.pushButtonagenda_saircadastro.clicked.connect(saircadastro)
agendainte.calendarWidget.clicked.connect(data_selecionada)
agendainte.pushButtonagenda.clicked.connect(nova_entrada)
agendainte.pushButtonagenda_saircadastro.clicked.connect(sair_agenda)

app.exec()