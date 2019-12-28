# -*- coding: utf-8 -*-

"""
In this example, we determine the event sender object.
QInputDialog提供了一种简单方便的对话框从用户得到一个值。
输入值可以是字符串,一个数字,或一个项目从一个列表。
这个例子显示一个按钮和一个文本框，用户点击按钮显示一个输入框，用户输入信息会显示在文本框中。
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')
        # 这行代码显示输入对话框。第一个字符串是一个对话框标题,第二个是对话框中的消息。
        # 对话框返回输入的文本和一个布尔值。点击Ok按钮,布尔值是True。

        if ok:
            self.le.setText(str(text))
            # 对话框收到的文本消息会显示在文本框中

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())