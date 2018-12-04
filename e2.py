
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QBasicTimer
import sys

class Window(QWidget):
    def __init__(self):
            super().__init__()
            self.initWindow()

    def initWindow(self):
        self.progress =  QProgressBar(self)
        self.progress.setGeometry(30,40,200,25)
        self.progress.setMinimum(0)
        self.progress.setMaximum(5000)
        self.start = QPushButton('Start', self)
        self.start.move(40,80)
        self.start.clicked.connect(self.doStart)
        self.stop = QPushButton('Stop', self)
        self.stop.move(140,80)
        self.stop.clicked.connect(self.doStop)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('Exercise 2')
        self.show()

    def timerEvent(self, e):
        if self.step >= 5000:
                self.timer.stop()
                self.step = 0
                return
        self.step = self.step + 1
        self.progress.setValue(self.step)

    def doStart(self):
        self.timer.start(1, self)

    def doStop(self):
        self.timer.stop()
        



if __name__ == '__main__':
    app = QApplication([])
    w = Window()
    sys.exit(app.exec_())



