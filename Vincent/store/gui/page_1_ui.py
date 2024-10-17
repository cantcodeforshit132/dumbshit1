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
        MainWindow.resize(1829, 1256)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(690, 570, 801, 71))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_change = QPushButton(self.gridLayoutWidget_2)
        self.btn_change.setObjectName(u"btn_change")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn_change.setFont(font)

        self.gridLayout_2.addWidget(self.btn_change, 0, 3, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 0))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.txt_cash = QLineEdit(self.gridLayoutWidget_2)
        self.txt_cash.setObjectName(u"txt_cash")
        self.txt_cash.setMinimumSize(QSize(0, 50))

        self.gridLayout_2.addWidget(self.txt_cash, 0, 1, 1, 1)

        self.lbl_due = QLabel(self.gridLayoutWidget_2)
        self.lbl_due.setObjectName(u"lbl_due")
        self.lbl_due.setMinimumSize(QSize(150, 0))
        self.lbl_due.setFont(font)

        self.gridLayout_2.addWidget(self.lbl_due, 0, 2, 1, 1)

        self.lbl_total = QLabel(self.centralwidget)
        self.lbl_total.setObjectName(u"lbl_total")
        self.lbl_total.setGeometry(QRect(770, 250, 611, 221))
        self.lbl_total.setFont(font)
        self.lbl_total.setAlignment(Qt.AlignCenter)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(320, 170, 314, 776))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)

        self.lbl_countlotto = QLabel(self.gridLayoutWidget)
        self.lbl_countlotto.setObjectName(u"lbl_countlotto")
        font2 = QFont()
        font2.setPointSize(15)
        self.lbl_countlotto.setFont(font2)
        self.lbl_countlotto.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_countlotto, 3, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)

        self.lbl_countcandy = QLabel(self.gridLayoutWidget)
        self.lbl_countcandy.setObjectName(u"lbl_countcandy")
        self.lbl_countcandy.setFont(font2)
        self.lbl_countcandy.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_countcandy, 0, 0, 1, 1)

        self.btn_cig = QPushButton(self.gridLayoutWidget)
        self.btn_cig.setObjectName(u"btn_cig")
        self.btn_cig.setMinimumSize(QSize(0, 150))
        self.btn_cig.setFont(font2)

        self.gridLayout.addWidget(self.btn_cig, 4, 2, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 1, 3, 1, 1)

        self.lbl_countcig = QLabel(self.gridLayoutWidget)
        self.lbl_countcig.setObjectName(u"lbl_countcig")
        self.lbl_countcig.setFont(font2)
        self.lbl_countcig.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_countcig, 4, 0, 1, 1)

        self.lbl_countbeer = QLabel(self.gridLayoutWidget)
        self.lbl_countbeer.setObjectName(u"lbl_countbeer")
        self.lbl_countbeer.setFont(font2)
        self.lbl_countbeer.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_countbeer, 2, 0, 1, 1)

        self.lbl_countenergy = QLabel(self.gridLayoutWidget)
        self.lbl_countenergy.setObjectName(u"lbl_countenergy")
        self.lbl_countenergy.setFont(font2)
        self.lbl_countenergy.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_countenergy, 1, 0, 1, 1)

        self.btn_candy = QPushButton(self.gridLayoutWidget)
        self.btn_candy.setObjectName(u"btn_candy")
        self.btn_candy.setMinimumSize(QSize(0, 150))
        self.btn_candy.setFont(font2)

        self.gridLayout.addWidget(self.btn_candy, 0, 2, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 4, 3, 1, 1)

        self.btn_beer = QPushButton(self.gridLayoutWidget)
        self.btn_beer.setObjectName(u"btn_beer")
        self.btn_beer.setMinimumSize(QSize(0, 150))
        self.btn_beer.setFont(font2)

        self.gridLayout.addWidget(self.btn_beer, 2, 2, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 3, 3, 1, 1)

        self.btn_lotto = QPushButton(self.gridLayoutWidget)
        self.btn_lotto.setObjectName(u"btn_lotto")
        self.btn_lotto.setMinimumSize(QSize(0, 150))
        self.btn_lotto.setFont(font2)

        self.gridLayout.addWidget(self.btn_lotto, 3, 2, 1, 1)

        self.btn_energy = QPushButton(self.gridLayoutWidget)
        self.btn_energy.setObjectName(u"btn_energy")
        self.btn_energy.setMinimumSize(QSize(0, 150))
        self.btn_energy.setFont(font2)

        self.gridLayout.addWidget(self.btn_energy, 1, 2, 1, 1)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setGeometry(QRect(910, 700, 201, 141))
        self.btn_clear.setFont(font)
        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(1090, 700, 181, 141))
        self.btn_exit.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_clear.clicked.connect(MainWindow.btn_reset_a)
        self.btn_exit.clicked.connect(MainWindow.btn_exit_a)
        self.btn_candy.clicked.connect(MainWindow.btn_candy_a)
        self.btn_energy.clicked.connect(MainWindow.btn_energy_a)
        self.btn_beer.clicked.connect(MainWindow.btn_beer_a)
        self.btn_lotto.clicked.connect(MainWindow.btn_lotto_a)
        self.btn_cig.clicked.connect(MainWindow.btn_cig_a)
        self.btn_change.clicked.connect(MainWindow.btn_change_a)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.btn_change.setText(QCoreApplication.translate("MainWindow", u"change", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cash", None))
        self.lbl_due.setText(QCoreApplication.translate("MainWindow", u"change due", None))
        self.lbl_total.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"1$", None))
        self.lbl_countlotto.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"12$", None))
        self.lbl_countcandy.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_cig.setText(QCoreApplication.translate("MainWindow", u"ciggeretes ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"4$", None))
        self.lbl_countcig.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_countbeer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_countenergy.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_candy.setText(QCoreApplication.translate("MainWindow", u"candy", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"15$", None))
        self.btn_beer.setText(QCoreApplication.translate("MainWindow", u"beer", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"6$", None))
        self.btn_lotto.setText(QCoreApplication.translate("MainWindow", u"lottory ticket", None))
        self.btn_energy.setText(QCoreApplication.translate("MainWindow", u"energy drinks", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"exit", None))
    # retranslateUi

