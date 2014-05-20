import sys
from PySide import QtCore, QtGui

app = QtGui.QApplication(sys.argv)

label = QtGui.QLabel()
label.setText("<font color=red>Hello World</font>")

label.show()
app.exec_()
sys.exit()