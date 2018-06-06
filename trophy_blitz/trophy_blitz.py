import argparse
import time
import os
import sys
import psutil
import signal
import threading
import webbrowser
import pyautogui
import pywinauto

from PyQt5 import QtCore, QtGui, QtWidgets
from dialogs.dialog import Ui_Dialog as Form

DEFAULT_URL = 'https://monportail.ulaval.ca'
SECONDS_BEFORE_KILL = 30

def get_procs(browser):
    procs = []
    for proc in psutil.process_iter():
        try:
            procs.append(proc.as_dict(attrs=['pid', 'name']))
        except:
            pass
            
    return [proc['pid'] for proc in procs if proc['name'] == browser]
    
def get_browser_window(browser):
    print("Finding default browser process...")
    app = pywinauto.application.Application() 
    procs = get_procs(browser)
    app_window = None
    
    for proc in procs:
        try:
            app.connect(process=int(proc))
            app_window = app.top_window_()
            print("Victory!")
            break
        except:
            pass
            
    return app_window

def kill_tab(app):
    app.set_focus()
    pyautogui.hotkey('ctrl', 'w')
     
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

def unleash_chaos():
    # verify if the browser is valid
    if args.web_browser not in ['chrome', 'firefox', 'MicrosoftEdge']:
            raise Exception(args.web_browser + " is not a browser. Select among 'chrome', 'firefox', 'MicrosoftEdge'.")
            
    webbrowser.open('https://news.ycombinator.com/')
    web_browser += '.exe'
    browser_window = get_browser_window(web_browser)

    while num_opened != npages:
        webbrowser.open(url)
        num_opened += 1
        num_refreshes -= 1

        if num_opened > 1:
            t = threading.Timer(SECONDS_BEFORE_KILL, lambda: kill_tab(browser_window)).start()
        
        seconds = 0
        while seconds < num_seconds and num_opened != npages:
            status = 'Opened: {0}/{1} | Seconds left: {2:3d}\r'.format(num_opened, npages, (num_seconds - seconds))
            sys.stdout.write(status)
            sys.stdout.flush()        
            time.sleep(1)
            seconds += 1
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('logo.png'))
    dialog = QtWidgets.QDialog()
    dialog.ui = Form()
    dialog.ui.setupUi(dialog)
    dialog.exec_()
