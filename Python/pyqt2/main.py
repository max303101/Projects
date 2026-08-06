from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
import re
from form import Ui_Form

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.onConfirm)

    def onConfirm(self):
        email = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        password_confirm = self.ui.lineEdit_3.text()
        if(re.search("[a-z](@gmail.com)", email) != None):
            if(password == password_confirm):
                self.ui.label_5.setText("Witaj " + email)
                self.ui.label_5.adjustSize()
            else:
                self.ui.label_5.setText("Hasła nie pasują do siebie!")
                self.ui.label_5.adjustSize()
        else:
            self.ui.label_5.setText("Nieprawidłowy email!")
            self.ui.label_5.adjustSize()

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()