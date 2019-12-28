#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
表格布局将空间划分为行和列。我们使用QGridLayout类创建一个网格布局。
"""

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 在我们的示例中,我们创建一个网格的按钮。
        grid = QGridLayout()
        self.setLayout(grid)

        # QGridLayout的实例被创建并设置应用程序窗口的布局。
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)] # 这些按钮的标签。

        for position, name in zip(positions, names): # 创建一个网格中的位置的列表。
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
            # 创建按钮并使用addWidget()方法添加到布局中。

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())