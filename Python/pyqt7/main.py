from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys
from PyQt6 import uic


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mainwindow.ui', self)
        self.actionReset.triggered.connect(self.onActionReset)
        self.actionZamknij.triggered.connect(self.close)
        self.currentPlayer = "O"

        self.mapa = [
            [self.pushButton_00, self.pushButton_01, self.pushButton_02],
            [self.pushButton_10, self.pushButton_11, self.pushButton_12],
            [self.pushButton_20, self.pushButton_21, self.pushButton_22]]

        self.pushButton_00.clicked.connect(self.on_button_pressed_00)
        self.pushButton_01.clicked.connect(self.on_button_pressed_01)
        self.pushButton_02.clicked.connect(self.on_button_pressed_02)
        self.pushButton_10.clicked.connect(self.on_button_pressed_10)
        self.pushButton_11.clicked.connect(self.on_button_pressed_11)
        self.pushButton_12.clicked.connect(self.on_button_pressed_12)
        self.pushButton_20.clicked.connect(self.on_button_pressed_20)
        self.pushButton_21.clicked.connect(self.on_button_pressed_21)
        self.pushButton_22.clicked.connect(self.on_button_pressed_22)

    def on_button_pressed_00(self):
        self.onButtonPress(self.pushButton_00)

    def on_button_pressed_01(self):
        self.onButtonPress(self.pushButton_01)

    def on_button_pressed_02(self):
        self.onButtonPress(self.pushButton_02)

    def on_button_pressed_10(self):
        self.onButtonPress(self.pushButton_10)

    def on_button_pressed_11(self):
        self.onButtonPress(self.pushButton_11)

    def on_button_pressed_12(self):
        self.onButtonPress(self.pushButton_12)

    def on_button_pressed_20(self):
        self.onButtonPress(self.pushButton_20)

    def on_button_pressed_21(self):
        self.onButtonPress(self.pushButton_21)

    def on_button_pressed_22(self):
        self.onButtonPress(self.pushButton_22)

    def onButtonPress(self, button):
        if button.text() == "":
            button.setText(self.currentPlayer)
            button.setEnabled(False)
            self.isAllCovered += 1
            if self.checkVictory()== "":
                if(self.currentPlayer == "O"):
                    self.currentPlayer = "X"
                else:
                    self.currentPlayer = "O"
            elif(self.checkVictory() == "Remis"):
                self.label.setText("Remis")
                self.pushButton_00.setEnabled(False)
                self.pushButton_01.setEnabled(False)
                self.pushButton_02.setEnabled(False)
                self.pushButton_10.setEnabled(False)
                self.pushButton_11.setEnabled(False)
                self.pushButton_12.setEnabled(False)
                self.pushButton_20.setEnabled(False)
                self.pushButton_21.setEnabled(False)
                self.pushButton_22.setEnabled(False)
            else:
                button.setEnabled(False)
                self.label.setText("Zwycięża " + self.currentPlayer)
                self.pushButton_00.setEnabled(False)
                self.pushButton_01.setEnabled(False)
                self.pushButton_02.setEnabled(False)
                self.pushButton_10.setEnabled(False)
                self.pushButton_11.setEnabled(False)
                self.pushButton_12.setEnabled(False)
                self.pushButton_20.setEnabled(False)
                self.pushButton_21.setEnabled(False)
                self.pushButton_22.setEnabled(False)

    def checkVictory(self):
        for i in range(3):
            if self.mapa[i][0].text() == self.mapa[i][1].text() == self.mapa[i][2].text() != "":
                return self.mapa[i][0].text()

        for j in range(3):
            if self.mapa[0][j].text() == self.mapa[1][j].text() == self.mapa[2][j].text() != "":
                return self.mapa[0][j].text()
        if self.mapa[0][0].text() == self.mapa[1][1].text() == self.mapa[2][2].text() != "":
            return self.mapa[0][0].text()
        if self.mapa[0][2].text() == self.mapa[1][1].text() == self.mapa[2][0].text() != "":
            return self.mapa[0][2].text()
                    
        if self.mapa[0][0].text() and self.mapa[0][1].text() and self.mapa[0][2].text() and self.mapa[1][0] and self.mapa[1][1] and self.mapa[1][2] and self.mapa[2][0] and self.mapa[2][1] and self.mapa[2][2] != "":
            return "Remis"

        return ""

    def onActionReset(self):
        self.pushButton_00.setText("")
        self.pushButton_01.setText("")
        self.pushButton_02.setText("")
        self.pushButton_10.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.pushButton_20.setText("")
        self.pushButton_21.setText("")
        self.pushButton_22.setText("")
        self.pushButton_00.setEnabled(True)
        self.pushButton_01.setEnabled(True)
        self.pushButton_02.setEnabled(True)
        self.pushButton_10.setEnabled(True)
        self.pushButton_11.setEnabled(True)
        self.pushButton_12.setEnabled(True)
        self.pushButton_20.setEnabled(True)
        self.pushButton_21.setEnabled(True)
        self.pushButton_22.setEnabled(True)
        self.label.setText("")
        self.currentPlayer = "O"


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()