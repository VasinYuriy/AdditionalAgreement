# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/loadSyllabusInfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loadSyllabusWindow(object):
    def setupUi(self, loadSyllabusWindow):
        loadSyllabusWindow.setObjectName("loadSyllabusWindow")
        loadSyllabusWindow.resize(720, 297)
        loadSyllabusWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(loadSyllabusWindow)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(loadSyllabusWindow)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.path_label = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_label.sizePolicy().hasHeightForWidth())
        self.path_label.setSizePolicy(sizePolicy)
        self.path_label.setMinimumSize(QtCore.QSize(350, 0))
        self.path_label.setMaximumSize(QtCore.QSize(16777215, 200000))
        self.path_label.setSizeIncrement(QtCore.QSize(0, 20))
        self.path_label.setFrameShape(QtWidgets.QFrame.Box)
        self.path_label.setText("")
        self.path_label.setAlignment(QtCore.Qt.AlignCenter)
        self.path_label.setWordWrap(True)
        self.path_label.setIndent(10)
        self.path_label.setObjectName("path_label")
        self.horizontalLayout.addWidget(self.path_label)
        spacerItem2 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(75, 25))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(loadSyllabusWindow)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.nextButton = QtWidgets.QPushButton(self.groupBox)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_2.addWidget(self.nextButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox)

        self.retranslateUi(loadSyllabusWindow)
        QtCore.QMetaObject.connectSlotsByName(loadSyllabusWindow)

    def retranslateUi(self, loadSyllabusWindow):
        _translate = QtCore.QCoreApplication.translate
        loadSyllabusWindow.setWindowTitle(_translate("loadSyllabusWindow", "Загрузка базы данных"))
        self.pushButton.setText(_translate("loadSyllabusWindow", "Обзор..."))
        self.nextButton.setText(_translate("loadSyllabusWindow", "Далее"))
