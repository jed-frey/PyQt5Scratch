#!/usr/bin/env python3

from PyQt5.uic import loadUiType
from PyQt5 import QtCore, QtWidgets
import sys

import numpy as np

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

#Ui_MainWindow, QMainWindow = loadUiType('window2.ui')

from window2 import Ui_MainWindow


class ControlCanvas(FigureCanvas):
    """ Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.).
    """
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)
        
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        
        
        fig1 = Figure()
        ax1f1 = fig1.add_subplot(111)
        ax1f1.plot(np.random.rand(5))
        
        
        self.canvas = FigureCanvas(fig1)        
        
        self.verticalLayout.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas, self.mplwindow, coordinates=True)
        self.mplvl.addWidget(self.toolbar)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    main = MainWindow() 
    main.show()
    sys.exit(app.exec_())
