# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout, QGridLayout, QVBoxLayout

app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 80px')

botao2 = QPushButton('Botão dois')
botao2.setStyleSheet('font-size: 40px')

botao3 = QPushButton('Botão tres')
botao3.setStyleSheet('font-size: 40px')

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 2, 1)
layout.addWidget(botao3, 3, 1)

central_widget.show()

app.exec()
####

