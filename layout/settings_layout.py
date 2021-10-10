from collections import namedtuple
from math import sqrt

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton

from buttons.button_factory import ButtonFactory
from settings import Settings

GuiElement = namedtuple("GuiElement", ["name", "button_type", "params", "checkable"])
GUI = [GuiElement("a", "AddToPollButton", "a", True),
       GuiElement("b", "AddToPollButton", "b", False),
       GuiElement("c", "AddToPollButton", "c", False)]


class SettingsLayout(QWidget):
    def __init__(self):
        super().__init__()
        self._button_factory = ButtonFactory()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        self.setLayout(grid)

        positions = [(i, 1) for i in range(len(GUI))]

        for position, gui_element in zip(positions, GUI):
            if gui_element == '':
                continue
            button = self._button_factory.create_button(gui_element.button_type, gui_element.name, gui_element.params)
            button.setCheckable(gui_element.checkable)
            grid.addWidget(button, *position)

    def _generate_seed(self):
        return self.poll
