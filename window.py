from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QMainWindow, QWidget, QGridLayout,
                               QLineEdit, QPushButton, QLabel)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # titulo
        self.setWindowTitle("Youtube Downloader")

        # Layout
        self.central_widget = QWidget()
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)
        self.setCentralWidget(self.central_widget)
        # self.adjustFixedSize()

    # fixar tamanho da tela
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    # adicionar widgets ao layout
    def addWidgetToLayout(self, widget: QWidget, *args, **kwargs):
        self.grid_layout.addWidget(widget, *args, **kwargs)



class Label(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        
    def configStyle(self):
        self.setStyleSheet('font-size: 20px;')

    
class UrlInput(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet('font-size: 25px')
        self.setPlaceholderText('url')
    
    def urlText(self):
        text = self.text()
        return text

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        
    def configStyle(self):
        font = self.font()
        font.setPixelSize(25)
        self.setFont(font)
        self.setMinimumSize(40, 40)
        self.setProperty('cssClass', 'specialButton')
         
    def clickedButtonConnect(self, func):
        self.clicked.connect(func)


