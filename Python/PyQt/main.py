from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
from form import Ui_Form

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.click)

    def click(self):
        self.ui.label.setText("Button Clicked!")


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()