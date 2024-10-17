
# By: <Your Name Here>
# Date: 2024-09-26
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

class CashRegister:
    def __init__(self):
        self.items = {
            "Apple": 0.50,
            "Banana": 0.30,
            "Orange": 0.60,
            "Grapes": 2.00,
            "Pineapple": 3.00,
        }
        self.total = 0.0

    def display_items(self):
        print("Available items:")
        for item, price in self.items.items():
            print(f"{item}: ${price:.2f}")

    def calculate_total(self):
        for item, price in self.items.items():
            quantity = int(input(f"Enter quantity for {item} (or 0 to skip): "))
            if quantity > 0:
                self.total += price * quantity

    def checkout(self):
        print(f"\nTotal amount due: ${self.total:.2f}")
        cash_received = float(input("Enter cash received: $"))
        if cash_received < self.total:
            print("Insufficient cash provided. Transaction cancelled.")
            return
        change = cash_received - self.total
        print(f"Change to be returned: ${change:.2f}")
        print("Thank you for your purchase!")

    def run(self):
        self.display_items()
        self.calculate_total()
        self.checkout()

if __name__ == "__main__":
    register = CashRegister()
    register.run()
