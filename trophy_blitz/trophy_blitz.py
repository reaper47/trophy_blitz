import argparse
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from dialogs.dialog import Ui_Dialog as Form

DEFAULT_URL = 'https://monportail.ulaval.ca'
     
# set up an argument parser
parser = argparse.ArgumentParser(description='Open a web page periodically')
parser.add_argument('-u', '--url', dest='url', default=DEFAULT_URL, help='url of the web page to open (default: ' + DEFAULT_URL)
parser.add_argument('-i', '--interval', dest='interval', default=1, help='time before opening a new page (default: 1 minute)')
parser.add_argument('-n', '--num-refreshes', dest='num_refreshes', default=1, help='total number of pages to open')
parser.add_argument('-w', '--webbrowser', dest='web_browser', default='chrome', help='default web browser (options: chrome, firefox, MicrosoftEdge')

# get the arguments
args = parser.parse_args()
url = args.url
num_refreshes = int(args.num_refreshes)
npages = num_refreshes
num_opened = 0
interval = int(args.interval)
num_seconds = interval*60
web_browser = args.web_browser
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('logo.png'))
    dialog = QtWidgets.QDialog()
    dialog.ui = Form()
    dialog.ui.setupUi(dialog)
    dialog.exec_()
