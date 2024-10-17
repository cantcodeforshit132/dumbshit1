
# By: <vincent>
# Date: 2024-09-19
# Program Details: <3 buttons that disply 3 nursery rimes>

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
        
        self.setWindowTitle("nursery rhyms")
        
    def btn_rime1_a(self):
        self.lbl_rimes.setText("Mary had a little lamb Little lamb,\n little lamb Mary had a little lamb It's fleece was white as snow Everywhere that Mary went Mary went,\n Mary went Everywhere that Mary went The lamb was sure to go It followed her to school one day School one day,\n school one day It followed her to school one day Which was againts the rules It made the children laugh and play Laugh and play,\n laugh and play It made the children laugh and play To see the lamb at school And so the teacher turned it out Turned it out,\n turned it out And so the teacher turned it out But still it lingered near Why does the lamb love Mary so?\n Love Mary so, love Mary so Why does the lamb love Mary so? \nThe eager children cry Why, Mary loves the lamb, you know The lamb, you know, the lamb, you know Why,\n Mary loves the lamb, you know The teacher did reply Mary had a little lamb Little lamb,\n little lamb Mary had a little lamb It's fleece was white as snow Everywhere that Mary went Mary went,\n Mary went Everywhere that Mary went The lamb was sure to go Mary had a little lamb Little lamb,\n little lamb Mary had a little lamb It's fleece was white as snow")
        self.btn_rime1.setEnabled(False)
        self.btn_rime2.setEnabled(True)
        self.btn_rime3.setEnabled(True)
        self.lbl_image.setPixmap(QPixmap(u"images/lttlelamb.jpg"))
    def btn_rime2_a(self):
        self.lbl_rimes.setText("Ring-a-ring o' roses A pocket full of posies A-tishoo! A-tishoo! \n We all fall down Ring-a-ring o' roses A pocket full of posies A-tishoo! A-tishoo! We all fall down")
        self.btn_rime1.setEnabled(True)
        self.btn_rime2.setEnabled(False)
        self.btn_rime3.setEnabled(True)
        self.lbl_image.setPixmap(QPixmap(u"images/download.jpg"))
    def btn_rime3_a(self):
        self.lbl_rimes.setText("Humpty Dumpty sat on a wall Humpty Dumpty had a great fall \n All the king's horses and all the king's men Couldn't put Humpty together again Humpty Dumpty sat on the ground Humpty Dumpty looked all around Gone were the chimneys,\n gone were the roofs All he could see were ankles and hooves Poor old Humpty\n Poor old Humpty Poor old Humpty Dumpty Poor old Humpty Poor old Humpty Poor old Humpty Poor old Humpty Dumpty \n Humpty Dumpty counted to ten Humpty Dumpty built up again All the king's horses and all the king's men Are happy that Humpty is together again")
        self.btn_rime1.setEnabled(True)
        self.btn_rime2.setEnabled(True)
        self.btn_rime3.setEnabled(False)
        self.lbl_image.setPixmap(QPixmap(u"images/egg.jpg"))