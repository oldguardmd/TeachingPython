from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsLineItem
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPen, QPainter
import math

ARM_LENGTH = 100
ROTATION_SPEED = .01
GOLDEN = (1 + 5 ** 0.5) / 2
SCREEN_HEIGHT = 1200
SCREEN_WIDTH = 1800


class RotatingArms(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.resize(SCREEN_WIDTH, SCREEN_HEIGHT)
        #print(f"Height: {float(self.height()) / 2}\nWidth: {float(self.width()) / 2}\n")
        #exit()
        self.arm1 = QGraphicsLineItem(0, 0, 0, -ARM_LENGTH)
        self.arm1.setPen(QPen(Qt.red))
        #self.arm.setLine(0,0,ARM_LENGTH * math.cos(0,))
        #self.arm2 = QGraphicsLineItem(0, 0, 0, -ARM_LENGTH)
        #self.arm2.setPen(QPen(Qt.blue))
        
        
        # Add arms to scene
        self.scene.addItem(self.arm1)
        #self.scene.addItem(self.arm2)

        self.angle1 = 0
        #self.angle2 = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_arms)
        self.timer.start(16)

    def update_arms(self):
        self.angle1 += ROTATION_SPEED
        #self.angle2 += ROTATION_SPEED * GOLDEN

        self.arm1.setLine(0, 0, ARM_LENGTH * math.cos(self.angle1), -ARM_LENGTH * math.sin(self.angle1))
        #self.arm2.setLine(ARM_LENGTH * math.cos(self.angle1), -ARM_LENGTH * math.sin(self.angle1),
        #                  ARM_LENGTH * math.cos(self.angle1 + self.angle2), -ARM_LENGTH * math.sin(self.angle1 + self.angle2))

app = QApplication([])
window = RotatingArms()
window.show()
app.exec_()
