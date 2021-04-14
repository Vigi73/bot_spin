# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(294, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(10, 640, 75, 23))
        self.btnStart.setObjectName("btnStart")
        self.btnStop = QtWidgets.QPushButton(self.centralwidget)
        self.btnStop.setGeometry(QtCore.QRect(10, 670, 75, 23))
        self.btnStop.setObjectName("btnStop")
        self.txtLog = QtWidgets.QTextBrowser(self.centralwidget)
        self.txtLog.setGeometry(QtCore.QRect(2, 410, 290, 221))
        self.txtLog.setStyleSheet("background-color: rgb(0, 62, 0);\n"
"color: rgb(255, 255, 255);")
        self.txtLog.setObjectName("txtLog")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(3, 9, 288, 385))
        self.groupBox.setObjectName("groupBox")
        self.toPull = QtWidgets.QSpinBox(self.groupBox)
        self.toPull.setGeometry(QtCore.QRect(230, 20, 42, 22))
        self.toPull.setProperty("value", 0)
        self.toPull.setObjectName("toPull")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(130, 20, 91, 20))
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(20, 151, 101, 17))
        self.checkBox.setObjectName("checkBox")
        self.point1 = QtWidgets.QLineEdit(self.groupBox)
        self.point1.setGeometry(QtCore.QRect(110, 60, 161, 20))
        self.point1.setText("")
        self.point1.setAlignment(QtCore.Qt.AlignCenter)
        self.point1.setObjectName("point1")
        self.point2 = QtWidgets.QLineEdit(self.groupBox)
        self.point2.setGeometry(QtCore.QRect(110, 90, 161, 20))
        self.point2.setAlignment(QtCore.Qt.AlignCenter)
        self.point2.setObjectName("point2")
        self.point3 = QtWidgets.QLineEdit(self.groupBox)
        self.point3.setGeometry(QtCore.QRect(110, 120, 161, 20))
        self.point3.setAlignment(QtCore.Qt.AlignCenter)
        self.point3.setObjectName("point3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(19, 58, 91, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(19, 90, 91, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 120, 91, 20))
        self.label_5.setObjectName("label_5")
        self.random = QtWidgets.QCheckBox(self.groupBox)
        self.random.setGeometry(QtCore.QRect(150, 150, 131, 20))
        self.random.setObjectName("random")
        self.travel = QtWidgets.QCheckBox(self.groupBox)
        self.travel.setGeometry(QtCore.QRect(150, 170, 131, 17))
        self.travel.setObjectName("travel")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 185, 270, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.sale = QtWidgets.QCheckBox(self.groupBox_2)
        self.sale.setGeometry(QtCore.QRect(10, 20, 81, 17))
        self.sale.setObjectName("sale")
        self.saleCount = QtWidgets.QSpinBox(self.groupBox_2)
        self.saleCount.setGeometry(QtCore.QRect(220, 20, 42, 22))
        self.saleCount.setObjectName("saleCount")
        self.coordLocacion = QtWidgets.QLineEdit(self.groupBox_2)
        self.coordLocacion.setGeometry(QtCore.QRect(150, 50, 113, 20))
        self.coordLocacion.setAlignment(QtCore.Qt.AlignCenter)
        self.coordLocacion.setObjectName("coordLocacion")
        self.coordSpin = QtWidgets.QLineEdit(self.groupBox_2)
        self.coordSpin.setGeometry(QtCore.QRect(150, 80, 113, 20))
        self.coordSpin.setAlignment(QtCore.Qt.AlignCenter)
        self.coordSpin.setObjectName("coordSpin")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(30, 50, 121, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(30, 80, 121, 16))
        self.label_7.setObjectName("label_7")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(9, 297, 271, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.selestedFish = QtWidgets.QCheckBox(self.groupBox_3)
        self.selestedFish.setGeometry(QtCore.QRect(190, 10, 70, 17))
        self.selestedFish.setObjectName("selestedFish")
        self.FishName = QtWidgets.QComboBox(self.groupBox_3)
        self.FishName.setGeometry(QtCore.QRect(10, 40, 251, 22))
        self.FishName.setObjectName("FishName")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(4, 395, 160, 13))
        self.label_2.setObjectName("label_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(190, 630, 101, 23))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Бот - спининг 1.0.0"))
        self.btnStart.setText(_translate("MainWindow", "Старт"))
        self.btnStop.setText(_translate("MainWindow", "Стоп"))
        self.groupBox.setTitle(_translate("MainWindow", "Основные настройки"))
        self.label.setText(_translate("MainWindow", "Сколько тащим:"))
        self.checkBox.setText(_translate("MainWindow", "сброс не зачёт"))
        self.label_3.setText(_translate("MainWindow", "1. Точка заброса:"))
        self.label_4.setText(_translate("MainWindow", "2. Точка заброса:"))
        self.label_5.setText(_translate("MainWindow", "3. Точка заброса:"))
        self.random.setText(_translate("MainWindow", "Рандом при забросе"))
        self.travel.setText(_translate("MainWindow", "Продливать путевку"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Продажа рыбы"))
        self.sale.setText(_translate("MainWindow", "Продавать"))
        self.label_6.setText(_translate("MainWindow", "Координаты локации:"))
        self.label_7.setText(_translate("MainWindow", "Координаты спининга:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Подбор рыбы"))
        self.selestedFish.setText(_translate("MainWindow", "Включить"))
        self.label_2.setText(_translate("MainWindow", "Лог вылова:"))