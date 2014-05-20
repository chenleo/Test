import sys
from PySide import QtGui, QtCore
class Example(QtGui.QWidget):
    def __init__(self, parent = None):
        super(Example, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        
        qbtn = QtGui.QPushButton("Quit", self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Quit Button")
        #self.setWindowIcon(QtGui.QIcon("icon.png"))
        
        self.show()

        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    sys.exit()

if __name__ == "__main__":
    main()