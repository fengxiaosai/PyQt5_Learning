#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
在这一部分的pyqt5教程中，我们将探讨PyQt5中的事件Event

事件 Event
所有的GUI程序都是事件驱动的。事件主要由用户触发，
但也可能有其他触发方式：例如网络连接、window manager或定时器。
当我们调用QApplication的exec_()方法时会使程序进入主循环。主循环会获取并分发事件。

在事件模型中，有三个参与者：
    事件源
    事件对象
    事件接收者
事件源是状态发生变化的对象。它会生成事件。
事件(对象)封装了事件源中状态的变动。
事件接收者是要通知的对象。事件源对象将事件处理的工作交给事件接收者。

PyQt5有一个独特的signal&slot(信号槽)机制来处理事件。
信号槽用于对象间的通信。
signal在某一特定事件发生时被触发，slot可以是任何callable对象。
当signal触发时会调用与之相连的slot。
"""
"""
信号槽 Signals & slots
这是一个使用信号槽的PyQt5例子。
这个例子中展示了一个QtGui.QLCDNumber和QtGui.QSlider。lcd的值会随着滑块的拖动而改变。
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)
        # 在这里将滚动条的valueChanged信号连接到lcd的display插槽。
        # sender是发出信号的对象。receiver是接收信号的对象。slot(插槽)是对信号做出反应的方法。

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())