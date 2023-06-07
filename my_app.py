import typing
from second_win import *
from instr import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout,
        QPushButton, QLabel, QLineEdit)

class MainWind(QWidget): #клас для головного вікна
    def __init__(self):
        super().__init__()
        self.set_appear() #задаємо параметри вікна
        self.initUI() #інтерфейс додатку
        self.connects() #підключаємо кнопки
        self.show() #показуємо вікно

    def set_appear(self):
        self.resize(win_width, win_height)
        self.setWindowTitle(txt_title)
        self.move(win_x, win_y)

    def initUI(self):
        self.hellotext = QLabel(txt_hello)
        self.instructions = QLabel(txt_instruction)
        self.btnnext = QPushButton(txt_next)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.hellotext, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.instructions, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.btnnext, alignment=Qt.AlignCenter)
        self.setLayout(self.main_layout)

    def next(self):
        self.tw= TestWin()
        self.hide()


    def connects(self):
        self.btnnext.clicked.connect(self.next)



app = QApplication([]) #створення додатку
main_win= MainWind()
app.exec_()