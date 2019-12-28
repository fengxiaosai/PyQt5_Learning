#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
重新实现事件处理器
在PyQt5中常通过重新实现事件处理器来处理事件。
在示例中重新实现了keyPressEvent()事件处理器。
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e): # 在示例中重新实现了keyPressEvent()事件处理器。
        if e.key() == Qt.Key_Escape:
            self.close()
            # 按下Escape键会使程序退出。


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())