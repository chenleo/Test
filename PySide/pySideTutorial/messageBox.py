import sys
from PySide import QtGui, QtCore
class Example(QtGui.QWidget):
    def __init__(self, parent = None):
        super(Example, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Message Box")
        #self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.show()
    
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, "Message",
                                           "Are you sure to quite?", QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    sys.exit()

if __name__ == "__main__":
    main()