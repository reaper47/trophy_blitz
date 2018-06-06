from PyQt5 import QtCore, QtGui, QtWidgets

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
        
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 5, 0, 1, 2)
        
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
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
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Trophy Blitz"))
        self.url.setText(_translate("Dialog", "URL:"))
        self.num_refreshes.setText(_translate("Dialog", "Number of refreshes:"))
        self.interval.setText(_translate("Dialog", "Interval (min)"))
        self.browser_label.setText(_translate("Dialog", "Browser:"))
