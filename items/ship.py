from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


class Ship(QLabel):
    def __init__(self, parent, name):
        super().__init__(parent)
        self.name = name
        self.pixmap = QPixmap(f"images/PR_Ships/{name}")
        self.setPixmap(self.pixmap)

    def mouseReleaseEvent(self, ev):
        print(f"click {id(self)} - {self.name}")
