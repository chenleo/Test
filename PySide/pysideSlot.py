import sys
import PySide
from PySide import QtGui, QtCore
app = QtGui.QApplication(sys.argv)

win = QtGui.QWidget()
win.setWindowTitle("Test Window")

btn = QtGui.QPushButton("test", win)

@QtCore.Slot()
def on_click():
    print("Clicked")
    
@QtCore.Slot()
def on_press():
    print("Pressed")

@QtCore.Slot()
def on_release():
    print("Released")

btn.clicked.connect(on_click)
btn.pressed.connect(on_press)
btn.released.connect(on_release)

win.show()
app.exec_()
sys.exit()