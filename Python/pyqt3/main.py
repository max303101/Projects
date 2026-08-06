from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
import re
import math
import json
from form import Ui_Form


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.onConfirm)

        self.file = open("slow.txt")
        self.dane = json.loads(self.file.read())
        self.file.close()



        self.ui.label.setText(str(self.dane["margarita"][0]) + " zł\n" + str(self.dane["margarita"][1]) + " cm średnicy\n" + str(self.dane["margarita"][2]) + " cm2")

        self.ui.label_2.setText(str(self.dane["margarita"][0]) + " zł\n" + str(self.dane["margarita"][1]) + " cm średnicy\n" + str(self.dane["margarita"][2]) + " cm2")

        self.ui.comboBox.currentTextChanged.connect(self.onChange1)
        self.ui.comboBox_2.currentTextChanged.connect(self.onChange2)

    def onConfirm(self):
        sred = round(int(self.ui.lineEdit_2.text()) * int(self.ui.lineEdit_2.text()) /2 * math.pi)
        self.dane[self.ui.lineEdit.text()] = [self.ui.lineEdit_2.text(), self.ui.lineEdit_3.text(), str(sred), 0]
        self.ui.comboBox.clear()
        self.ui.comboBox_2.clear()
        for key in self.dane.keys():
            self.ui.comboBox.addItem(key)
            self.ui.comboBox_2.addItem(key)
        self.file = open("slow.txt", "w")
        json.dump(self.dane, self.file)
        self.file.close()


    def onChange1(self):
        text = self.ui.comboBox.currentText()
        self.ui.label.setText(str(self.dane[text][0]) + " zł\n" + str(self.dane[text][1]) + " cm średnicy\n" + str(self.dane[text][2]) + " cm2")
        

    def onChange2(self):
        text = self.ui.comboBox_2.currentText()
        self.ui.label_2.setText(str(self.dane[text][0]) + " zł\n" + str(self.dane[text][1]) + " cm średnicy\n" + str(self.dane[text][2]) + " cm2")



app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()