
# By: <Your Name Here>
# Date: 2024-10-02
# Program Details: <Program Description Here>

import os, sys, math
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


    def btn_exit_a(self):
        exit()
    
    def btn_meters_a(self):
        try:
            x=float(self.txt_m.text())
            self.lbl_ft.setText(f"feet {x*3.281}")
        except:  self.lbl_ft.setText("number only fumb duck")  
    def btn_centimeters_a(self):
        try:
            x=float(self.txt_cm.text())
            self.lbl_in.setText(f"inches {x*2.54}")
        except: self.lbl_in.setText("number only fumb duck")    
    
    def btn_reset_a(self):
        self.lbl_ft.setText("feet")
        self.lbl_in.setText("inches")
        self.txt_cm.setText("")
        self.txt_m.setText("")