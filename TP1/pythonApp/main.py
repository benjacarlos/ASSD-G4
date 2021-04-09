import os
from enum import Enum


from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog
from src.tp1Application import myTp1Application


##################################
# GRUPO 4 - ASSD - TP1 - 2021 :) #
##################################

if __name__ == "__main__":

    app = QApplication([])
    myMainWindow = QMainWindow()

    #############################################
    # Se aplican estilos según CSS StyleSheet   #
    #############################################

    with open ("src/style/style.qss", "r") as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)

    #############################################

    widget = myTp1Application()

    #############################################
    # Centralización de pantalla de aplicación  #
    #############################################

    qr = widget.frameGeometry()
    centerPoint = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(centerPoint)
    widget.move(qr.topLeft())

    #############################################

    widget.setWindowTitle("Trabajo Práctico 1 - Grupo 4 - ASSD - 1Q2021")
    widget.show()
    app.exec()
