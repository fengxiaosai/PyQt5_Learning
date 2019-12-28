# -*- coding: utf-8 -*-

"""
In this example, we determine the event sender object.
QColorDialog显示一个用于选择颜色值的对话框。
这个应用程序显示一个按钮和一个QFrame。QFrame的背景为黑色。
通过QColorDialog,我们可以改变它的背景。
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame,
                             QColorDialog, QApplication)
from PyQt5.QtGui import QColor


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0) # 初始化QFrame的颜色为黑色

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor() # 这一行代码弹出QColorDialog

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())
            # 要先检查col的值。如果点击的是Cancel按钮，返回的颜色值是无效的。
            # 当颜色值有效时，通过样式表(style sheet)来改变背景颜色。


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())