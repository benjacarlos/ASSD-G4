# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/myTp1MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 847)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.includeFAA = QtWidgets.QCheckBox(self.centralwidget)
        self.includeFAA.setGeometry(QtCore.QRect(150, 720, 21, 20))
        self.includeFAA.setText("")
        self.includeFAA.setObjectName("includeFAA")
        self.includeSH = QtWidgets.QCheckBox(self.centralwidget)
        self.includeSH.setGeometry(QtCore.QRect(360, 720, 21, 20))
        self.includeSH.setText("")
        self.includeSH.setObjectName("includeSH")
        self.includeAnalogKey = QtWidgets.QCheckBox(self.centralwidget)
        self.includeAnalogKey.setGeometry(QtCore.QRect(580, 720, 21, 20))
        self.includeAnalogKey.setText("")
        self.includeAnalogKey.setObjectName("includeAnalogKey")
        self.includeRF = QtWidgets.QCheckBox(self.centralwidget)
        self.includeRF.setGeometry(QtCore.QRect(810, 720, 21, 20))
        self.includeRF.setText("")
        self.includeRF.setObjectName("includeRF")
        self.includeFAALabel = QtWidgets.QLabel(self.centralwidget)
        self.includeFAALabel.setGeometry(QtCore.QRect(120, 700, 101, 16))
        self.includeFAALabel.setObjectName("includeFAALabel")
        self.includeSHLabel = QtWidgets.QLabel(self.centralwidget)
        self.includeSHLabel.setGeometry(QtCore.QRect(330, 700, 101, 16))
        self.includeSHLabel.setObjectName("includeSHLabel")
        self.includeAnalogKeyLabel = QtWidgets.QLabel(self.centralwidget)
        self.includeAnalogKeyLabel.setGeometry(QtCore.QRect(540, 700, 101, 16))
        self.includeAnalogKeyLabel.setObjectName("includeAnalogKeyLabel")
        self.includeFRLabel = QtWidgets.QLabel(self.centralwidget)
        self.includeFRLabel.setGeometry(QtCore.QRect(780, 700, 101, 16))
        self.includeFRLabel.setObjectName("includeFRLabel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 20, 20, 241))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(400, 20, 20, 241))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(40, 250, 371, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(40, 10, 371, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(700, 10, 371, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(1060, 20, 20, 241))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(690, 20, 20, 241))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(700, 250, 371, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.signalTypeInput = QtWidgets.QComboBox(self.centralwidget)
        self.signalTypeInput.setGeometry(QtCore.QRect(170, 50, 211, 26))
        self.signalTypeInput.setObjectName("signalTypeInput")
        self.signalTypeInput.addItem("")
        self.signalTypeInput.addItem("")
        self.signalTypeInput.addItem("")
        self.signalTypeInput.addItem("")
        self.signalTypeInput.addItem("")
        self.signalTypeInput.addItem("")
        self.inputSignalXinLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputSignalXinLabel.setGeometry(QtCore.QRect(40, 0, 121, 16))
        self.inputSignalXinLabel.setObjectName("inputSignalXinLabel")
        self.sampleSignalLabel = QtWidgets.QLabel(self.centralwidget)
        self.sampleSignalLabel.setGeometry(QtCore.QRect(700, 0, 121, 16))
        self.sampleSignalLabel.setObjectName("sampleSignalLabel")
        self.acceptParametersButton = QtWidgets.QPushButton(self.centralwidget)
        self.acceptParametersButton.setGeometry(QtCore.QRect(940, 780, 171, 32))
        self.acceptParametersButton.setObjectName("acceptParametersButton")
        self.signalTypeLabel = QtWidgets.QLabel(self.centralwidget)
        self.signalTypeLabel.setGeometry(QtCore.QRect(80, 50, 81, 21))
        self.signalTypeLabel.setObjectName("signalTypeLabel")
        self.oscilatorPeriod = QtWidgets.QLineEdit(self.centralwidget)
        self.oscilatorPeriod.setGeometry(QtCore.QRect(830, 90, 113, 21))
        self.oscilatorPeriod.setObjectName("oscilatorPeriod")
        self.dutyCycleInputBox = QtWidgets.QLineEdit(self.centralwidget)
        self.dutyCycleInputBox.setGeometry(QtCore.QRect(830, 140, 113, 21))
        self.dutyCycleInputBox.setObjectName("dutyCycleInputBox")
        self.periodInputLabel = QtWidgets.QLabel(self.centralwidget)
        self.periodInputLabel.setGeometry(QtCore.QRect(779, 90, 41, 20))
        self.periodInputLabel.setObjectName("periodInputLabel")
        self.dutyCycleInputLabel = QtWidgets.QLabel(self.centralwidget)
        self.dutyCycleInputLabel.setGeometry(QtCore.QRect(719, 140, 101, 20))
        self.dutyCycleInputLabel.setObjectName("dutyCycleInputLabel")
        self.stackedInputSignalOptions = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedInputSignalOptions.setGeometry(QtCore.QRect(110, 90, 221, 131))
        self.stackedInputSignalOptions.setObjectName("stackedInputSignalOptions")
        self.stackedSine = QtWidgets.QWidget()
        self.stackedSine.setObjectName("stackedSine")
        self.periodInputLabel_7 = QtWidgets.QLabel(self.stackedSine)
        self.periodInputLabel_7.setGeometry(QtCore.QRect(20, 90, 60, 16))
        self.periodInputLabel_7.setObjectName("periodInputLabel_7")
        self.periodInputLabel_6 = QtWidgets.QLabel(self.stackedSine)
        self.periodInputLabel_6.setGeometry(QtCore.QRect(20, 50, 60, 16))
        self.periodInputLabel_6.setObjectName("periodInputLabel_6")
        self.phaseForSine = QtWidgets.QLineEdit(self.stackedSine)
        self.phaseForSine.setGeometry(QtCore.QRect(80, 90, 113, 21))
        self.phaseForSine.setObjectName("phaseForSine")
        self.periodInputLabel_5 = QtWidgets.QLabel(self.stackedSine)
        self.periodInputLabel_5.setGeometry(QtCore.QRect(20, 10, 60, 16))
        self.periodInputLabel_5.setObjectName("periodInputLabel_5")
        self.fForSine = QtWidgets.QLineEdit(self.stackedSine)
        self.fForSine.setGeometry(QtCore.QRect(80, 50, 113, 21))
        self.fForSine.setObjectName("fForSine")
        self.vpForSine = QtWidgets.QLineEdit(self.stackedSine)
        self.vpForSine.setGeometry(QtCore.QRect(80, 10, 113, 21))
        self.vpForSine.setObjectName("vpForSine")
        self.stackedInputSignalOptions.addWidget(self.stackedSine)
        self.stackedCosine = QtWidgets.QWidget()
        self.stackedCosine.setObjectName("stackedCosine")
        self.periodInputBox_8 = QtWidgets.QLineEdit(self.stackedCosine)
        self.periodInputBox_8.setGeometry(QtCore.QRect(80, 50, 113, 21))
        self.periodInputBox_8.setObjectName("periodInputBox_8")
        self.periodInputLabel_8 = QtWidgets.QLabel(self.stackedCosine)
        self.periodInputLabel_8.setGeometry(QtCore.QRect(20, 10, 60, 16))
        self.periodInputLabel_8.setObjectName("periodInputLabel_8")
        self.periodInputLabel_9 = QtWidgets.QLabel(self.stackedCosine)
        self.periodInputLabel_9.setGeometry(QtCore.QRect(20, 50, 60, 16))
        self.periodInputLabel_9.setObjectName("periodInputLabel_9")
        self.periodInputBox_9 = QtWidgets.QLineEdit(self.stackedCosine)
        self.periodInputBox_9.setGeometry(QtCore.QRect(80, 10, 113, 21))
        self.periodInputBox_9.setObjectName("periodInputBox_9")
        self.periodInputBox_10 = QtWidgets.QLineEdit(self.stackedCosine)
        self.periodInputBox_10.setGeometry(QtCore.QRect(80, 90, 113, 21))
        self.periodInputBox_10.setObjectName("periodInputBox_10")
        self.periodInputLabel_10 = QtWidgets.QLabel(self.stackedCosine)
        self.periodInputLabel_10.setGeometry(QtCore.QRect(20, 90, 60, 16))
        self.periodInputLabel_10.setObjectName("periodInputLabel_10")
        self.stackedInputSignalOptions.addWidget(self.stackedCosine)
        self.stackedImpulse = QtWidgets.QWidget()
        self.stackedImpulse.setObjectName("stackedImpulse")
        self.periodInputBox_11 = QtWidgets.QLineEdit(self.stackedImpulse)
        self.periodInputBox_11.setGeometry(QtCore.QRect(80, 50, 113, 21))
        self.periodInputBox_11.setObjectName("periodInputBox_11")
        self.periodInputLabel_11 = QtWidgets.QLabel(self.stackedImpulse)
        self.periodInputLabel_11.setGeometry(QtCore.QRect(20, 10, 60, 16))
        self.periodInputLabel_11.setObjectName("periodInputLabel_11")
        self.periodInputLabel_12 = QtWidgets.QLabel(self.stackedImpulse)
        self.periodInputLabel_12.setGeometry(QtCore.QRect(20, 50, 60, 16))
        self.periodInputLabel_12.setObjectName("periodInputLabel_12")
        self.periodInputBox_12 = QtWidgets.QLineEdit(self.stackedImpulse)
        self.periodInputBox_12.setGeometry(QtCore.QRect(80, 10, 113, 21))
        self.periodInputBox_12.setObjectName("periodInputBox_12")
        self.periodInputBox_13 = QtWidgets.QLineEdit(self.stackedImpulse)
        self.periodInputBox_13.setGeometry(QtCore.QRect(80, 90, 113, 21))
        self.periodInputBox_13.setObjectName("periodInputBox_13")
        self.periodInputLabel_13 = QtWidgets.QLabel(self.stackedImpulse)
        self.periodInputLabel_13.setGeometry(QtCore.QRect(20, 90, 60, 16))
        self.periodInputLabel_13.setObjectName("periodInputLabel_13")
        self.stackedInputSignalOptions.addWidget(self.stackedImpulse)
        self.stackedAM = QtWidgets.QWidget()
        self.stackedAM.setObjectName("stackedAM")
        self.periodInputBox_14 = QtWidgets.QLineEdit(self.stackedAM)
        self.periodInputBox_14.setGeometry(QtCore.QRect(80, 50, 113, 21))
        self.periodInputBox_14.setObjectName("periodInputBox_14")
        self.periodInputLabel_14 = QtWidgets.QLabel(self.stackedAM)
        self.periodInputLabel_14.setGeometry(QtCore.QRect(20, 10, 60, 16))
        self.periodInputLabel_14.setObjectName("periodInputLabel_14")
        self.periodInputLabel_15 = QtWidgets.QLabel(self.stackedAM)
        self.periodInputLabel_15.setGeometry(QtCore.QRect(20, 50, 60, 16))
        self.periodInputLabel_15.setObjectName("periodInputLabel_15")
        self.periodInputBox_15 = QtWidgets.QLineEdit(self.stackedAM)
        self.periodInputBox_15.setGeometry(QtCore.QRect(80, 10, 113, 21))
        self.periodInputBox_15.setObjectName("periodInputBox_15")
        self.periodInputBox_16 = QtWidgets.QLineEdit(self.stackedAM)
        self.periodInputBox_16.setGeometry(QtCore.QRect(80, 90, 113, 21))
        self.periodInputBox_16.setObjectName("periodInputBox_16")
        self.periodInputLabel_16 = QtWidgets.QLabel(self.stackedAM)
        self.periodInputLabel_16.setGeometry(QtCore.QRect(20, 90, 60, 16))
        self.periodInputLabel_16.setObjectName("periodInputLabel_16")
        self.stackedInputSignalOptions.addWidget(self.stackedAM)
        self.timePlot = plotTimeClass(self.centralwidget)
        self.timePlot.setGeometry(QtCore.QRect(30, 270, 531, 411))
        self.timePlot.setObjectName("timePlot")
        self.frequencyPlot = plotFrequencyClass(self.centralwidget)
        self.frequencyPlot.setGeometry(QtCore.QRect(580, 270, 531, 411))
        self.frequencyPlot.setObjectName("frequencyPlot")
        self.clockPlot = plotClockClass(self.centralwidget)
        self.clockPlot.setGeometry(QtCore.QRect(420, 20, 271, 241))
        self.clockPlot.setObjectName("clockPlot")
        self.clockSignalLabel = QtWidgets.QLabel(self.centralwidget)
        self.clockSignalLabel.setGeometry(QtCore.QRect(420, 0, 121, 16))
        self.clockSignalLabel.setObjectName("clockSignalLabel")
        self.itbaLogoPlacer = QtWidgets.QLabel(self.centralwidget)
        self.itbaLogoPlacer.setGeometry(QtCore.QRect(450, 770, 211, 71))
        self.itbaLogoPlacer.setText("")
        self.itbaLogoPlacer.setPixmap(QtGui.QPixmap("designer/../resources/itbaLogo.png"))
        self.itbaLogoPlacer.setObjectName("itbaLogoPlacer")
        self.plotIncludeFAA = QtWidgets.QCheckBox(self.centralwidget)
        self.plotIncludeFAA.setGeometry(QtCore.QRect(150, 750, 21, 20))
        self.plotIncludeFAA.setText("")
        self.plotIncludeFAA.setChecked(True)
        self.plotIncludeFAA.setObjectName("plotIncludeFAA")
        self.plotIncludeSH = QtWidgets.QCheckBox(self.centralwidget)
        self.plotIncludeSH.setGeometry(QtCore.QRect(360, 750, 21, 20))
        self.plotIncludeSH.setText("")
        self.plotIncludeSH.setChecked(True)
        self.plotIncludeSH.setObjectName("plotIncludeSH")
        self.plotIncludeAnalogKey = QtWidgets.QCheckBox(self.centralwidget)
        self.plotIncludeAnalogKey.setGeometry(QtCore.QRect(580, 750, 21, 20))
        self.plotIncludeAnalogKey.setText("")
        self.plotIncludeAnalogKey.setChecked(True)
        self.plotIncludeAnalogKey.setObjectName("plotIncludeAnalogKey")
        self.plotIncludeRF = QtWidgets.QCheckBox(self.centralwidget)
        self.plotIncludeRF.setGeometry(QtCore.QRect(810, 750, 21, 20))
        self.plotIncludeRF.setText("")
        self.plotIncludeRF.setChecked(True)
        self.plotIncludeRF.setObjectName("plotIncludeRF")
        self.plotLabel = QtWidgets.QLabel(self.centralwidget)
        self.plotLabel.setGeometry(QtCore.QRect(120, 750, 31, 16))
        self.plotLabel.setObjectName("plotLabel")
        self.plotLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.plotLabel_2.setGeometry(QtCore.QRect(330, 750, 31, 16))
        self.plotLabel_2.setObjectName("plotLabel_2")
        self.plotLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.plotLabel_3.setGeometry(QtCore.QRect(550, 750, 31, 16))
        self.plotLabel_3.setObjectName("plotLabel_3")
        self.plotLabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.plotLabel_4.setGeometry(QtCore.QRect(780, 750, 31, 16))
        self.plotLabel_4.setObjectName("plotLabel_4")
        self.creditsButton = QtWidgets.QPushButton(self.centralwidget)
        self.creditsButton.setGeometry(QtCore.QRect(1080, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.creditsButton.setFont(font)
        self.creditsButton.setObjectName("creditsButton")
        self.plotXin = QtWidgets.QCheckBox(self.centralwidget)
        self.plotXin.setGeometry(QtCore.QRect(180, 230, 121, 20))
        self.plotXin.setChecked(True)
        self.plotXin.setObjectName("plotXin")
        self.maxFToPlot = QtWidgets.QLineEdit(self.centralwidget)
        self.maxFToPlot.setGeometry(QtCore.QRect(1000, 720, 71, 21))
        self.maxFToPlot.setObjectName("maxFToPlot")
        self.maxFToPlotLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxFToPlotLabel.setGeometry(QtCore.QRect(990, 680, 101, 16))
        self.maxFToPlotLabel.setObjectName("maxFToPlotLabel")
        self.maxFToPlotLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.maxFToPlotLabel_2.setGeometry(QtCore.QRect(1010, 700, 51, 16))
        self.maxFToPlotLabel_2.setObjectName("maxFToPlotLabel_2")
        self.maxFToPlotLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.maxFToPlotLabel_3.setGeometry(QtCore.QRect(1080, 720, 21, 20))
        self.maxFToPlotLabel_3.setObjectName("maxFToPlotLabel_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedInputSignalOptions.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.includeFAALabel.setText(_translate("MainWindow", "Antialias Filter"))
        self.includeSHLabel.setText(_translate("MainWindow", "Sample & Hold"))
        self.includeAnalogKeyLabel.setText(_translate("MainWindow", "Analog Switch"))
        self.includeFRLabel.setText(_translate("MainWindow", "Recovery Filter"))
        self.signalTypeInput.setItemText(0, _translate("MainWindow", "Sine"))
        self.signalTypeInput.setItemText(1, _translate("MainWindow", "Cosine"))
        self.signalTypeInput.setItemText(2, _translate("MainWindow", "3/2 Sine"))
        self.signalTypeInput.setItemText(3, _translate("MainWindow", "Sawtooth"))
        self.signalTypeInput.setItemText(4, _translate("MainWindow", "Impulse"))
        self.signalTypeInput.setItemText(5, _translate("MainWindow", "AM"))
        self.inputSignalXinLabel.setText(_translate("MainWindow", "Input Signal Xin"))
        self.sampleSignalLabel.setText(_translate("MainWindow", "Sample Signal"))
        self.acceptParametersButton.setText(_translate("MainWindow", "Enter parameters"))
        self.signalTypeLabel.setText(_translate("MainWindow", "Signal Type"))
        self.periodInputLabel.setText(_translate("MainWindow", "fs [Hz]"))
        self.dutyCycleInputLabel.setText(_translate("MainWindow", "Duty Cycle [%]"))
        self.periodInputLabel_7.setText(_translate("MainWindow", "?? [??]"))
        self.periodInputLabel_6.setText(_translate("MainWindow", "f [Hz]"))
        self.periodInputLabel_5.setText(_translate("MainWindow", "Vp [V]"))
        self.periodInputLabel_8.setText(_translate("MainWindow", "Vp"))
        self.periodInputLabel_9.setText(_translate("MainWindow", "f"))
        self.periodInputLabel_10.setText(_translate("MainWindow", "??"))
        self.periodInputLabel_11.setText(_translate("MainWindow", "Vp"))
        self.periodInputLabel_12.setText(_translate("MainWindow", "f"))
        self.periodInputLabel_13.setText(_translate("MainWindow", "??"))
        self.periodInputLabel_14.setText(_translate("MainWindow", "Vp"))
        self.periodInputLabel_15.setText(_translate("MainWindow", "f"))
        self.periodInputLabel_16.setText(_translate("MainWindow", "??"))
        self.clockSignalLabel.setText(_translate("MainWindow", "Clock Signal"))
        self.plotLabel.setText(_translate("MainWindow", "Plot"))
        self.plotLabel_2.setText(_translate("MainWindow", "Plot"))
        self.plotLabel_3.setText(_translate("MainWindow", "Plot"))
        self.plotLabel_4.setText(_translate("MainWindow", "Plot"))
        self.creditsButton.setText(_translate("MainWindow", "Credits"))
        self.plotXin.setText(_translate("MainWindow", "Plot Input Signal"))
        self.maxFToPlot.setText(_translate("MainWindow", "400000"))
        self.maxFToPlotLabel.setText(_translate("MainWindow", "Max Frequency"))
        self.maxFToPlotLabel_2.setText(_translate("MainWindow", "To Plot"))
        self.maxFToPlotLabel_3.setText(_translate("MainWindow", "Hz"))
from src.plotclockclass import plotClockClass
from src.plotfrequencyclass import plotFrequencyClass
from src.plottimeclass import plotTimeClass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
