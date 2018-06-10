import sys
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt
from utils import unleash_chaos
from trophy_gui import Ui_MainWindow

class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.Exit.rejected.connect(self.exit_app)
        self.Exit.accepted.connect(self.goto_blitz)
        self.abort_blitz.rejected.connect(self.goto_config)

        self.countdown = 1

    def exit_app(self):
        QCoreApplication.exit()
        
    def goto_blitz(self):
        browser = self.browser_combobox.currentText()
        url = self.url_edit.displayText()
        refreshes = self.refreshes_spinbox.value()
        interval = self.interval_spinbox.value()

        if url == '':
            url = 'https://www.google.com/'

        self.lcdNumber.setProperty("value", interval*60)
        self.num_refreshes_left.setText('Opened 1/{0} pages.'.format(refreshes))
        self.blitz_thread = threading.Thread(target=unleash_chaos, args=(browser, url, refreshes, interval, self.lcdNumber, self.num_refreshes_left))
        self.blitz_thread.start()

        self.stackedWidget.setCurrentIndex(1)
        
    def goto_config(self):
        self.num_refreshes_left.setText('Killing the blitz...')
        self.blitz_thread.do_run = False
        self.blitz_thread.join()
        self.stackedWidget.setCurrentIndex(0)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
