from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, QRect
from game_of_life_utils import ALIVE, EMPTY


class Canvas(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setFixedSize(self.parent.width(), self.parent.height() - 100)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(200, 200, 200))

        cell_size = self.parent.cell_size * self.parent.scale
        cell_size_int = int(cell_size)

        for y in range(self.parent.grid_height):
            for x in range(self.parent.grid_width):
                if self.parent.grid[y, x] == ALIVE:
                    rect = QRect(x * cell_size, y * cell_size, cell_size_int, cell_size_int)
                    painter.fillRect(rect, QColor(255, 255, 0))

        pen = painter.pen()
        pen.setColor(QColor(150, 150, 150))
        painter.setPen(pen)

        for x in range(0, self.width(), cell_size_int):
            painter.drawLine(x, 0, x, self.height())

        for y in range(0, self.height(), cell_size_int):
            painter.drawLine(0, y, self.width(), y)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            x = int(event.position().toPoint().x() // (self.parent.cell_size * self.parent.scale))
            y = int(event.position().toPoint().y() // (self.parent.cell_size * self.parent.scale))
            if 0 <= x < self.parent.grid_width and 0 <= y < self.parent.grid_height:
                if self.parent.current_template:
                    self.place_template(x, y)
                else:
                    self.parent.grid[y, x] = ALIVE if self.parent.grid[y, x] == EMPTY else EMPTY
                self.update()

    def place_template(self, x, y):
        for dy, dx in self.parent.current_template:
            ny, nx = y + dy, x + dx
            if 0 <= ny < self.parent.grid_height and 0 <= nx < self.parent.grid_width:
                self.parent.grid[ny, nx] = ALIVE
        self.update()
