from pyqtgraph.Qt import QtGui, QtCore, USE_PYSIDE, USE_PYQT5
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
#QtGui.QApplication.setGraphicsSystem('raster')
#app = QtGui.QApplication([])
#mw = QtGui.QMainWindow()
#mw.resize(800,800)

win = QtGui.QWidget()
win.setWindowTitle('pyqtgraph example: ScatterPlotSpeedTest')
ui = Ui_Form()
ui.setupUi(win)
win.show()

p = ui.plot
p.setRange(xRange=[-500, 500], yRange=[-500, 500])

data = np.random.normal(size=(50,500), scale=100)
sizeArray = (np.random.random(500) * 20.).astype(int)
ptr = 0

def update():
    global curve, data, ptr, p, lastTime, fps
    p.clear()
    size = sizeArray
    curve = pg.ScatterPlotItem(x=data[ptr%50], y=data[(ptr+1)%50], pen='w', brush='b', size=size)
    p.addItem(curve)
    ptr += 1
    p.repaint()
    #app.processEvents()  ## force complete redraw for every plot
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)
    


## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()