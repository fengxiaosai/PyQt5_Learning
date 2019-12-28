#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
控件可以在网格中跨越多个行或列。在下一个示例中,我们说明了这一点。

"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)
        # 创建一个窗口,其中有三个标签,两个行编辑和一个文本编辑窗口小控件。然后使用QGridLayout完成布局。

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        #创建一个网格布局和设置组件之间的间距
        grid.addWidget(reviewEdit, 3, 1, 5, 1)
        # 在添加一个小的控件到网格的时候, 可以提供小部件的行和列跨。在例子中, reviewEdit控件跨度5行。



        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())