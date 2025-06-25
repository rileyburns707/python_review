# Radio buttons - limited to only 1 option
import sys     # "this module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter"
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)   # x, y, width, height
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Gift Card", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.initUI()
        
    def initUI(self):
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)
        
        # apply CSS properties to a group of widgets
        self.setStyleSheet("QRadioButton{" 
                            "font-size: 40px;"
                            "font-family: Arial;"
                            "padding: 10px;"
                            "}")
        
        # can only select 1 radio button in a group, this is why we needed separate groups
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)

        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        # to make the buttons do something we need to connect a signal to a slot
        self.radio1.toggled.connect(self.radio_button_channged)
        self.radio2.toggled.connect(self.radio_button_channged)
        self.radio3.toggled.connect(self.radio_button_channged)
        self.radio4.toggled.connect(self.radio_button_channged)
        self.radio5.toggled.connect(self.radio_button_channged)
        
    def radio_button_channged(self):
        # finds which which radio button sent the signal and stores it in a local variable
        radio_button = self.sender()    # sender returns the widget that sent the signal
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")
        

def main():
    app = QApplication(sys.argv)    # "sys.argv" allows PyQt to process any command line argumens intended for it
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) # ".exec_()" waits for user input and handles events. Makes sure window stays showing

if __name__ == "__main__":
    main()