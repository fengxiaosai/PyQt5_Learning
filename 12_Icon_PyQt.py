#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
应用程序图标是一个小的图像，
通常在标题栏的左上角显示。
在下面的例子中我们将介绍如何做pyqt5的图标。
同时我们也将介绍一些新方法。


"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

'''
前面的例子是在程序风格。Python编程语言支持程序和面向对象编程风格。Pyqt5使用OOP编程。
面向对象编程有三个重要的方面：类、变量和方法。这里我们创建一个新的类为Examle。Example继承自QWidget类。
'''
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 300, 220)
        # 设置窗口的标题
        self.setWindowTitle('Icon')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('cauc.jpg'))

        # 显示窗口
        self.show()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())