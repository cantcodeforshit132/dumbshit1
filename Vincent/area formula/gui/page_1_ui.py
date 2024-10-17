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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1834, 1261)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(500, 220, 461, 80))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.txt_length = QLineEdit(self.gridLayoutWidget)
        self.txt_length.setObjectName(u"txt_length")
        self.txt_length.setMinimumSize(QSize(5, 0))
        self.txt_length.setMaximumSize(QSize(250, 16777215))

        self.gridLayout.addWidget(self.txt_length, 0, 1, 1, 1)

        self.lbl_length = QLabel(self.gridLayoutWidget)
        self.lbl_length.setObjectName(u"lbl_length")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.lbl_length.setFont(font)
        self.lbl_length.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_length, 0, 0, 1, 1)

        self.gridLayoutWidget_3 = QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(450, 900, 661, 191))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_reset = QPushButton(self.gridLayoutWidget_3)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setMinimumSize(QSize(0, 150))
        font1 = QFont()
        font1.setPointSize(20)
        self.btn_reset.setFont(font1)

        self.gridLayout_3.addWidget(self.btn_reset, 0, 1, 1, 1)

        self.btn_exit = QPushButton(self.gridLayoutWidget_3)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(0, 150))
        self.btn_exit.setFont(font1)

        self.gridLayout_3.addWidget(self.btn_exit, 0, 2, 1, 1)

        self.btn_area = QPushButton(self.gridLayoutWidget_3)
        self.btn_area.setObjectName(u"btn_area")
        self.btn_area.setMinimumSize(QSize(0, 150))
        self.btn_area.setFont(font1)

        self.gridLayout_3.addWidget(self.btn_area, 0, 0, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(1240, 510, 461, 80))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.txt_height = QLineEdit(self.gridLayoutWidget_2)
        self.txt_height.setObjectName(u"txt_height")
        self.txt_height.setMinimumSize(QSize(5, 0))
        self.txt_height.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_2.addWidget(self.txt_height, 0, 1, 1, 1)

        self.lbl_height = QLabel(self.gridLayoutWidget_2)
        self.lbl_height.setObjectName(u"lbl_height")
        self.lbl_height.setFont(font)
        self.lbl_height.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_height, 0, 0, 1, 1)

        self.lbl_answer = QLabel(self.centralwidget)
        self.lbl_answer.setObjectName(u"lbl_answer")
        self.lbl_answer.setGeometry(QRect(420, 360, 741, 441))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.lbl_answer.setFont(font2)
        self.lbl_answer.setStyleSheet(u"background-color: rgb(160, 170, 255);")
        self.lbl_answer.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(340, 120, 1171, 91))
        font3 = QFont()
        font3.setPointSize(50)
        font3.setBold(True)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"background-color: rgb(255, 66, 66);")
        self.label_4.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_area.clicked.connect(MainWindow.btn_area_a)
        self.btn_reset.clicked.connect(MainWindow.btn_reset_a)
        self.btn_exit.clicked.connect(MainWindow.btn_exit_a)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.lbl_length.setText(QCoreApplication.translate("MainWindow", u"enter length", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"reset", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"exit", None))
        self.btn_area.setText(QCoreApplication.translate("MainWindow", u"find area", None))
        self.lbl_height.setText(QCoreApplication.translate("MainWindow", u"enter height", None))
        self.lbl_answer.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Area finder", None))
    # retranslateUi

