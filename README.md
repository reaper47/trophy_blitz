# Trophy Blitz

Need to automate refreshing a web page hundreds of times to receive an achievement? Well, this app's got you covered. Trophy Blitz is a PyQt5 Python2/3 application used to open a web page a number of times on a set interval. 

Unfortunately, this program solely works under Windows as it searches for processes the Windows way. But hey! Not all hope is lost. If there is a single demand for it to work under Linux, I will make it work for this godlike OS.

## Setup

1. If not already done, download and install [Python 3][0] or [Python 2.7][1].
1. From PowerShell or a DOS, run the following command to install the dependencies:

    - For Python 2.7: `python -m pip install python-qt5 psutil pyautogui pywinauto`
    
    - For Python 3: `python -m pip install pyqt5 psutil pyautogui pywinauto`
    
1. Under the `trophy_blitz` subdirectory, run `python main.py`. You can also double click `main.py`.
1. Select your parameters.
1. Press OK and let the blitzing start. You can cancel the ongoing operation at any time by pressing the `Abort` button.


### Happy Blitzing :D

[0]: https://www.python.org/ftp/python/3.6.5/python-3.6.5-amd64.exe
[1]: https://www.python.org/ftp/python/2.7.15/python-2.7.15.amd64.msi
