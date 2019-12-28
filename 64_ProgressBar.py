# -*- coding: utf-8 -*-

"""
This example shows a QProgressBar widget.
一个进度条是一个显示任务进展的控件。
QProgressBar控件提供了一个水平或垂直PyQt5工具包的进度条。
可以设置进度条的最小和最大值。默认值是0到99。
这个例子显示一个水平的进度条和一个按钮，用户通过点击按钮开始和停止进度条
"""
import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar,
                             QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.pbar = QProgressBar(self) # QProgressBar的构造方法
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer() # 我们使用定时器timer来激活QProgressBa
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()

    def timerEvent(self, e):
    # 每个QObject及其子类都有一个timerEvent()事件处理器。我们要重新实现这个事件处理器来响应定时器事件。
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        # 我们在doAction()方法中启动/停止定时器。
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            # 我们调用start()方法启动一个计时器。这个方法有两个参数:超时和对象将接收的事件。

            self.btn.setText('Stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())