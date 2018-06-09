import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt

from trophy_gui import Ui_MainWindow

class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.Exit.rejected.connect(self.exit_app)
        self.Exit.accepted.connect(self.goto_blitz)
        self.abort_blitz.rejected.connect(self.goto_config)

    def exit_app(self):
        QCoreApplication.exit()
        
    def goto_blitz(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def goto_config(self):
        self.stackedWidget.setCurrentIndex(0)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

