import sys

from PyQt5.QtWidgets import QApplication
from qtpy import QtWidgets

from interfas import Ui_ElVirus

app = QApplication(sys.argv)

window = QtWidgets.QMainWindow()

ui = Ui_ElVirus()
ui.setupUi(window)
window.show()

sys.exit(app.exec_())
