from PySide6.QtWidgets import  QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from PySide6.QtWidgets import  QPushButton, QVBoxLayout, QWidget,QHBoxLayout,QLabel,QLineEdit
from datetime import datetime

class Control(QWidget):
    def __init__(self,name, parent=None):
        super().__init__(parent)
      
        self.font = QFont('SF Pro Display', 12)
        self.font.setWeight(QFont.Weight.DemiBold) # 900
        self.tag=name
        self.Name=QLabel()
        self.Name.setText(name)
        self.Name.setFont(self.font)
        self.Name.setTextFormat(Qt.MarkdownText)
        self.Name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Name.setFixedSize(100,20)
        self.Name.setTextFormat(Qt.MarkdownText)
        self.Volt=QLineEdit("0.0 V")
        self.Volt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Volt.setFixedSize(100,20)
        self.Volt.setReadOnly(True)
        self.Current=QLineEdit("0.0 A")
        self.Current.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Current.setFixedSize(100,20)
        self.Current.setReadOnly(True)
        self.Status=QLineEdit("OFF")
        self.Status.setStyleSheet("background-color: green")
        self.Status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Status.setFixedSize(100,20)
        self.Status.setReadOnly(True)
        self.Rlon=QPushButton(text="ON",parent=self)
        self.Rlon.setFixedSize(45, 25)
        self.Rlof=QPushButton(text="OFF",parent=self)
        self.Rlof.setFixedSize(45, 25)
        self.Read=QPushButton(text="READ",parent=self)
        self.Read.setFixedSize(100, 25)
        #self.Read.setEnabled(True)
        self.Fault=QPushButton(text="Fault Reset",parent=self)
        self.Read.setFixedSize(100, 25)
        self.Time=QLineEdit("00:00:00")
        self.Time.setReadOnly(True)        
        self.Time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Time.setFixedSize(100,20)

        self.conHLayout1=QHBoxLayout()
        self.conHLayout1.addWidget(self.Volt)
        self.conHLayout1.addWidget(self.Current)

        self.conHLayout2=QHBoxLayout()
        self.conHLayout2.addWidget(self.Rlon)
        self.conHLayout2.addWidget(self.Rlof)
        

        self.conVLayout=QVBoxLayout()
        self.conVLayout.addWidget(self.Name)
        self.conVLayout.addWidget(self.Volt)
        self.conVLayout.addWidget(self.Current)
        #self.conVLayout.addLayout(self.conHLayout1)
        self.conVLayout.addWidget(self.Status)
        self.conVLayout.addWidget(self.Time)
        self.conVLayout.addLayout(self.conHLayout2)
        self.conVLayout.addWidget(self.Read)
        self.conVLayout.addWidget(self.Fault)
        
        # self.conVLayout.addWidget(self.Volt)
        # self.conVLayout.addWidget(self.Current)
       
        
   
    def conDisplay(self,msg):
        print(msg)
        if(msg.find("_V-") >=0):
            self.msgSplit=msg.split("_V-",1)
            self.Volt.setText(self.msgSplit[1]+" V")
        if(msg.find("_C-") >=0):
            self.msgSplit=msg.split("_C-",1)
            self.Current.setText(self.msgSplit[1]+" A")
        if(msg.find("RS1") >=0):
            self.Status.setText("ON")
            self.Status.setStyleSheet("background-color: red")
            
        if(msg.find("RS0") >=0):
            self.Status.setText("OFF")
            self.Status.setStyleSheet("background-color: green")
        if((msg.find("_VF1_CF0") >=0)):
            self.Fault.setStyleSheet("background-color: red")
        if((msg.find("_VF0_CF1") >=0)):
            self.Fault.setStyleSheet("background-color: red")
        if((msg.find("_VF1_CF1") >=0)):
            self.Fault.setStyleSheet("background-color: red")
        if((msg.find("_VF0_CF0") >=0)):
            self.Fault.setStyleSheet("background-color: none")