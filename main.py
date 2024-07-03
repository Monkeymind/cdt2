from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,QHBoxLayout,QComboBox,QLabel,QTextEdit,QLineEdit,QFormLayout 
from PySide6.QtCore import Qt

from baseFrame import Window
import sys
import qdarktheme
app= QApplication(sys.argv)


if __name__ == '__main__':
   
    #mainWindow=ButtonClass()
    w1=Window()

    #mainWindow.mainLayout(w1.box())


    #mainWindow.show()
    w1.show()
    app.exec()

