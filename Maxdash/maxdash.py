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
        self.Exit.clicked.connect(self.exit)

        self.thread.progress_update.connect(self.update)

        self.thread.start()

    def exit(self):
        os.system('sudo ifconfig can0 down')
        self.close()
    
    def update(self):
        msg = self.thread.getData()
        if(msg["ERR"] != None):
            self.ERRtxt.setText(str(msg["ERR"]))
        if(msg["OilP"] != None):
            self.OilPtxt.setText(str(msg["OilP"]) + " kpa")
        if(msg["CT"] != None):
            self.CTtxt.setText(str(msg["CT"]) + " °C")
        if(msg["MAP"] != None):
            self.MAPtxt.setText(str(msg["MAP"]) + " kpa")
        if(msg["RPM"] != None):
            self.RPMtxt.setText(str(msg["RPM"]))
        if(msg["OilT"] != None):
            self.OilTtxt.setText(str(msg["OilT"]) + " °C")
        if(msg["AFR"] != None):
            self.AFRtxt.setText(str(msg["AFR"]))
        if(msg["V"] != None):
            self.BVtxt.setText(str(msg["V"]) + " V")
        if(msg["IA"] != None):
            self.IAtxt.setText(str(msg["IA"]) + " btd")
        if(msg["IAT"] != None):
            self.IATtxt.setText(str(msg["IAT"]) + " °C")
        if(msg["TPS"] != None):
            self.TPStxt.setText(str(msg["TPS"]) + " %")
        




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main() 
    window.show()
    sys.exit(app.exec_())