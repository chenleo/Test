import sys
from PySide import QtCore, QtGui

class Example(QtGui.QMainWindow):
    
    def __init__(self, parent = None):
        super(Example,self).__init__(parent)
        self.initUI()
    
    def initUI(self):               
        
        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QtGui.QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
        
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')    
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    sys.exit()

if __name__ == "__main__":
    main()