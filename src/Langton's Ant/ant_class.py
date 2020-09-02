from PyQt5.QtWidgets import QGraphicsEllipseItem
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtCore import Qt


ant = QGraphicsEllipseItem(50, 50, 10, 10)
ant.setBrush(QBrush(QColor(0, 0, 255), Qt.SolidPattern))