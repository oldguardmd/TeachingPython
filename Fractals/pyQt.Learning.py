import sys
import time
import math
import random

from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsLineItem, QGraphicsEllipseItem
from PyQt5.QtCore import Qt, QRectF, QTimer
from PyQt5.QtGui import QPen, QPainter, QBrush, QColor

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
        self.angle2 = random.randint(0,359)
        self.arm2 = QGraphicsLineItem(-ARM_LENGTH * math.cos(self.angle1), -ARM_LENGTH * math.sin(self.angle1),-ARM_LENGTH * math.cos(self.angle2), -ARM_LENGTH * math.sin(self.angle2))
        self.arm2.setPen(QPen(Qt.blue))
        self.scene.addItem(self.arm2)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_arms)
        self.timer.start(16)
    
    def update_arms(self):
        self.angle1 += ROTATION_SPEED
        self.angle2 += ROTATION_SPEED * GOLDEN
        arm1_start_x = 0    # We never change the center point of the first line, so it will always be zero
        arm1_start_y = 0    # We never change teh center point of the first line, so it will always be zero
        arm1_end_x = ARM_LENGTH * math.cos(self.angle1)  # The X point for a line ARM_LENGTH long
        arm1_end_y = -ARM_LENGTH * math.sin(self.angle1) # The Y point for al ine ARM_LENGTH long
        arm2_start_x = arm1_end_x   # We could just use the end point of ARM1, but this was easier for me to visualize
        arm2_start_y = arm1_end_y   # We could just use the end point of ARM1, but this was easier for me to visualize 
        arm2_end_x = arm1_end_x + ARM_LENGTH * math.cos(self.angle2)    # Calculate the arm2 X end point based on the starting point of ARM1 
        arm2_end_y = arm1_end_y + -ARM_LENGTH * math.sin(self.angle2)   # Calculate the arm2 Y end point based on the starting point of ARM1

        self.arm1.setLine(arm1_start_x, arm1_start_y, arm1_end_x, arm1_end_y) # Set the new position of arm1
        self.arm2.setLine(arm2_start_x, arm2_start_y, arm2_end_x, arm2_end_y) # Set the new position of arm2
        self.scene.addEllipse(arm2_end_x,arm2_end_y,1,1,QPen(Qt.white))
        
        return 

app = QApplication([])

window = RotatingArms()
window.show()
app.exec()
    