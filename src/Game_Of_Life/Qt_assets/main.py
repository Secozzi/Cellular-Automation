from pathlib import Path

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

import random
import numpy as np

class GameOfLife(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        uic.loadUi(Path("main.ui"), self)
        self.init_buttons()
        self.show()

    def init_buttons(self):
        self.restart_game.clicked.connect(self.add_graph)

    def add_graph(self):
        fs = 500
        f = random.randint(1, 100)
        ts = 1 / fs
        length_of_signal = 100
        t = np.linspace(0, 1, length_of_signal)

        cosinus_signal = np.cos(2 * np.pi * f * t)
        sinus_signal = np.sin(2 * np.pi * f * t)

        self.mplWidget.canvas.axes.clear()
        self.mplWidget.canvas.axes.plot(t, cosinus_signal)
        self.mplWidget.canvas.axes.plot(t, sinus_signal)
        self.mplWidget.canvas.axes.legend(('cosinus', 'sinus'), loc='upper right')
        self.mplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
        self.mplWidget.canvas.draw()

def launch_app():
    import sys
    app = QApplication(sys.argv)
    gol = GameOfLife()
    sys.exit(app.exec_())

if __name__ == '__main__':
    launch_app()