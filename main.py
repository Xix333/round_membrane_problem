import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PySide6.QtCore import QRect
import RoundMembrane




path_to_visualization = os.path.join('..','membrane.png')







class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.round_membrane = RoundMembrane.RoundMembrane(1,1)
        self.setGeometry(QRect(100, 100, 1280, 720))
        self.setWindowTitle('Round Membrane Problem')

        widget = QWidget(parent=self)
        self.setCentralWidget(widget)


        self.TextBox = QLineEdit(text='2, 1')
        button_mode_set = QPushButton("Set the modes", parent=self)
        button_mode_set.clicked.connect(self.setModes)


        plotLayout = QHBoxLayout()

        
        self.round_membrane.visualize()

        plotLayout.addWidget(self.round_membrane)

        problemSetupLayout = QHBoxLayout()
        problemSetupLayout.addWidget(self.TextBox)
        problemSetupLayout.addWidget(button_mode_set)
        

        allLayouts = QVBoxLayout()
        allLayouts.addLayout(plotLayout)
        allLayouts.addLayout(problemSetupLayout)
        
        widget.setLayout(allLayouts)
        self.show()

    def setModes(self):
            if (self.TextBox.text() != '' and str.isnumeric(self.TextBox.text().split(', ')[0]) and str.isnumeric(self.TextBox.text().split(', ')[1])):
                self.round_membrane.m = int(self.TextBox.text().split(',')[0])
                self.round_membrane.n = int(self.TextBox.text().split(',')[1])
                self.round_membrane.refreshData()
                self.round_membrane.visualize()
            else:
                pass



app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()