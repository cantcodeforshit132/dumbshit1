# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_1.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1833, 1259)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(170, 0, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 550, 361, 671))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_rime1 = QPushButton(self.gridLayoutWidget)
        self.btn_rime1.setObjectName(u"btn_rime1")
        self.btn_rime1.setMinimumSize(QSize(0, 150))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.btn_rime1.setFont(font1)
        self.btn_rime1.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.btn_rime1, 2, 0, 1, 1)

        self.btn_rime3 = QPushButton(self.gridLayoutWidget)
        self.btn_rime3.setObjectName(u"btn_rime3")
        self.btn_rime3.setMinimumSize(QSize(0, 150))
        self.btn_rime3.setFont(font1)
        self.btn_rime3.setStyleSheet(u"background-color: rgb(255, 254, 237);")

        self.gridLayout.addWidget(self.btn_rime3, 1, 0, 1, 1)

        self.btn_rime2 = QPushButton(self.gridLayoutWidget)
        self.btn_rime2.setObjectName(u"btn_rime2")
        self.btn_rime2.setMinimumSize(QSize(0, 150))
        self.btn_rime2.setFont(font1)
        self.btn_rime2.setStyleSheet(u"background-color: rgb(216, 0, 4);")

        self.gridLayout.addWidget(self.btn_rime2, 0, 0, 1, 1)

        self.lbl_rimes = QLabel(self.centralwidget)
        self.lbl_rimes.setObjectName(u"lbl_rimes")
        self.lbl_rimes.setGeometry(QRect(490, 530, 1231, 721))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.lbl_rimes.setFont(font2)
        self.lbl_rimes.setAutoFillBackground(False)
        self.lbl_rimes.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lbl_rimes.setScaledContents(True)
        self.lbl_rimes.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(370, 20, 971, 321))
        font3 = QFont()
        font3.setFamilies([u"Rockwell"])
        font3.setPointSize(50)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"background-color: rgb(7, 181, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(780, 430, 631, 101))
        font4 = QFont()
        font4.setPointSize(50)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"background-color: rgb(14, 50, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.lbl_image = QLabel(self.centralwidget)
        self.lbl_image.setObjectName(u"lbl_image")
        self.lbl_image.setGeometry(QRect(20, 320, 341, 211))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_rime1.clicked.connect(MainWindow.btn_rime1_a)
        self.btn_rime2.clicked.connect(MainWindow.btn_rime2_a)
        self.btn_rime3.clicked.connect(MainWindow.btn_rime3_a)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.btn_rime1.setText(QCoreApplication.translate("MainWindow", u"mary had a little lamb", None))
        self.btn_rime3.setText(QCoreApplication.translate("MainWindow", u"humpty dumpty ", None))
        self.btn_rime2.setText(QCoreApplication.translate("MainWindow", u"ring around the rosie", None))
        self.lbl_rimes.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"3 nursery rimes", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"lyrics", None))
        self.lbl_image.setText("")
    # retranslateUi

