from PyQt5.QtWidgets import QPushButton

from settings import Settings


class AddToPollButton(QPushButton):
    def __init__(self, name, group_name):
        super().__init__(name)
        self.group_name = group_name

    def mouseReleaseEvent(self, ev):
        if self.group_name not in Settings.poll:
            Settings.poll.add(self.group_name)
        else:
            Settings.poll.remove(self.group_name)
        print(Settings.poll)
