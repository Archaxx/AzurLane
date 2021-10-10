import os
import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from layout.settings_layout import SettingsLayout
from settings import Settings
from items.ship import Ship
from layout.ship_grind_layout import ShipGrindLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._set_title()
        self._settings_gui()
        # self._generate_ship_list()
        # self._add_ships()

    def _settings_gui(self):
        layout = SettingsLayout()
        self.setCentralWidget(layout)

    def _set_title(self):
        self.title = "Azur Lane Guess Who"
        self.setWindowTitle(self.title)

    def _generate_ship_list(self):
        files = os.listdir("images/PR_Ships")
        self.ship_list = random.sample(files, Settings.number_of_ship)

    def _add_ships(self):
        ship_list = [Ship(self, ship) for ship in self.ship_list]
        layout = ShipGrindLayout(ship_list)
        self.setCentralWidget(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

