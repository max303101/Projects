from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog
import sys
import random
from PyQt6 import uic

class Dialog1(QDialog):
    def __init__(self, genPass):
        super().__init__()
        uic.loadUi('dialog1.ui', self)
        self.pushButton.clicked.connect(self.close)
        self.label.setText(genPass)

class Dialog2(QDialog):
    def __init__(self, name, surname, station, password):
        super().__init__()
        uic.loadUi('dialog2.ui', self)
        self.pushButton.clicked.connect(self.close)
        self.label.setText(f"Imię: {name} Nazwisko: {surname}, Stanowisko: {station}, Hasło: {password}")

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mainwindow.ui', self)
        self.pushButton.clicked.connect(self.onClickGenerate)
        self.pushButton_2.clicked.connect(self.onClickConfirm)
        self.paletaL = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.paletaC = "0123456789"
        self.paletaZ = "!@#$%^&*()_+-="
        self.paleta = ""
        self.outPassword = ""
        self.symbolAmount = 0


    def onClickGenerate(self):
        self.paleta = ""
        self.outPassword = ""
        self.symbolAmount = self.lineEdit_3.text()
        if(self.checkBox.isChecked()):
            self.paleta += self.paletaL
        if(self.checkBox_2.isChecked()):
            self.paleta += self.paletaC
        if(self.checkBox_3.isChecked()):
            self.paleta += self.paletaZ

        # Generate random password
        for i in range(int(self.symbolAmount)):
            self.outPassword += self.paleta[random.randint(0, len(self.paleta) - 1)]
        dialog1 = Dialog1(self.outPassword)
        dialog1.exec()





    def onClickConfirm(self):
        name = self.lineEdit.text()
        surname = self.lineEdit_2.text()
        station = self.comboBox.currentText()
        password = self.outPassword
        dialog2 = Dialog2(name, surname, station, password)
        dialog2.exec()
        


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()