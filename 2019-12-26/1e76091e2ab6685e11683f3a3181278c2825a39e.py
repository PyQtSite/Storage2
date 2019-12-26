from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class AnimatedTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
    def addAnimation(self, url, filename):
        self.url = url
        self.filename = filename
        self.insertHtml("<img src='"+self.url+"'/>")
        self.movie = QMovie(self)
        self.movie.setFileName(filename)
        self.movie.setCacheMode(QMovie.CacheNone)
        self.movie.frameChanged.connect(self.subAnimate)
        self.movie.start()
    def subAnimate(self,a):
        self.document().addResource(QTextDocument.ImageResource,QUrl(self.url),self.movie.currentPixmap())
        self.setLineWrapColumnOrWidth(0)  # 加上换行才可以，不加不刷新 与self.movie.setCacheMode(QMovie.CacheNone)缺一不可

class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.addBtn = QPushButton('增加一gif')
        self.m_editAnimated = AnimatedTextEdit()
        self.setMinimumHeight(400)
        self.setWindowTitle('gif动画')
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.addBtn)
        vlayout.addWidget(self.m_editAnimated)
        self.setLayout(vlayout)
        self.addBtn.clicked.connect(self.slot_add_clicked)
    def slot_add_clicked(self):
        self.m_editAnimated.addAnimation(url='yyy', filename='1.gif')  # 此处yyy是随便定义的，及时刷入yyy图片，实现gif效果


if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()