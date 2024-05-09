import serial.tools.list_ports
from PySide6.QtWidgets import  QFrame,QTextEdit,QGroupBox,QComboBox,QLabel,QGridLayout,QMessageBox,QPushButton

class comPort(QGroupBox):
    def __init__(self):
        super().__init__()
        self.setTitle('ComPort')
        self.bserUpdate = QPushButton(text="Update",parent=self)
        self.bserUpdate.setFixedSize(100, 30)
        self.SerList=QComboBox()
        self.SerList.setFixedSize(500, 30)
        self.bPortConnect = QPushButton(text="Connect",parent=self)
        self.bPortConnect.setFixedSize(100, 30)
        self.bPortConnect.setStyleSheet("background-color: green")
        #self.bPortConnect.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.lBaudrate=QLabel(text="BaudRate: 9600",parent=self)
        self.lBaudrate.setFixedWidth(90)
        
        self.serHlayOut=QGridLayout(self)
        self.serHlayOut.addWidget(self.bserUpdate,0,0)
        self.serHlayOut.addWidget(self.SerList,0,1)
        self.serHlayOut.addWidget(self.lBaudrate,0,2)
        self.serHlayOut.addWidget(self.bPortConnect,0,3)
       
        
        # self.serHlayOut=QHBoxLayout()
        # self.serHlayOut.addWidget(self.bserUpdate)
        # self.serHlayOut.addWidget(self.SerList)
        # self.serHlayOut.addWidget(self.lBaudrate)
        # self.serHlayOut.addWidget(self.bPortConnect)
        

        self.portlist =serial.tools.list_ports.comports()
        for comNum in range(len(self.portlist)):
            print(str(comNum+1)+"- "+str(self.portlist[comNum]))
            self.SerList.addItem(str(self.portlist[comNum]))
    def updatePortList(self):
        print("updatePortList")
        self.portlist.clear()
        self.SerList.clear()
        self.portlist =serial.tools.list_ports.comports()
        for comNum in range(len(self.portlist)):
            print(str(comNum+1)+"- "+str(self.portlist[comNum].description))
            self.SerList.addItem(str(self.portlist[comNum]))
    
    def portConnect(self):
        self.portConn="a"
        if self.bPortConnect.text() == "Connect":
            self.index=self.SerList.currentIndex()
            print(str(self.index))
            try:
                self.portConn=serial.Serial(port=(self.portlist[self.index].device),timeout=.1)
                #self.portConn.open()
                
                self.bPortConnect.setText("Disconnect")
                self.bPortConnect.setStyleSheet("background-color: red")
                print(self.portlist[self.index].device +"- Port Connected")
                
            except:
                print("Port Connect Func error")
                
                

        else:
           # comPort.portConn.close()
            self.bPortConnect.setText("Connect")
            self.bPortConnect.setStyleSheet("background-color: green")  

    def porDisconnect(self):
        self.portConn.close()
        self.bPortConnect.setText("Connect")
        self.bPortConnect.setStyleSheet("background-color: green")
                        







