from pathlib import Path

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer, QThreadPool
from PyQt5 import uic
from worker import GoL_Worker

import random
import numpy as np

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from game_of_life import Board

class GameOfLife(QMainWindow):
    def __init__(self):
        super().__init__()

        self.grid_width = 200
        self.grid_height = 200
        self.speed = 1

        self.timer = QTimer()

        self.init_ui()

    def stop_thread(self):
        pass

    def start_thread(self):
        self.threadpool = QThreadPool()


    def init_ui(self):
        uic.loadUi(Path("Qt_assets/main.ui"), self)
        self.init_mpl()
        self.init_buttons()
        self.show()

    def init_mpl(self):
        self.mplWidget.axes.clear()
        self.mplWidget.axes.set_title("Conway's game of life")

    def init_buttons(self):
        self.restart_game.clicked.connect(self.set_board)
        self.grid_width_slider.valueChanged.connect(self.set_grid_width)
        self.grid_height_slider.valueChanged.connect(self.set_grid_height)
        self.speed_slider.valueChanged.connect(self.set_speed)
        self.iteration_play.clicked.connect(self.set_timer)
        self.iteration_next.clicked.connect(self.next_iteration)

    def set_timer(self):
        if self.iteration_play.isChecked():
            self.timer.stop()
        else:
            self.timer.start()

    def set_grid_width(self, value):
        self.grid_width = value

    def set_grid_height(self, value):
        self.grid_height = value

    def set_speed(self, value):
        print(value)
        self.speed = value
        self.timer.setInterval(1000 / self.speed)

    def next_iteration(self):
        self.call_worker()


    def set_board(self):
        self.board = np.random.randint(2, size=(self.grid_height, self.grid_width))
        print(type(self.board))

        self.show()

        self.timer.setInterval(1000 / self.speed)
        self.timer.timeout.connect(self.call_worker)
        self.timer.start()

    def call_worker(self):
        self.worker = GoL_Worker(self.board, self.grid_height, self.grid_width)
        self.worker.signals.output.connect(self.graph_grid)
        self.worker.signals.finished.connect(self.stop_thread)

        self.threadpool.start(self.worker)

    def graph_grid(self, input_array):
        self.mplWidget.axes.cla()  # Clear the canvas.
        self.mplWidget.axes.imshow(input_array)
        # Trigger the canvas to update and redraw.
        self.mplWidget.draw()

def launch_app():
    import sys
    app = QApplication(sys.argv)
    gol = GameOfLife()
    gol.start_thread()
    sys.exit(app.exec_())

if __name__ == '__main__':
    launch_app()