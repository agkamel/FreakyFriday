

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from datetime import datetime


app = QApplication(sys.argv)

# Set main window and it's properties
window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80)

# Set Layout
layout = QGridLayout()
# ------------------------
# Basic window Code
# ------------------------
# window.move(60, 15)
# helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
# helloMsg.move(60, 15)
# helloButton = QPushButton('Hello World!', parent=window)
# helloButton.move(550, 200)


# ------------------------
# Basic GridLayout Code
# ------------------------
# Setting Our GridLayout
# layout = QGridLayout()
# layout.addWidget(QPushButton('Button (0, 0)'), 0, 0)
# layout.addWidget(QPushButton('Button (0, 1)'), 0, 1)
# layout.addWidget(QPushButton('Button (0, 2)'), 0, 2)
# layout.addWidget(QPushButton('Button (1, 0)'), 1, 0)
# layout.addWidget(QPushButton('Button (1, 1)'), 1, 1)
# layout.addWidget(QPushButton('Button (1, 2)'), 1, 2)
# layout.addWidget(QPushButton('Button (2, 0)'), 2, 0)
# layout.addWidget(QPushButton('Button (2, 1) + 2 Columns Span'), 2, 1, 1, 2)
# window.setLayout(layout)


# Show our window
window.setLayout(layout)
window.show()
