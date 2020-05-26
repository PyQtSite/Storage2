
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,QPushButton,QLabel,QDateTimeEdit,QLineEdit,QCheckBox,QTableView,QComboBox,QFileDialog, QMessageBox)
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QIcon,QStandardItemModel,QStandardItem
from traceback import format_exc
from PyQt5.QtCore import pyqtSignal


class Ui_QTaskConfigWindow(QWidget):
    errorMsgSignal = pyqtSignal(str)
    taskConfigInfoSignal = pyqtSignal(int)
    #@profile(precision=4, stream=open('memory_profiler.log', 'w+'))
    def __init__(self):
        super(Ui_QTaskConfigWindow,self).__init__()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.initUI()

    #@profile(precision=4, stream=open('memory_profiler.log', 'w+'))
    def initUI(self):
        self.labelTaskNumber = QLabel(' ')
        self.labelTaskNumberValue =QLabel()
        self.labelTaskTime = QLabel(' ')
        self.lineeditTaskTime = QLineEdit(" ")
        self.labelAlgorithmPath = QLabel(' ')
        self.lineeditAlgorithmPath = QLineEdit(" ")
        self.pushbuttonAlgorithmPath = QPushButton()
        tempIcon = QIcon('iconbase/fileopen.png')
        self.pushbuttonAlgorithmPath.setIcon(tempIcon)
        self.pushbuttonAlgorithmPath.clicked.connect(self.pushbuttonAlgorithmPathOnActivated)
        self.comboboxAlgorithmType = QComboBox()

        self.labelDataPath = QLabel(' ')
        self.checkboxOnlineData = QCheckBox(' ')
        self.checkboxOfflineData = QCheckBox(' ')
        self.checkboxOfflineData.toggle()
        self.checkboxOfflineData.stateChanged.connect(self.checkboxOfflineDataOnStateChanged)  # 状态改变时触发信号
        self.checkboxOnlineData.stateChanged.connect(self.checkboxOnlineDataOnStateChanged)  # 状态改变时触发信号,先创建两个控件，再连接，否则因为未创建而报错

        self.lineeditOfflineDataPath = QLineEdit(" ")
        self.pushbuttonOfflineDataPath = QPushButton()
        self.pushbuttonOfflineDataPath.setIcon(tempIcon)
        self.pushbuttonOfflineDataPath.clicked.connect(self.pushbuttonOfflineDataPathOnActivated)

        self.labelSavePath = QLabel(' ')
        self.lineeditSavePath = QLineEdit("")
        self.pushbuttonSavePath = QPushButton()
        self.pushbuttonSavePath.setIcon(tempIcon)
        self.pushbuttonSavePath.clicked.connect(self.pushbuttonSavePathOnActivated)

        self.checkboxStartNow = QCheckBox(' ')
        self.checkboxStartNow.toggle()
        self.checkboxStartTiming = QCheckBox(' ')
        self.datatimeeditSetupTime = QDateTimeEdit()
        self.datatimeeditSetupTime.setDisplayFormat("HH:mm:ss")
        self.checkboxStartNow.stateChanged.connect(self.checkboxStartNowOnStateChanged)  # 状态改变时触发信号
        self.checkboxStartTiming.stateChanged.connect(self.checkboxStartTimingOnStateChanged)  # 状态改变时触发信号

        self.checkboxSaveOriginalData = QCheckBox(' ')
        #self.checkboxSaveOriginalData.toggle()
        self.checkboxSaveSamples = QCheckBox(' ')
        #self.checkboxSaveSamples.toggle()
        self.checkboxSaveIdentifyResult = QCheckBox(' ')
        #self.checkboxSaveIdentifyResult.toggle()

        # 设置干扰类型
        self.labelCategory = QLabel(' ')

        self.tableviewCategory = QTableView()
        self.tableviewCategory.horizontalHeader().setStretchLastSection(True)

        self.listCategory = ['1','2','3','4','5','6','7']
        category_num = len(self.listCategory)
        self.standarditemmodelCategoryTabel = QStandardItemModel(category_num, 2)
        self.standarditemmodelCategoryTabel.setHorizontalHeaderLabels([' a', 'b '])

        for row in range(category_num):
            item_checked = QStandardItem()
            item_checked.setCheckState(Qt.Checked)
            item_checked.setCheckable(True)
            self.standarditemmodelCategoryTabel.setItem(row, 0, item_checked)
            item = QStandardItem(self.listCategory[row])
            # 设置每个位置的文本值
            self.standarditemmodelCategoryTabel.setItem(row, 1, item)

        self.tableviewCategory.setModel(self.standarditemmodelCategoryTabel)

        self.pushbuttonOK = QPushButton('  确定  ')
        self.pushbuttonOK.clicked.connect(self.pushbuttonOKOnActivated)
        # self.cancel_pushButton = QPushButton('取消')
        # 页面布局
        hboxlayoutTaskNumer = QHBoxLayout()
        hboxlayoutTaskTime = QHBoxLayout()
        hboxlayoutCheck = QHBoxLayout()
        hboxlayoutDataPath = QHBoxLayout()
        hboxlayoutAlgorithmPath = QHBoxLayout()
        hboxlayoutSavePath = QHBoxLayout()
        hboxlayoutOK = QHBoxLayout()
        vboxlayoutMain = QVBoxLayout()

        hboxlayoutTaskNumer.addWidget(self.labelTaskNumber)
        hboxlayoutTaskNumer.addWidget(self.labelTaskNumberValue)
        hboxlayoutTaskNumer.addStretch()
        hboxlayoutTaskTime.addWidget(self.labelTaskTime)
        hboxlayoutTaskTime.addWidget(self.lineeditTaskTime)
        hboxlayoutTaskTime.addWidget(self.checkboxStartNow)
        hboxlayoutTaskTime.addWidget(self.checkboxStartTiming)
        #hboxlayoutTaskTime.addWidget(self.datatimeeditSetupTime)
        hboxlayoutCheck.addStretch(2)
        hboxlayoutCheck.addWidget(self.checkboxSaveOriginalData)
        hboxlayoutCheck.addWidget(self.checkboxSaveSamples)
        hboxlayoutCheck.addWidget(self.checkboxSaveIdentifyResult)
        hboxlayoutCheck.addStretch(1)
        hboxlayoutDataPath.addWidget(self.labelDataPath)
        hboxlayoutDataPath.addWidget(self.checkboxOnlineData)
        hboxlayoutDataPath.addWidget(self.checkboxOfflineData)
        hboxlayoutDataPath.addWidget(self.lineeditOfflineDataPath)
        hboxlayoutDataPath.addWidget(self.pushbuttonOfflineDataPath)

        # save_path_hBoxLayout.addStretch()
        hboxlayoutSavePath.addWidget(self.labelSavePath)
        hboxlayoutSavePath.addWidget(self.lineeditSavePath)
        hboxlayoutSavePath.addWidget(self.pushbuttonSavePath)
        hboxlayoutAlgorithmPath.addWidget(self.labelAlgorithmPath)
        hboxlayoutAlgorithmPath.addWidget(self.comboboxAlgorithmType)
        hboxlayoutAlgorithmPath.addWidget(self.lineeditAlgorithmPath)
        hboxlayoutAlgorithmPath.addWidget(self.pushbuttonAlgorithmPath)
        hboxlayoutOK.addStretch()
        hboxlayoutOK.addWidget(self.pushbuttonOK)
        hboxlayoutOK.addStretch()
        # save_path_hBoxLayout.addWidget(self.cancel_pushButton)
        vboxlayoutMain.addLayout(hboxlayoutTaskNumer)
        vboxlayoutMain.addLayout(hboxlayoutTaskTime)
        vboxlayoutMain.addLayout(hboxlayoutCheck)
        vboxlayoutMain.addWidget(self.labelCategory)
        vboxlayoutMain.addWidget(self.tableviewCategory)
        vboxlayoutMain.addLayout(hboxlayoutDataPath)
        vboxlayoutMain.addLayout(hboxlayoutAlgorithmPath)
        vboxlayoutMain.addLayout(hboxlayoutSavePath)
        vboxlayoutMain.addLayout(hboxlayoutOK)
        self.setLayout(vboxlayoutMain)
        self.setWindowTitle(' 窗口')
        # self.setStyleSheet(StyleSheet)
        self.show()


    def checkboxOfflineDataOnStateChanged(self):
        pass

    def checkboxOnlineDataOnStateChanged(self):
        pass

    def checkboxStartNowOnStateChanged(self):
        pass

    def checkboxStartTimingOnStateChanged(self):
        pass

    def pushbuttonAlgorithmPathOnActivated(self):
       pass

    def pushbuttonOfflineDataPathOnActivated(self):
      pass

    def pushbuttonSavePathOnActivated(self):
        pass

    def pushbuttonOKOnActivated(self):
       pass

    def sendTaskConfigInfo(self):
        pass
