import sys
import time
from PySide import QtCore, QtGui
from __future__ import print_function

class PunchingBag(QtCore.QObject):
    """
        punsheit emit the signal
    """
    punched = QtCore.Signal()
    
    def __init__(self, parent = None):
        super(PunchingBag,self).__init__(parent)
    
    def punch(self):
        self.punched.emit()
        
QtCore.Slot()
def say_punched():
    """
    Give evidence that a bag was punched.
    """
    print("Bag was punched")

bag = PunchingBag()
bag.punched.connect(say_punched)
for i in range(10):
    bag.punch()
    time.sleep(1)