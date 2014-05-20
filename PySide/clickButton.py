import sys
from PySide import QtCore, QtGui

#define functions:
def sayHello():
    print "Hello World!"
    
app = QtGui.QApplication(sys.argv)

button = QtGui.QPushButton("Click Me")
button.clicked.connect(sayHello)

button.show()
app.exec_()
sys.exit()