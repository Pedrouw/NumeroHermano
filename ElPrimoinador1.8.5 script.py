import time
from types import MethodType
from PyQt5 import QtCore, QtGui, QtWidgets
from subprocess import call
import os
import sys

def emercode():
    call([r'C:\Users\Javiera Letelier\PycharmProjects\NumeroHermano\Beta del Programa\run.bat'])
    path = sys.argv[0].replace(" ", "-")
    os.path.dirname(sys.argv[0])
    exit()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 581)
        MainWindow.setFixedSize(792, 581)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 341, 51))

        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)

        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

        self.pushButton.setGeometry(QtCore.QRect(310, 200, 171, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.primath)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 120, 151, 61))

        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 120, 151, 61))

        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)

        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(170, 270, 441, 261))
        self.textBrowser.setObjectName("textBrowser")


        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(240, 130, 91, 51))

        font = QtGui.QFont()
        font.setPointSize(12)

        self.spinBox.setFont(font)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox.setMaximum(999999)
        self.spinBox.setProperty("value", 0)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(540, 130, 91, 51))

        font = QtGui.QFont()
        font.setPointSize(12)

        self.spinBox_2.setFont(font)
        self.spinBox_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox_2.setObjectName("spinBox_2")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def primath(self):
        num1 = self.spinBox.value()
        num2 = self.spinBox_2.value()
        cont = 0
        result = []
        for i in range(num1, num2 + 1):
            primos = True
            for j in range (2, 10):
                if i == j:
                    break
                elif i % j == 0:
                    primos = False
                else:
                    continue
            if primos:
                result.append(i) 
                cont += 1

        if num1 >= num2:
            while num1 != 33 and num2 != 12:
                self.textBrowser.append("El primer número indicado debe ser menor")
                break
            if num1 == 33 and num2 == 12:
                emercode()
        else:
            self.textBrowser.append(str(result))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "El Primoinador"))
        self.label.setText(_translate("MainWindow", "El Primoinador!"))
        self.pushButton.setText(_translate("MainWindow", "Encontrar primos"))
        self.label_2.setText(_translate("MainWindow", "Desde el:"))
        self.label_3.setText(_translate("MainWindow", "Hasta el:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
