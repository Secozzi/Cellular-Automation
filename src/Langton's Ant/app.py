from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QColor, QBrush


class Settings:
    BLOCK_WIDTH = 10
    BLOCK_HEIGHT = 10
    NUM_BLOCKS_X = 50
    NUM_BLOCKS_Y = 50

    SCREEN_WIDTH = BLOCK_WIDTH * NUM_BLOCKS_X
    SCREEN_HEIGHT = BLOCK_HEIGHT * NUM_BLOCKS_Y


class AppScene(QGraphicsScene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.lines = []

        self.draw_grid()
        self.set_opacity(0.7)
        self.draw_rect(3, 3, QColor(0, 255, 0))

    def draw_grid(self):
        width = Settings.SCREEN_WIDTH
        height = Settings.SCREEN_HEIGHT
        self.setSceneRect(0, 0, width, height)
        self.setItemIndexMethod(QGraphicsScene.NoIndex)

        pen = QPen(QColor(100, 100, 100), 1, Qt.SolidLine)

        for x in range(0, Settings.NUM_BLOCKS_X + 1):
            _x = x * Settings.BLOCK_WIDTH
            self.lines.append(self.addLine(_x, 0, _x, height, pen))

        for y in range(0, Settings.NUM_BLOCKS_Y + 1):
            _y = y * Settings.BLOCK_HEIGHT
            self.lines.append(self.addLine(0, _y, width, _y, pen))

    def sert_visible(self, visible=True):
        for line in self.lines:
            line.setVisible(visible)

    def draw_rect(self, col, row, color):
        # TODO: Make sure it doesn't draw of screen
        col = col * Settings.BLOCK_HEIGHT
        row = row * Settings.BLOCK_WIDTH
        rect = QGraphicsRectItem(row, col, Settings.BLOCK_WIDTH, Settings.BLOCK_HEIGHT)
        rect.setBrush(QBrush(color, Qt.SolidPattern))
        self.addItem(rect)

    def delete_grid(self):
        for line in self.lines:
            self.removeItem(line)
        del self.lines[:]

    def set_opacity(self, opacity):
        for line in self.lines:
            line.setOpacity(opacity)


class Appview(QGraphicsView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(Settings.SCREEN_WIDTH + 10, Settings.SCREEN_HEIGHT + 10)

    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)


if __name__ == "__main__":
    import sys
    sys._excepthook = sys.excepthook

    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = exception_hook
    app = QApplication(sys.argv)

    QScene = AppScene()
    win = Appview()
    win.setScene(QScene)
    win.show()
    sys.exit(app.exec_())