# CSS styles using setStyleSheet()
import sys     # "this module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter"
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")    # since I'm using a layout manager I don't need to add the button to self
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()
        
    def initUI(self):
        # to create layout manager in the MainWindow we need to add a layout manager (QHboxLayout) to a central widget (QWidget), and this central widget will be added to the main window
        # this is because main window widgets already have a specified layout and format
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        # triple quotes create a mulit-line strings
        self.setStyleSheet("""      
                QPushButton{
                    font-size: 40px;
                    font-family: Arial;
                    padding: 15px 75px;
                    margin: 25px;
                    border: 3px solid;
                    border-radius: 15px;
                }   

                QPushButton#button1{
                    background-color: red;
                } 

                QPushButton#button2{
                    background-color: hsl(122, 100, 64);
                } 
                
                #button3{
                    background-color: hsl(204, 100, 64);
                } 
                           
                QPushButton#button1:hover{
                    background-color: red;
                } 

                QPushButton#button2:hover{
                    background-color: hsl(122, 100, 84);
                } 
                
                #button3:hover{
                    background-color: hsl(204, 100, 84);
                } 
        """)
        

def main():
    app = QApplication(sys.argv)    # "sys.argv" allows PyQt to process any command line argumens intended for it
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) # ".exec_()" waits for user input and handles events. Makes sure window stays showing

if __name__ == "__main__":
    main()