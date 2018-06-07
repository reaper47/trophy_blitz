from PyQt5 import QtCore, QtGui, QtWidgets
from utils import unleash_chaos_gui

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        self.line_number = 1
    
        Dialog.setObjectName("Dialog")
        Dialog.resize(389, 157)
        self.gridlayout = QtWidgets.QGridLayout(Dialog)
        self.gridlayout.setObjectName("gridlayout")

        self.browser_label = self.add_label(Dialog, "browser_label")
        self.browser = self.add_combobox(Dialog, ["Firefox", "Chrome", "Edge"])
        
        self.url = self.add_label(Dialog, "url")
        self.userEdit = self.add_line_edit(Dialog, "userEdit", "https://news.ycombinator.com/news")
       
        self.num_refreshes = self.add_label(Dialog, "num_refreshes")
        self.num_refreshes_edit = self.add_spinbox(Dialog, 1, "num_refreshes_edit")
       
        self.interval = self.add_label(Dialog, "interval")
        self.interval_edit = self.add_spinbox(Dialog, 1, "interval_edit")
        
        self.retranslateUi(Dialog)
        
        self.button_box = self.add_ok_cancel_button_box(Dialog, 'button_box', 'Blitz It', 'Exit')
        self.button_box.accepted.connect(self.blitz_it)
        self.button_box.rejected.connect(self.exit)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def add_label(self, dialog, text):
        label = QtWidgets.QLabel(dialog)
        label.setObjectName(text)
        self.gridlayout.addWidget(label, self.line_number, 0, 1, 1)
        return label
        
    def add_combobox(self, dialog, items):
        combobox = QtWidgets.QComboBox(dialog)
        combobox.addItems(items)
        self.gridlayout.addWidget(combobox, self.line_number, 1, 1, 1)
        self.line_number += 1
        return combobox
    
    def add_spinbox(self, dialog, minimum, name):
        spinbox = QtWidgets.QSpinBox(dialog)
        spinbox.setObjectName(name)
        spinbox.setMinimum(minimum)
        self.gridlayout.addWidget(spinbox, self.line_number, 1, 1, 1)
        self.line_number += 1
        return spinbox
        
    def add_line_edit(self, dialog, name, placeholder):
        line_edit = QtWidgets.QLineEdit(dialog)
        line_edit.setObjectName(name)
        line_edit.setPlaceholderText(placeholder)
        self.gridlayout.addWidget(line_edit, self.line_number, 1, 1, 1)
        self.line_number += 1
        return line_edit
        
    def add_ok_cancel_button_box(self, dialog, object_name, ok_button_text, cancel_button_text):
        button_box = QtWidgets.QDialogButtonBox(dialog)
        button_box.setOrientation(QtCore.Qt.Horizontal)
        button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        button_box.button(QtWidgets.QDialogButtonBox.Ok).setText(ok_button_text)
        button_box.button(QtWidgets.QDialogButtonBox.Cancel).setText(cancel_button_text)
        button_box.setObjectName(object_name)
        self.gridlayout.addWidget(button_box, self.line_number, 0, 1, 2)
        self.line_number += 1
        return button_box
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Trophy Blitz"))
        self.url.setText(_translate("Dialog", "URL:"))
        self.num_refreshes.setText(_translate("Dialog", "Number of refreshes:"))
        self.interval.setText(_translate("Dialog", "Interval (min)"))
        self.browser_label.setText(_translate("Dialog", "Browser:"))
        
    def blitz_it(self):
        browser = self.browser.currentText()
        url = self.userEdit.displayText()
        refreshes = self.num_refreshes_edit.value()
        interval = self.interval_edit.value()
        
        unleash_chaos_gui(browser, url, refreshes, interval)
    
    def exit(self):
        QtCore.QCoreApplication.quit()
        