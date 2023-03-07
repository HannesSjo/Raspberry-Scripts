import os
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
        os.system('sudo ifconfig can0 down')
        self.close()
    
    def update(self, msg):
        self.RPMtxt.setText(str(msg[0]))
        self.TPStxt.setText(str(msg[1]) + " %")
        self.MAPtxt.setText(str(msg[2]) + " kpa")
        self.AFRtxt.setText(str(msg[3]))




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main() 
    window.show()
    sys.exit(app.exec_())