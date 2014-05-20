import sys
from PySide import QtGui, QtCore

app = QtGui.QApplication(sys.argv)

wid = QtGui.QWidget()
wid.resize(250, 150)
wid.setWindowTitle("Simple")

wid.show()
app.exec_()
sys.exit()