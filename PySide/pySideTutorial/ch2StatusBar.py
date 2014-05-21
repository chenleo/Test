import sys
from PySide import QtCore, QtGui

class Example(QtGui.QMainWindow):
    
    def __init__(self, parent = None):
        super(Example,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.statusBar().showMessage('Ready')
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')    
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    sys.exit()

if __name__ == "__main__":
    main()