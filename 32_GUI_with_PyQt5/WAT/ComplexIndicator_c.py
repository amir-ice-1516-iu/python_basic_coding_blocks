# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ComplexIndicator.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1024, 280))
        Form.setMaximumSize(QtCore.QSize(1024, 280))
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 4, 1083, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.reactiionTimeCategoryLabel = QtWidgets.QLabel(self.layoutWidget)
        self.reactiionTimeCategoryLabel.setObjectName("reactiionTimeCategoryLabel")
        self.verticalLayout.addWidget(self.reactiionTimeCategoryLabel)
        self.category1Type1 = QtWidgets.QCheckBox(self.layoutWidget)
        self.category1Type1.setObjectName("category1Type1")
        self.verticalLayout.addWidget(self.category1Type1)
        self.category1Type2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.category1Type2.setObjectName("category1Type2")
        self.verticalLayout.addWidget(self.category1Type2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.meaningCategoryLabel = QtWidgets.QLabel(self.layoutWidget)
        self.meaningCategoryLabel.setObjectName("meaningCategoryLabel")
        self.verticalLayout_2.addWidget(self.meaningCategoryLabel)
        self.category2Type1 = QtWidgets.QCheckBox(self.layoutWidget)
        self.category2Type1.setObjectName("category2Type1")
        self.verticalLayout_2.addWidget(self.category2Type1)
        self.category2Type2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.category2Type2.setObjectName("category2Type2")
        self.verticalLayout_2.addWidget(self.category2Type2)
        self.category2Type3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.category2Type3.setObjectName("category2Type3")
        self.verticalLayout_2.addWidget(self.category2Type3)
        self.category2Type4 = QtWidgets.QCheckBox(self.layoutWidget)
        self.category2Type4.setObjectName("category2Type4")
        self.verticalLayout_2.addWidget(self.category2Type4)
        self.category2Type5 = QtWidgets.QCheckBox(self.layoutWidget)
        self.category2Type5.setObjectName("category2Type5")
        self.verticalLayout_2.addWidget(self.category2Type5)
        self.category2Type6 = QtWidgets.QCheckBox(self.layoutWidget)
        self.category2Type6.setObjectName("category2Type6")
        self.verticalLayout_2.addWidget(self.category2Type6)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.physicalReactionsCategoryLabel = QtWidgets.QLabel(self.layoutWidget)
        self.physicalReactionsCategoryLabel.setObjectName("physicalReactionsCategoryLabel")
        self.verticalLayout_3.addWidget(self.physicalReactionsCategoryLabel)
        self.category3Type1 = QtWidgets.QCheckBox(self.layoutWidget)
        self.category3Type1.setObjectName("category3Type1")
        self.verticalLayout_3.addWidget(self.category3Type1)
        self.category3Type2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.category3Type2.setObjectName("category3Type2")
        self.verticalLayout_3.addWidget(self.category3Type2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.speechCategoryLabel = QtWidgets.QLabel(self.layoutWidget)
        self.speechCategoryLabel.setObjectName("speechCategoryLabel")
        self.verticalLayout_4.addWidget(self.speechCategoryLabel)
        self.category4Type1 = QtWidgets.QCheckBox(self.layoutWidget)
        self.category4Type1.setObjectName("category4Type1")
        self.verticalLayout_4.addWidget(self.category4Type1)
        self.category4Type2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.category4Type2.setObjectName("category4Type2")
        self.verticalLayout_4.addWidget(self.category4Type2)
        self.category4Type3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.category4Type3.setObjectName("category4Type3")
        self.verticalLayout_4.addWidget(self.category4Type3)
        self.category4Type4 = QtWidgets.QCheckBox(self.layoutWidget)
        self.category4Type4.setObjectName("category4Type4")
        self.verticalLayout_4.addWidget(self.category4Type4)
        self.category4Type5 = QtWidgets.QCheckBox(self.layoutWidget)
        self.category4Type5.setObjectName("category4Type5")
        self.verticalLayout_4.addWidget(self.category4Type5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.patternsCategoryLabel = QtWidgets.QLabel(self.layoutWidget)
        self.patternsCategoryLabel.setObjectName("patternsCategoryLabel")
        self.verticalLayout_5.addWidget(self.patternsCategoryLabel)
        self.category5Type1 = QtWidgets.QCheckBox(self.layoutWidget)
        self.category5Type1.setObjectName("category5Type1")
        self.verticalLayout_5.addWidget(self.category5Type1)
        self.category5Type2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.category5Type2.setObjectName("category5Type2")
        self.verticalLayout_5.addWidget(self.category5Type2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.updateExistingComplexIndicator = QtWidgets.QPushButton(self.layoutWidget)
        self.updateExistingComplexIndicator.setObjectName("updateExistingComplexIndicator")
        self.horizontalLayout_2.addWidget(self.updateExistingComplexIndicator)
        self.complexIndicatorToUpdate = QtWidgets.QLineEdit(self.layoutWidget)
        self.complexIndicatorToUpdate.setText("")
        self.complexIndicatorToUpdate.setObjectName("complexIndicatorToUpdate")
        self.horizontalLayout_2.addWidget(self.complexIndicatorToUpdate)
        self.selectedTypeLabel = QtWidgets.QLabel(self.layoutWidget)
        self.selectedTypeLabel.setObjectName("selectedTypeLabel")
        self.horizontalLayout_2.addWidget(self.selectedTypeLabel)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.addNewComplexIndicator = QtWidgets.QPushButton(self.layoutWidget)
        self.addNewComplexIndicator.setObjectName("addNewComplexIndicator")
        self.horizontalLayout.addWidget(self.addNewComplexIndicator)
        self.newComplexIndicatorToAdd = QtWidgets.QLineEdit(self.layoutWidget)
        self.newComplexIndicatorToAdd.setText("")
        self.newComplexIndicatorToAdd.setObjectName("newComplexIndicatorToAdd")
        self.horizontalLayout.addWidget(self.newComplexIndicatorToAdd)
        self.selectedComplexIndicatorCategory = QtWidgets.QComboBox(self.layoutWidget)
        self.selectedComplexIndicatorCategory.setObjectName("selectedComplexIndicatorCategory")
        self.selectedComplexIndicatorCategory.addItem("")
        self.selectedComplexIndicatorCategory.addItem("")
        self.selectedComplexIndicatorCategory.addItem("")
        self.selectedComplexIndicatorCategory.addItem("")
        self.selectedComplexIndicatorCategory.addItem("")
        self.selectedComplexIndicatorCategory.addItem("")
        self.horizontalLayout.addWidget(self.selectedComplexIndicatorCategory)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Complex Indicator"))
        self.reactiionTimeCategoryLabel.setText(_translate("Form", "Reaction Time"))
        self.category1Type1.setText(_translate("Form", "Prolonged reaction times"))
        self.category1Type2.setText(_translate("Form", "Failures"))
        self.meaningCategoryLabel.setText(_translate("Form", "Meaning"))
        self.category2Type1.setText(_translate("Form", "Meaningless reactions"))
        self.category2Type2.setText(_translate("Form", "Mishearing or not understandable"))
        self.category2Type3.setText(_translate("Form", "Repetition of sw"))
        self.category2Type4.setText(_translate("Form", "Mediate Reactions"))
        self.category2Type5.setText(_translate("Form", "Rhymes of word completing"))
        self.category2Type6.setText(_translate("Form", "False reproduction"))
        self.physicalReactionsCategoryLabel.setText(_translate("Form", "Physical Reactions"))
        self.category3Type1.setText(_translate("Form", "Gestures, Bodily Movements"))
        self.category3Type2.setText(_translate("Form", "Physical  excitation"))
        self.speechCategoryLabel.setText(_translate("Form", "Speech"))
        self.category4Type1.setText(_translate("Form", "Foreign Language Reactions"))
        self.category4Type2.setText(_translate("Form", "Multiple Word Response"))
        self.category4Type3.setText(_translate("Form", "Slips of the tongue"))
        self.category4Type4.setText(_translate("Form", "Stuttering, Misprodunciations"))
        self.category4Type5.setText(_translate("Form", "Sounds, Interjections"))
        self.patternsCategoryLabel.setText(_translate("Form", "Patterns"))
        self.category5Type1.setText(_translate("Form", "Perseveration"))
        self.category5Type2.setText(_translate("Form", "Stereotypes"))
        self.updateExistingComplexIndicator.setText(_translate("Form", "Update"))
        self.selectedTypeLabel.setText(_translate("Form", "Dummy Type.................."))
        self.addNewComplexIndicator.setText(_translate("Form", "Add New"))
        self.selectedComplexIndicatorCategory.setItemText(0, _translate("Form", "None"))
        self.selectedComplexIndicatorCategory.setItemText(1, _translate("Form", "Reaction Time"))
        self.selectedComplexIndicatorCategory.setItemText(2, _translate("Form", "Meaning"))
        self.selectedComplexIndicatorCategory.setItemText(3, _translate("Form", "Physical Reactions"))
        self.selectedComplexIndicatorCategory.setItemText(4, _translate("Form", "Speech"))
        self.selectedComplexIndicatorCategory.setItemText(5, _translate("Form", "Pattern"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())