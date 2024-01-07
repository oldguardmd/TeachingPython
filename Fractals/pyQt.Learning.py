import sys
import time
import math

from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsLineItem
from PyQt5.QtCore import Qt, QRectF, QTimer
from PyQt5.QtGui import QPen

ARM_LENGTH = 100
ROTATION_SPEED = .01
GOLDEN = (1 + 5 ** 0.5) / 2


class RotatingArms(QGraphicsView):
    def __init__(self):
        super().__init__()
        scene_rect = QRectF(-400, -300, 800, 600)  # Set the desired sceneRect
        self.scene = QGraphicsScene(scene_rect, self)
        self.setScene(self.scene)
        #self.setGeometry(100, 100, 800, 600)

        # Create Line 1
        self.angle1 = 0
        self.arm1 = QGraphicsLineItem(0, 0, -ARM_LENGTH * math.cos(self.angle1), -ARM_LENGTH * math.sin(self.angle1))
        self.arm1.setPen(QPen(Qt.red))
        self.scene.addItem(self.arm1)

        # Create Line 2
        self.angle2 = 0
        self.arm2 = QGraphicsLineItem(-ARM_LENGTH * math.cos(self.angle1), -ARM_LENGTH * math.sin(self.angle1),-ARM_LENGTH * math.cos(self.angle2), -ARM_LENGTH * math.sin(self.angle2))
        self.arm2.setPen(QPen(Qt.blue))
        self.scene.addItem(self.arm2)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_arms)
        self.timer.start(16)
    
    def update_arms(self):
        self.angle1 += ROTATION_SPEED
        self.angle2 += ROTATION_SPEED * GOLDEN
        arm1_start_x = 0
        arm1_start_y = 0
        arm1_end_x = ARM_LENGTH * math.cos(self.angle1)
        arm1_end_y = -ARM_LENGTH * math.sin(self.angle1)
        arm2_start_x = arm1_end_x
        arm2_start_y = arm1_end_y
        arm2_end_x = arm1_end_x + ARM_LENGTH * math.cos(self.angle2)
        arm2_end_y = arm1_end_y + -ARM_LENGTH * math.sin(self.angle2)


        self.arm1.setLine(arm1_start_x, arm1_start_y, arm1_end_x, arm1_end_y)
        self.arm2.setLine(arm2_start_x, arm2_start_y, arm2_end_x, arm2_end_y)

        return 

app = QApplication([])

window = RotatingArms()
window.show()
app.exec()
    