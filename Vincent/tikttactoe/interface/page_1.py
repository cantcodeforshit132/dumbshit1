
# By: <vincent>
# Date: 2024-10-02
# Program Details: <thic thac thoe>

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
    
    turn = 1
    
    win=0
    lose=0
    tie=0
    
    def btn_exit_a(self):
        exit()
    
    def btn_start_a(self):
        self.btn_1.setEnabled(True)
        self.btn_2.setEnabled(True)
        self.btn_3.setEnabled(True)
        self.btn_4.setEnabled(True)
        self.btn_5.setEnabled(True)
        self.btn_6.setEnabled(True)
        self.btn_7.setEnabled(True)
        self.btn_8.setEnabled(True)
        self.btn_9.setEnabled(True)
        self.btn_start.setEnabled(False)
    
    def btn_reset_a(self):
        self.btn_1.setEnabled(False)
        self.btn_2.setEnabled(False)
        self.btn_3.setEnabled(False)
        self.btn_4.setEnabled(False)
        self.btn_5.setEnabled(False)
        self.btn_6.setEnabled(False)
        self.btn_7.setEnabled(False)
        self.btn_8.setEnabled(False)
        self.btn_9.setEnabled(False)
        self.btn_start.setEnabled(True)
        self.btn_1.setText("")
        self.btn_2.setText("")
        self.btn_3.setText("")
        self.btn_4.setText("")
        self.btn_5.setText("")
        self.btn_6.setText("")
        self.btn_7.setText("")
        self.btn_8.setText("")
        self.btn_9.setText("")
        self.lbl_winlosstie.setText("")
        self.turn=1
        
    def btn_meth4kids_a(self):
        btn=self.sender()
        btn.setText("X")
        btn.setEnabled(False)
        self.ai()
        self.win_check()
        
    def ai(self):
        cornernum=random.randint(1,4)
        
        if self.btn_5.text() == "X" and self.turn == 1:
        
            if cornernum == 1:
                self.btn_1.setText("O")
                self.btn_1.setEnabled(False)
                
            elif cornernum == 2:
                self.btn_3.setText("O")
                self.btn_3.setEnabled(False)
                
            elif cornernum == 3:
                self.btn_7.setText("O")
                self.btn_7.setEnabled(False)
                
            elif cornernum == 4:
                self.btn_9.setText("O")
                self.btn_9.setEnabled(False)
            self.turn += 1
                
        if self.btn_5.text() == "" and self.turn == 1:
            self.btn_5.setText("O")
            self.btn_5.setEnabled(False)
            self.turn += 1
                
        if self.turn == 2:
            
             #right three
            if self.btn_1.text() == "O" and self.btn_2.text() == "O" and self.btn_3.text() == "":
                self.btn_3.setText("O")
                self.btn_3.setEnabled(False)
            elif self.btn_4.text() == "O" and self.btn_5.text() == "O" and self.btn_6.text() == "":
                self.btn_6.setText("O")
                self.btn_6.setEnabled(False)
            elif self.btn_7.text() == "O" and self.btn_8.text() == "O" and self.btn_9.text() == "":
                self.btn_9.setText("O")
                self.btn_9.setEnabled(False)    
            #left three
            elif self.btn_6.text() == "O" and self.btn_5.text() == "O" and self.btn_4.text() == "":
                self.btn_4.setText("O")
                self.btn_4.setEnabled(False)
            elif self.btn_3.text() == "O" and self.btn_2.text() == "O" and self.btn_1.text() == "":
                self.btn_1.setText("O")
                self.btn_1.setEnabled(False)
            elif self.btn_9.text() == "O" and self.btn_8.text() == "O" and self.btn_7.text() == "":
                self.btn_7.setText("O")
                self.btn_7.setEnabled(False)
            #bottom three
            elif self.btn_1.text() == "O" and self.btn_4.text() == "O" and self.btn_7.text() == "":
                self.btn_7.setText("O")
                self.btn_7.setEnabled(False)
            elif self.btn_2.text() == "O" and self.btn_5.text() == "O" and self.btn_8.text() == "":
                self.btn_8.setText("O")
                self.btn_8.setEnabled(False)
            elif self.btn_3.text() == "O" and self.btn_6.text() == "O" and self.btn_9.text() == "":
                self.btn_9.setText("O")
                self.btn_9.setEnabled(False)   
            #top three
            elif self.btn_7.text() == "O" and self.btn_4.text() == "O" and self.btn_1.text() == "":
                self.btn_1.setText("O")
                self.btn_1.setEnabled(False)
            elif self.btn_8.text() == "O" and self.btn_5.text() == "O" and self.btn_2.text() == "":
                self.btn_2.setText("O")
                self.btn_2.setEnabled(False)
            elif self.btn_9.text() == "O" and self.btn_6.text() == "O" and self.btn_3.text() == "":
                self.btn_3.setText("O")
                self.btn_3.setEnabled(False)
            # H middle 2
            elif self.btn_1.text() == "O" and self.btn_3.text() == "O" and self.btn_2.text() == "":
                self.btn_2.setText("O")
                self.btn_2.setEnabled(False)
            elif self.btn_7.text() == "O" and self.btn_9.text() == "O" and self.btn_8.text() == "":
                self.btn_8.setText("O")
                self.btn_8.setEnabled(False)
            # V middle 2
            elif self.btn_1.text() == "O" and self.btn_7.text() == "O" and self.btn_4.text() == "":
                self.btn_4.setText("O")
                self.btn_4.setEnabled(False)
            elif self.btn_3.text() == "O" and self.btn_9.text() == "O" and self.btn_6.text() == "":
                self.btn_6.setText("O")
                self.btn_6.setEnabled(False)
            # D middle
            elif self.btn_3.text() == "O" and self.btn_7.text() == "O" and self.btn_2.text() == "":
                self.btn_2.setText("O")
                self.btn_2.setEnabled(False)
            elif self.btn_1.text() == "O" and self.btn_9.text() == "O" and self.btn_2.text() == "":
                self.btn_2.setText("O")
                self.btn_2.setEnabled(False)
            # diagnols
            elif self.btn_1.text() == "O" and self.btn_5.text() == "O" and self.btn_9.text() == "":
                self.btn_9.setText("O")
                self.btn_9.setEnabled(False)
            elif self.btn_3.text() == "O" and self.btn_5.text() == "O" and self.btn_7.text() == "":
                self.btn_7.setText("O")
                self.btn_7.setEnabled(False)
            elif self.btn_7.text() == "O" and self.btn_5.text() == "O" and self.btn_3.text() == "":
                self.btn_3.setText("O")
                self.btn_3.setEnabled(False)
            elif self.btn_9.text() == "O" and self.btn_5.text() == "O" and self.btn_1.text() == "":
                self.btn_1.setText("O")
                self.btn_1.setEnabled(False)
            #weird t thang
            elif self.btn_1.text() == "O" and self.btn_6.text() == "O" and self.btn_7.text() == "O"  and self.btn_2.text() == "":
                self.btn_2.setText("O")
                self.btn_2.setEnabled(False)
            elif self.btn_3.text() == "O" and self.btn_4.text() == "O" and self.btn_9.text() == "O"  and self.btn_2.text() == "":
                self.btn_2.setText("O")
                self.btn_2.setEnabled(False)
            elif self.btn_7.text() == "O" and self.btn_9.text() == "O" and self.btn_2.text() == "O"  and self.btn_4.text() == "":
                self.btn_4.setText("O")
                self.btn_4.setEnabled(False)
            elif self.btn_1.text() == "O" and self.btn_3.text() == "O" and self.btn_8.text() == "O"  and self.btn_4.text() == "":
                self.btn_4.setText("O")
                self.btn_4.setEnabled(False)
           
           
           
            #right three
            elif self.btn_1.text() == "X" and self.btn_2.text() == "X" and self.btn_3.text() == "":
                self.btn_3.setText("O")
                self.btn_3.setEnabled(False)
            elif self.btn_4.text() == "X" and self.btn_5.text() == "X" and self.btn_6.text() == "":
                self.btn_6.setText("O")
                self.btn_6.setEnabled(False)
            elif self.btn_7.text() == "X" and self.btn_8.text() == "X" and self.btn_9.text() == "":
                self.btn_9.setText("O")
                self.btn_9.setEnabled(False)    
            #left three
            elif self.btn_6.text() == "X" and self.btn_5.text() == "X" and self.btn_4.text() == "":
                self.btn_4.setText("O")
                self.btn_4.setEnabled(False)
            elif self.btn_3.text() == "X" and self.btn_2.text() == "X" and self.btn_1.text() == "":
                self.btn_1.setText("O")
                self.btn_1.setEnabled(False)
            elif self.btn_9.text() == "X" and self.btn_8.text() == "X" and self.btn_7.text() == "":
                self.btn_7.setText("O")
                self.btn_7.setEnabled(False)
            #bottom three
            elif self.btn_1.text() == "X" and self.btn_4.text() == "X" and self.btn_7.text() == "":
                self.btn_7.setText("O")
                self.btn_7.setEnabled(False)
            elif self.btn_2.text() == "X" and self.btn_5.text() == "X" and self.btn_8.text() == "":
                self.btn_8.setText("O")
                self.btn_8.setEnabled(False)
            elif self.btn_3.text() == "X" and self.btn_6.text() == "X" and self.btn_9.text() == "":
                self.btn_9.setText("O")
                self.btn_9.setEnabled(False)   
            #top three
            elif self.btn_7.text() == "X" and self.btn_4.text() == "X" and self.btn_1.text() == "":
                self.btn_1.setText("O")
                self.btn_1.setEnabled(False)
            elif self.btn_8.text() == "X" and self.btn_5.text() == "X" and self.btn_2.text() == "":
                self.btn_2.setText("O")
                self.btn_2.setEnabled(False)
            elif self.btn_9.text() == "X" and self.btn_6.text() == "X" and self.btn_3.text() == "":
                self.btn_3.setText("O")
                self.btn_3.setEnabled(False)
            # H middle 2
            elif self.btn_1.text() == "X" and self.btn_3.text() == "X" and self.btn_2.text() == "":
                self.btn_2.setText("O")
                self.btn_2.setEnabled(False)
            elif self.btn_7.text() == "X" and self.btn_9.text() == "X" and self.btn_8.text() == "":
                self.btn_8.setText("O")
                self.btn_8.setEnabled(False)
            # V middle 2
            elif self.btn_1.text() == "X" and self.btn_7.text() == "X" and self.btn_4.text() == "":
                self.btn_4.setText("O")
                self.btn_4.setEnabled(False)
            elif self.btn_3.text() == "X" and self.btn_9.text() == "X" and self.btn_6.text() == "":
                self.btn_6.setText("O")
                self.btn_6.setEnabled(False)
            # D middle
            elif self.btn_3.text() == "X" and self.btn_7.text() == "X" and self.btn_2.text() == "":
                self.btn_2.setText("O")
                self.btn_2.setEnabled(False)
            elif self.btn_1.text() == "X" and self.btn_9.text() == "X" and self.btn_2.text() == "":
                self.btn_2.setText("O")
                self.btn_2.setEnabled(False)
            # diagnols
            elif self.btn_1.text() == "X" and self.btn_5.text() == "X" and self.btn_9.text() == "":
                self.btn_9.setText("O")
                self.btn_9.setEnabled(False)
            elif self.btn_1.text() == "X" and self.btn_5.text() == "X" and self.btn_9.text() == "O":
                self.btn_3.setText("O")
                self.btn_3.setEnabled(False)
            elif self.btn_3.text() == "X" and self.btn_5.text() == "X" and self.btn_7.text() == "":
                self.btn_7.setText("O")
                self.btn_7.setEnabled(False)
            elif self.btn_3.text() == "X" and self.btn_5.text() == "X" and self.btn_7.text() == "O":
                self.btn_1.setText("O")
                self.btn_1.setEnabled(False)
            elif self.btn_7.text() == "X" and self.btn_5.text() == "X" and self.btn_3.text() == "":
                self.btn_3.setText("O")
                self.btn_3.setEnabled(False)
            elif self.btn_7.text() == "X" and self.btn_5.text() == "X" and self.btn_3.text() == "O":
                self.btn_9.setText("O")
                self.btn_9.setEnabled(False)
            elif self.btn_9.text() == "X" and self.btn_5.text() == "X" and self.btn_1.text() == "":
                self.btn_1.setText("O")
                self.btn_1.setEnabled(False)
            elif self.btn_9.text() == "X" and self.btn_5.text() == "X" and self.btn_1.text() == "O":
                self.btn_7.setText("O")
                self.btn_7.setEnabled(False)
            #weird t thang
            elif self.btn_1.text() == "X" and self.btn_6.text() == "X" and self.btn_7.text() == "X"  and self.btn_2.text() == "":
                self.btn_2.setText("O")
                self.btn_2.setEnabled(False)
            elif self.btn_3.text() == "X" and self.btn_4.text() == "X" and self.btn_9.text() == "X"  and self.btn_2.text() == "":
                self.btn_2.setText("O")
                self.btn_2.setEnabled(False)
            elif self.btn_7.text() == "X" and self.btn_9.text() == "X" and self.btn_2.text() == "X"  and self.btn_4.text() == "":
                self.btn_4.setText("O")
                self.btn_4.setEnabled(False)
            elif self.btn_1.text() == "X" and self.btn_3.text() == "X" and self.btn_8.text() == "X"  and self.btn_4.text() == "":
                self.btn_4.setText("O")
                self.btn_4.setEnabled(False)
            # dumb shit dustin trys
            elif self.btn_1.text() == "X" and self.btn_8.text() == "X" and self.btn_7.text() == "":
                self.btn_7.setText("O")
                self.btn_7.setEnabled(False)
            elif self.btn_1.text() == "X" and self.btn_6.text() == "X" and self.btn_3.text() == "":
                self.btn_3.setText("O")
                self.btn_3.setEnabled(False)
            elif self.btn_3.text() == "X" and self.btn_8.text() == "X" and self.btn_9.text() == "":
                self.btn_9.setText("O")
                self.btn_9.setEnabled(False)
            elif self.btn_3.text() == "X" and self.btn_4.text() == "X" and self.btn_1.text() == "":
                self.btn_1.setText("O")
                self.btn_1.setEnabled(False)
            elif self.btn_7.text() == "X" and self.btn_6.text() == "X" and self.btn_1.text() == "":
                self.btn_1.setText("O")
                self.btn_1.setEnabled(False)
            elif self.btn_7.text() == "X" and self.btn_2.text() == "X" and self.btn_1.text() == "":
                self.btn_1.setText("O")
                self.btn_1.setEnabled(False)
            elif self.btn_9.text() == "X" and self.btn_4.text() == "X" and self.btn_3.text() == "":
                self.btn_3.setText("O")
                self.btn_3.setEnabled(False)
            elif self.btn_9.text() == "X" and self.btn_2.text() == "X" and self.btn_3.text() == "":
                self.btn_3.setText("O")
                self.btn_3.setEnabled(False)
            
            elif self.btn_2.text() == "X" and self.btn_8.text() == "X" and self.btn_1.text() == "":
                self.btn_1.setText("O")
                self.btn_1.setEnabled(False)
            elif self.btn_4.text() == "X" and self.btn_6.text() == "X" and self.btn_3.text() == "":
                self.btn_3.setText("O")
                self.btn_3.setEnabled(False)
            # jaydens dumb shit (playtested scenarios)
            elif self.btn_2.text() == "X" and self.btn_4.text() == "X" and self.btn_1.text() == "":
                self.btn_1.setText("O")
                self.btn_1.setEnabled(False)
            elif self.btn_2.text() == "X" and self.btn_6.text() == "X" and self.btn_3.text() == "":
                self.btn_3.setText("O")
                self.btn_3.setEnabled(False)
            elif self.btn_4.text() == "X" and self.btn_8.text() == "X" and self.btn_7.text() == "":
                self.btn_7.setText("O")
                self.btn_7.setEnabled(False)
            elif self.btn_8.text() == "X" and self.btn_6.text() == "X" and self.btn_9.text() == "":
                self.btn_9 .setText("O")
                self.btn_9.setEnabled(False)
    def win_check(self):
        #HORIZONTAL LINES
        if self.btn_1.text() == "X" and self.btn_2.text() == "X" and self.btn_3.text() == "X":
            self.lbl_winlosstie.setText("WIN")
            self.win=self.win+1
            self.lbl_win.setText(f"wins {self.win}")
        elif self.btn_4.text() == "X" and self.btn_5.text() == "X" and self.btn_6.text() == "X":
            self.lbl_winlosstie.setText("WIN")
            self.win=self.win+1
            self.lbl_win.setText(f"wins {self.win}")
        elif self.btn_7.text() == "X" and self.btn_8.text() == "X" and self.btn_9.text() == "X":
            self.lbl_winlosstie.setText("WIN")
            self.win=self.win+1
            self.lbl_win.setText(f"wins {self.win}")
        #VERTICAL LINES
        elif self.btn_1.text() == "X" and self.btn_4.text() == "X" and self.btn_7.text() == "X":
            self.lbl_winlosstie.setText("WIN")
            self.win=self.win+1
            self.lbl_win.setText(f"wins {self.win}")
        elif self.btn_2.text() == "X" and self.btn_5.text() == "X" and self.btn_8.text() == "X":
            self.lbl_winlosstie.setText("WIN")
            self.win=self.win+1
            self.lbl_win.setText(f"wins {self.win}")
        elif self.btn_3.text() == "X" and self.btn_6.text() == "X" and self.btn_9.text() == "X":
            self.lbl_winlosstie.setText("WIN")
            self.win=self.win+1
            self.lbl_win.setText(f"wins {self.win}")
        #DIAGONAL LINES
        elif self.btn_1.text() == "X" and self.btn_5.text() == "X" and self.btn_9.text() == "X":
            self.lbl_winlosstie.setText("WIN")
            self.win=self.win+1
            self.lbl_win.setText(f"wins {self.win}")
        elif self.btn_7.text() == "X" and self.btn_5.text() == "X" and self.btn_3.text() == "X":
            self.lbl_winlosstie.setText("WIN")
            self.win=self.win+1
            self.lbl_win.setText(f"wins {self.win}")
            
        #AI
        if self.btn_1.text() == "O" and self.btn_2.text() == "O" and self.btn_3.text() == "O":
            self.lbl_winlosstie.setText("LOSE")
            self.lose=self.lose+1
            self.lbl_lose.setText(f"loses {self.lose}")
        elif self.btn_4.text() == "O" and self.btn_5.text() == "O" and self.btn_6.text() == "O":
            self.lbl_winlosstie.setText("LOSE")
            self.lose=self.lose+1
            self.lbl_lose.setText(f"loses {self.lose}")
        elif self.btn_7.text() == "O" and self.btn_8.text() == "O" and self.btn_9.text() == "O":
            self.lbl_winlosstie.setText("LOSE")
            self.lose=self.lose+1
            self.lbl_lose.setText(f"loses {self.lose}")
        #VERTICAL LINES
        elif self.btn_1.text() == "O" and self.btn_4.text() == "O" and self.btn_7.text() == "O":
            self.lbl_winlosstie.setText("LOSE")
            self.lose=self.lose+1
            self.lbl_lose.setText(f"loses {self.lose}")
        elif self.btn_2.text() == "O" and self.btn_5.text() == "O" and self.btn_8.text() == "O":
            self.lbl_winlosstie.setText("LOSE")
            self.lose=self.lose+1
            self.lbl_lose.setText(f"loses {self.lose}")
        elif self.btn_3.text() == "O" and self.btn_6.text() == "O" and self.btn_9.text() == "O":
            self.lbl_winlosstie.setText("LOSE")
            self.lose=self.lose+1
            self.lbl_lose.setText(f"loses {self.lose}")
        #DIAGONAL LINES
        elif self.btn_1.text() == "O" and self.btn_5.text() == "O" and self.btn_9.text() == "O":
            self.lbl_winlosstie.setText("LOSE")
            self.lose=self.lose+1
            self.lbl_lose.setText(f"loses {self.lose}")
        elif self.btn_7.text() == "O" and self.btn_5.text() == "O" and self.btn_3.text() == "O":
            self.lbl_winlosstie.setText("LOSE")
            self.lose=self.lose+1
            self.lbl_lose.setText(f"loses {self.lose}")
            
        #DRAW 
        elif self.btn_1.text() != "" and self.btn_2.text() != "" and self.btn_3.text() != "" and self.btn_4.text() != "" and self.btn_5.text() != "" and self.btn_6.text() != "" and self.btn_7.text() != "" and self.btn_8.text() != "" and self.btn_9.text() != "":
            self.lbl_winlosstie.setText("TIE")
            self.tie=self.tie+1
            self.lbl_tie.setText(f"ties {self.tie}")