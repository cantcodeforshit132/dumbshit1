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
        MainWindow.resize(780, 302)
        MainWindow.setWindowOpacity(0.000000000000000)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(50, 70, 681, 140))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.txt_cm = QLineEdit(self.gridLayoutWidget)
        self.txt_cm.setObjectName(u"txt_cm")
        self.txt_cm.setMaximumSize(QSize(250, 16777215))

        self.gridLayout.addWidget(self.txt_cm, 2, 1, 1, 1)

        self.txt_m = QLineEdit(self.gridLayoutWidget)
        self.txt_m.setObjectName(u"txt_m")
        self.txt_m.setMaximumSize(QSize(250, 16777215))

        self.gridLayout.addWidget(self.txt_m, 1, 1, 1, 1)

        self.lbl_ft = QLabel(self.gridLayoutWidget)
        self.lbl_ft.setObjectName(u"lbl_ft")

        self.gridLayout.addWidget(self.lbl_ft, 1, 2, 1, 1)

        self.lbl_in = QLabel(self.gridLayoutWidget)
        self.lbl_in.setObjectName(u"lbl_in")

        self.gridLayout.addWidget(self.lbl_in, 2, 2, 1, 1)

        self.btn_mf = QPushButton(self.gridLayoutWidget)
        self.btn_mf.setObjectName(u"btn_mf")

        self.gridLayout.addWidget(self.btn_mf, 0, 0, 1, 1)

        self.btn_cmin = QPushButton(self.gridLayoutWidget)
        self.btn_cmin.setObjectName(u"btn_cmin")

        self.gridLayout.addWidget(self.btn_cmin, 3, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setBold(True)
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(410, 210, 207, 41))
        font2 = QFont()
        font2.setPointSize(15)
        self.btn_exit.setFont(font2)
        self.btn_reset = QPushButton(self.centralwidget)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setGeometry(QRect(210, 210, 207, 41))
        self.btn_reset.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_mf.clicked.connect(MainWindow.btn_meters_a)
        self.btn_cmin.clicked.connect(MainWindow.btn_centimeters_a)
        self.btn_exit.clicked.connect(MainWindow.btn_exit_a)
        self.btn_reset.clicked.connect(MainWindow.btn_reset_a)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"centimeters -> inches", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"meters -> feet", None))
        self.lbl_ft.setText(QCoreApplication.translate("MainWindow", u"feet", None))
        self.lbl_in.setText(QCoreApplication.translate("MainWindow", u"inches", None))
        self.btn_mf.setText(QCoreApplication.translate("MainWindow", u"convert m->ft", None))
        self.btn_cmin.setText(QCoreApplication.translate("MainWindow", u"convert cm->in", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"meters", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"centimeters", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"exit", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"reset", None))
    # retranslateUi

