import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsLineItem
from PyQt5.QtCore import Qt, QTimer
import PyQt5.QtGui as QtGui

class RotatingLine(QGraphicsView):
    def __init__(self):
        super().__init__()

        # Set up the scene
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # Create a line item
        self.line = QGraphicsLineItem(0, 0, 100, 0)
        self.line.setPos(self.width() / 2, self.height() / 2)
        self.scene.addItem(self.line)

        # Set up the rotation angle and rotation speed
        self.angle = 0
        self.rotation_speed = 1  # You can adjust the rotation speed as needed

        # Set up a timer to trigger the rotation
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.rotate_line)
        self.timer.start(16)  # Adjust the timer interval as needed

    def rotate_line(self):
        # Rotate the line around the center point
        self.angle += self.rotation_speed
        self.line.setRotation(self.angle)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RotatingLine()
    window.setGeometry(100, 100, 800, 600)  # Set the initial size of the window
    window.show()
    sys.exit(app.exec_())
