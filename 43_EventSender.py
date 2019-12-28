# -*- coding: utf-8 -*-

"""
事件发送者
有时需要知道信号是由哪个控件发出的。对此PyQt5提供了sender()方法。

"""

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        # 创建两个按钮。在buttonClicked()方法中通过调用sender()方法来判断当前按下的是哪个按钮。
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        # 两个按钮连接到了同一个插槽。

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
    # 通过调用sender()方法来判断信号源， 并将其名称显示在窗体的状态栏中。

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())