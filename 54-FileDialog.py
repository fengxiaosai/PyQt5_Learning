# -*- coding: utf-8 -*-

"""
In this example, we determine the event sender object.
QFileDialog是一个让用户选择文件和目录的对话框，可用以选择打开或保存文件
这个例子展示了一个菜单栏，中部TextEdit控件和一个状态栏。
菜单项Open会显示用于选择文件的QtGui.QFileDialog对话框。选定文件的内容会加载到TextEdit控件中。
"""
import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        # 示例窗体继承自QMainWindow，因为我们要将TextEdit控件置于窗体中央。

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        # 弹出QFileDialog对话框，第一个字符串参数是对话框的标题，
        # 第二个指定对话框的工作目录，默认情况下文件筛选器会匹配所有类型的文件(*)

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)
            # 读取了选择的文件并将文件内容显示到了TextEdit控件。

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())