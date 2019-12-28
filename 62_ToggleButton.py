# -*- coding: utf-8 -*-

"""
In this example, we create three toggle buttons.
They will control the background color of a QFrame.

ToggleButton是QPushButton的一种特殊模式。
它是一个有两种状态的按钮：按下与未按下。
通过点击在这两种状态间来回切换。这种功能在某些场景会很实用。
代码中我们创建了三个ToggleButton与一个QWidget。
我们将QWidget的背景色设为黑色。
ToggleButton会切换颜色值中的红色、绿色与蓝色部分。
QWidget的背景颜色依赖于按下的按钮。
"""
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QFrame, QApplication)
from PyQt5.QtGui import QColor


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.col = QColor(0, 0, 0) #这是初始黑颜色的值

        # 创建一个QPushButton并通过其setCheckable()方法来得到一个ToggleButton。
        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)

        redb.clicked[bool].connect(self.setColor)
        # 将clicked信号连接到用户自定义的方法。我们通过clicked信号操作一个布尔值。

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()

    def setColor(self, pressed):

        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "Red": # 如果按下的是red按钮，我们要相应地更新颜色中的红包部分。
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" %
                                  self.col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())