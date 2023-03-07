import os
import can
import time
from PyQt5.QtCore import QThread, pyqtSignal

class canbus(QThread):
    progress_update = pyqtSignal(int)
    errors = []

    def __init__(self):
        super().__init__()
        os.system('sudo ip link set can0 type can bitrate 500000')
        os.system('sudo ifconfig can0 up')        
    
    def run(self):
        can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
        can0.set_filters([{"can_id": 0x520, "can_mask": 0x21}])
        while(True):
            #RPM = 0x520 01, TPS = 0x520 23, MAP = 0x520 45, Lambda = 0x520 67,
            #IA = 0x521 45, V = 0x530 01, IAT = 0x530 45, CT = 0x530 67
            #Errors = 0x534 45, , OilP = 0x536 45, OilT = 0x536 67 
            #0x520, 0x521, 0x530, 0x534, 0x536
            msg = can0.recv(10.0)
            
            #for m in msg.data:
            #    res = self.formatter(m)

            data = msg.data

            rpm = self.formatter(data[0], data[1])
            tps = self.formatter(data[2], data[3])*0.1
            map = self.formatter(data[4], data[5])*0.1
            afr = (self.formatter(data[6], data[7])*0.001)* 14.7

            self.sendData(rpm, tps, map, afr)

            time.sleep(0.5)

    def formatter(self, pos0, pos1):
        pos0 = bin(pos0)
        pos1 = bin(pos1)

        pos0 = pos0[2:]
        pos1 = pos1[2:]

        res = pos1 + pos0

        res = int(res, 2)
        return res

    def sendData(self, rpm, tps, map, afr):
        msg = [rpm, tps, map, afr]
        self.progress_update.emit(msg)
