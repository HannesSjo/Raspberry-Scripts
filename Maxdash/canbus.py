import os
import can
import time
from PyQt5.QtCore import QThread, pyqtSignal

class canbus(QThread):
    progress_update = pyqtSignal(int)
    msg = {"RPM": 0, "TPS": 0, "MAP": 0, "AFR": 0, "IA": 0, "V": 0, "IAT": 0, "CT": 0, "ERR": 0, "OilP": 0, "OilT":0}

    def __init__(self):
        super().__init__()
        os.system('sudo ip link set can0 type can bitrate 500000')
        os.system('sudo ifconfig can0 up')        
    
    def run(self):
        while(True):
            #RPM = 0x520 01, TPS = 0x520 23, MAP = 0x520 45, Lambda = 0x520 67,
            #IA = 0x521 45, V = 0x530 01, IAT = 0x530 45, CT = 0x530 67
            #Errors = 0x534 45, , OilP = 0x536 45, OilT = 0x536 67 
            #0x520, 0x521, 0x530, 0x534, 0x536
            
            can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
            can0.set_filters([{"can_id": 0x520, "can_mask": 0xFFFFFF}])
            res = can0.recv(10.0)
            
            if(res.arbitration_id == 0x520):

                data = res.data

                self.msg["RPM"] = self.formatter(data[0], data[1])
                self.msg["TPS"] = self.formatter(data[2], data[3])*0.1
                self.msg["MAP"] = self.formatter(data[4], data[5])*0.1
                self.msg["AFR"] = (self.formatter(data[6], data[7])*0.001)* 14.7

            can0.set_filters([{"can_id": 0x521, "can_mask": 0xFFFFFF}])
            res = can0.recv(10.0)

            if(res.arbitration_id == 0x521):
                self.msg["IA"] = self.formatter(data[4], data[5])*0.1
            
            can0.set_filters([{"can_id": 0x530, "can_mask": 0xFFFFFF}])
            res = can0.recv(10.0)

            if(res.arbitration_id == 0x530):
                self.msg["V"] = self.formatter(data[0], data[1])*0.01
                self.msg["IAT"] = self.formatter(data[4], data[5])*0.1
                self.msg["CT"] = self.formatter(data[6], data[7])*0.1

            can0.set_filters([{"can_id": 0x534, "can_mask": 0xFFFFFF}])
            res = can0.recv(10.0)

            if(res.arbitration_id == 0x534):
                self.msg["ERR"] = self.formatter(data[4], data[5])

            can0.set_filters([{"can_id": 0x536, "can_mask": 0xFFFFFF}])
            res = can0.recv(10.0)

            if(res.arbitration_id == 0x536):
                self.msg["OilP"] = self.formatter(data[4], data[5])*0.1
                self.msg["OilT"] = self.formatter(data[6], data[7])*0.1

            self.sendData()
            time.sleep(0.01)

    def formatter(self, pos0, pos1):
        pos0 = bin(pos0)
        pos1 = bin(pos1)

        pos0 = pos0[2:]
        pos1 = pos1[2:]

        res = pos1 + pos0

        res = int(res, 2)
        return res

    def sendData(self):
        self.progress_update.emit()
    
    def getData(self):
        return self.msg
