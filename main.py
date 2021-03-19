from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QListWidget, QGridLayout

from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from datetime import datetime
from PyQt5.QtCore import QDateTime, Qt, QTimer
from datetime import datetime
import sys

class Activity(QWidget):
    start_time = None
    end_time = None
    duration = None
    def __init__(self,parent=None):
        super(Activity, self).__init__(parent)
        self.setWindowTitle('QTimer example')

        self.listFile=QListWidget()
        self.label=QLabel('Label')
        self.label.setAlignment(Qt.AlignCenter)
        self.startBtn=QPushButton('Start')
        self.endBtn=QPushButton('Stop')

        outerlayout = QVBoxLayout()
        labellayout = QVBoxLayout()
        layout=QGridLayout()

        self.timer=QTimer()
        self.timer.timeout.connect(self.showTime)

        labellayout.addWidget(self.label)
        layout.addWidget(self.startBtn,1,0)
        layout.addWidget(self.endBtn,1,1)
        outerlayout.addLayout(labellayout)
        outerlayout.addLayout(layout)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)

        self.setLayout(outerlayout)

    def showTime(self):
        current_time = datetime.now()
        self.duration = current_time - self.start_time
        self.label.setText("Activity in Progress\n {}".format(self.duration))

    def startTimer(self):
        if (self.start_time is None):
            self.start_time = datetime.now()
        print(self.start_time)
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)

    def endTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)

class MainWindow(QWidget):
    # self.widgets = {
    # "button": [],
    # "message": [],
    # }

    def __init__(self):
        super().__init__()
        self.w = None  # No external window yet.
        self.button = QPushButton("Start Activity")
        self.button.clicked.connect(self.start_activity)
        layout=QGridLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def start_activity(self, checked):
       self.timer_window = Activity()
       self.hide()
       self.timer_window.show()
        # if self.w is None:
        #     self.w = AnotherWindow()
        #     self.w.show()

        # else:
        #     self.w.close()  # Close window.
        #     self.w = None  # Discard reference.

if __name__ == '__main__':
    app=QApplication(sys.argv)
    # form=WinForm()
    # form.show()
window = MainWindow()
window.show()
sys.exit(app.exec_())
# sys.exit(app.exec_())
