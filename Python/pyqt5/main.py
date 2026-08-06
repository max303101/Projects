from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox
import sys
import math
from PyQt6 import uic
import pyqtgraph

class Dialog(QDialog):
    def __init__(self):
        super().__init__()

        uic.loadUi('niewiem.ui', self)
        self.pushButton.clicked.connect(self.close)

    

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('mainwindow.ui', self)
        self.actionkwadratowa.triggered.connect(self.onActionKwadratowa)
        self.a = 0
        self.b = 0
        self.c = 0
        self.mainWidget = pyqtgraph.PlotWidget()

    def onActionKwadratowa(self):
        dialog = Dialog()

        dialog.exec()
        self.a = int(dialog.lineEdit_a.text())
        self.b = int(dialog.lineEdit_b.text())
        self.c = int(dialog.lineEdit_c.text())
        if(self.a > 0 or self.a < 0):
            self.x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        elif(self.a == 0):
            self.x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.y = []
        for i in self.x:
            self.wyn = self.a * pow(i, 2) + self.b * i + self.c
            self.y.append(self.wyn)

        self.delta = pow(self.b, 2) + 4 * self.a * self.c
        
        
        self.mainWidget.plot(self.x, self.y)
        self.setCentralWidget(self.mainWidget)
        if self.delta > 0:
            self.x1 = (-self.b + math.sqrt(self.delta)) / (2 * self.a)
            self.x2 = (-self.b - math.sqrt(self.delta)) / (2 * self.a)
            QMessageBox.information(self, "Miejsca zerowe", "x1: " + str(self.x1) + "\nx2: " + str(self.x2))
        elif self.delta == 0:
            self.x1 = -self.b / (2 * self.a)
            QMessageBox.information(self, "Miejsce zerowe", "x: " + str(self.x1))
        elif self.delta < 0:
            QMessageBox.information(self, "Błąd", "Brak pierwiastków równania kwadratowego.")


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()