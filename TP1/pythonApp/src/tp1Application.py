from PyQt5.QtWidgets import *
from src.ui.myTp1MainWindow import Ui_MainWindow
from scipy import signal
import numpy as np

class myTp1Application(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(myTp1Application, self).__init__()
        self.setupUi(self)
        #self.plotTimeSignal()
        self.data = 0
        self.includeFAAOption = False
        self.includeSHOption = False
        self.includeAnalogSwitchOption = False
        self.includeRFilterOption = False
        self.signalType = "Nada"
        self.frequency = 0
        self.vp = 0
        self.phase = 0
        self.period = 0
        self.dutyCycle = 0
        self.FAAFilterNum = [1.53832195e+45]
        self.FAAFilterDen = [1, 1.30204833e+06, 1.52443780e+12, 1.09680680e+18, 6.33511591e+23, 2.62677859e+29, 7.97250241e+34, 1.56615935e+40, 1.53832195e+45]


        self.acceptParametersButton.clicked.connect(self.acceptParameters)


    def acceptParameters(self):
        ErrorMessage = ""
        msgWrongInput = QMessageBox()
        msgWrongInput.setIcon(QMessageBox.Warning)
        msgWrongInput.setWindowTitle('Error')
        self.includeFAAOption = False
        self.includeSHOption = False
        self.includeAnalogSwitchOption = False
        self.includeRFilterOption = False
        self.signalType = str(self.signalTypeInput.currentText())
        self.vp = float(self.vpForSine.text())
        self.frequency = float(self.fForSine.text())
        self.phase = float(self.phaseForSine.text())
        self.period = float(self.periodInputBox.text())
        self.dutyCycle = float(self.dutyCycleInputBox.text())
        self.plotTimeSignal()

    def plotTimeSignal(self):
        period = 1.0 / self.frequency
        if self.signalType == 'Sine':
            t = np.linspace(0, 4*period, 1000)
            y = self.vp * np.sin(2*np.pi*self.frequency*t)
        elif self.signalType == 'Cosine':
            t = np.linspace(0, 4*period, 1000)
            y = self.vp * np.sin(2*np.pi*self.frequency*t + 0.5*np.pi)
        elif self.signalType == 'Sawtooth':
            t = np.linspace(0, 4*period, 1000)
            y = self.vp * signal.sawtooth(2*np.pi*self.frequency*t)
        elif self.signalType == 'Impulse':
            t = np.linspace(0, 4*period, 1000)
            y = self.vp * signal.square(2 * np.pi * self.frequency * t, 0.5)

        dt = t[1] - t[0]
        self.timePlot.canvas.axes.clear()
        self.timePlot.canvas.axes.plot(t,y,label='Xin')
        self.timePlot.canvas.figure.tight_layout()

        if self.includeFAA.isChecked():
            print ("FAA esta incluido")
            x=y
            (num, den, dt) = signal.cont2discrete((self.FAAFilterNum, self.FAAFilterDen), dt)
            yout = signal.filtfilt(num.squeeze(), den.squeeze(), x)
            self.timePlot.canvas.axes.plot(t,yout,label='Xin Filtrada')
            self.timePlot.canvas.figure.tight_layout()
        if self.includeSH.isChecked():
            print ("SH esta incluido")
        if self.includeAnalogKey.isChecked():
            print ("Analog Key esta incluido")
        if self.includeRF.isChecked():
            print ("Recovery Filter esta incluido")

        self.timePlot.canvas.axes.grid(which='both', axis='both')
        theLegend = self.timePlot.canvas.axes.legend(fancybox=True, framealpha=0.5, fontsize=6)
        self.timePlot.canvas.axes.axes.set_xlabel("Time [s]")
        self.timePlot.canvas.axes.axes.set_ylabel("V [V]")
        self.timePlot.canvas.axes.title.set_text('Signal in Time')
        self.timePlot.canvas.draw()














