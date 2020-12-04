from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_Dialog
import sys
import time

# 
app = QtWidgets.QApplication(sys.argv)

# 
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

Dialog.setWindowIcon(QtGui.QIcon("iconfinder_Translate_692155.ico"))
Dialog.setWindowTitle("Translator")

# 
def pbt():
	msgout = ui.lineEdit_2.text()
	msgout = msgout.replace('ъ', '')
	ui.label_2.setText(msgout)

def pbo():
	msgin = ui.lineEdit.text()
	glas = ["я", "ю", "ё", "е", "и", "ы", "о", "у", "а", "э", ".", ")", "(", "/", "\\", "*", "-", "+", ",", " "]
	res = ""

	for symb in msgin:
		if symb.lower() not in glas:
			res += f"{symb}ъ"
		else:
			res += f"{symb}"

	ui.label.setText(res)

def main():
	ui.pushButton.clicked.connect(pbo)
	ui.pushButton_2.clicked.connect(pbt)
	sys.exit(app.exec_())

	

while True:
	main()
	


input()