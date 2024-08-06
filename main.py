import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QSlider, QLabel, QGridLayout, \
    QComboBox
from PyQt6.QtCore import QTimer, Qt
from game_of_life_ui import Canvas
from game_of_life_utils import Grid, update_grid, ALIVE, EMPTY

TEMPLATES = {
    'Block': [(0, 0), (0, 1), (1, 0), (1, 1)],
    'Blinker': [(0, 0), (0, 1), (0, 2)],
    'Glider': [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
    'Toad': [(1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2)],
    'Beacon': [(0, 0), (0, 1), (1, 0), (2, 3), (3, 2), (3, 3)],
    'Pulsar': [
        (2, 4), (2, 5), (2, 6), (2, 10), (2, 11), (2, 12),
        (4, 2), (4, 7), (4, 9), (4, 14),
        (5, 2), (5, 7), (5, 9), (5, 14),
        (6, 2), (6, 7), (6, 9), (6, 14),
        (7, 4), (7, 5), (7, 6), (7, 10), (7, 11), (7, 12),
        (9, 4), (9, 5), (9, 6), (9, 10), (9, 11), (9, 12),
        (10, 2), (10, 7), (10, 9), (10, 14),
        (11, 2), (11, 7), (11, 9), (11, 14),
        (12, 2), (12, 7), (12, 9), (12, 14),
        (14, 4), (14, 5), (14, 6), (14, 10), (14, 11), (14, 12)
    ],
    'LWSS': [
        (0, 1), (0, 4),
        (1, 0), (1, 4),
        (2, 4),
        (3, 0), (3, 3)
    ],
    'Pentadecathlon': [
        (1, 2), (1, 3), (2, 1), (2, 4), (3, 2), (3, 3),
        (4, 2), (4, 3), (5, 1), (5, 4), (6, 2), (6, 3)
    ],
    'Gosper Glider Gun': [
        (5, 1), (5, 2), (6, 1), (6, 2),
        (5, 11), (6, 11), (7, 11),
        (4, 12), (8, 12),
        (3, 13), (9, 13),
        (3, 14), (9, 14),
        (6, 15),
        (4, 16), (8, 16),
        (5, 17), (6, 17), (7, 17), (6, 18),
        (3, 21), (4, 21), (5, 21), (3, 22), (4, 22), (5, 22),
        (2, 23), (6, 23),
        (1, 25), (2, 25), (6, 25), (7, 25),
        (3, 35), (4, 35), (3, 36), (4, 36)
    ]
}


class GameOfLife(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Game of Life')
        self.setGeometry(100, 100, 800, 600)
        self.grid_height = 60
        self.grid_width = 80
        self.cell_size = 10
        self.scale = 1
        self.running = False
        self.timer_interval = 100
        self.current_template = None

        self.grid = Grid(self.grid_height, self.grid_width)
        self.canvas = Canvas(self)

        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.toggle_simulation)

        self.stop_button = QPushButton('Stop')
        self.stop_button.clicked.connect(self.stop_simulation)

        self.reset_button = QPushButton('Reset')
        self.reset_button.clicked.connect(self.reset_grid)

        self.speed_slider = QSlider(Qt.Orientation.Horizontal)
        self.speed_slider.setMinimum(1)
        self.speed_slider.setMaximum(200)
        self.speed_slider.setValue(self.timer_interval)
        self.speed_slider.valueChanged.connect(self.update_speed)

        self.speed_label = QLabel('Simulation Speed')

        # Создание выпадающего списка для выбора шаблона
        self.template_combo = QComboBox()
        self.template_combo.addItems(TEMPLATES.keys())
        self.template_combo.currentTextChanged.connect(self.select_template)
        self.template_combo.setStyleSheet("QComboBox::drop-down { border: 1px solid black; }"
                                          "QComboBox::down-arrow { image: url(arrow_down.png); }")

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.reset_button)
        layout.addWidget(self.speed_label)
        layout.addWidget(self.speed_slider)
        layout.addWidget(self.template_combo)  # Добавление выпадающего списка

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_simulation)

    def select_template(self, template_name):
        self.current_template = TEMPLATES.get(template_name, None)

    def toggle_simulation(self):
        self.running = not self.running
        if self.running:
            self.timer.start(self.timer_interval)
        else:
            self.timer.stop()

    def stop_simulation(self):
        self.running = False
        self.timer.stop()

    def reset_grid(self):
        self.grid = Grid(self.grid_height, self.grid_width)
        self.canvas.update()

    def update_simulation(self):
        if self.running:
            self.grid = update_grid(self.grid)
            self.canvas.update()

    def update_speed(self):
        speed = self.speed_slider.value()
        self.timer_interval = 200 - speed
        if self.running:
            self.timer.start(self.timer_interval)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GameOfLife()
    window.show()
    sys.exit(app.exec())
