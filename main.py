import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from window import Window, UrlInput, Button, Label
from style import setupTheme
from downloader import downlaod, validator_url



if __name__ == '__main__':
    # cria app e janela
    app = QApplication(sys.argv)
    setupTheme()
    window = Window()
    
    # display
    label = Label("Insira a url abaixo: ")
    url = UrlInput()  
    button = Button("Baixar")

    # Layout
    window.addWidgetToLayout(label, 1, 1, 1,2)
    window.addWidgetToLayout(button, 2, 2)
    window.addWidgetToLayout(url, 2, 1)
    
    # texturl
    text = url.urlText
    
    # exec
    if text() is not None:
        button.clickedButtonConnect(lambda: downlaod(text()))
    window.show()
    app.exec()
