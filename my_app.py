from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout,
        QPushButton, QLabel, QLineEdit)

app = QApplication([])
window = QWidget()
window.show()
app.exec_()