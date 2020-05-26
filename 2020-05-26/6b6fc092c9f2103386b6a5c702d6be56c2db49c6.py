import sys
from functools import partial
from PyQt5.QtCore import (QFile, QFileInfo, QSettings, QSignalMapper,
        QTimer,Qt,QByteArray)
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog,
        QMainWindow, QMessageBox, QTextEdit,QMdiArea,QWidget)
from PyQt5.QtGui import QIcon,QKeySequence

from ui_Qtest import Ui_QTaskConfigWindow
#import qrc_resources
import objgraph
import psutil
import gc
from os import getpid
from traceback import print_exc
#from memory_profiler import profile
__version__ = "1.0.0"
from time import sleep

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        fileNewAction = self.createAction("&New", self.fileNew,
                QKeySequence.New, "filenew", "Create a text file")
        fileOpenAction = self.createAction("&Open...", self.fileOpen,
                QKeySequence.Open, "fileopen",
                "Open an existing text file")

        fileToolbar = self.addToolBar("File")
        fileToolbar.setObjectName("FileToolbar")
        self.addActions(fileToolbar, (fileNewAction, fileOpenAction))



    def createAction(self, text, slot=None, shortcut=None, icon=None,
                     tip=None, checkable=False, signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/{0}.png".format(icon)))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            action.triggered.connect(slot)
        if checkable:
            action.setCheckable(True)
        return action


    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    #@profile
    def fileNew(self):
        try:
            print(u'openSystemConfig内存使用：', round(psutil.Process(getpid()).memory_info().rss / 1024 / 1024, 4))
            #print(u'memory_info：', psutil.Process(getpid()).memory_info())
            #print(u'memory_info：', psutil.Process(getpid()).memory_full_info())
            objgraph.show_growth(shortnames=False)
            #templist = objgraph.by_type('QIcon')
            #print('objgraph.by_type:', templist)
            #if len(templist) >= 1:
             #  objgraph.show_backrefs(templist[-1], filename='obj.png')

            # textEdit = textedit.TextEdit()
            #self.systemConfigWindow = Ui_QSystemConfigWindow()
            #a = sys.getrefcount(self.systemConfigWindow)
            #self.mdi.addSubWindow(self.systemConfigWindow).show()
            #self.mdi.closeActiveSubWindow()

            #self.systemConfigWindow.systemConfigInfoSignal.connect(self.setSystemConfigInfo)
            #self.systemConfigWindow.pushbuttonOKOnActivated()
            self.taskConfigWindow = Ui_QTaskConfigWindow()
            self.mdi.addSubWindow(self.taskConfigWindow).show()
            #self.mdi.closeActiveSubWindow()
            #self.systemConfigWindow = None
            #self.taskConfigWindow = None
            #templist = None
            '''
            sleep(5)


            self.taskConfigWindow = Ui_QTaskConfigWindow()
            self.mdi.addSubWindow(self.taskConfigWindow).show()
            self.taskConfigWindow.systemConfigInfo = self.systemConfigInfo
            # textEdit.close()
            sleep(5)
            for win_temp in self.mdi.subWindowList():
                win_temp_widget = win_temp.widget()
                if (win_temp_widget is not None) and (isinstance(win_temp_widget, Ui_QTaskConfigWindow)):
                    self.mdi.setActiveSubWindow(win_temp)
                    self.mdi.closeActiveSubWindow()
                    
                elif (win_temp_widget is not None) and (isinstance(win_temp_widget, Ui_QSystemConfigWindow)):
                    self.mdi.setActiveSubWindow(win_temp)
                    #self.mdi.removeSubWindow(self.systemConfigWindow)
                    self.mdi.closeActiveSubWindow()
            #self.mdi.removeSubWindow(self.systemConfigWindow)
            #b = sys.getrefcount(self.systemConfigWindow)
            win_temp = None
            win_temp_widget = None
            self.systemConfigInfo = None
            self.systemConfigWindow = None
            self.taskConfigWindow = None
'''

        except Exception as e:
            print(print_exc())

    def fileOpen(self):
        #self.mdi.closeActiveSubWindow()

        #self.taskConfigWindow = Ui_QTaskConfigWindow()
        #self.mdi.addSubWindow(self.taskConfigWindow).show()
        #self.taskConfigWindow.systemConfigInfo = self.systemConfigInfo
        self.fileSave()

    def fileSave(self):
        for win_temp in self.mdi.subWindowList():
            win_temp_widget = win_temp.widget()
            if (win_temp_widget is not None) and (isinstance(win_temp_widget, Ui_QTaskConfigWindow)):
                self.mdi.setActiveSubWindow(win_temp)
                self.mdi.closeActiveSubWindow()

            elif (win_temp_widget is not None) and (isinstance(win_temp_widget, Ui_QSystemConfigWindow)):
                self.mdi.setActiveSubWindow(win_temp)
                # self.mdi.removeSubWindow(self.systemConfigWindow)
                self.mdi.closeActiveSubWindow()
        # self.mdi.removeSubWindow(self.systemConfigWindow)
        # b = sys.getrefcount(self.systemConfigWindow)
        #win_temp = None
        #win_temp_widget = None
        self.systemConfigInfo = None
        self.systemConfigWindow = None
        self.taskConfigWindow = None



if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon(":/icon.png"))
    #app.setOrganizationName("Qtrac Ltd.")
    #app.setOrganizationDomain("qtrac.eu")
    #app.setApplicationName("Text Editor")
    form = MainWindow()
    form.show()

    app.exec_()
