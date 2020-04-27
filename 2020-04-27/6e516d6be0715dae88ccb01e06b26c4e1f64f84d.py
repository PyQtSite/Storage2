import sys
from PyQt5.QtWidgets import *
from UI_demo.Q111_demo import Mywindow1

class button(QPushButton):
    def __init__(self,*args,**kwargs):
        super(button,self).__init__(*args,**kwargs)

    def hideEvent(self,event):
        super(button,self).hideEvent(event)
        print("112121212121",self.sender())

    def showEvent(self,event):
        super(button,self).showEvent(event)
        print("11221",self.sender())



class Mywindow(QWidget):
    def __init__(self):
        super(Mywindow,self).__init__()
        self.button1=button(self)
        self.button1.setText("隐藏")
        self.button1.setGeometry(50,50,50,50)

        self.button2=button(self)
        self.button2.setText("显示")
        self.button2.setGeometry(150,50,50,50)

        self.button1.clicked.connect(self.hidepushbutton)
        self.button2.clicked.connect(self.showpushbutton)

        self.a=Mywindow1()
        self.button2.clicked.connect(self.a.show)


    def hidepushbutton(self):
        print(self.sender())
        self.button1.hide()

    def showpushbutton(self):
        print(self.sender())
        self.button1.show()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = Mywindow()
    # myWin.show()
    myWin.showFullScreen()
    sys.exit(app.exec_())

