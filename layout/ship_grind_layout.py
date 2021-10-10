from math import sqrt

from PyQt5.QtWidgets import QWidget, QGridLayout

from settings import Settings


class ShipGrindLayout(QWidget):
    def __init__(self, ship_list):
        super().__init__()
        self.ship_list = ship_list
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        self.setLayout(grid)

        # TODO zmiana ixi na ixj
        positions = [(i, j)
                     for i in range(int(sqrt(Settings.number_of_ship)))
                     for j in range(int(sqrt(Settings.number_of_ship)))]

        for position, ship in zip(positions, self.ship_list):
            grid.addWidget(ship, *position)
