import sys
from PySide import QtCore, QtGui

from __future__ import print_function
 
# Insert PySide/PyQt imports here
 
class Circle(QtCore.QObject):
    ''' Represents a circle defined by the x and y
    coordinates of its center and its radius r. '''
    # Signal emitted when the circle is resized,
    # carrying its integer radius
    resized = QtCore.Signal(int)
    # Signal emitted when the circle is moved, carrying
    # the x and y coordinates of its center.
    moved = QtCore.Signal(int, int)
 
    def __init__(self, x, y, r, parent=None):
        # Initialize the Circle as a QObject so it can emit signals
        #QObject.__init__(self)
        super(Circle,self).__init__(parent)
 
        # "Hide" the values and expose them via properties
        self._x = x
        self._y = y
        self._r = r

    @property
    def x(self):
        return self._x
 
    @x.setter
    def x(self, new_x):
        self._x = new_x
        # After the center is moved, emit the
    # moved signal with the new coordinates
        self.moved.emit(new_x, self.y)
 
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, new_y):
        self._y = new_y
        # After the center is moved, emit the moved
    # signal with the new coordinates
        self.moved.emit(self.x, new_y)
 
    @property
    def r(self):
        return self._r
 
    @r.setter
    def r(self, new_r):
        self._r = new_r
        # After the radius is changed, emit the
    # resized signal with the new radius
        self.resized.emit(new_r)
    
@QtCore.Slot(int, int)
def on_moved(x, y):
    print('Circle was moved to (%s, %s).' % (x, y))

@QtCore.Slot(int)
def on_resized(r):
    print('Circle was resized to radius %s.' % r)
    
c = Circle(5, 5, 4)
 
# Connect the Circle's signals to our simple slots
c.moved.connect(on_moved)
c.resized.connect(on_resized)
 
# Move the circle one unit to the right
c.x += 1
 
# Increase the circle's radius by one unit
c.r += 1