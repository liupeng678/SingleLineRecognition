# -*- coding: utf-8 -*-
"""
需要安装的库：



"""


from EmotionRecongnition import Ui_MainWindow
from sys import argv,exit
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(argv)

    window = QMainWindow()
    ui = Ui_MainWindow(window)

    window.show()
    exit(app.exec_())