# PyQt5 QLabels
import sys     # "this module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter"
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt # Qt is used for alignments


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)   # x, y, width, height
        
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: blue;"
                            "background-color: green;"
                            "font-weight: bold;"
                            "text-decoration: underline;")
        # vertical alignment 
        # label.setAlignment(Qt.AlignTop) # vertically aligned to the top
        # label.setAlignment(Qt.AlignBottom)
        # label.setAlignment(Qt.AlignVCenter)

        # horizontal aligment
        # label.setAlignment(Qt.AlignRight)   # horizaontally aligned right
        # label.setAlignment(Qt.AlignHCenter)
        # label.setAlignment(Qt.AlignLeft)

        # combining horizontal and vertical positioning
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)   # center and center
        label.setAlignment(Qt.AlignCenter)   # center and center

def main():
    app = QApplication(sys.argv)    # "sys.argv" allows PyQt to process any command line argumens intended for it
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) # ".exec_()" waits for user input and handles events. Makes sure window stays showing

if __name__ == "__main__":
    main()