# -*- coding: utf-8 -*-
"""
Created on Mon May 19 15:33:51 2014

@author: chen
"""

# simple.py

import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)

wid = QtGui.QWidget()
wid.resize(250, 150)
wid.setWindowTitle('Simple')
wid.show()

sys.exit(app.exec_())
