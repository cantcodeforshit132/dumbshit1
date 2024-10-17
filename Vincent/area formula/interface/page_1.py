
# By: <vincent>
# Date: 2024-09-23
# Program Details: <area finder>

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

    def btn_area_a(self):
        try:
                x=float(self.txt_length.text())
                y=float(self.txt_height.text())
                answer=x*y
                self.lbl_answer.setText(f"the area is {answer}")
                self.btn_area.setEnabled(False)
                self.btn_reset.setEnabled(True)
        except: self.lbl_answer.setText("this is a calculator not a dictionary stupid")
    def btn_reset_a(self):
        self.lbl_answer.setText("")
        self.txt_height.setText("")
        self.txt_length.setText("")
        self.btn_area.setEnabled(True)
        self.btn_reset.setEnabled(False)
    def btn_exit_a(self):
        exit()