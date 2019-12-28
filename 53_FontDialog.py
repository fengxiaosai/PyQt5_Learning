# -*- coding: utf-8 -*-

"""
In this example, we determine the event sender object.
QFontDialog对话框用以选择字体
在这个例子中，创建了一个按钮和一个标签，通过QFontDialog来改变标签的字体
"""
import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
                             QSizePolicy, QLabel, QFontDialog, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed,
                          QSizePolicy.Fixed)

        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()

    def showDialog(self):
        font, ok = QFontDialog.getFont()
        # 这一行代码弹出字体选择对话框，getFont()方法返回字体名称和ok参数，
        # 如果用户点击了ok他就是True,否则就是false

        if ok:
            self.lbl.setFont(font)
            # 如果点击了ok，标签的字体就会被改变

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())