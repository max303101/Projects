from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog, QDialog
import sys
from PyQt6 import uic
from PyQt6.QtGui import QFont

class Dialog(QDialog):
    def __init__(self):
        super().__init__()

        uic.loadUi('dialog.ui', self)
        self.pushbutton.clicked.connect(self.saveConfirmPlik)
        self.pushButton_2.clicked.connect(self.saveRejectPlik)
        self.pushButton_3.clicked.connect(self.saveCancelPlik)

class FontDialog(QDialog):
    def __init__(self, usedFont):
        super().__init__()

        uic.loadUi('czcionka.ui', self)
        self.pushButton_2.clicked.connect(self.close)
        self.lineEdit.setText(str(usedFont.pixelSize()))
        self.checkBox.setChecked(usedFont.bold())
        self.checkBox_2.setChecked(usedFont.italic())
        self.checkBox_3.setChecked(usedFont.underline())
        self.fontComboBox.setCurrentFont(usedFont)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('mainwindow.ui', self)
        self.actionZapisz.triggered.connect(self.actionZapiszPlik)
        self.actionOtw_rz.triggered.connect(self.actionOtworzPlik)
        self.actionZako_cz.triggered.connect(self.actionZakonczPlik)
        self.actionNowy.triggered.connect(self.actionNowyPlik)
        self.actionCzcinka.triggered.connect(self.actionCzcionka)
        self.font = QFont("Arial")
        self.font.setPixelSize(16)
        self.plainTextEdit.setFont(self.font) 

    def actionZapiszPlik(self):
        file = QFileDialog.getSaveFileName(self,
        "Save File", "/Users/pt21borysm/Desktop/pyqt6", "Text Files (*.txt)")
        if file[0]:
            with open(file[0], 'w') as file:
                text = self.plainTextEdit.toPlainText()
                file.write(text)
                QMessageBox.information(self, "Zapisano", "Plik został zapisany")
        

    def actionOtworzPlik(self):
        fileName = QFileDialog.getOpenFileName(self,
        "Open File", "/Users/pt21borysm/Desktop/pyqt6", "Text Files (*.txt)")
        if fileName[0]:
            with open(fileName[0], 'r') as file:
                data = file.read()
                self.plainTextEdit.setPlainText(data)

    def actionZakonczPlik(self):
        self.close()

    def actionNowyPlik(self):
        if not self.plainTextEdit.isEmpty():
            self.plainTextEdit.clear()
    
    def actionCzcionka(self):
        dialog = FontDialog(self.font)
        dialog.exec()
        self.font = dialog.fontComboBox.currentFont()
        self.font.setPixelSize(int(dialog.lineEdit.text()))
        self.font.setBold(dialog.checkBox.isChecked())
        self.font.setItalic(dialog.checkBox_2.isChecked())
        self.font.setUnderline(dialog.checkBox_3.isChecked())
        self.plainTextEdit.setFont(self.font)



app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()