import sys
from PySide import QtGui, QtCore
class Example(QtGui.QWidget):
    def __init__(self, parent = None):
        super(Example, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        
        QtGui.QToolTip.setFont(QtGui.QFont("SansSerif", 10))
        
        self.setToolTip("This is a <b>QWidget</b> widget")
        
        btn = QtGui.QPushButton("Button", self)
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Tooltips")
        #self.setWindowIcon(QtGui.QIcon("icon.png"))
        
        self.show()

        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    sys.exit()

if __name__ == "__main__":
    main()