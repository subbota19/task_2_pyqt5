import sys, os, numpy, cmath
from pyqtgraph import PlotWidget, plot
import pyqtgraph
from PyQt5 import QtWidgets
import graphic


class App(QtWidgets.QMainWindow, graphic.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.make_axis)
        self.pushButton_5.clicked.connect(self.exit)

    def exit(self):
        sys.exit()

    def make_axis(self):
        self.widget.clear()

        self.max_x = eval(self.lineEdit.text())
        self.min_x = eval(self.lineEdit_3.text())
        self.max_y = eval(self.lineEdit_2.text())
        self.min_y = eval(self.lineEdit_4.text())
        self.main_step = eval(self.lineEdit_7.text())

        list_x = [x for x in numpy.arange(self.min_x, self.max_x, self.main_step)]
        list_sin_y = [cmath.sin(y).real for y in list_x]
        list_cos_y = [cmath.cos(y).real for y in list_x]

        self.widget.setLimits(xMin=self.min_x, xMax=self.max_x, yMin=self.min_y, yMax=self.max_y)
        self.widget.addLegend()


        self.widget.plot(list_x, list_sin_y, pen='r', name="sin(x)")
        self.widget.plot(list_x, list_cos_y, pen='b', name="cos(x)")

        self.widget.showGrid(x=True, y=True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()
