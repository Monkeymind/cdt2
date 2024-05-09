from PySide6.QtWidgets import  QPushButton
from PySide6.QtGui import QFont,QIcon
from PySide6.QtWidgets import  QPushButton, QVBoxLayout, QWidget,QHBoxLayout,QMessageBox,QTabWidget,QRadioButton,QFrame
from PySide6.QtCore import Qt
import time
import qdarktheme
from datetime import datetime
from comport import comPort
from controlClass import Control
from controlCvCcClass import ControlCvCc
class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        qdarktheme.setup_theme()
        # Button with a parent widget
        self.setWindowTitle("EGSE-2")
        self.font = QFont('SF Pro Display', 12)
        self.font.setWeight(QFont.Weight.DemiBold) # 900
        self.setWindowIcon(QIcon("E:\pyQt_7\icon_1\egse.png"))

        #self.setWindowFlags(QFrame.StyledPanel | QFrame.Raised)
        # css = QWidget{
        #         Background: #AA00AA;
        #         color:white;
        #         font:12px bold;
        #     font-weight:bold;
        #     border-radius: 1px;
        #     height: 11px;
        # }
        # QDialog{
        #     Background-image:url('img/titlebar bg.png');
        #     font-size:12px;
        #     color: black;

        # }
        
        


        self.bas1=Control("BAS-1")
        self.chg1=Control("CHG-1")
        self.bas2=Control("BAS-2")
        self.chg2=Control("CHG-2")

        self.str1=Control("STR-1")
        self.str2=Control("STR-2")
        self.str3=Control("STR-3")
        self.str4=Control("STR-4")
        self.str5=Control("STR-5")
        self.str6=Control("STR-6")
        self.str7=Control("STR-7")
        self.str8=Control("STR-8")
        

        
        self.cv1=ControlCvCc("CV-1")
        self.cv2=ControlCvCc("CV-2")
        self.cv3=ControlCvCc("CV-3")
        self.cv4=ControlCvCc("CV-4")
        self.cv5=ControlCvCc("CV-5")
        self.cv6=ControlCvCc("CV-6")
        self.cc1=ControlCvCc("CC-1")
        self.cc2=ControlCvCc("CC-2")
        self.cc3=ControlCvCc("CC-3")
        self.cc4=ControlCvCc("CC-4")
        self.cc5=ControlCvCc("CC-5")
        self.cc6=ControlCvCc("CC-6")





        self.stAllOn=QPushButton(text="All STRING ON",parent=self)
        self.stAllOn.setFixedSize(200, 30)
        self.stAllOff=QPushButton(text="All STRING OFF",parent=self)
        self.stAllOff.setFixedSize(200, 30)
        self.strAllHlayout=QHBoxLayout()
        self.strAllHlayout.addWidget(self.stAllOn)
        self.strAllHlayout.addWidget(self.stAllOff)

        self.radio1=QRadioButton("Main",self)
        self.radio1.setFixedSize(100,30)
        self.radio1.setChecked(True)
        self.radio2=QRadioButton("Redundant",self)
        self.radio2.setFixedSize(100,30)
        self.radioHlayout=QHBoxLayout()
        self.radioHlayout.addWidget(self.radio1)
        self.radioHlayout.addWidget(self.radio2)




        self.comPort=comPort()


        
        self.mainVLayOut=QVBoxLayout()
        self.mainVLayOut1=QVBoxLayout()
        self.mainVLayOut2=QVBoxLayout()
        self.mainVLayOut.addWidget(self.comPort)
        
        self.basStrLayout=QWidget()
        self.cvccLayout=QWidget()

        self.basHlayOut=QHBoxLayout()
        
        self.basHlayOut.addLayout(self.bas1.conVLayout)
        self.basHlayOut.addLayout(self.chg1.conVLayout)
        self.basHlayOut.addLayout(self.bas2.conVLayout)
        self.basHlayOut.addLayout(self.chg2.conVLayout)
        self.mainVLayOut1.addLayout(self.radioHlayout)
        self.mainVLayOut1.addLayout(self.basHlayOut)

        self.mainVLayOut1.addLayout(self.strAllHlayout)                          

        self.strHlayOut=QHBoxLayout()
        self.strHlayOut.addLayout(self.str1.conVLayout)
        self.strHlayOut.addLayout(self.str2.conVLayout)
        self.strHlayOut.addLayout(self.str3.conVLayout)
        self.strHlayOut.addLayout(self.str4.conVLayout)
        self.strHlayOut.addLayout(self.str5.conVLayout)
        self.strHlayOut.addLayout(self.str6.conVLayout)
        self.strHlayOut.addLayout(self.str7.conVLayout)
        self.strHlayOut.addLayout(self.str8.conVLayout)
        self.mainVLayOut1.addLayout(self.strHlayOut)
        
        self.basStrLayout.setLayout(self.mainVLayOut1)

        self.CVAllON=QPushButton(text="CV All ON",parent=self)
        self.CVAllON.setFixedSize(100, 30)
        self.CVAllOFF=QPushButton(text="CV All OFF",parent=self)
        self.CVAllOFF.setFixedSize(100, 30)


        self.cvHlayOutAbove=QHBoxLayout()
        self.cvHlayOutAbove.addWidget(self.CVAllON)
        self.cvHlayOutAbove.addWidget(self.CVAllOFF)
        
        self.cvccHlayOut=QHBoxLayout()
        self.cvccHlayOut.addLayout(self.cv1.conVLayout)
        self.cvccHlayOut.addLayout(self.cv2.conVLayout)
        self.cvccHlayOut.addLayout(self.cv3.conVLayout)
        self.cvccHlayOut.addLayout(self.cv4.conVLayout)
        self.cvccHlayOut.addLayout(self.cv5.conVLayout)
        self.cvccHlayOut.addLayout(self.cv6.conVLayout)

        self.CCAllON=QPushButton(text="CC All ON",parent=self)
        self.CCAllON.setFixedSize(100, 30)
        self.CCAllOFF=QPushButton(text="CC All OFF",parent=self)
        self.CCAllOFF.setFixedSize(100, 30)


        self.ccHlayOutAbove=QHBoxLayout()
        self.ccHlayOutAbove.addWidget(self.CCAllON)
        self.ccHlayOutAbove.addWidget(self.CCAllOFF)
        


        self.cvccHlayOut2=QHBoxLayout()
        self.cvccHlayOut2.addLayout(self.cc1.conVLayout)
        self.cvccHlayOut2.addLayout(self.cc2.conVLayout)
        self.cvccHlayOut2.addLayout(self.cc3.conVLayout)
        self.cvccHlayOut2.addLayout(self.cc4.conVLayout)
        self.cvccHlayOut2.addLayout(self.cc5.conVLayout)
        self.cvccHlayOut2.addLayout(self.cc6.conVLayout)

        self.mainVLayOut2.addLayout(self.cvHlayOutAbove)
        self.mainVLayOut2.addLayout(self.cvccHlayOut)

        self.mainVLayOut2.addLayout(self.ccHlayOutAbove)
        self.mainVLayOut2.addLayout(self.cvccHlayOut2)

        self.cvccLayout.setLayout(self.mainVLayOut2)

        self.main1=QWidget()
        self.main1.setLayout(self.mainVLayOut1) 
        self.main2=QWidget()
        self.main2.setLayout(self.mainVLayOut2)    
        self.tabLayout=QTabWidget()
        self.tabLayout.addTab(self.main1,"Battery & String")
        self.tabLayout.addTab(self.main2,"CV & CC")
        
        self.mainVLayOut.addWidget(self.tabLayout)
      

        # self.textBOX=QTextEdit()
        # self.textBOX.setFixedSize(800,40)


        # self.textHlayout=QHBoxLayout()
        # self.textHlayout.addWidget(self.textBOX)
       # self.mainVLayOut.addLayout(self.textHlayout)

        self.setLayout(self.mainVLayOut)
        
        self.comPort.bserUpdate.clicked.connect(self.comPort.updatePortList)
        self.comPort.bPortConnect.clicked.connect(self.comPort.portConnect)
        
        self.bas1.Read.clicked.connect(lambda *, row=["BAS01_READ",self.bas1]: self.sendCommand(row[0],row[1]))
        self.bas1.Rlon.clicked.connect(lambda *, row=["BAS01_RLON",self.bas1]: self.sendCommand(row[0],row[1]))
        self.bas1.Rlof.clicked.connect(lambda *, row=["BAS01_RLOF",self.bas1]: self.sendCommand(row[0],row[1]))
        self.bas1.Fault.clicked.connect(lambda *, row=["BAS01_FACL",self.bas1]: self.sendCommand(row[0],row[1]))

        self.bas2.Read.clicked.connect(lambda *, row=["BAS02_READ",self.bas2]: self.sendCommand(row[0],row[1]))
        self.bas2.Rlon.clicked.connect(lambda *, row=["BAS02_RLON",self.bas2]: self.sendCommand(row[0],row[1]))
        self.bas2.Rlof.clicked.connect(lambda *, row=["BAS02_RLOF",self.bas2]: self.sendCommand(row[0],row[1]))
        self.bas2.Fault.clicked.connect(lambda *, row=["BAS02_FACL",self.bas2]: self.sendCommand(row[0],row[1]))

        self.chg1.Read.clicked.connect(lambda *, row=["CHG01_READ",self.chg1]: self.sendCommand(row[0],row[1]))
        self.chg1.Rlon.clicked.connect(lambda *, row=["CHG01_RLON",self.chg1]: self.sendCommand(row[0],row[1]))
        self.chg1.Rlof.clicked.connect(lambda *, row=["CHG01_RLOF",self.chg1]: self.sendCommand(row[0],row[1]))
        self.chg1.Fault.clicked.connect(lambda *, row=["CHG01_FACL",self.chg1]: self.sendCommand(row[0],row[1]))

        self.chg2.Read.clicked.connect(lambda *, row=["CHG02_READ",self.chg2]: self.sendCommand(row[0],row[1]))
        self.chg2.Rlon.clicked.connect(lambda *, row=["CHG02_RLON",self.chg2]: self.sendCommand(row[0],row[1]))
        self.chg2.Rlof.clicked.connect(lambda *, row=["CHG02_RLOF",self.chg2]: self.sendCommand(row[0],row[1]))
        self.chg2.Fault.clicked.connect(lambda *, row=["CHG02_FACL",self.chg2]: self.sendCommand(row[0],row[1]))


        self.str1.Read.clicked.connect(lambda *, row=["STR01_READ",self.str1]: self.sendCommand(row[0],row[1]))
        self.str1.Rlon.clicked.connect(lambda *, row=["STR01_RLON",self.str1]: self.sendCommand(row[0],row[1]))
        self.str1.Rlof.clicked.connect(lambda *, row=["STR01_RLOF",self.str1]: self.sendCommand(row[0],row[1]))
        self.str1.Fault.clicked.connect(lambda *, row=["STR01_FACL",self.str1]: self.sendCommand(row[0],row[1]))

        
        self.str2.Read.clicked.connect(lambda *, row=["STR02_READ",self.str2]: self.sendCommand(row[0],row[1]))
        self.str2.Rlon.clicked.connect(lambda *, row=["STR02_RLON",self.str2]: self.sendCommand(row[0],row[1]))
        self.str2.Rlof.clicked.connect(lambda *, row=["STR02_RLOF",self.str2]: self.sendCommand(row[0],row[1]))
        self.str2.Fault.clicked.connect(lambda *, row=["STR02_FACL",self.str2]: self.sendCommand(row[0],row[1]))


        self.str3.Read.clicked.connect(lambda *, row=["STR03_READ",self.str3]: self.sendCommand(row[0],row[1]))
        self.str3.Rlon.clicked.connect(lambda *, row=["STR03_RLON",self.str3]: self.sendCommand(row[0],row[1]))
        self.str3.Rlof.clicked.connect(lambda *, row=["STR03_RLOF",self.str3]: self.sendCommand(row[0],row[1]))
        self.str3.Fault.clicked.connect(lambda *, row=["STR03_FACL",self.str3]: self.sendCommand(row[0],row[1]))


        self.str4.Read.clicked.connect(lambda *, row=["STR04_READ",self.str4]: self.sendCommand(row[0],row[1]))
        self.str4.Rlon.clicked.connect(lambda *, row=["STR04_RLON",self.str4]: self.sendCommand(row[0],row[1]))
        self.str4.Rlof.clicked.connect(lambda *, row=["STR04_RLOF",self.str4]: self.sendCommand(row[0],row[1]))
        self.str4.Fault.clicked.connect(lambda *, row=["STR04_FACL",self.str4]: self.sendCommand(row[0],row[1]))


        self.str5.Read.clicked.connect(lambda *, row=["STR05_READ",self.str5]: self.sendCommand(row[0],row[1]))
        self.str5.Rlon.clicked.connect(lambda *, row=["STR05_RLON",self.str5]: self.sendCommand(row[0],row[1]))
        self.str5.Rlof.clicked.connect(lambda *, row=["STR05_RLOF",self.str5]: self.sendCommand(row[0],row[1]))
        self.str5.Fault.clicked.connect(lambda *, row=["STR05_FACL",self.str5]: self.sendCommand(row[0],row[1]))
   

        self.str6.Read.clicked.connect(lambda *, row=["STR06_READ",self.str6]: self.sendCommand(row[0],row[1]))
        self.str6.Rlon.clicked.connect(lambda *, row=["STR06_RLON",self.str6]: self.sendCommand(row[0],row[1]))
        self.str6.Rlof.clicked.connect(lambda *, row=["STR06_RLOF",self.str6]: self.sendCommand(row[0],row[1]))
        self.str6.Fault.clicked.connect(lambda *, row=["STR06_FACL",self.str6]: self.sendCommand(row[0],row[1]))

        self.str7.Read.clicked.connect(lambda *, row=["STR07_READ",self.str7]: self.sendCommand(row[0],row[1]))
        self.str7.Rlon.clicked.connect(lambda *, row=["STR07_RLON",self.str7]: self.sendCommand(row[0],row[1]))
        self.str7.Rlof.clicked.connect(lambda *, row=["STR07_RLOF",self.str7]: self.sendCommand(row[0],row[1]))
        self.str7.Fault.clicked.connect(lambda *, row=["STR07_FACL",self.str7]: self.sendCommand(row[0],row[1]))

        self.str8.Read.clicked.connect(lambda *, row=["STR08_READ",self.str8]: self.sendCommand(row[0],row[1]))
        self.str8.Rlon.clicked.connect(lambda *, row=["STR08_RLON",self.str8]: self.sendCommand(row[0],row[1]))
        self.str8.Rlof.clicked.connect(lambda *, row=["STR08_RLOF",self.str8]: self.sendCommand(row[0],row[1]))
        self.str8.Fault.clicked.connect(lambda *, row=["STR08_FACL",self.str8]: self.sendCommand(row[0],row[1]))

        self.cv1.Read.clicked.connect(lambda *, row=["CV-01_READ",self.cv1]: self.sendCommand(row[0],row[1]))
        self.cv1.Rlon.clicked.connect(lambda *, row=["CV-01_RLON",self.cv1]: self.sendCommand(row[0],row[1]))
        self.cv1.Rlof.clicked.connect(lambda *, row=["CV-01_RLOF",self.cv1]: self.sendCommand(row[0],row[1]))
        self.cv1.setDac.clicked.connect(lambda *, row=["CV-01_DACV",self.cv1]: self.sendCommand(row[0],row[1]))
        self.cv1.Fault.clicked.connect(lambda *, row=["CV-01_FACL",self.cv1]: self.sendCommand(row[0],row[1]))


        self.cv2.Read.clicked.connect(lambda *, row=["CV-02_READ",self.cv2]: self.sendCommand(row[0],row[1]))
        self.cv2.Rlon.clicked.connect(lambda *, row=["CV-02_RLON",self.cv2]: self.sendCommand(row[0],row[1]))
        self.cv2.Rlof.clicked.connect(lambda *, row=["CV-02_RLOF",self.cv2]: self.sendCommand(row[0],row[1]))
        self.cv2.setDac.clicked.connect(lambda *, row=["CV-02_DACV",self.cv2]: self.sendCommand(row[0],row[1]))
        self.cv2.Fault.clicked.connect(lambda *, row=["CV-02_FACL",self.cv2]: self.sendCommand(row[0],row[1]))

        self.cv3.Read.clicked.connect(lambda *, row=["CV-03_READ",self.cv3]: self.sendCommand(row[0],row[1]))
        self.cv3.Rlon.clicked.connect(lambda *, row=["CV-03_RLON",self.cv3]: self.sendCommand(row[0],row[1]))
        self.cv3.Rlof.clicked.connect(lambda *, row=["CV-03_RLOF",self.cv3]: self.sendCommand(row[0],row[1]))
        self.cv3.setDac.clicked.connect(lambda *, row=["CV-03_DACV",self.cv3]: self.sendCommand(row[0],row[1]))
        self.cv3.Fault.clicked.connect(lambda *, row=["CV-03_FACL",self.cv3]: self.sendCommand(row[0],row[1]))


        self.cv4.Rlon.clicked.connect(lambda *, row=["CV-04_RLON",self.cv4]: self.sendCommand(row[0],row[1]))
        self.cv4.Rlof.clicked.connect(lambda *, row=["CV-04_RLOF",self.cv4]: self.sendCommand(row[0],row[1]))
        self.cv4.Read.clicked.connect(lambda *, row=["CV-04_READ",self.cv4]: self.sendCommand(row[0],row[1]))
        self.cv4.setDac.clicked.connect(lambda *, row=["CV-04_DACV",self.cv4]: self.sendCommand(row[0],row[1]))
        self.cv4.Fault.clicked.connect(lambda *, row=["CV-04_FACL",self.cv4]: self.sendCommand(row[0],row[1]))



        self.cv5.Read.clicked.connect(lambda *, row=["CV-05_READ",self.cv5]: self.sendCommand(row[0],row[1]))
        self.cv5.Rlon.clicked.connect(lambda *, row=["CV-05_RLON",self.cv5]: self.sendCommand(row[0],row[1]))
        self.cv5.Rlof.clicked.connect(lambda *, row=["CV-05_RLOF",self.cv5]: self.sendCommand(row[0],row[1]))
        self.cv5.setDac.clicked.connect(lambda *, row=["CV-05_DACV",self.cv5]: self.sendCommand(row[0],row[1]))
        self.cv5.Fault.clicked.connect(lambda *, row=["CV-05_FACL",self.cv5]: self.sendCommand(row[0],row[1]))


        self.cv6.Read.clicked.connect(lambda *, row=["CV-06_READ",self.cv6]: self.sendCommand(row[0],row[1]))
        self.cv6.Rlon.clicked.connect(lambda *, row=["CV-06_RLON",self.cv6]: self.sendCommand(row[0],row[1]))
        self.cv6.Rlof.clicked.connect(lambda *, row=["CV-06_RLOF",self.cv6]: self.sendCommand(row[0],row[1]))
        self.cv6.setDac.clicked.connect(lambda *, row=["CV-06_DACV",self.cv6]: self.sendCommand(row[0],row[1]))
        self.cv6.Fault.clicked.connect(lambda *, row=["CV-06_FACL",self.cv6]: self.sendCommand(row[0],row[1]))





        self.cc1.Read.clicked.connect(lambda *, row=["CC-01_READ",self.cc1]: self.sendCommand(row[0],row[1]))
        self.cc1.Rlon.clicked.connect(lambda *, row=["CC-01_RLON",self.cc1]: self.sendCommand(row[0],row[1]))
        self.cc1.Rlof.clicked.connect(lambda *, row=["CC-01_RLOF",self.cc1]: self.sendCommand(row[0],row[1]))
        self.cc1.setDac.clicked.connect(lambda *, row=["CC-01_DACC",self.cc1]: self.sendCommand(row[0],row[1]))
        self.cc1.Fault.clicked.connect(lambda *, row=["CC-01_FACL",self.cc1]: self.sendCommand(row[0],row[1]))

        self.cc2.Read.clicked.connect(lambda *, row=["CC-02_READ",self.cc2]: self.sendCommand(row[0],row[1]))
        self.cc2.Rlon.clicked.connect(lambda *, row=["CC-02_RLON",self.cc2]: self.sendCommand(row[0],row[1]))
        self.cc2.Rlof.clicked.connect(lambda *, row=["CC-02_RLOF",self.cc2]: self.sendCommand(row[0],row[1]))
        self.cc2.setDac.clicked.connect(lambda *, row=["CC-02_DACC",self.cc2]: self.sendCommand(row[0],row[1]))
        self.cc2.Fault.clicked.connect(lambda *, row=["CC-02_FACL",self.cc2]: self.sendCommand(row[0],row[1]))


        self.cc3.Read.clicked.connect(lambda *, row=["CC-03_READ",self.cc3]: self.sendCommand(row[0],row[1]))
        self.cc3.Rlon.clicked.connect(lambda *, row=["CC-03_RLON",self.cc3]: self.sendCommand(row[0],row[1]))
        self.cc3.Rlof.clicked.connect(lambda *, row=["CC-03_RLOF",self.cc3]: self.sendCommand(row[0],row[1]))
        self.cc3.setDac.clicked.connect(lambda *, row=["CC-03_DACC",self.cc3]: self.sendCommand(row[0],row[1]))
        self.cc3.Fault.clicked.connect(lambda *, row=["CC-03_FACL",self.cc3]: self.sendCommand(row[0],row[1]))


        self.cc4.Read.clicked.connect(lambda *, row=["CC-04_READ",self.cc4]: self.sendCommand(row[0],row[1]))
        self.cc4.Rlon.clicked.connect(lambda *, row=["CC-04_RLON",self.cc4]: self.sendCommand(row[0],row[1]))
        self.cc4.Rlof.clicked.connect(lambda *, row=["CC-04_RLOF",self.cc4]: self.sendCommand(row[0],row[1]))
        self.cc4.setDac.clicked.connect(lambda *, row=["CC-04_DACC",self.cc4]: self.sendCommand(row[0],row[1]))
        self.cc4.Fault.clicked.connect(lambda *, row=["CC-04_FACL",self.cc4]: self.sendCommand(row[0],row[1]))



        self.cc5.Read.clicked.connect(lambda *, row=["CC-05_READ",self.cc5]: self.sendCommand(row[0],row[1]))
        self.cc5.Rlon.clicked.connect(lambda *, row=["CC-05_RLON",self.cc5]: self.sendCommand(row[0],row[1]))
        self.cc5.Rlof.clicked.connect(lambda *, row=["CC-05_RLOF",self.cc5]: self.sendCommand(row[0],row[1]))
        self.cc5.setDac.clicked.connect(lambda *, row=["CC-05_DACC",self.cc5]: self.sendCommand(row[0],row[1]))
        self.cc5.Fault.clicked.connect(lambda *, row=["CC-05_FACL",self.cc5]: self.sendCommand(row[0],row[1]))


        self.cc6.Read.clicked.connect(lambda *, row=["CC-06_READ",self.cc6]: self.sendCommand(row[0],row[1]))
        self.cc6.Rlon.clicked.connect(lambda *, row=["CC-06_RLON",self.cc6]: self.sendCommand(row[0],row[1]))
        self.cc6.Rlof.clicked.connect(lambda *, row=["CC-06_RLOF",self.cc6]: self.sendCommand(row[0],row[1]))
        self.cc6.setDac.clicked.connect(lambda *, row=["CC-06_DACC",self.cc6]: self.sendCommand(row[0],row[1]))
        self.cc6.Fault.clicked.connect(lambda *, row=["CC-06_FACL",self.cc6]: self.sendCommand(row[0],row[1]))

        self.radio1.clicked.connect(self.radio_One)
        self.radio2.clicked.connect(self.radio_Two)


        self.stAllOn.clicked.connect(self.STR_ALL_ON)
        self.stAllOff.clicked.connect(self.STR_ALL_OFF)


        self.CVAllON.clicked.connect(self.CV_ALL_ON)
        self.CVAllOFF.clicked.connect(self.CV_ALL_OFF)

        self.CCAllON.clicked.connect(self.CC_ALL_ON)
        self.CCAllOFF.clicked.connect(self.CC_ALL_OFF)

        self.radio_One()

    def sendCommand(self,command,serCon):
        if(command.find("_DACV") >=0):
            #self.cv1.setDac.clicked.connect(lambda *, row=["CV-01_DACV",self.cv1]: self.sendCommand(row[0],row[1]))
            command=command+str(serCon.dial.value()*22  )
        
        if(command.find("_DACC") >=0):
            #self.cv1.setDac.clicked.connect(lambda *, row=["CV-01_DACV",self.cv1]: self.sendCommand(row[0],row[1]))
            command=command+str(serCon.dial.value()*1.2)
            
        print(command) 
        try:
            self.bCommand =bytes(command,'ascii')
            
            
            self.comPort.portConn.write(self.bCommand)
            self.comPort.portConn.flush()
            for k in range(8):
                self.rxData=self.comPort.portConn.readline().strip().decode('ascii')
                #  self.comPort.portConn.reset_input_buffer()

                #print(self.rxData)
                #self.textBOX1.append(self.current_time+": "+self.rxData)
                serCon.conDisplay(self.rxData)
            
        except:
            portName=self.comPort.portlist[self.comPort.index].device
            print("sendCommand error")
            self.comPort.porDisconnect() 
            self.msgBox = QMessageBox()
            self.msgBox.setText( portName + " is Disconnected")
            self.msgBox.exec()   
            
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")
        serCon.Time.setText(self.current_time)





    def STR_ALL_ON(self):
        comListON=[("STR01_RLON",self.str1),
                   ("STR02_RLON",self.str2),
                   ("STR03_RLON",self.str3),
                   ("STR04_RLON",self.str4),
                   ("STR05_RLON",self.str5),
                   ("STR06_RLON",self.str6),
                   ("STR07_RLON",self.str7),
                   ("STR08_RLON",self.str8),]
        
        for comandSTR,STRcls in comListON:
            self.sendCommand(comandSTR,STRcls)
            time.sleep(.3)

    def STR_ALL_OFF(self):
        comListOF=[("STR01_RLOF",self.str1),
                   ("STR02_RLOF",self.str2),
                   ("STR03_RLOF",self.str3),
                   ("STR04_RLOF",self.str4),
                   ("STR05_RLOF",self.str5),
                   ("STR06_RLOF",self.str6),
                   ("STR07_RLOF",self.str7),
                   ("STR08_RLOF",self.str8),]
        for comandSTR,STRcls in comListOF:
            self.sendCommand(comandSTR,STRcls)
            time.sleep(.3)
    def setValue(self):
        print("set Dac")
        print(self.cv1.dial.value())
        print(type(self.cv1.dial.value()))



    def CV_ALL_ON(self):
        comListON=[("CV-01_RLON",self.cv1),
                   ("CV-02_RLON",self.cv2),
                   ("CV-03_RLON",self.cv3),
                   ("CV-04_RLON",self.cv4),
                   ("CV-05_RLON",self.cv5),
                   ("CV-06_RLON",self.cv6),]
                   
        for comandSTR,STRcls in comListON:
            self.sendCommand(comandSTR,STRcls)
            time.sleep(.3)


    def CV_ALL_OFF(self):
            comListON=[("CV-01_RLOF",self.cv1),
                    ("CV-02_RLOF",self.cv2),
                    ("CV-03_RLOF",self.cv3),
                    ("CV-04_RLOF",self.cv4),
                    ("CV-05_RLOF",self.cv5),
                    ("CV-06_RLOF",self.cv6),]
                    
            for comandSTR,STRcls in comListON:
                self.sendCommand(comandSTR,STRcls)
                time.sleep(.3)

    def CC_ALL_ON(self):
            comListON=[("CC-01_RLON",self.cc1),
                    ("CC-02_RLON",self.cc2),
                    ("CC-03_RLON",self.cc3),
                    ("CC-04_RLON",self.cc4),
                    ("CC-05_RLON",self.cc5),
                    ("CC-06_RLON",self.cc6),]
                    
            for comandSTR,STRcls in comListON:
                self.sendCommand(comandSTR,STRcls)
                time.sleep(.3)


    def CC_ALL_OFF(self):
            comListON=[("CC-01_RLOF",self.cc1),
                    ("CC-02_RLOF",self.cc2),
                    ("CC-03_RLOF",self.cc3),
                    ("CC-04_RLOF",self.cc4),
                    ("CC-05_RLOF",self.cc5),
                    ("CC-06_RLOF",self.cc6),]
                    
            for comandSTR,STRcls in comListON:
                self.sendCommand(comandSTR,STRcls)
                time.sleep(.3)


    def radio_One(self):
        self.bas1.Read.setEnabled(True)
        self.bas1.Rlon.setEnabled(True)
        self.bas1.Rlof.setEnabled(True)
        self.bas1.Fault.setEnabled(True)
        self.chg1.Read.setEnabled(True)
        self.chg1.Rlon.setEnabled(True)
        self.chg1.Rlof.setEnabled(True)
        self.chg1.Fault.setEnabled(True)
        self.bas2.Read.setEnabled(False)
        self.bas2.Rlon.setEnabled(False)
        self.bas2.Rlof.setEnabled(False)
        self.bas2.Fault.setEnabled(False)
        self.chg2.Read.setEnabled(False)
        self.chg2.Rlon.setEnabled(False)
        self.chg2.Rlof.setEnabled(False)
        self.chg2.Fault.setEnabled(False)


    def radio_Two(self):
        self.bas1.Read.setEnabled(False)
        self.bas1.Rlon.setEnabled(False)
        self.bas1.Rlof.setEnabled(False)
        self.bas1.Fault.setEnabled(False)
        self.chg1.Read.setEnabled(False)
        self.chg1.Rlon.setEnabled(False)
        self.chg1.Rlof.setEnabled(False)
        self.chg1.Fault.setEnabled(False)
        self.bas2.Read.setEnabled(True)
        self.bas2.Rlon.setEnabled(True)
        self.bas2.Rlof.setEnabled(True)
        self.bas2.Fault.setEnabled(True)
        self.chg2.Read.setEnabled(True)
        self.chg2.Rlon.setEnabled(True)
        self.chg2.Rlof.setEnabled(True)
        self.chg2.Fault.setEnabled(True)

