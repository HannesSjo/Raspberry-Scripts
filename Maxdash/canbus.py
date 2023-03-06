import os
import can
import time
from PyQt5.QtCore import QThread, pyqtSignal

class canbus(QThread):
    progress_update = pyqtSignal(int)
    errors = []

    def __init__(self):
        super().__init__()
        os.system('sudo ip link set can0 type can bitrate 100000')
        os.system('sudo ifconfig can0 up')
        can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
        
    
    def run(self):
        while(True):
            #RPM = 0x520 01, TPS = 0x520 23, MAP = 0x520 45, Lambda = 0x520 67,
            #IA = 0x521 45, V = 0x530 01, IAT = 0x530 45, CT = 0x530 67
            #Errors = 0x534 45, , OilP = 0x536 45, OilT = 0x536 67 
            #0x520, 0x521, 0x530, 0x534, 0x536

            msg520 = can.Message(arbitration_id=0x520, data=[0, 1, 2, 3, 4, 5, 6, 7], is_extended_id=False)
            msg521 = can.Message(arbitration_id=0x521, data=[0, 1, 2, 3, 4, 5, 6, 7], is_extended_id=False)
            msg530 = can.Message(arbitration_id=0x530, data=[0, 1, 2, 3, 4, 5, 6, 7], is_extended_id=False)
            msg534 = can.Message(arbitration_id=0x534, data=[0, 1, 2, 3, 4, 5, 6, 7], is_extended_id=False)
            msg536 = can.Message(arbitration_id=0x536, data=[0, 1, 2, 3, 4, 5, 6, 7], is_extended_id=False)

            self.sendData(msg520)
            time.sleep(0.5)

    def formatter():
        result = [0, 0, 0, 0]
        return result

    def sendData(self, msg):
        self.progress_update.emit(msg)
