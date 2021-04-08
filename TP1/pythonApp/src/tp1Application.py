from PyQt5.QtWidgets import *
from src.ui.myTp1MainWindow import Ui_MainWindow
from scipy import signal
from scipy.fftpack import fft, fftfreq
import numpy as np

class myTp1Application(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(myTp1Application, self).__init__()
        self.setupUi(self)
        self.data = 0
        self.signalType = "Nada"
        self.frequency = 0
        self.vp = 0
        self.phase = 0
        self.period = 0
        self.dutyCycle = 0
        self.y = []

        #######################################
        # Definición de FAA y RF implementado #
        # Legendre, N=8, fp=100K, fa=150k     #
        # Ap=40, Aa=1                         #
        #######################################

        self.FAAFilterNum = [1.53832195e+45]
        self.FAAFilterDen = [1, 1.30204833e+06, 1.52443780e+12, 1.09680680e+18, 6.33511591e+23, 2.62677859e+29, 7.97250241e+34, 1.56615935e+40, 1.53832195e+45]


        self.acceptParametersButton.clicked.connect(self.acceptParameters)
        self.creditsButton.clicked.connect(self.showCredits)

    def showCredits(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("ASSD - 1Q2021 \n \n Profesor: \n Jacoby, Daniel \n \n Alumnos:\n Chiocci, Ramiro \n Lin, Benjamín \n Mestanza,Nicolás \n Molina, Facundo \n Navarro, Paulo")
        msgBox.setWindowTitle("QMessageBox Example")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.exec()

    def acceptParameters(self):
        self.signalType = "Nada"
        self.frequency = 0
        self.vp = 0
        self.phase = 0
        self.period = 0
        self.dutyCycle = 0
        self.y = []
        self.dt = 0
        self.f=0
        self.fourierSignal = 0
        ErrorMessage = ""
        msgWrongInput = QMessageBox()
        msgWrongInput.setIcon(QMessageBox.Warning)
        msgWrongInput.setWindowTitle('Error')

        self.signalType = str(self.signalTypeInput.currentText())

        try:
            self.vp = float(self.vpForSine.text())
            if (self.vp <= 0) or (self.vp > 10) :
                raise Exception("Exception")
        except:
            ErrorMessage = ErrorMessage + "The Vp must be a valid number (0 to 10 V) \n"

        try:
            self.frequency = float(self.fForSine.text())
            if (self.frequency <= 0):
                raise Exception("Exception")
        except:
            ErrorMessage = ErrorMessage + "The frequency must be a valid postive number\n"

        try:
            self.phase = float(self.phaseForSine.text())
        except:
            ErrorMessage = ErrorMessage + "The Phase must be a valid number\n"

        try:
            self.period = float(self.oscilatorPeriod.text())
            if self.period <= 0:
                raise Exception("Exception")
        except:
            ErrorMessage = ErrorMessage + "The Fs must be a valid positive number\n"

        try:
            self.dutyCycle = float(self.dutyCycleInputBox.text())/100
            if self.dutyCycle <= 0 or self.dutyCycle > 1:
                raise Exception("Exception")
        except:
            ErrorMessage = ErrorMessage + "The Duty Cycle must be a valid number (0 to 100)\n"

        if ErrorMessage != "":
            msgWrongInput.setText(ErrorMessage)
            msgWrongInput.exec()
            self.signalType = "Nada"
            self.frequency = 0
            self.vp = 0
            self.phase = 0
            self.period = 0
            self.dutyCycle = 0
            self.y = []
            self.dt = 0
            self.f=0
            self.fourierSignal=0

        else:
            self.defineInput()
            self.plotTimeSignal()
            self.defineInput()
            self.plotFrequencySignal()
            self.plotClockSignal()

    def plotClockSignal(self):
        self.clockPlot.canvas.axes.clear()
        self.clockPlot.canvas.axes.plot(self.t,self.yForOscillator)
        self.clockPlot.canvas.figure.tight_layout()
        self.clockPlot.canvas.axes.axes.set_xlabel("Time [s]")
        self.clockPlot.canvas.axes.grid(which='both', axis='both')
        self.clockPlot.canvas.figure.tight_layout()
        self.clockPlot.canvas.draw()

    def defineOscillatorSampler(self):
        self.yForOscillator = (signal.square(2 * np.pi * self.period * self.t, self.dutyCycle) + 1)/2.

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


        elif self.signalType == "3/2 Sine":
            self.y=[]
            period = period * 3 / 2
            self.t = np.linspace(0, 4*period, 1000)
            tempT =  np.linspace(0, period, 100)
            tempY = self.vp * np.sin(2 * np.pi * self.frequency * tempT)
            for i in range(0, 10):              # 10 * 100 = 1000 . Size of t array. Don-t change
                for tempSinSum in tempY:
                    self.y.append(tempSinSum)

        elif self.signalType == 'AM':
            self.fm = 0.2 * self.frequency
            self.fp = 2 * self.frequency
            m = 0.5
            period = 1/self.fm
            self.t = np.linspace(0, period, 1000)
            self.y = np.cos(2 * np.pi * 1.8 * self.fp * self.t) + 2*np.cos(2 * np.pi * 2 * self.fp * self.t) + np.cos(2*np.pi*2.2 * self.fp * self.t)


        self.dt = self.t[1] - self.t[0]

        self.defineOscillatorSampler()

    def plotTimeSignal(self):

        self.timePlot.canvas.axes.clear()
        self.timePlot.canvas.axes.plot(self.t,self.y,label='Xin')
        self.timePlot.canvas.figure.tight_layout()

        if self.includeFAA.isChecked():
            self.signalFilteredByFAA()
            if self.plotIncludeFAA.isChecked():
                self.timePlot.canvas.axes.plot(self.t,self.y,label='Xin Filtrada')
                self.timePlot.canvas.figure.tight_layout()


        if self.includeSH.isChecked():
            self.signalWithSH()
            if self.plotIncludeSH.isChecked():
                self.timePlot.canvas.axes.plot(self.t,self.y,label='Xin SH')
                self.timePlot.canvas.figure.tight_layout()


        if self.includeAnalogKey.isChecked():
            self.signalWithAnalogSwitch()
            if self.plotIncludeAnalogKey.isChecked():
                self.timePlot.canvas.axes.plot(self.t,self.y,label='Xin with Analog Switch')
                self.timePlot.canvas.figure.tight_layout()


        if self.includeRF.isChecked():
            self.signalFilteredByRF()
            if self.plotIncludeRF.isChecked():
                self.timePlot.canvas.axes.plot(self.t,self.y,label='Xin Recovered with RF')
                self.timePlot.canvas.figure.tight_layout()



        self.timePlot.canvas.axes.axes.tick_params(axis='x',labelrotation=90)
        title = "Signal: " + self.signalType
        self.timePlot.canvas.axes.axes.set_xlabel("Time [s]")
        self.timePlot.canvas.axes.axes.set_ylabel("Amplitude [V]")
        self.timePlot.canvas.axes.title.set_text(title)
        self.timePlot.canvas.axes.grid(which='both', axis='both')
        theLegend = self.timePlot.canvas.axes.legend(fancybox=True, framealpha=0.5, fontsize=6)
        self.timePlot.canvas.figure.tight_layout()

        self.timePlot.canvas.draw()

    def plotFrequencySignal(self):
        self.timeToFTT()
        self.frequencyPlot.canvas.axes.clear()
        self.frequencyPlot.canvas.axes.plot(self.f, self.fourierSignal, label='Xin')
        self.frequencyPlot.canvas.figure.tight_layout()


        if self.includeFAA.isChecked():
            self.signalFilteredByFAA()
            self.timeToFTT()
            if self.plotIncludeFAA.isChecked():
                self.frequencyPlot.canvas.axes.plot(self.f, self.fourierSignal, label='Xin Filtrada')
                self.frequencyPlot.canvas.figure.tight_layout()


        if self.includeSH.isChecked():
            self.signalWithSH()
            self.timeToFTT()
            if self.plotIncludeSH.isChecked():
                self.frequencyPlot.canvas.axes.plot(self.f, self.fourierSignal, label='Xin SH')
                self.frequencyPlot.canvas.figure.tight_layout()


        if self.includeAnalogKey.isChecked():
            self.signalWithAnalogSwitch()
            self.timeToFTT()
            if self.plotIncludeAnalogKey.isChecked():
                self.frequencyPlot.canvas.axes.plot(self.f, self.fourierSignal, label='Xin SH and Analog')
                self.frequencyPlot.canvas.figure.tight_layout()


        if self.includeRF.isChecked():
            self.signalFilteredByRF()
            self.timeToFTT()
            if self.plotIncludeRF.isChecked():
                self.frequencyPlot.canvas.axes.plot(self.f, np.abs(self.fourierSignal), label='Xin Recovered by RF')
                self.frequencyPlot.canvas.figure.tight_layout()



        self.frequencyPlot.canvas.axes.axes.tick_params(axis='x',labelrotation=90)
        title = "Spectrum: " + self.signalType
        self.frequencyPlot.canvas.axes.axes.set_xlabel("Frequency [Hz]")
        self.frequencyPlot.canvas.axes.axes.set_ylabel("Magnitude")
        self.frequencyPlot.canvas.axes.title.set_text(title)
        self.frequencyPlot.canvas.axes.grid(which='both', axis='both')
        theLegend = self.frequencyPlot.canvas.axes.legend(fancybox=True, framealpha=0.5, fontsize=6)
        self.frequencyPlot.canvas.axes.set_xlim(0, 400000)
        self.frequencyPlot.canvas.figure.tight_layout()
        self.frequencyPlot.canvas.draw()

    def timeToFTT(self):
        self.fourierSignal = fft(self.y,n=1000000)

        ###########################################################################################
        # Redefino la transformada de Fourier solo para quedarme con las frecuencias positivas.   #
        # Para mas info: https://docs.scipy.org/doc/scipy/reference/tutorial/fft.html             #
        ###########################################################################################

        self.f = fftfreq(len(self.fourierSignal), self.dt)[:len(self.fourierSignal)//2]
        self.fourierSignal = 2.0/len(self.fourierSignal) * np.abs(self.fourierSignal[0:len(self.fourierSignal)//2])



    def signalFilteredByFAA(self):
        print ("FAA esta incluido")

        (self.num, self.den, self.dt) = signal.cont2discrete((self.FAAFilterNum, self.FAAFilterDen), self.dt)
        self.y = signal.filtfilt(self.num.squeeze(), self.den.squeeze(), self.y)

    def signalWithSH(self):
        print ("SH esta incluido")
        self.valueToHold = 0
        self.changed = False
        self.yForSignalSH = []

        for clockSignalIndex in range(len(self.yForOscillator)):

            if self.yForOscillator[clockSignalIndex] == 1:
                self.yForSignalSH.append(self.valueToHold)

            if self.yForOscillator[clockSignalIndex] == 0:
                self.yForSignalSH.append(self.y[clockSignalIndex])
                self.valueToHold = self.y[clockSignalIndex]

        self.y = self.yForSignalSH

    def signalWithAnalogSwitch(self):
        print ("AnalogSwitch esta incluido")

        tempY = []

        for i in range(0, len(self.t)):
            if self.yForOscillator[i] == 1:
                tempY.append(self.y[i])
            else:
                tempY.append(0)
        self.y = tempY


    def signalFilteredByRF(self):
        print ("RecoveryFilter esta incluido")

        # Se usa RF el mismo que FAA por diseño del grupo

        self.signalFilteredByFAA()














