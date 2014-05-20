import sys
from PySide import QtCore, QtGui, QtDeclarative

app = QtGui.QApplication(sys.argv)

view = QtDeclarative.QDeclarativeView()
url = QtCore.QUrl("view/view.qml")
view.setSource(url)

#app.aboutQt()
view.show()
sys.exit(app.exec_())