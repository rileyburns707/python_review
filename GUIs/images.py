# PyQt5 QLabels
import sys     # "this module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter"
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)   # x, y, width, height

        label = QLabel(self)    # self refers to the window object
        label.setGeometry(0,0, 250, 250)    # size of image

        pixmap = QPixmap("GUIs/paddington.png")
        label.setPixmap(pixmap)
        
        label.setScaledContents(True)

        label.setGeometry((self.width() - label.width()) // 2,  # integer division to round to the nearest whole pixel
                          (self.height()- label.height()) // 2,
                          label.width(),
                          label.height())


def main():
    app = QApplication(sys.argv)    # "sys.argv" allows PyQt to process any command line argumens intended for it
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) # ".exec_()" waits for user input and handles events. Makes sure window stays showing

if __name__ == "__main__":
    main()