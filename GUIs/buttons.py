# Buttons
import sys     # "this module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter"
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)   # x, y, width, height
        self.button = QPushButton("Click me!", self) # local variable. Did not put self.button there. Changed to self.button later
        self.label = QLabel("Hello", self)
        self.initUI()
        
    def initUI(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)  # checkbox.*signal*.connect(*slot*). Signal is an event and the slot is the action the widget will take

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px;")
    
    ''' # before we added self.label
    def on_click(self):
        print("Button clicked!")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)
    '''

    def on_click(self):
        self.label.setText("Goodbye")


def main():
    app = QApplication(sys.argv)    # "sys.argv" allows PyQt to process any command line argumens intended for it
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) # ".exec_()" waits for user input and handles events. Makes sure window stays showing

if __name__ == "__main__":
    main()