# line edits a.k.a text boxes
import sys     # "this module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter"
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)   # x, y, width, height
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()
        
    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(210, 10, 100, 40)
        self.line_edit.setStyleSheet("font-size: 25px;" 
                                    "font-family: Arial;")
        self.button.setStyleSheet("font-size: 25px;" 
                                    "font-family: Arial;")
        self.line_edit.setPlaceholderText("Enter your name")
        self.button.clicked.connect(self.submit)
        
    def submit(self):
        text = self.line_edit.text()    # returns text
        print(f"Hello {text}")
        

def main():
    app = QApplication(sys.argv)    # "sys.argv" allows PyQt to process any command line argumens intended for it
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) # ".exec_()" waits for user input and handles events. Makes sure window stays showing

if __name__ == "__main__":
    main()