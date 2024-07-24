from plotbox import plotBox
from PySide6.QtWidgets import QRadioButton,QComboBox,QDoubleSpinBox,QLabel,QLineEdit,QPushButton, QVBoxLayout, QHBoxLayout,QGroupBox
from PySide6.QtCore import Qt,QRect

class battTestPage():
    def __init__(self, parent=None):
        #super().__init__(parent)
        #self.bserUpdate = QPushButton(text="Update",parent=self)
        self.bChargTest = QPushButton(text="Charge Test")
        self.vPlot=plotBox("Voltage")
        self.cPlot=plotBox("Current")

        self.rChargDisc=QRadioButton("Charge then Discharge")
        self.rChargDisc.setChecked(True)
        self.rDiscCharg=QRadioButton("Discharge then Charge")


        self.radioHLayout=QHBoxLayout()
        self.radioHLayout.addWidget(self.rChargDisc)
        self.radioHLayout.addWidget(self.rDiscCharg)
        
        self.TestOrderGroup = QGroupBox("Test Order")
        self.TestOrderGroup.setLayout(self.radioHLayout)


        self.rloopRadio=QRadioButton("Loop Test")
        self.rloopRadio.setChecked(False)

        self.noOfCycleSpinBox=QDoubleSpinBox()        
        self.noOfCycleSpinBox.setMinimum(0)
        self.noOfCycleSpinBox.setMaximum(30)
        self.noOfCycleSpinBox.setValue(1)
        self.noOfCycleSpinBox.setSingleStep(1)
        self.noOfCycleSpinBox.setDecimals(0)
        self.noOfCycleSpinBox.setSuffix(" Cycle")
  
        
        self.cyclecHLayout=QHBoxLayout()
        self.cyclecHLayout.addWidget(self.rloopRadio)
        self.cyclecHLayout.addWidget(self.noOfCycleSpinBox)

        self.cycleBoxGroup = QGroupBox("Test Cycle")
        self.cycleBoxGroup.setLayout(self.cyclecHLayout)
        
        self.bMasterTest = QPushButton(text="Test")
        self.bMasterTest.setFixedSize(100,40)
        self.bMasterTest.setStyleSheet("background-color : Green")
        
        self.testInputHbox=QHBoxLayout()
        self.testInputHbox.addWidget(self.TestOrderGroup)
        self.testInputHbox.addWidget(self.cycleBoxGroup)
        self.testInputHbox.addWidget(self.bMasterTest)







        self.batterySlnoLabel=QLabel("Battery Sl.no")
        self.batterySlno=QLineEdit()
        
        self.testEngLabel=QLabel("Test Engineer")
        self.testEng=QLineEdit()
        self.testDetail=QHBoxLayout()
        self.testDetail.addWidget(self.batterySlnoLabel)
        self.testDetail.addWidget(self.batterySlno)
        self.testDetail.addWidget(self.testEngLabel)
        self.testDetail.addWidget(self.testEng)

        self.bChargTest = QPushButton(text="Start")
        self.bChargTest.setFixedSize(120,30)
        self.bChargTest.setStyleSheet("background-color: green")
        self.dPsVolt=QLineEdit()
        self.dPsVolt.setPlaceholderText("0.0 V")
        self.dPsVolt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dPsVolt.setFixedSize(120,20)
        self.dPsAmp=QLineEdit()
        self.dPsAmp.setPlaceholderText("0.0 A")
        self.dPsAmp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dPsAmp.setFixedSize(120,20)
        self.chargHlayout=QHBoxLayout()
        
        
        self.chargHlayout.addWidget(self.dPsVolt,alignment=Qt.AlignHCenter)
        self.chargHlayout.addWidget(self.dPsAmp,alignment=Qt.AlignHCenter)
        self.chargHlayout.addWidget(self.bChargTest,alignment=Qt.AlignHCenter)
        self.chrgBox = QGroupBox("Test Data")
        #self.chrgBox.setAlignment(Qt.AlignCenter)
        self.chrgBox.setLayout(self.chargHlayout)

        self.bLoadTest = QPushButton(text="Start")  #
        
        self.bLoadTest.setFixedSize(120,30)
        self.bLoadTest.setStyleSheet("background-color: green")
        
        self.dLdVolt=QLineEdit()
        self.dLdVolt.setPlaceholderText("0.0 V")
        self.dLdVolt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dLdVolt.setFixedSize(120,20)
        self.dLdAmp=QLineEdit()
        self.dLdAmp.setPlaceholderText("0.0 A")
        self.dLdAmp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dLdAmp.setFixedSize(120,20)
        self.LoadHlayout=QHBoxLayout()

        # self.dLdRes=QLineEdit()
        # self.dLdRes.setPlaceholderText("0 R")
        # self.dLdRes.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.dLdRes.setFixedSize(120,20)

        # self.dLdPow=QLineEdit()
        # self.dLdPow.setPlaceholderText("0 W")
        # self.dLdPow.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.dLdPow.setFixedSize(120,20)

        self.LoadHlayout=QHBoxLayout()
        self.LoadHlayout.addWidget(self.dLdVolt,alignment=Qt.AlignHCenter)
        self.LoadHlayout.addWidget(self.dLdAmp,alignment=Qt.AlignHCenter)
        # self.LoadHlayout.addWidget(self.dLdRes,alignment=Qt.AlignHCenter)
        # self.LoadHlayout.addWidget(self.dLdPow,alignment=Qt.AlignHCenter)


        self.LoadHlayout.addWidget(self.bLoadTest,alignment=Qt.AlignHCenter)
        self.loadBox = QGroupBox("Load Test")
        self.loadBox.setLayout(self.LoadHlayout)
        

        self.TestHlayout=QHBoxLayout()
        self.TestHlayout.addWidget(self.chrgBox)
        #self.TestHlayout.addWidget(self.loadBox)
        self.TestHlayout.setAlignment(Qt.AlignCenter)

            
    
        self.voltHlayout=QVBoxLayout()
        self.voltHlayout.addWidget(self.vPlot)

        self.currHlayout=QVBoxLayout()
        self.currHlayout.addWidget(self.cPlot)

        self.plotHlayout=QHBoxLayout()
        self.plotHlayout.addLayout(self.voltHlayout)
        self.plotHlayout.addLayout(self.currHlayout)

        self.mainVLayOut2=QVBoxLayout()        
        self.mainVLayOut2.addLayout(self.testDetail)
        self.mainVLayOut2.addLayout(self.testInputHbox)
        # self.mainVLayOut2.addWidget(self.TestOrderGroup)
        # self.mainVLayOut2.addWidget(self.cycleBoxGroup)
        self.mainVLayOut2.addLayout(self.TestHlayout)
        self.mainVLayOut2.addLayout(self.plotHlayout)
        self.mainVLayOut2.setAlignment(Qt.AlignCenter)


    def chargTestStart(self):
        self.bChargTest.setText("End")
        self.bChargTest.setStyleSheet("background-color: red")
        self.bLoadTest.setEnabled(False)
    def chargTestEnd(self):
        self.bChargTest.setText("Start")
        self.bChargTest.setStyleSheet("background-color: green")
        self.bLoadTest.setEnabled(True)
    def dischargTestStart(self):
        self.bLoadTest.setText("End")
        self.bLoadTest.setStyleSheet("background-color: red")
        self.bChargTest.setEnabled(False)
    def dischargTestEnd(self):
        self.bLoadTest.setText("Start")
        self.bLoadTest.setStyleSheet("background-color: green")
        self.bChargTest.setEnabled(True)
    def testDetailClear(self):
        self.batterySlno.clear()
        self.testEng.clear()
        self.dPsVolt.clear()
        self.dPsAmp.clear()
        self.dLdVolt.clear()
        self.dLdAmp.clear()
        self.dLdRes.clear()
        self.dLdPow.clear()

