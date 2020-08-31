from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot, QRunnable
import numpy as np

class WorkerSignals(QObject):
    finished = pyqtSignal()
    output = pyqtSignal(np.ndarray)

class GoL_Worker(QRunnable):
    def __init__(self, input_array, height, width):
        super(GoL_Worker, self).__init__()

        self.input_array = input_array
        self.height = height
        self.width = width

        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        result = self.create_new_array()

        self.signals.output.emit(result)
        self.signals.finished.emit()

    @pyqtSlot()
    def create_new_array(self):
        return np.random.randint(2, size=(self.height, self.width))