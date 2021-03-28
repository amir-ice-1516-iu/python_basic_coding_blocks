# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Files/Interview.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 450)
        self.complexIndicatorsSelection = QtWidgets.QWidget(Form)
        self.complexIndicatorsSelection.setGeometry(QtCore.QRect(0, 126, 1024, 280))
        self.complexIndicatorsSelection.setObjectName("complexIndicatorsSelection")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1021, 131))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.interviewDetailsLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.interviewDetailsLabel.setFont(font)
        self.interviewDetailsLabel.setObjectName("interviewDetailsLabel")
        self.verticalLayout_2.addWidget(self.interviewDetailsLabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.wordSerialNumberLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.wordSerialNumberLabel.setFont(font)
        self.wordSerialNumberLabel.setObjectName("wordSerialNumberLabel")
        self.horizontalLayout_3.addWidget(self.wordSerialNumberLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.testWordLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.testWordLabel.setFont(font)
        self.testWordLabel.setObjectName("testWordLabel")
        self.horizontalLayout_3.addWidget(self.testWordLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.testRoundLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.testRoundLabel.setFont(font)
        self.testRoundLabel.setObjectName("testRoundLabel")
        self.horizontalLayout_3.addWidget(self.testRoundLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.interviewOperationalButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.interviewOperationalButton.setFont(font)
        self.interviewOperationalButton.setObjectName("interviewOperationalButton")
        self.horizontalLayout_2.addWidget(self.interviewOperationalButton)
        self.timerLabel = QtWidgets.QLCDNumber(self.widget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.timerLabel.setFont(font)
        self.timerLabel.setSmallDecimalPoint(False)
        self.timerLabel.setProperty("value", 0.2)
        self.timerLabel.setObjectName("timerLabel")
        self.horizontalLayout_2.addWidget(self.timerLabel)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeTakenLabel = QtWidgets.QLabel(self.widget)
        self.timeTakenLabel.setObjectName("timeTakenLabel")
        self.verticalLayout.addWidget(self.timeTakenLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.responseWrodLabel = QtWidgets.QLabel(self.widget)
        self.responseWrodLabel.setObjectName("responseWrodLabel")
        self.horizontalLayout.addWidget(self.responseWrodLabel)
        self.lastResponseWord = QtWidgets.QLineEdit(self.widget)
        self.lastResponseWord.setObjectName("lastResponseWord")
        self.horizontalLayout.addWidget(self.lastResponseWord)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(0, 416, 1021, 41))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.closeWidgetButton = QtWidgets.QPushButton(self.widget1)
        self.closeWidgetButton.setObjectName("closeWidgetButton")
        self.horizontalLayout_5.addWidget(self.closeWidgetButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.infoLabel = QtWidgets.QLabel(self.widget1)
        self.infoLabel.setObjectName("infoLabel")
        self.horizontalLayout_5.addWidget(self.infoLabel)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Interview"))
        self.interviewDetailsLabel.setText(_translate("Form", "Dummy Interview Details"))
        self.wordSerialNumberLabel.setText(_translate("Form", "Word SL"))
        self.testWordLabel.setText(_translate("Form", "Dummy Word"))
        self.testRoundLabel.setText(_translate("Form", "Round"))
        self.interviewOperationalButton.setText(_translate("Form", "Timer/Next"))
        self.timeTakenLabel.setText(_translate("Form", "Time Taken :"))
        self.responseWrodLabel.setText(_translate("Form", "Response Word:"))
        self.closeWidgetButton.setText(_translate("Form", "Close"))
        self.closeWidgetButton.setShortcut(_translate("Form", "Esc"))
        self.infoLabel.setText(_translate("Form", "*Press Esc to close any time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())