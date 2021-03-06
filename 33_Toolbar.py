#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
工具栏提供了一个快速访问的入口。
在下面的例子中,创建一个简单的工具栏。工具栏有有一个按钮,点击关闭窗口。
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        '''
        类似于例32的菜单栏的例子,创建一个QAction事件。该事件有一个标签、图标和快捷键。退出窗口的方法
        '''
        exitAction = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())