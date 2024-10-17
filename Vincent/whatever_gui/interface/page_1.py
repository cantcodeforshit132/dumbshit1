
# By: <vincent>
# Date: 2024-09-16
# Program Details: <>

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import manager
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow
from gui.page_1_ui import Ui_MainWindow

if __name__ == "__main__":    
    manager.start()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        with manager.image_gui_path():
            self.setupUi(self)
        
    def btn_name_a(self):
        self.label.setText("vincent")
        self.label.setStyleSheet("color: rgb(255, 0, 4);background-color: rgb(0, 0, 0);")
        self.btn_name.setEnabled(False)
        self.btn_reset.setEnabled(True)
        self.btn_date.setEnabled(True)
        self.btn_random100.setEnabled(True)
        self.btn_nothing.setEnabled(True)
        self.lbl_image.setPixmap(QPixmap(u"images/download.jpg"))
    def btn_exit_a(self):
        exit()
  
    def btn_reset_a(self):
        self.label.setText("hello")
        self.label.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.btn_name.setEnabled(True)
        self.btn_reset.setEnabled(False)
        self.btn_date.setEnabled(True)
        self.btn_random100.setEnabled(True)
        self.btn_nothing.setEnabled(True)
        self.lbl_image.setPixmap(QPixmap(u"images/coding.png"))
    def btn_date_a(self):
        self.label.setText("september 20th 2024")
        self.label.setStyleSheet("color: rgb(247, 23, 255);background-color: rgb(25, 255, 247);")
        self.btn_name.setEnabled(True)
        self.btn_reset.setEnabled(True)
        self.btn_date.setEnabled(False)
        self.btn_random100.setEnabled(True)
        self.btn_nothing.setEnabled(True)
        self.lbl_image.setPixmap(QPixmap(u"images/snake.jpg"))
    def btn_random100_a(self):
        self.label.setText("4586386")
        self.label.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(252, 252, 252);")
        self.btn_name.setEnabled(True)
        self.btn_reset.setEnabled(True)
        self.btn_date.setEnabled(True)
        self.btn_random100.setEnabled(False)
        self.btn_nothing.setEnabled(True)
        self.lbl_image.setPixmap(QPixmap(u"images/codingmeme.jpg"))
        
    def btn_nothing_a(self):
        self.label.setText("something happend")
        self.label.setStyleSheet("color: rgb(255, 184, 197);background-color: rgb(255, 183, 66);")
        self.btn_name.setEnabled(True)
        self.btn_reset.setEnabled(True)
        self.btn_date.setEnabled(True)
        self.btn_random100.setEnabled(True)
        self.btn_nothing.setEnabled(False)
        self.lbl_image.setPixmap(QPixmap(u"images/chicken.jpg"))
        
    