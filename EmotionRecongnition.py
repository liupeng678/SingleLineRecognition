# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EmotionRecongnition_UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
#from skimage.measure import label
from PyQt5 import QtCore, QtGui, QtWidgets
import image1_rc
import numpy as np
import cv2

#from preprocess  import *
#from skimage import measure, color
import math
import matplotlib.pyplot as plt
from sympy import *

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        
        self.timer_camera = QtCore.QTimer() # 定时器

        self.setupUi(MainWindow)
        self.retranslateUi(MainWindow)
        self.slot_init() # 槽函数设置

        self.cap = cv2.VideoCapture() # 屏幕画面对象
        self.CAM_NUM = 0 # 摄像头标号
        
        # self.__flag_work = 0
        self.boundaries = [([0, 0, 0], [180, 255, 46])]


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(765, 645)
        MainWindow.setMinimumSize(QtCore.QSize(765, 645))
        MainWindow.setMaximumSize(QtCore.QSize(765, 645))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/images_test/result.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("#MainWindow{border-image: url(:/newPrefix/images_test/background.PNG);}\n"
"\n"
"#QInputDialog{border-image: url(:/newPrefix/images_test/light.png);}\n"
"\n"
"QMenuBar{border-color:transparent;}\n"
"QToolButton[objectName=pushButton_doIt]{\n"
"border:5px;}\n"
"\n"
"QToolButton[objectName=pushButton_doIt]:hover {\n"
"image:url(:/newPrefix/images_test/run_hover.png);}\n"
"\n"
"QToolButton[objectName=pushButton_doIt]:pressed {\n"
"image:url(:/newPrefix/images_test/run_pressed.png);}\n"
"\n"
"QScrollBar:vertical{\n"
"background:transparent;\n"
"padding:2px;\n"
"border-radius:8px;\n"
"max-width:14px;}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"background:#9acd32;\n"
"min-height:50px;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"background:#9eb764;}\n"
"\n"
"QScrollBar::handle:vertical:pressed{\n"
"background:#9eb764;\n"
"}\n"
"QScrollBar::add-page:vertical{\n"
"background:none;\n"
"}\n"
"                               \n"
"QScrollBar::sub-page:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"background:none;}\n"
"                                 \n"
"QScrollBar::sub-line:vertical{\n"
"background:none;\n"
"}\n"
"QScrollArea{\n"
"border:0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal{\n"
"background:transparent;\n"
"padding:0px;\n"
"border-radius:6px;\n"
"max-height:12px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"background:#9acd32;\n"
"min-width:50px;\n"
"border-radius:6px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"background:#9eb764;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed{\n"
"background:#9eb764;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-page:horizontal{\n"
"background:none;\n"
"}\n"
"QScrollBar::add-line:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal{\n"
"background:none;\n"
"}\n"
"QToolButton::hover{\n"
"border:0px;\n"
"} ")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_scanResult = QtWidgets.QLabel(self.centralwidget)
        self.label_scanResult.setGeometry(QtCore.QRect(60, 360, 151, 31))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(18)
        self.label_scanResult.setFont(font)
        self.label_scanResult.setObjectName("label_scanResult")
        self.label_face = QtWidgets.QLabel(self.centralwidget)
        self.label_face.setGeometry(QtCore.QRect(10, 70, 420, 280))
        self.label_face.setMinimumSize(QtCore.QSize(420, 280))
        self.label_face.setMaximumSize(QtCore.QSize(420, 280))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_face.setFont(font)
        self.label_face.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_face.setStyleSheet("border-image: url(:/newPrefix/images_test/slice.png);")
        self.label_face.setAlignment(QtCore.Qt.AlignCenter)
        self.label_face.setObjectName("label_face")
        self.textEdit_camera = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_camera.setGeometry(QtCore.QRect(60, 20, 360, 30))
        self.textEdit_camera.setMinimumSize(QtCore.QSize(360, 30))
        self.textEdit_camera.setMaximumSize(QtCore.QSize(360, 30))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(12)
        self.textEdit_camera.setFont(font)
        self.textEdit_camera.setStyleSheet("background-color: transparent;\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.textEdit_camera.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_camera.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_camera.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_camera.setReadOnly(True)
        self.textEdit_camera.setObjectName("textEdit_camera")
        self.textEdit_pic = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_pic.setGeometry(QtCore.QRect(470, 20, 360, 30))
        self.textEdit_pic.setMinimumSize(QtCore.QSize(360, 30))
        self.textEdit_pic.setMaximumSize(QtCore.QSize(360, 30))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(12)
        self.textEdit_pic.setFont(font)
        self.textEdit_pic.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_pic.setStyleSheet("background-color: transparent;\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.textEdit_pic.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_pic.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_pic.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_pic.setReadOnly(True)
        self.textEdit_pic.setObjectName("textEdit_pic")
        self.toolButton_camera = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_camera.setGeometry(QtCore.QRect(10, 10, 50, 45))
        self.toolButton_camera.setMinimumSize(QtCore.QSize(50, 39))
        self.toolButton_camera.setMaximumSize(QtCore.QSize(50, 45))
        self.toolButton_camera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_camera.setAutoFillBackground(False)
        self.toolButton_camera.setStyleSheet("background-color: transparent;")
        self.toolButton_camera.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/images_test/g1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_camera.setIcon(icon1)
        self.toolButton_camera.setIconSize(QtCore.QSize(50, 39))
        self.toolButton_camera.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_camera.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_camera.setAutoRaise(False)
        self.toolButton_camera.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_camera.setObjectName("toolButton_camera")
        self.toolButton_model = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_model.setGeometry(QtCore.QRect(0, 360, 50, 40))
        self.toolButton_model.setMinimumSize(QtCore.QSize(0, 0))
        self.toolButton_model.setMaximumSize(QtCore.QSize(50, 40))
        self.toolButton_model.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_model.setAutoFillBackground(False)
        self.toolButton_model.setStyleSheet("background-color: transparent;")
        self.toolButton_model.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/images_test/folder_web.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_model.setIcon(icon2)
        self.toolButton_model.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_model.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_model.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_model.setAutoRaise(False)
        self.toolButton_model.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_model.setObjectName("toolButton_model")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 400, 321, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(210, 360, 450, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("color: rgb(0, 189, 189);")
        self.label_result.setObjectName("label_result")
        self.toolButton_camera_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_camera_2.setGeometry(QtCore.QRect(420, 10, 50, 45))
        self.toolButton_camera_2.setMinimumSize(QtCore.QSize(50, 39))
        self.toolButton_camera_2.setMaximumSize(QtCore.QSize(50, 45))
        self.toolButton_camera_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_camera_2.setAutoFillBackground(False)
        self.toolButton_camera_2.setStyleSheet("background-color: transparent;")
        self.toolButton_camera_2.setText("")
        self.toolButton_camera_2.setIcon(icon1)
        self.toolButton_camera_2.setIconSize(QtCore.QSize(50, 39))
        self.toolButton_camera_2.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_camera_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_camera_2.setAutoRaise(False)
        self.toolButton_camera_2.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_camera_2.setObjectName("toolButton_camera_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(441, 70, 321, 281))
        self.label.setStyleSheet("border-image: url(:/newPrefix/images_test/background.PNG);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 410, 321, 231))
        self.label_2.setStyleSheet("border-image: url(:/newPrefix/images_test/background.PNG);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 410, 341, 231))
        self.label_3.setStyleSheet("border-image: url(:/newPrefix/images_test/background.PNG);")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionGoogle_Translate = QtWidgets.QAction(MainWindow)
        self.actionGoogle_Translate.setObjectName("actionGoogle_Translate")
        self.actionHTML_type = QtWidgets.QAction(MainWindow)
        self.actionHTML_type.setObjectName("actionHTML_type")
        self.actionsoftware_version = QtWidgets.QAction(MainWindow)
        self.actionsoftware_version.setObjectName("actionsoftware_version")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " recongnition v1.2 "))
        self.label_scanResult.setText(_translate("MainWindow", "<html><head/><body><p>拟合函数：<br/></p></body></html>"))
        self.label_face.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.textEdit_camera.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00007f;\">开启摄像头</span></p></body></html>"))
        self.textEdit_pic.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00007f;\">计算视频帧的轨道曲率</span></p></body></html>"))
        self.label_result.setText(_translate("MainWindow", "None"))
        self.label.setText(_translate("MainWindow", "视频帧分析"))
        self.label_2.setText(_translate("MainWindow", "照片映射"))
        self.label_3.setText(_translate("MainWindow", "曲率图片"))
        self.actionGoogle_Translate.setText(_translate("MainWindow", "Google Translate"))
        self.actionHTML_type.setText(_translate("MainWindow", "HTML type"))
        self.actionsoftware_version.setText(_translate("MainWindow", "software version"))

    def slot_init(self): # 定义槽函数
        self.toolButton_camera.clicked.connect(self.button_open_camera_click)
        self.toolButton_camera_2.clicked.connect(self.choose_pic)
        self.timer_camera.timeout.connect(self.show_camera)


    def button_open_camera_click(self):
        if self.timer_camera.isActive() == False: # 检查定时状态
            flag = self.cap.open(self.CAM_NUM) # 检查相机状态
            if flag == False: # 相机打开失败提示
                msg = QtWidgets.QMessageBox.warning(self.centralwidget, u"Warning",
                                                    u"请检测相机与电脑是否连接正确！ ",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)

            else:
                # 准备运行识别程序
                
                QtWidgets.QApplication.processEvents()
                self.textEdit_camera.setText('实时摄像已开启')
                self.label_face.setText('正在启动识别系统...\n\nleading')
                # 新建对象
                




                QtWidgets.QApplication.processEvents()
                # 打开定时器
                self.timer_camera.start(30)
        else:
            # 定时器未开启，界面回复初始状态
            self.timer_camera.stop()
            self.cap.release()
            self.label_face.clear()
            self.textEdit_camera.setText('实时摄像已关闭')
            self.label_result.setText('None')
            

    def show_camera(self):
        # 定时器槽函数，每隔一段时间执行
        flag, self.image = self.cap.read() # 获取画面
        #self.image=cv2.flip(self.image, 1) # 左右翻转
        frameClone = cv2.resize( self.image,(420,280))
        # 在Qt界面中显示人脸
        show = cv2.cvtColor(frameClone, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label_face.setPixmap(QtGui.QPixmap.fromImage(showImage))
        QtWidgets.QApplication.processEvents()

    def choose_pic(self):
       # self.image =
        img_resize = cv2.resize(self.image, (500, 600), interpolation=cv2.INTER_AREA)
        frame=cv2.cvtColor(img_resize,cv2.COLOR_BGR2HSV)
        
        lower = np.array(self.boundaries[0][0], dtype = "uint8")    
        upper = np.array(self.boundaries[0][1], dtype = "uint8")
        mask = cv2.inRange(frame, lower, upper)
        #res = cv2.bitwise_and(frame,frame, mask= mask)



        mask = ~mask
        #ret, mask = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)
        #cv2.imwrite("./data/test.jpg",mask)
        #print(mask.shape)    
                # 进行与操作    
        #output = cv2.bitwise_and(img_resize, img_resize, mask = mask)

        # labeled_img, num = label(mask, neighbors=4, background=0, return_num=True)
        # max_label = 0
        # max_num = 0
        # for i in range(1, num+1): # 这里从1开始，防止将背景设置为最大连通域
        #     if np.sum(labeled_img == i) > max_num:
        #         max_num = np.sum(labeled_img == i)
        #         max_label = i
        # lcc = (labeled_img == max_label)
        # print(lcc.shape)
        # #plt.imshow(lcc)
        # print(mask.shape)
  






        frameClone = cv2.resize(mask,(300,250),interpolation=cv2.INTER_AREA)
        
        show = cv2.cvtColor(frameClone, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(showImage))


        x = np.arange(500)
         #print(x)
        y = np.zeros((500))
        realx =  np.zeros((600))  # 真实的x坐标
        #realx = np.arange(500)
        realy =  np.zeros((600))  # 真实的Y便宜
        y  = mask[599,:]  # 先确定realx起始点
        #print(y)
        
        for j in range (600):
            flage = 1
            y  = mask[599-j,:]

            for i in range(500):   
                if y[i]==0 and flage ==1:
                        flage = 0
                        realx[j] = i
                        
                        
                        temp1 = i
                if flage==0 and y[i]==0:
                        temp2 = i
                        d1 = int((temp2-temp1)/2)
                        realx[j] =  realx[j] +d1
                        realy[j] = j
                        break
        




        f2 = np.polyfit(realx, realy, 3)
        p2 = np.poly1d(f2)
        #print(p2)
        #print(float(p2[1]))
        xx = np.arange(600)
        yy = np.zeros(600)
        yvals = p2(realx)  #拟合y值


        str1 = str(p2)
        self.label_result.setText(str1)

        # 求导数
        w = 0
        x1 = symbols("x")  # 符号x，自变量
        function = (float(p2[3])*(x1)**3+float(p2[2])*(x1)**2+float(p2[1])*(x1)+float(p2[0]))
        dify2 =function.diff(x1,x1)
        #dify = diff(function,x1,x1) #求导
        dify = diff(function,x1) #求导
        
        # print(dify)  #打印导数
        # print(dify2)  #打印导数
        dify3 = 1/((abs(dify2))/((1+dify**2)**1.5))
        #print("qulv is:",dify3)  #打印曲率
        realqulv = np.zeros(len(realx))
        for i in range(len(realx)):

            realqulv[i]=dify3.subs('x',realx[i])
        #print("qulv is:",realqulv)  #打印曲率



        plot1 = plt.plot(realx, realy, 's',label='original values')
        plot1 = plt.plot(xx, yy, 's',label='original values')
        plot2 = plt.plot(realx, yvals, '.y',label='polyfit values')
        #for a,c, b in zip(realx, yvals,realqulv):
        #        plt.text(a, c, b, ha='center', va='bottom', fontsize=3)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend(loc=4) #指定legend的位置右下角
        plt.title('polyfitting')
        plt.show()
        plt.savefig('test.png')
        
        
        




  