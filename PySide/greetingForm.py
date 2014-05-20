import sys
from PySide import QtCore
from PySide import QtGui

class Form(QtGui.QDialog):
    def __init__(self, parent = None):
        super(Form, self).__init__(parent)
        self.edit = QtGui.QLineEdit("Write my Name Here")
        self.button = QtGui.QPushButton("Show Greetings")
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
        self.button.clicked.connect(self.greetings)
    
    def greetings(self):
        print ("Hello %s" % self.edit.text())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = Form()
    form.show()
    
    sys.exit(app.exec_())