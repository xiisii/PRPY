import sip
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QFileDialog
import matplotlib.pyplot as plt

class MatplotlibCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, dpi=100):
        fig = Figure(dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(fig)
        fig.tight_layout()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 668)
        MainWindow.setIconSize(QtCore.QSize(10, 10))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.centralwidget.setFont(font)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setStyleSheet("background-color: rgb(36, 52, 76);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("LCDMono2")
        font.setPointSize(30)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("FileName")
        self.label_2.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setMidLineWidth(1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setStyleSheet("color: rgb(255, 255, 127);")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setStyleSheet("color: rgb(255, 255, 127);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setStyleSheet("color: rgb(255, 255, 127);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_2.addWidget(self.comboBox_3)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setStyleSheet("color: rgb(255, 255, 127);")
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout_2.addWidget(self.comboBox_4)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setStyleSheet("color: rgb(255, 255, 127);")
        self.comboBox_5.setObjectName("comboBox_5")
        self.horizontalLayout_2.addWidget(self.comboBox_5)
        self.spacerItem = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(self.spacerItem)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"border: 2px solid #000000;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setStretch(0, 6)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"border: 2px solid #000000;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setStretch(0, 6)
        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"border: 2px solid #000000;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setStretch(0, 6)
        self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setStyleSheet("QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"border: 2px solid #000000;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.setStretch(0, 6)
        self.gridLayout.addWidget(self.frame_5, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 10)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.filename = ''
        self.df = []

        self.canv = MatplotlibCanvas(self)
        self.canv2 = MatplotlibCanvas(self)
        self.canv3 = MatplotlibCanvas(self)
        self.canv4 = MatplotlibCanvas(self)

        self.value = 'bmh'
        self.value1 = 'full'
        self.value2 = 'full'
        self.value3 = 'full'
        self.value4 = 'cnt'

        self.themes = ['bmh', 'classic', 'dark_background', 'fast',
                       'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-bright',
                       'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark',
                       'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook',
                       'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk',
                       'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn',
                       'Solarize_Light2', 'tableau-colorblind10']

        self.themes2 = ['full','cnt','casual','registered']
        self.themes3 = ['full','temp','atemp','hum','windspeed']
        self.themes4 = ['cnt', 'casual', 'registered']

        self.comboBox.addItems(self.themes)
        self.comboBox_2.addItems(self.themes2)
        self.comboBox_3.addItems(self.themes3)
        self.comboBox_4.addItems(self.themes2)
        self.comboBox_5.addItems(self.themes4)

        self.comboBox.currentIndexChanged['QString'].connect(self.Update)
        self.comboBox_2.currentIndexChanged['QString'].connect(self.Update1)
        self.comboBox_3.currentIndexChanged['QString'].connect(self.Update2)
        self.comboBox_4.currentIndexChanged['QString'].connect(self.Update3)
        self.comboBox_5.currentIndexChanged['QString'].connect(self.Update4)

        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.Visualize)
        self.pushButton_3.clicked.connect(self.Import)
        self.pushButton_4.clicked.connect(self.info)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Visualization"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" color:#4798a8;\">Visualize Data App</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "File Name"))
        self.label_6.setText(_translate("MainWindow", "Select Theme"))
        self.pushButton_3.setText(_translate("MainWindow", "Import "))
        self.pushButton_2.setText(_translate("MainWindow", "Visualize"))
        self.pushButton_4.setText(_translate("MainWindow", "Info"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))
        self.label_3.setText(_translate("MainWindow", "Line Plot"))
        self.label_4.setText(_translate("MainWindow", "Scatter plot"))
        self.label_7.setText(_translate("MainWindow", "Plot Histogram"))
        self.label_8.setText(_translate("MainWindow", "Horizontal Bar Graph"))

    def Visualize(self):
        try:
            self.verticalLayout_3.removeWidget(self.canv)
            sip.delete(self.canv)
            sip.delete(self.toolbar)
            self.toolbar = None
            self.canv = None

            self.verticalLayout_4.removeWidget(self.toolbar2)
            self.verticalLayout_4.removeWidget(self.canv2)
            sip.delete(self.canv2)
            sip.delete(self.toolbar2)
            self.toolbar2 = None
            self.canv2 = None

            self.verticalLayout_5.removeWidget(self.toolbar3)
            self.verticalLayout_5.removeWidget(self.canv3)
            sip.delete(self.canv3)
            sip.delete(self.toolbar3)
            self.toolbar3 = None
            self.canv3 = None

            self.verticalLayout_8.removeWidget(self.toolbar4)
            self.verticalLayout_8.removeWidget(self.canv4)
            sip.delete(self.canv4)
            self.canv4 = None

        except Exception as e:
            print(e)
            pass

        self.bd1(self.value1)
        self.bd2(self.value2)
        self.bd3(self.value3)
        self.bd4(self.value4)

    def bd1(self, value1):
        plt.clf()
        plt.style.use(self.value)

        self.canv = MatplotlibCanvas(self)
        self.verticalLayout_3.addWidget(self.canv)

        self.toolbar = Navi(self.canv, self.centralwidget)
        self.verticalLayout_3.addWidget(self.toolbar)
        self.toolbar.setStyleSheet("background-color: rgb(255, 255, 255);")

        ax = self.canv.axes
        self.df['dteday'] = pd.to_datetime(self.df['dteday'])
        if value1 == 'cnt':
            self.canv.axes.plot(self.df['dteday'], self.df['cnt'], label='cnt', color='tab:purple')
            ax.set_title('Date - Bikes Rented: CNT')
        if value1 == 'casual':
            self.canv.axes.plot(self.df['dteday'], self.df['casual'], label='casual', color='tab:red')
            ax.set_title('Date - Bikes Rented: CASUAL')
        if value1 == 'registered':
            self.canv.axes.plot(self.df['dteday'], self.df['registered'], label='registered', color='tab:blue')
            ax.set_title('Date - Bikes Rented: REGISTERED')
        if value1 == 'full':
            self.canv.axes.plot(self.df['dteday'], self.df['registered'], label='registered', color='tab:purple')
            self.canv.axes.plot(self.df['dteday'], self.df['casual'], label='casual', color='tab:red')
            self.canv.axes.plot(self.df['dteday'], self.df['cnt'], label='cnt', color='tab:blue')
            ax.set_title('Date - Bikes Rented: CNT vs. CASUAL vs. REGISTERED')

        legend = ax.legend()
        legend.set_draggable(True)

        ax.set_xlabel('Date')
        ax.set_ylabel('Bikes Rented')

    def bd2(self, value2):
        plt.clf()
        plt.style.use(self.value)

        self.canv3 = MatplotlibCanvas(self)
        self.verticalLayout_4.addWidget(self.canv3)

        self.toolbar3 = Navi(self.canv3, self.centralwidget)
        self.verticalLayout_4.addWidget(self.toolbar3)
        self.toolbar3.setStyleSheet("background-color: rgb(255, 255, 255);")

        ax = self.canv3.axes
        if value2 == 'temp':
            self.canv3.axes.scatter(self.df['temp'], self.df['cnt'], c=self.df['cnt'], cmap='Spectral',
                                    edgecolor='black', linewidth=1, alpha=0.75)
            ax.set_xlabel('Temperature')
            ax.set_title('Temperature vs. Bikes Rentals')
        if value2 == 'atemp':
            self.canv3.axes.scatter(self.df['atemp'], self.df['cnt'], c=self.df['cnt'], cmap='Spectral',
                                    edgecolor='black', linewidth=1, alpha=0.75)
            ax.set_xlabel('Atmospheric temperature')
            ax.set_title('Atmospheric temperature vs. Bikes Rentals')
        if value2 == 'windspeed':
            self.canv3.axes.scatter(self.df['windspeed'], self.df['cnt'], c=self.df['cnt'], cmap='Spectral',
                                    edgecolor='black', linewidth=1, alpha=0.75)
            ax.set_xlabel('Windspeed')
            ax.set_title('Windspeed vs. Bikes Rentals')
        if value2 == 'hum':
            self.canv3.axes.scatter(self.df['hum'], self.df['cnt'], c=self.df['cnt'], cmap='Spectral',
                                    edgecolor='black', linewidth=1, alpha=0.75)
            ax.set_xlabel('Humidity')
            ax.set_title('Humidity vs. Bikes Rentals')
        if value2 == 'full':
            self.canv3.axes.scatter(self.df['temp'], self.df['cnt'], color='tab:purple')
            self.canv3.axes.scatter(self.df['atemp'], self.df['cnt'], color='tab:red')
            self.canv3.axes.scatter(self.df['windspeed'], self.df['cnt'], color='tab:blue')
            self.canv3.axes.scatter(self.df['hum'], self.df['cnt'], color='tab:green')
            ax.set_title('Temperature vs. Atmospheric temperature vs. Windspeed vs. Humidity vs. Bikes Rentals')
            legend = ax.legend(['temp', 'atemp', 'windspeed', 'hum'])
            legend.set_draggable(True)

        ax.set_ylabel('Bikes Rented')

    def bd3(self, value3):
        plt.clf()
        plt.style.use(self.value)

        self.canv2 = MatplotlibCanvas(self)
        self.verticalLayout_6.addWidget(self.canv2)

        self.toolbar2 = Navi(self.canv2, self.centralwidget)
        self.verticalLayout_6.addWidget(self.toolbar2)
        self.toolbar2.setStyleSheet("background-color: rgb(255, 255, 255);")

        ax = self.canv2.axes
        if value3 == 'cnt':
            self.canv2.axes.hist(self.df['cnt'], label='cnt', color='tab:purple')
            ax.set_title('Frequency: CNT')
        if value3 == 'casual':
            self.canv2.axes.hist(self.df['casual'], label='casual', color='tab:red')
            ax.set_title('Frequency: CASUAL')
        if value3 == 'registered':
            self.canv2.axes.hist(self.df['registered'], label='registered', color='tab:blue')
            ax.set_title('Frequency: REGISTERED')
        if value3 == 'full':
            self.canv2.axes.hist(self.df['registered'], label='registered', bins=35, edgecolor='w', alpha=.8)
            self.canv2.axes.hist(self.df['casual'], label='casual', bins=35, edgecolor='w', alpha=.8)
            self.canv2.axes.hist(self.df['cnt'], label='cnt', bins=35, edgecolor='w', alpha=.8)
            ax.set_title('Frequency: CNT vs. CASUAL vs. REGISTERED')

        legend = ax.legend()
        legend.set_draggable(True)

        ax.set_ylabel('Frequency')
        ax.set_xlabel('Bikes Rented')

    def bd4(self, value4):
        plt.clf()
        plt.style.use(self.value)

        self.canv4 = MatplotlibCanvas(self)
        self.verticalLayout_8.addWidget(self.canv4)

        self.toolbar4 = Navi(self.canv4, self.centralwidget)
        self.verticalLayout_8.addWidget(self.toolbar4)
        self.toolbar4.setStyleSheet("background-color: rgb(255, 255, 255);")

        ax = self.canv4.axes
        if value4 == 'cnt':
            self.canv4.axes.barh(self.abc['weekday'], self.abc['cnt'], label='cnt', color='tab:purple')
            ax.set_title('WeekDay - Bikes Rented: CNT')
        if value4 == 'casual':
            self.canv4.axes.barh(self.abc['weekday'], self.abc['casual'], label='casual', color='tab:red')
            ax.set_title('WeekDay - Bikes Rented: CASUAL')
        if value4 == 'registered':
            self.canv4.axes.barh(self.abc['weekday'], self.abc['registered'], label='registered', color='tab:blue')
            ax.set_title('WeekDay - Bikes Rented: REGISTERED')

        day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        y_pos = np.arange(len(day))
        ax.set_yticks(y_pos, labels=day)
        ax.invert_yaxis()

        ax.set_ylabel('The day names')
        ax.set_xlabel('Bikes Rented')
        legend = ax.legend()
        legend.set_draggable(True)

    def Import(self):
        self.filename = QFileDialog.getOpenFileName(filter="csv (*.csv)")[0]
        import os
        base_name = os.path.basename(self.filename)
        self.Title = os.path.splitext(base_name)[0]
        self.label_2.setText(self.Title)
        self.df = pd.read_csv(self.filename).fillna(0)

        self.abc = self.df['weekday'].value_counts().rename_axis('weekday').reset_index(name='counts')

        t7 = self.df['weekday'] == 6
        t6 = self.df['weekday'] == 5
        t5 = self.df['weekday'] == 4
        t4 = self.df['weekday'] == 3
        t3 = self.df['weekday'] == 2
        t2 = self.df['weekday'] == 1
        cn = self.df['weekday'] == 0

        self.abc['tong_cnt'] = pd.Series(
            [self.df[t7]['cnt'].sum(), self.df[t6]['cnt'].sum(), self.df[t5]['cnt'].sum(),
             self.df[t4]['cnt'].sum(), self.df[t3]['cnt'].sum(), self.df[t2]['cnt'].sum(),
             self.df[cn]['cnt'].sum()]
            , index=[0, 1, 2, 3, 4, 5, 6])

        self.abc['tong_casual'] = pd.Series(
            [self.df[t7]['casual'].sum(), self.df[t6]['casual'].sum(), self.df[t5]['casual'].sum(),
             self.df[t4]['casual'].sum(), self.df[t3]['casual'].sum(), self.df[t2]['casual'].sum(),
             self.df[cn]['casual'].sum()]
            , index=[0, 1, 2, 3, 4, 5, 6])

        self.abc['tong_registered'] = pd.Series(
            [self.df[t7]['registered'].sum(), self.df[t6]['registered'].sum(), self.df[t5]['registered'].sum(),
             self.df[t4]['registered'].sum(), self.df[t3]['registered'].sum(), self.df[t2]['registered'].sum(),
             self.df[cn]['registered'].sum()]
            , index=[0, 1, 2, 3, 4, 5, 6])

        self.abc['cnt'] = np.where(self.abc['counts'] != 0, self.abc['tong_cnt'] / self.abc['counts'], 0)
        self.abc['casual'] = np.where(self.abc['counts'] != 0, self.abc['tong_casual'] / self.abc['counts'], 0)
        self.abc['registered'] = np.where(self.abc['counts'] != 0, self.abc['tong_registered'] / self.abc['counts'], 0)

    def info(self):
        import info
        inf0 = info.cl_Form_10()
        inf0.show()

    def Update(self, value):
        self.value = value
        self.Visualize()

    def Update1(self,value):
        self.value1 = value
        self.Visualize()

    def Update2(self,value):
        self.value2 = value
        self.Visualize()

    def Update3(self,value):
        self.value3 = value
        self.Visualize()

    def Update4(self,value):
        self.value4 = value
        self.Visualize()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
