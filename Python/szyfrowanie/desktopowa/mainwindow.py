from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(758, 410)
        Form.setStyleSheet("background-color: rgb(95, 158, 160);")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 141, 31))
        self.label_2.setStyleSheet("color: rgb(250, 235, 215);\n"
"font: 14pt \"Segoe UI\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(470, 30, 201, 31))
        self.label_3.setStyleSheet("color: rgb(250, 235, 215);\n"
"font: 14pt \"Segoe UI\";")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(470, 200, 201, 41))
        self.label_5.setStyleSheet("color: rgb(250, 235, 215);\n"
"font: 14pt \"Segoe UI\";")
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(parent=Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 110, 191, 161))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(290, 110, 75, 24))
        self.pushButton.setStyleSheet("background-color: rgb(173, 216, 230);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 270, 75, 24))
        self.pushButton_2.setStyleSheet("background-color: rgb(173, 216, 230);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 350, 181, 24))
        self.pushButton_3.setStyleSheet("background-color: rgb(173, 216, 230);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(480, 80, 181, 101))
        self.label.setMinimumSize(QtCore.QSize(181, 101))
        self.label.setMaximumSize(QtCore.QSize(181, 101))
        self.label.setStyleSheet("\n"
"color: rgb(240, 248, 255);\n"
"border-radius: 25px;\n"
"border: 1px solid rgb(250, 235, 215);")
        self.label.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label.setLineWidth(5)
        self.label.setMidLineWidth(5)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(480, 260, 191, 111))
        self.label_4.setStyleSheet("color: rgb(240, 248, 255);\n"
"border-radius: 25px;\n"
"border: 1px solid rgb(250, 235, 215);")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Podaj tekst"))
        self.label_3.setText(_translate("Form", "Tekst zaszyfrowany"))
        self.label_5.setText(_translate("Form", "Tekst odszyfrowany"))
        self.pushButton.setText(_translate("Form", "Zaszyfruj"))
        self.pushButton_2.setText(_translate("Form", "Odszyfruj"))
        self.pushButton_3.setText(_translate("Form", "Zapisz szyfr w pliku"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_4.setText(_translate("Form", "TextLabel"))
