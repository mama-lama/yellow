import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from random import randrange


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.do_paint = False
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        self.x = randrange(300, 500)
        self.y = randrange(0, 400)
        qp.setBrush(QColor(255, 255, 0))
        r1 = randrange(30, 100)
        qp.drawEllipse(self.x - randrange(100, 300), randrange(0, 400), r1, r1)
        qp.drawEllipse(self.x, self.y, r1, r1)
        qp.drawEllipse(self.x + 100, randrange(0, 300), r1, r1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())