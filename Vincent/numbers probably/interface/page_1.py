
# By: <vincent>
# Date: 2024-09-20
# Program Details: <formating outputs>

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

run=True
while run:
    try:

        num1=float(input("number 1: "))
        num2=float(input("number 2: "))

        total=num1*num2

        print(f"the answer is {'{0:.2f}'.format(total)}")
        run=False
    except:
        print("numbers only this is a calculator not a dictionary")