import os
import sys
import time
from canbus import canbus
from PyQt5.QtCore import QThread
from PyQt5 import QtWidgets, uic

class Main(QtWidgets.QMainWindow):
    thread = canbus()
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi('main.ui', self)
        self.showMaximized()
        self.Exit.clicked.connect(self.exit)

        self.thread.progress_update.connect(self.update)

        self.thread.start()

    def exit(self):
        os.system('sudo ifconfig can0 down')
        self.close()
    
    def update(self):
        msg = self.thread.getData()
        if(msg["ERR"] != None):
            self.ERRtxt.setText(str(round(msg["ERR"], 0)))
        if(msg["OilP"] != None):
            self.OilPtxt.setText(str(round(msg["OilP"], 1)) + " kpa")
        if(msg["CT"] != None):
            self.CTtxt.setText(str(round(msg["CT"], 1)) + " °C")
        if(msg["MAP"] != None):
            self.MAPtxt.setText(str(round(msg["MAP"], 1)) + " kpa")
        if(msg["RPM"] != None):
            self.RPMtxt.setText(str(round(msg["RPM"], 0)))
        if(msg["OilT"] != None):
            self.OilTtxt.setText(str(round(msg["OilT"], 1)) + " °C")
        if(msg["AFR"] != None):
            self.AFRtxt.setText(str(round(msg["AFR"], 2)))
        if(msg["V"] != None):
            self.BVtxt.setText(str(round(msg["V"], 2)) + " V")
        if(msg["IA"] != None):
            self.IAtxt.setText(str(round(msg["IA"], 1)) + " btdc")
        if(msg["IAT"] != None):
            self.IATtxt.setText(str(round(msg["IAT"], 1)) + " °C")
        if(msg["TPS"] != None):
            self.TPStxt.setText(str(round(msg["TPS"], 1)) + " %")
        




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main() 
    window.show()
    sys.exit(app.exec_())