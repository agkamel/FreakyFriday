#INSTALL PyQt5 WITH:
# 1. ANACONDA:
# conda install -c anaconda pyqt
# 2. PIP:
# pip install PyQt5
#3. LINUX:
# sudo apt-get install python3-pyqt5

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from datetime import datetime
app = QApplication(sys.argv)

date_str = "Click the Button!"
widgets = {
    "button": [],
    "message": [],
    }



# Set main window and it's properties

window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80)

# Set Layout
layout = QGridLayout()


def clear_widgets():
    ''' remove all existing widgets from the window
        & clear the dictionary of widgets'''
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
            for i in range(0,len(widgets[widget])):
                widgets[widget].pop()

()

def button_refresh():
    global date_str
    clear_widgets()
    date_str = "Today is:" + str(datetime.now())
    frame1()

def frame1():
    '''Define our main frame'''

    button = QPushButton('What is the date?')
    button.clicked.connect(button_refresh)
    message = QLabel(date_str)

    widgets["button"].append(button)
    widgets['message'].append(message)
    layout.addWidget(widgets["button"][-1], 0, 0)
    layout.addWidget(widgets["message"][-1], 0, 1)
    widgets['button'][-1].show()
    widgets['message'][-1].show()



# Show our window
window.setLayout(layout)
window.show()
frame1()

sys.exit(app.exec_())
