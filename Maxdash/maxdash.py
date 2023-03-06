import sys
import time
from canbus import canbus
from PyQt5.QtCore import QThread
from PyQt5 import QtWidgets, uic

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi('main.ui', self)
        self.Exit.clicked.connect(self.exit)

        self.thread = canbus()
        self.thread.progress_update.connect(self.update)

        self.thread.start()

    def exit(self):
        self.close()
    
    def update(self, newText):
        print(newText)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main() 
    window.show()
    sys.exit(app.exec_())