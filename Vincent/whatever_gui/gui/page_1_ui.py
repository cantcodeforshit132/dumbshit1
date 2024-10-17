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
        MainWindow.resize(1831, 1261)
        MainWindow.setCursor(QCursor(Qt.OpenHandCursor))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(320, 860, 1171, 119))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_name = QPushButton(self.gridLayoutWidget)
        self.btn_name.setObjectName(u"btn_name")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.btn_name.setFont(font)
        self.btn_name.setStyleSheet(u"background-color: rgb(255, 0, 4);")

        self.gridLayout.addWidget(self.btn_name, 0, 0, 1, 1)

        self.btn_exit = QPushButton(self.gridLayoutWidget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet(u"background-color: rgb(0, 132, 255);")

        self.gridLayout.addWidget(self.btn_exit, 0, 1, 1, 1)

        self.btn_reset = QPushButton(self.gridLayoutWidget)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setFont(font)

        self.gridLayout.addWidget(self.btn_reset, 1, 0, 1, 1)

        self.btn_random100 = QPushButton(self.gridLayoutWidget)
        self.btn_random100.setObjectName(u"btn_random100")
        self.btn_random100.setFont(font)

        self.gridLayout.addWidget(self.btn_random100, 2, 0, 1, 1)

        self.btn_date = QPushButton(self.gridLayoutWidget)
        self.btn_date.setObjectName(u"btn_date")
        self.btn_date.setFont(font)

        self.gridLayout.addWidget(self.btn_date, 1, 1, 1, 1)

        self.btn_nothing = QPushButton(self.gridLayoutWidget)
        self.btn_nothing.setObjectName(u"btn_nothing")
        self.btn_nothing.setFont(font)

        self.gridLayout.addWidget(self.btn_nothing, 2, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(490, 660, 831, 201))
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)
        self.lbl_image = QLabel(self.centralwidget)
        self.lbl_image.setObjectName(u"lbl_image")
        self.lbl_image.setGeometry(QRect(490, 10, 811, 611))
        self.lbl_image.setScaledContents(True)
        self.lbl_image.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_name.clicked.connect(MainWindow.btn_name_a)
        self.btn_exit.clicked.connect(MainWindow.btn_exit_a)
        self.btn_reset.clicked.connect(MainWindow.btn_reset_a)
        self.btn_date.clicked.connect(MainWindow.btn_date_a)
        self.btn_random100.clicked.connect(MainWindow.btn_random100_a)
        self.btn_nothing.clicked.connect(MainWindow.btn_nothing_a)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"blurple", None))
        self.btn_name.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"exit", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"reset", None))
        self.btn_random100.setText(QCoreApplication.translate("MainWindow", u"random num", None))
        self.btn_date.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.btn_nothing.setText(QCoreApplication.translate("MainWindow", u"this does something", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("MainWindow", u"hello", None))
        self.lbl_image.setText("")
    # retranslateUi

