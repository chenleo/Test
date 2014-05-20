import sys
from PySide import QtCore
from PySide import QtGui

app = QtGui.QApplication(sys.argv)
#code range
class AbsolutePositioningExample(QtGui.QWidget):
    "Example of PySide Absolute position"
    def __init__(self, parent= None):
        super(AbsolutePositioningExample, self).__init__(parent)
        
        self.setMinimumSize(400, 185)
        self.setWindowTitle("Dynamic Greeter")
        
        self.salutation_lbl = QtGui.QLabel("Salutation:", self)
        self.salutation_lbl.move(5, 5)
        
        self.salutations = ['Ahoy',
                            'Good day',
                            'Hello',
                            'Heyo',
                            'Hi',
                            'Salutations',
                            'Wassup',
                            'Yo']
        
        self.salutation = QtGui.QComboBox(self)
        self.salutation.addItems(self.salutations)
        self.salutation.setMinimumWidth(285)
        self.salutation.move(110, 5)
        
        self.recipient_lbl = QtGui.QLabel('Recipient:', self)
        self.recipient_lbl.move(5, 30)
        
        
        self.recipient = QtGui.QLineEdit(self)
        self.recipient.setPlaceholderText("e.g. 'world' or 'Matey'")
        self.recipient.setMinimumWidth(285)
        self.recipient.move(110, 30)
        
        self.greeting_lbl = QtGui.QLabel('Greeting:', self)
        self.greeting_lbl.move(5, 75)
        
        self.greeting = QtGui.QLabel('', self)
        self.greeting.move(110, 75)
        
        self.build_button = QtGui.QPushButton('Build Greeting', self)
        self.build_button.setMinimumWidth(145)
        self.build_button.move(250, 150)

class LayoutExample(QtGui.QWidget):
    """
    A Layout example
    """
    def __init__(self,parent = None):
        super(LayoutExample,self).__init__(parent)
        
        self.setWindowTitle('Dynamic Greeter')
        self.setMinimumWidth(400)
        
        # Create the QVBoxLayout that lays out the whole form
        self.layout = QtGui.QVBoxLayout()
 
        # Create the form layout that manages the labeled controls
        self.form_layout = QtGui.QFormLayout()
        
        # The salutations that we want to make available
        self.salutations = ['Ahoy',
                            'Good day',
                            'Hello',
                            'Heyo',
                            'Hi',
                            'Salutations',
                            'Wassup',
                            'Yo']
 
        # Create and fill the combo box to choose the salutation
        self.salutation = QtGui.QComboBox(self)
        self.salutation.addItems(self.salutations)
        
        # Add it to the form layout with a label
        self.form_layout.addRow('Salutation:', self.salutation)
 
        # Create the entry control to specify a recipient
        # and set its placeholder text
        self.recipient = QtGui.QLineEdit(self)
        self.recipient.setPlaceholderText("e.g. 'world' or 'Matey'")
 
        # Add it to the form layout with a label
        self.form_layout.addRow('Recipient:', self.recipient)
 
        # Create and add the label to show the greeting text
        self.greeting = QtGui.QLabel('', self)
        self.form_layout.addRow('Greeting:', self.greeting)
 
        # Add the form layout to the main VBox layout
        self.layout.addLayout(self.form_layout)
 
        # Add stretch to separate the form layout from the button
        self.layout.addStretch(1)
 
        # Create a horizontal box layout to hold the button
        self.button_box = QtGui.QHBoxLayout()
 
        # Add stretch to push the button to the far right
        self.button_box.addStretch(1)
 
        # Create the build button with its caption
        self.build_button = QtGui.QPushButton('Build Greeting', self)
 
        # Add it to the button box
        self.button_box.addWidget(self.build_button)
 
        # Add the button box to the bottom of the main VBox layout
        self.layout.addLayout(self.button_box)
 
        # Set the VBox layout as the window's main layout
        self.setLayout(self.layout)
        
        #The button connection
        self.build_button.clicked.connect(self.show_greeting)
        
    @QtCore.Slot()
    def show_greeting(self):
        self.greeting.setText('%s, %s!' %
                              (self.salutations[self.salutation.currentIndex()],
                              self.recipient.text()))
# display range
#form = AbsolutePositioningExample()
form = LayoutExample()
form.show()
app.exec_()
sys.exit()