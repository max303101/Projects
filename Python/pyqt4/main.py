from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox
import sys
import re
import math
import json
import random
from PyQt6 import uic

class Dialog(QDialog):
    def __init__(self):
        super().__init__()



class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("mainwindow.ui", self)
        self.actionLiniowa.triggered.connect(self.onActionLiniowa)
        self.pushButton.clicked.connect(self.onClick)


    def onActionLiniowa(self):
        dialog = Dialog()
        dialog.exec()
        x = int(self.lineEdit.text())
        a = int(self.lineEdit_2.text())
        b = int(self.lineEdit_3.text())
        if a > 0:
            dialog.label_3.setText("Funkcja jest: rosnąca")
        elif a < 0:
            dialog.label_3.setText("Funkcja jest: malejąca")
        elif a == 0:
            dialog.label_3.setText("Funkcja jest: stała")
        dialog.label.setText("y = " + a + "x + " + b)
        dialog.label_2.setText("Dla x: " + str(x) + " y: " + str(a*x + b))

    def onClick(self):

        dialog = QMessageBox()
        
        dialog.exec()


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()