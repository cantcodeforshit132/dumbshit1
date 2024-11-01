
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
    
    
    
    cards = ["02_of_clubs.png","02_of_diamonds.png","02_of_hearts.png","02_of_spades.png","03_of_clubs.png","03_of_diamonds.png","03_of_hearts.png","03_of_spades.png","04_of_clubs.png","04_of_diamonds.png","04_of_hearts.png","04_of_spades.png","05_of_clubs.png","05_of_diamonds.png","05_of_hearts.png","05_of_spades.png","06_of_clubs.png","06_of_diamonds.png","06_of_hearts.png","06_of_spades.png","07_of_clubs.png","07_of_diamonds.png","07_of_hearts.png","07_of_spades.png","08_of_clubs.png","08_of_diamonds.png","08_of_hearts.png","08_of_spades.png","09_of_clubs.png","09_of_diamonds.png","09_of_hearts.png","09_of_spades.png","10_jack_of_clubs.png","10_jack_of_diamonds.png","10_jack_of_hearts.png","10_jack_of_spades.png","10_king_of_clubs.png","10_king_of_diamonds.png","10_king_of_hearts.png","10_king_of_spades.png","10_of_clubs.png","10_of_diamonds.png","10_of_hearts.png","10_of_spades.png","10_queen_of_clubs.png","10_queen_of_diamonds.png","10_queen_of_hearts.png","10_queen_of_spades.png","11_ace_of_clubs.png","11_ace_of_diamonds.png","11_ace_of_hearts.png","11_ace_of_spades.png"]
    backupcards = ["02_of_clubs.png","02_of_diamonds.png","02_of_hearts.png","02_of_spades.png","03_of_clubs.png","03_of_diamonds.png","03_of_hearts.png","03_of_spades.png","04_of_clubs.png","04_of_diamonds.png","04_of_hearts.png","04_of_spades.png","05_of_clubs.png","05_of_diamonds.png","05_of_hearts.png","05_of_spades.png","06_of_clubs.png","06_of_diamonds.png","06_of_hearts.png","06_of_spades.png","07_of_clubs.png","07_of_diamonds.png","07_of_hearts.png","07_of_spades.png","08_of_clubs.png","08_of_diamonds.png","08_of_hearts.png","08_of_spades.png","09_of_clubs.png","09_of_diamonds.png","09_of_hearts.png","09_of_spades.png","10_jack_of_clubs.png","10_jack_of_diamonds.png","10_jack_of_hearts.png","10_jack_of_spades.png","10_king_of_clubs.png","10_king_of_diamonds.png","10_king_of_hearts.png","10_king_of_spades.png","10_of_clubs.png","10_of_diamonds.png","10_of_hearts.png","10_of_spades.png","10_queen_of_clubs.png","10_queen_of_diamonds.png","10_queen_of_hearts.png","10_queen_of_spades.png","11_ace_of_clubs.png","11_ace_of_diamonds.png","11_ace_of_hearts.png","11_ace_of_spades.png"]
    
    count=0
    
   
    
    def btn_start_a(self):
        random.shuffle(self.cards)
        ph1c1 = random.choice(self.cards)
        self.lbl_ph11.setPixmap(QPixmap(f"images/{ph1c1}"))
        self.lbl_ph11.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
        self.cards.remove(ph1c1)
        value1=int(ph1c1[0:2])
        print(value1)
        ph1c2 = random.choice(self.cards)
        self.lbl_ph12.setPixmap(QPixmap(f"images/{ph1c2}"))
        self.lbl_ph12.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
        self.cards.remove(ph1c2)
        value2=int(ph1c2[0:2])
        print(value2)
        self.btn_start.setEnabled(False)
        self.count+=1
        hvaule= value1 + value2
        print(hvaule)
    
    def btn_double_a(self):
        pass
            
    def btn_hit_a(self):
        if self.count==1:
            a = random.choice(self.cards)
            self.lbl_ph13.setPixmap(QPixmap(f"images/{a}"))
            self.cards.remove(a)
            self.count+=1
            self.lbl_ph13.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
        
        elif self.count==2:
            a = random.choice(self.cards)
            self.lbl_ph14.setPixmap(QPixmap(f"images/{a}"))
            self.cards.remove(a)
            self.count+=1
            self.lbl_ph14.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
            
        elif self.count==3:
            a = random.choice(self.cards)
            self.lbl_ph15.setPixmap(QPixmap(f"images/{a}"))
            self.cards.remove(a)
            self.count+=1
            self.lbl_ph15.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
            
        elif self.count==4:
            a = random.choice(self.cards)
            self.lbl_ph16.setPixmap(QPixmap(f"images/{a}"))
            self.cards.remove(a)
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