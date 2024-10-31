
# By: <vincent>
# Date: 2024-10-28
# Program Details: <black jack>

import os, sys, random
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
    
    
    
    cards = ["images/02_of_clubs.png","images/02_of_diamonds.png","images/02_of_hearts.png","images/02_of_spades.png","images/03_of_clubs.png","images/03_of_diamonds.png","images/03_of_hearts.png","images/03_of_spades.png","images/04_of_clubs.png","images/04_of_diamonds.png","images/04_of_hearts.png","images/04_of_spades.png","images/05_of_clubs.png","images/05_of_diamonds.png","images/05_of_hearts.png","images/05_of_spades.png","images/06_of_clubs.png","images/06_of_diamonds.png","images/06_of_hearts.png","images/06_of_spades.png","images/07_of_clubs.png","images/07_of_diamonds.png","images/07_of_hearts.png","images/07_of_spades.png","images/08_of_clubs.png","images/08_of_diamonds.png","images/08_of_hearts.png","images/08_of_spades.png","images/09_of_clubs.png","images/09_of_diamonds.png","images/09_of_hearts.png","images/09_of_spades.png","images/10_jack_of_clubs.png","images/10_jack_of_diamonds.png","images/10_jack_of_hearts.png","images/10_jack_of_spades.png","images/10_king_of_clubs.png","images/10_king_of_diamonds.png","images/10_king_of_hearts.png","images/10_king_of_spades.png","images/10_of_clubs.png","images/10_of_diamonds.png","images/10_of_hearts.png","images/10_of_spades.png","images/10_queen_of_clubs.png","images/10_queen_of_diamonds.png","images/10_queen_of_hearts.png","images/10_queen_of_spades.png","images/11_ace_of_clubs.png","images/11_ace_of_diamonds.png","images/11_ace_of_hearts.png","images/11_ace_of_spades.png"]
    backupcards = ["images/02_of_clubs.png","images/02_of_diamonds.png","images/02_of_hearts.png","images/02_of_spades.png","images/03_of_clubs.png","images/03_of_diamonds.png","images/03_of_hearts.png","images/03_of_spades.png","images/04_of_clubs.png","images/04_of_diamonds.png","images/04_of_hearts.png","images/04_of_spades.png","images/05_of_clubs.png","images/05_of_diamonds.png","images/05_of_hearts.png","images/05_of_spades.png","images/06_of_clubs.png","images/06_of_diamonds.png","images/06_of_hearts.png","images/06_of_spades.png","images/07_of_clubs.png","images/07_of_diamonds.png","images/07_of_hearts.png","images/07_of_spades.png","images/08_of_clubs.png","images/08_of_diamonds.png","images/08_of_hearts.png","images/08_of_spades.png","images/09_of_clubs.png","images/09_of_diamonds.png","images/09_of_hearts.png","images/09_of_spades.png","images/10_jack_of_clubs.png","images/10_jack_of_diamonds.png","images/10_jack_of_hearts.png","images/10_jack_of_spades.png","images/10_king_of_clubs.png","images/10_king_of_diamonds.png","images/10_king_of_hearts.png","images/10_king_of_spades.png","images/10_of_clubs.png","images/10_of_diamonds.png","images/10_of_hearts.png","images/10_of_spades.png","images/10_queen_of_clubs.png","images/10_queen_of_diamonds.png","images/10_queen_of_hearts.png","images/10_queen_of_spades.png","images/11_ace_of_clubs.png","images/11_ace_of_diamonds.png","images/11_ace_of_hearts.png","images/11_ace_of_spades.png"]
    
    
    count=0
    
    def btn_start_a(self):
        random.shuffle(self.cards)
        self.lbl_ph11.setPixmap(QPixmap(f"{self.cards[0]}"))
        self.lbl_ph11.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
        self.cards.pop(0)
        self.lbl_ph12.setPixmap(QPixmap(f"{self.cards[0]}"))
        self.lbl_ph12.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
        self.cards.pop(0)
        self.btn_start.setEnabled(False)
        self.count+=1
    
    def btn_double_a(self):
        pass
            
    def btn_hit_a(self):
        if self.count==1:
            self.lbl_ph13.setPixmap(QPixmap(f"{self.cards[0]}"))
            self.cards.pop(0)
            self.count+=1
            self.lbl_ph13.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
        
        elif self.count==2:
            self.lbl_ph14.setPixmap(QPixmap(f"{self.cards[0]}"))
            self.cards.pop(0)
            self.count+=1
            self.lbl_ph14.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
            
        elif self.count==3:
            self.lbl_ph15.setPixmap(QPixmap(f"{self.cards[0]}"))
            self.cards.pop(0)
            self.count+=1
            self.lbl_ph15.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
            
        elif self.count==4:
            self.lbl_ph16.setPixmap(QPixmap(f"{self.cards[0]}"))
            self.cards.pop(0)
            self.count+=1
            self.lbl_ph16.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
    
    def btn_stand_a(self):
        pass
    
    def btn_bet_a(self):
        pass
    
    def btn_split_a(self):
        pass
    
    def btn_exit_a(self):
        exit()