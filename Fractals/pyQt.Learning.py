import sys
import time
import math

from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsLineItem
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPen

ARM_LENGTH = 100
ROTATION_SPEED = .01


class RotatingArms(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(self)
        print(dir(self.scene))
        self.setScene(self.scene)
        self.setGeometry(100, 100, 800, 400)

        self.arm1 = QGraphicsLineItem(0, 0, 0, -ARM_LENGTH)
        self.arm1.setPen(QPen(Qt.red))
        self.scene.addItem(self.arm1)
        self.angle1 = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_arms)
        self.timer.start(16)
    
    def update_arms(self):
        self.angle1 += ROTATION_SPEED
        #self.angle2 += ROTATION_SPEED * GOLDEN

        self.arm1.setLine(0, 0, ARM_LENGTH * math.cos(self.angle1), -ARM_LENGTH * math.sin(self.angle1))
        return 

app = QApplication([])

window = RotatingArms()
window.show()
app.exec()
    