from PyQt6.QtWidgets import QApplication, QWidget
import sys
import random
import os
from formul import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Szyfrowanie. Wykonane przez: pt21borysm")
        self.ui.pushButton.clicked.connect(self.onClick1)
        self.ui.pushButton_2.clicked.connect(self.onClick2)

    def onClick1(self):
        def szyfruj(ciag):
            ind = []
            i = 0
            napis = []
            for x in ciag:
                ind.append(i)
                i += 1
                napis.append(x)
            random.shuffle(ind)
            o = 0
            szyfNapis = ""
            for n in ind:
                szyfNapis += napis[n]
            #print(szyfNapis)
            
            if os.path.exists("file.txt"):
                os.remove("file.txt")
            else:
                open("file.txt", "x")
            with open("file.txt", "w") as f:
                f.write(szyfNapis + "\n")
                for e in ind:
                    f.write(str(e) + ",")
                f.close()
            return szyfNapis
        
        strin = self.ui.plainTextEdit.toPlainText()
        self.ui.label.setText(szyfruj(strin))

    def onClick2(self):
        def deszyfruj():
            with open("file.txt", "r") as f:
                napis = f.readline()
                index = f.readline()
            inde = str(index)
            ind = inde.split(",")
            ind.pop(ind.__len__()-1)
            indTab = []
            for e in ind:
                indTab.append(int(e))
            tabDesz = ""
            for e in range(indTab.__len__()):
                tabDesz += napis[indTab.index(e)]
            return tabDesz
        self.ui.label_4.setText(deszyfruj())
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()