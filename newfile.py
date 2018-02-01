import time
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
# time.sleep(10)

'''
window = pg.plot(title="HW")
SPI = pg.ScatterPlotItem(pen=None, symbol='t', symbolPen=None, symbolSize=10, symbolBrush=(100, 100, 255, 50))
x = [1,2,3]
y = [4,5,6]
SPI.addPoints(x, y)
'''
x = np.arange(10)
y = np.random.normal(size=(3, 10))
plotWidget = pg.plot(title="Three plot curves", x, y, pen=None)


'''
n = 300
s1 = pg.ScatterPlotItem(size=10, pen=pg.mkPen(None), brush=pg.mkBrush(255, 255, 255, 120))
pos = np.random.normal(size=(2,n), scale=1e-5)
spots = [{'pos': pos[:,i], 'data': 1} for i in range(n)] + [{'pos': [0,0], 'data': 1}]
s1.addPoints(spots)
window.plotItem(s1)
'''

# Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()


'''
p5 = win.addPlot(title="Scatter plot, axis labels, log scale")
x = np.random.normal(size=1000) * 1e-5
y = x*1000 + 0.005 * np.random.normal(size=1000)
y -= y.min()-1.0
mask = x > 1e-15
x = x[mask]
y = y[mask]
p5.plot(x, y, pen=None, symbol='t', symbolPen=None, symbolSize=10, symbolBrush=(100, 100, 255, 50))
p5.setLabel('left', "Y Axis", units='A')
p5.setLabel('bottom', "Y Axis", units='s')
p5.setLogMode(x=True, y=False)
'''


