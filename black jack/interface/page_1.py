
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
    
    h1vaule = 0
    
    ph1c1 = random.choice(cards)
    ph1c2 = random.choice(cards)
    h1card1=int(ph1c1[0:2])
    h1card2=int(ph1c2[0:2])
   


        
   
    
    def btn_start_a(self):
        random.shuffle(self.cards)
        ph1c1 = random.choice(self.cards)
        self.lbl_ph11.setPixmap(QPixmap(f"images/{ph1c1}"))
        self.lbl_ph11.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
        self.cards.remove(ph1c1)
        h1card1=int(ph1c1[0:2])
        # print(h1card1)
        ph1c2 = random.choice(self.cards)
        self.lbl_ph12.setPixmap(QPixmap(f"images/{ph1c2}"))
        self.lbl_ph12.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
        self.cards.remove(ph1c2)
        h1card2=int(ph1c2[0:2])
        # print(h1card2)
        self.btn_start.setEnabled(False)
        self.count+=1
        self.h1vaule = h1card1 + h1card2
        # print(self.h1vaule)
        self.lbl_hand1.setText(f"hand 1:{self.h1vaule}")
        if self.h1vaule == 21:
            self.lbl_hand1.setText("hand 1: black jack")
    
    def btn_double_a(self):
        pass
            
    def btn_hit_a(self):
        if self.count==1:
            ph1c3 = random.choice(self.cards)
            self.lbl_ph13.setPixmap(QPixmap(f"images/{ph1c3}"))
            self.cards.remove(ph1c3)
            self.count+=1
            self.lbl_ph13.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
            h1card3=int(ph1c3[0:2])
            self.h1vaule += h1card3
            # print(self.h1vaule)
            self.lbl_hand1.setText(f"hand 1:{self.h1vaule}")
            if self.h1vaule >= 22:
                self.lbl_hand1.setText("hand 1: bust")
                self.btn_hit.setEnabled(False)
            
            
        elif self.count==2:
            ph1c4 = random.choice(self.cards)
            self.lbl_ph14.setPixmap(QPixmap(f"images/{ph1c4}"))
            self.cards.remove(ph1c4)
            self.count+=1
            self.lbl_ph14.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
            h1card4=int(ph1c4[0:2])
            self.h1vaule += h1card4
            # print(self.h1vaule)
            self.h1vaule >= 22
            # print("bust")
            self.lbl_hand1.setText(f"hand 1:{self.h1vaule}")
            if self.h1vaule >= 22:
                self.lbl_hand1.setText("hand 1: bust")
                self.btn_hit.setEnabled(False)
            
        elif self.count==3:
            ph1c5 = random.choice(self.cards)
            self.lbl_ph15.setPixmap(QPixmap(f"images/{ph1c5}"))
            self.cards.remove(ph1c5)
            self.count+=1
            self.lbl_ph15.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
            h1card5=int(ph1c5[0:2])
            self.h1vaule += h1card5
            # print(self.h1vaule)
            self.h1vaule >= 22
            # print("bust")
            self.lbl_hand1.setText(f"hand 1:{self.h1vaule}")
            if self.h1vaule >= 22:
                self.lbl_hand1.setText("hand 1: bust")
                self.btn_hit.setEnabled(False)
            
        elif self.count==4:
            ph1c6 = random.choice(self.cards)
            self.lbl_ph16.setPixmap(QPixmap(f"images/{ph1c6}"))
            self.cards.remove(ph1c6)
            self.count+=1
            self.lbl_ph16.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
            h1card6=int(ph1c6[0:2])
            self.h1vaule += h1card6
            # print(self.h1vaule)
            self.h1vaule >= 22
            # print("bust")
            self.lbl_hand1.setText(f"hand 1:{self.h1vaule}")
            if self.h1vaule >= 22:
                self.lbl_hand1.setText("hand 1: bust")
                self.btn_hit.setEnabled(False)
            
    def btn_stand_a(self):
        self.btn_hit.setEnabled(False)
        self.btn_stand.setEnabled(False)
        
        dhc1 = random.choice(self.cards)
        self.lbl_d1.setPixmap(QPixmap(f"images/{dhc1}"))
        self.lbl_d1.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
        self.cards.remove(dhc1)
        dhc1v = int(dhc1[0:2])
        
        
        dhc2 = random.choice(self.cards)
        self.lbl_d2.setPixmap(QPixmap(f"images/{dhc2}"))
        self.lbl_d2.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
        self.cards.remove(dhc2)
        dhc2v = int(dhc2[0:2])
        dht = dhc1v + dhc2v
        self.lbl_dealer.setText(f"hand value:{dht}")
        
        if dht <=16:
            dhc3 = random.choice(self.cards)
            self.lbl_d3.setPixmap(QPixmap(f"images/{dhc3}"))
            self.lbl_d3.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
            self.cards.remove(dhc3)
            dhc3v = int(dhc3[0:2])
            dht += dhc3v
            self.lbl_dealer.setText(f"hand value:{dht}")
        
        if dht <=16:
            dhc4 = random.choice(self.cards)
            self.lbl_d4.setPixmap(QPixmap(f"images/{dhc4}"))
            self.lbl_d4.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
            self.cards.remove(dhc4)
            dhc4v = int(dhc4[0:2])
            dht += dhc4v
            self.lbl_dealer.setText(f"hand value:{dht}")
        
        if dht <=16:
            dhc5 = random.choice(self.cards)
            self.lbl_d5.setPixmap(QPixmap(f"images/{dhc5}"))
            self.lbl_d5.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
            self.cards.remove(dhc5)
            dhc5v = int(dhc5[0:2])
            dht += dhc5v
            self.lbl_dealer.setText(f"hand value:{dht}")
            
        if dht >= 22:
            self.lbl_dealer.setText("dealer bust")
        
    
    def btn_bet_a(self):
        pass
    
    def btn_split_a(self):
        if self.h1card1 == self.h1card2:
            self.btn_split.setEnabled(False)
            ph1c2 = random.choice(self.cards)
            self.lbl_ph12.setPixmap(QPixmap(f"images/{ph1c2}"))
            self.lbl_ph12.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
            self.cards.remove(ph1c2)
            h1card2=int(ph1c2[0:2])
            self.h1vaule = self.h1card1 + h1card2
            self.lbl_hand1.setText(f"hand 1:{self.h1vaule}")
            
            self.lbl_ph21.setPixmap(QPixmap(f"images/{self.ph1c2}"))
        
            ph2c2 = random.choice(self.cards)
            self.lbl_ph22.setPixmap(QPixmap(f"images/{ph2c2}"))
            self.lbl_ph22.setStyleSheet("background-color: rgb(0,0,0);  border: 3px solid #000000;")
            self.cards.remove(ph2c2)
            h1card2=int(ph2c2[0:2])
        
    
    def btn_exit_a(self):
        exit()
        
    def btn_hand1_a(self):
        pass
    
    def btn_hand2_a(self):
        pass
    
    def btn_hand3_a(self):
        pass
    
    def btn_hand4_a(self):
        pass