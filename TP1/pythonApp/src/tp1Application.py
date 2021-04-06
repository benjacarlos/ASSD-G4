from PyQt5.QtWidgets import *
from src.ui.myTp1MainWindow import Ui_MainWindow
from scipy import signal
from scipy.fftpack import fft, fftfreq
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
        self.defineInput()
        self.plotTimeSignal()
        self.plotFrequencySignal()

    def defineInput(self):
        period = 1.0 / self.frequency
        self.t = np.linspace(0, 4*period, 1000)
        if self.signalType == 'Sine':
            self.y = self.vp * np.sin(2*np.pi*self.frequency*self.t)
        elif self.signalType == 'Cosine':
            self.y = self.vp * np.sin(2*np.pi*self.frequency*self.t + 0.5*np.pi)
        elif self.signalType == 'Sawtooth':
            self.y = self.vp * signal.sawtooth(2*np.pi*self.frequency*self.t)
        elif self.signalType == 'Impulse':
            self.y = self.vp * signal.square(2 * np.pi * self.frequency * self.t, 0.5)
        elif self.signalType == 'AM':
            self.fm = 0.2 * self.frequency
            self.fp = 2 * self.frequency
            m = 0.5
            period = 1/self.fm
            self.t = np.linspace(0, period, 1000)
            ym = np.cos(2 * np.pi * self.fm * self.t)
            yp = np.cos(2 * np.pi * self.fp * self.t)
            self.y = np.cos(2 * np.pi * 1.8 * self.fp * self.t) + 2*np.cos(2 * np.pi * 2 * self.fp * self.t) + np.cos(2*np.pi*2.2 * self.fp * self.t)
            # self.y = self.amplitude * (m * ym + 1)*yp
        self.dt = self.t[1] - self.t[0]




    def plotTimeSignal(self):

        self.timePlot.canvas.axes.clear()
        self.timePlot.canvas.axes.plot(self.t,self.y,label='Xin')
        self.timePlot.canvas.figure.tight_layout()

        if self.includeFAA.isChecked():
            print ("FAA esta incluido")
            (num, den, dt) = signal.cont2discrete((self.FAAFilterNum, self.FAAFilterDen), self.dt)
            self.y = signal.filtfilt(num.squeeze(), den.squeeze(), self.y)
            self.timePlot.canvas.axes.plot(self.t,self.y,label='Xin Filtrada')
            self.timePlot.canvas.figure.tight_layout()
        if self.includeSH.isChecked():
            print ("SH esta incluido")
        if self.includeAnalogKey.isChecked():
            print ("Analog Key esta incluido")
        if self.includeRF.isChecked():
            print ("Recovery Filter esta incluido")

        title = "Signal Sampled: " + self.signalType
        self.timePlot.canvas.axes.axes.set_xlabel("Time [s]")
        self.timePlot.canvas.axes.axes.set_ylabel("V [V]")
        self.timePlot.canvas.axes.title.set_text(title)
        self.timePlot.canvas.axes.grid(which='both', axis='both')
        theLegend = self.timePlot.canvas.axes.legend(fancybox=True, framealpha=0.5, fontsize=6)
        self.timePlot.canvas.figure.tight_layout()

        self.timePlot.canvas.draw()

    def plotFrequencySignal(self):
        self.timeToFTT()
        self.frequencyPlot.canvas.axes.clear()
        self.frequencyPlot.canvas.axes.plot(self.f, np.abs(self.fourierSignal), label='Xin')
        self.frequencyPlot.canvas.figure.tight_layout()

        if self.includeFAA.isChecked():
            print ("FAA esta incluido")
            (num, den, dt) = signal.cont2discrete((self.FAAFilterNum, self.FAAFilterDen), self.dt)
            self.y = signal.filtfilt(num.squeeze(), den.squeeze(), self.y)
            self.timeToFTT()
            self.frequencyPlot.canvas.axes.plot(self.f, np.abs(self.fourierSignal), label='Xin Filtrada')
            self.frequencyPlot.canvas.figure.tight_layout()
        if self.includeSH.isChecked():
            print ("SH esta incluido")
        if self.includeAnalogKey.isChecked():
            print ("Analog Key esta incluido")
        if self.includeRF.isChecked():
            print ("Recovery Filter esta incluido")

        title = "Signal Sampled: " + self.signalType
        self.frequencyPlot.canvas.axes.axes.set_xlabel("Frequency [s]")
        self.frequencyPlot.canvas.axes.axes.set_ylabel("Amplitud [Db]")
        self.frequencyPlot.canvas.axes.title.set_text(title)
        self.frequencyPlot.canvas.axes.grid(which='both', axis='both')
        theLegend = self.frequencyPlot.canvas.axes.legend(fancybox=True, framealpha=0.5, fontsize=6)
        self.frequencyPlot.canvas.axes.set_xlim(0, self.frequency * 10)
        self.frequencyPlot.canvas.figure.tight_layout()
        self.frequencyPlot.canvas.draw()

    def timeToFTT(self):
        self.fourierSignal = fft(self.y,n=1000000)#, n=100000)
        #self.signal_psd = 20 * np.log(np.abs(self.fourierSignal))
        self.f = fftfreq(len(self.fourierSignal), self.dt)
        i = self.f > 0
        self.f = self.f[i]
        self.fourierSignal = self.fourierSignal[i]












