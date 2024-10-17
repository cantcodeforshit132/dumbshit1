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
        MainWindow.resize(917, 850)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(20, 290, 152, 464))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_reset = QPushButton(self.gridLayoutWidget_2)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setMinimumSize(QSize(150, 150))
        font = QFont()
        font.setPointSize(25)
        self.btn_reset.setFont(font)

        self.gridLayout_2.addWidget(self.btn_reset, 1, 0, 1, 1)

        self.btn_start = QPushButton(self.gridLayoutWidget_2)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setMinimumSize(QSize(150, 150))
        self.btn_start.setFont(font)

        self.gridLayout_2.addWidget(self.btn_start, 0, 0, 1, 1)

        self.btn_exit = QPushButton(self.gridLayoutWidget_2)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(150, 150))
        self.btn_exit.setFont(font)

        self.gridLayout_2.addWidget(self.btn_exit, 2, 0, 1, 1)

        self.lbl_winlosstie = QLabel(self.centralwidget)
        self.lbl_winlosstie.setObjectName(u"lbl_winlosstie")
        self.lbl_winlosstie.setGeometry(QRect(160, 30, 701, 251))
        font1 = QFont()
        font1.setPointSize(200)
        font1.setBold(True)
        self.lbl_winlosstie.setFont(font1)
        self.lbl_winlosstie.setAlignment(Qt.AlignCenter)
        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setEnabled(False)
        self.btn_1.setGeometry(QRect(320, 280, 150, 150))
        self.btn_1.setMinimumSize(QSize(150, 150))
        self.btn_1.setMaximumSize(QSize(150, 150))
        font2 = QFont()
        font2.setPointSize(100)
        font2.setBold(True)
        self.btn_1.setFont(font2)
        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setEnabled(False)
        self.btn_2.setGeometry(QRect(470, 280, 150, 150))
        self.btn_2.setMinimumSize(QSize(150, 150))
        self.btn_2.setMaximumSize(QSize(150, 150))
        self.btn_2.setFont(font2)
        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setEnabled(False)
        self.btn_3.setGeometry(QRect(620, 280, 150, 150))
        self.btn_3.setMinimumSize(QSize(150, 150))
        self.btn_3.setMaximumSize(QSize(150, 150))
        self.btn_3.setFont(font2)
        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setEnabled(False)
        self.btn_4.setGeometry(QRect(320, 430, 150, 150))
        self.btn_4.setMinimumSize(QSize(150, 150))
        self.btn_4.setMaximumSize(QSize(150, 150))
        self.btn_4.setFont(font2)
        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setEnabled(False)
        self.btn_5.setGeometry(QRect(470, 430, 150, 150))
        self.btn_5.setMinimumSize(QSize(150, 150))
        self.btn_5.setMaximumSize(QSize(150, 150))
        self.btn_5.setFont(font2)
        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setEnabled(False)
        self.btn_6.setGeometry(QRect(620, 430, 150, 150))
        self.btn_6.setMinimumSize(QSize(150, 150))
        self.btn_6.setMaximumSize(QSize(150, 150))
        self.btn_6.setFont(font2)
        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setEnabled(False)
        self.btn_7.setGeometry(QRect(320, 580, 150, 150))
        self.btn_7.setMinimumSize(QSize(150, 150))
        self.btn_7.setMaximumSize(QSize(150, 150))
        self.btn_7.setFont(font2)
        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setEnabled(False)
        self.btn_8.setGeometry(QRect(470, 580, 150, 150))
        self.btn_8.setMinimumSize(QSize(150, 150))
        self.btn_8.setMaximumSize(QSize(150, 150))
        self.btn_8.setFont(font2)
        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setEnabled(False)
        self.btn_9.setGeometry(QRect(620, 580, 150, 150))
        self.btn_9.setMinimumSize(QSize(150, 150))
        self.btn_9.setMaximumSize(QSize(150, 150))
        self.btn_9.setFont(font2)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(360, 760, 381, 80))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_lose = QLabel(self.gridLayoutWidget)
        self.lbl_lose.setObjectName(u"lbl_lose")
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        self.lbl_lose.setFont(font3)

        self.gridLayout.addWidget(self.lbl_lose, 0, 1, 1, 1)

        self.lbl_win = QLabel(self.gridLayoutWidget)
        self.lbl_win.setObjectName(u"lbl_win")
        self.lbl_win.setFont(font3)

        self.gridLayout.addWidget(self.lbl_win, 0, 0, 1, 1)

        self.lbl_tie = QLabel(self.gridLayoutWidget)
        self.lbl_tie.setObjectName(u"lbl_tie")
        self.lbl_tie.setFont(font3)

        self.gridLayout.addWidget(self.lbl_tie, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_1.clicked.connect(MainWindow.btn_meth4kids_a)
        self.btn_2.clicked.connect(MainWindow.btn_meth4kids_a)
        self.btn_3.clicked.connect(MainWindow.btn_meth4kids_a)
        self.btn_4.clicked.connect(MainWindow.btn_meth4kids_a)
        self.btn_5.clicked.connect(MainWindow.btn_meth4kids_a)
        self.btn_6.clicked.connect(MainWindow.btn_meth4kids_a)
        self.btn_7.clicked.connect(MainWindow.btn_meth4kids_a)
        self.btn_8.clicked.connect(MainWindow.btn_meth4kids_a)
        self.btn_9.clicked.connect(MainWindow.btn_meth4kids_a)
        self.btn_reset.clicked.connect(MainWindow.btn_reset_a)
        self.btn_start.clicked.connect(MainWindow.btn_start_a)
        self.btn_exit.clicked.connect(MainWindow.btn_exit_a)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"reset", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"exit", None))
        self.lbl_winlosstie.setText("")
        self.btn_1.setText("")
        self.btn_2.setText("")
        self.btn_3.setText("")
        self.btn_4.setText("")
        self.btn_5.setText("")
        self.btn_6.setText("")
        self.btn_7.setText("")
        self.btn_8.setText("")
        self.btn_9.setText("")
        self.lbl_lose.setText(QCoreApplication.translate("MainWindow", u"loses", None))
        self.lbl_win.setText(QCoreApplication.translate("MainWindow", u"wins", None))
        self.lbl_tie.setText(QCoreApplication.translate("MainWindow", u"ties", None))
    # retranslateUi

