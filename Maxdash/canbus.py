import os
import can
import time
import textwrap
from PyQt5.QtCore import QThread, pyqtSignal

class canbus(QThread):
    progress_update = pyqtSignal(int)
    errors = []

    def __init__(self):
        super().__init__()
        #os.system('sudo ip link set can0 type can bitrate 500000')
        #os.system('sudo ifconfig can0 up')        
    
    def run(self):
        filters = [
            {"can_id": 0x520},
        ]
        can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan', can_filters=filters)
        while(True):
            #RPM = 0x520 01, TPS = 0x520 23, MAP = 0x520 45, Lambda = 0x520 67,
            #IA = 0x521 45, V = 0x530 01, IAT = 0x530 45, CT = 0x530 67
            #Errors = 0x534 45, , OilP = 0x536 45, OilT = 0x536 67 
            #0x520, 0x521, 0x530, 0x534, 0x536
            msg = can0.recv(10.0)
            print(msg.data)

            time.sleep(0.5)

    def formatter():
        result = [0, 0, 0, 0]
        return result

    def sendData(self, msg):
        if(msg == None):
            print("nothing")
        else:
              self.progress_update.emit(msg)
