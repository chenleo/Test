import sys
from PySide import QtGui, QtCore
class Example(QtGui.QWidget):
    def __init__(self, parent = None):
        super(Example, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        
        self.resize(250, 150)
        self.center()
        self.setWindowTitle("Center")
        
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    sys.exit()

if __name__ == "__main__":
    main()