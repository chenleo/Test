import QtQuick 1.1

Rectangle {
    width: 200
    height: 200
    color: "red"
    Text {
        anchors.centerIn: parent
        text: "Hello World"
    }
    MouseArea {
        anchors.fill: parent
        onClicked: {
            Qt.quit();
        }
    }
}

