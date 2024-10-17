
# By: <Your Name Here>
# Date: 2024-10-01
# Program Details: <Program Description Here>

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

    cig=0
    lotto=0
    beer=0
    candy=0
    energy=0
    total=0
    def btn_cig_a(self):
        self.total=self.total+15
        self.lbl_total.setText(f"{self.total}$")
        self.cig=self.cig+1
        self.lbl_countcig.setText(str(self.cig))
        
    def btn_lotto_a(self):
        self.total=self.total+6
        self.lbl_total.setText(f"{self.total}$")
        self.lotto=self.lotto+1
        self.lbl_countlotto.setText(str(self.lotto))
    
    def btn_beer_a(self):
        self.total=self.total+12
        self.lbl_total.setText(f"{self.total}$")
        self.beer=self.beer+1
        self.lbl_countbeer.setText(str(self.beer))
    
    def btn_energy_a(self):
        self.total=self.total+4
        self.lbl_total.setText(f"{self.total}$")
        self.energy=self.energy+1
        self.lbl_countenergy.setText(str(self.energy))
    
    def btn_candy_a(self):
        self.total=self.total+1
        self.lbl_total.setText(f"{self.total}$")
        self.candy=self.candy+1
        self.lbl_countcandy.setText(str(self.candy))
    
    def btn_change_a(self):
        try:
            cash=self.txt_cash.text()
            change=float(cash)-self.total
            self.lbl_due.setText(f"{'{0:.2f}'.format(change)}")
        except: self.lbl_due.setText("CASH ONLY RETARD ")
            
    def btn_exit_a(self):
        exit()
    
    def btn_reset_a(self):
        self.lbl_total.setText("total")
        self.cig=0
        self.lotto=0
        self.beer=0
        self.candy=0
        self.energy=0
        self.total=0
        self.lbl_countcig.setText("0")
        self.lbl_countlotto.setText("0")
        self.lbl_countbeer.setText("0")
        self.lbl_countenergy.setText("0")
        self.lbl_countcandy.setText("0")
        self.lbl_due.setText("0")
        self.txt_cash.setText("")
