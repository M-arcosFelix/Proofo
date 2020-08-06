# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FindingDetailWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FindingDetailWindow(object):
    def setupUi(self, FindingDetailWindow):
        FindingDetailWindow.setObjectName("FindingDetailWindow")
        FindingDetailWindow.resize(304, 514)
        self.gridLayout = QtWidgets.QGridLayout(FindingDetailWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.FindingWindowNameLBL = QtWidgets.QLabel(FindingDetailWindow)
        self.FindingWindowNameLBL.setMaximumSize(QtCore.QSize(16777215, 25))
        self.FindingWindowNameLBL.setObjectName("FindingWindowNameLBL")
        self.verticalLayout.addWidget(self.FindingWindowNameLBL)
        self.FindingWindowNameTextEdit = QtWidgets.QTextEdit(FindingDetailWindow)
        self.FindingWindowNameTextEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.FindingWindowNameTextEdit.setReadOnly(True)
        self.FindingWindowNameTextEdit.setObjectName("FindingWindowNameTextEdit")
        self.verticalLayout.addWidget(self.FindingWindowNameTextEdit)
        self.FindingWindowCriticalityLBL = QtWidgets.QLabel(FindingDetailWindow)
        self.FindingWindowCriticalityLBL.setMaximumSize(QtCore.QSize(16777215, 25))
        self.FindingWindowCriticalityLBL.setObjectName("FindingWindowCriticalityLBL")
        self.verticalLayout.addWidget(self.FindingWindowCriticalityLBL)
        self.FindingWindowCriticalityTextEdit = QtWidgets.QTextEdit(FindingDetailWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FindingWindowCriticalityTextEdit.sizePolicy().hasHeightForWidth())
        self.FindingWindowCriticalityTextEdit.setSizePolicy(sizePolicy)
        self.FindingWindowCriticalityTextEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.FindingWindowCriticalityTextEdit.setReadOnly(True)
        self.FindingWindowCriticalityTextEdit.setObjectName("FindingWindowCriticalityTextEdit")
        self.verticalLayout.addWidget(self.FindingWindowCriticalityTextEdit)
        self.FindingWindowTypeLBL = QtWidgets.QLabel(FindingDetailWindow)
        self.FindingWindowTypeLBL.setObjectName("FindingWindowTypeLBL")
        self.verticalLayout.addWidget(self.FindingWindowTypeLBL)
        self.FindingWindowTypeTextEdit = QtWidgets.QTextEdit(FindingDetailWindow)
        self.FindingWindowTypeTextEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.FindingWindowTypeTextEdit.setReadOnly(True)
        self.FindingWindowTypeTextEdit.setObjectName("FindingWindowTypeTextEdit")
        self.verticalLayout.addWidget(self.FindingWindowTypeTextEdit)
        self.FindingWindowDescriptionLBL = QtWidgets.QLabel(FindingDetailWindow)
        self.FindingWindowDescriptionLBL.setMaximumSize(QtCore.QSize(16777215, 25))
        self.FindingWindowDescriptionLBL.setObjectName("FindingWindowDescriptionLBL")
        self.verticalLayout.addWidget(self.FindingWindowDescriptionLBL)
        self.FindingWindowDescriptionTextEdit = QtWidgets.QTextEdit(FindingDetailWindow)
        self.FindingWindowDescriptionTextEdit.setMaximumSize(QtCore.QSize(16777215, 150))
        self.FindingWindowDescriptionTextEdit.setReadOnly(True)
        self.FindingWindowDescriptionTextEdit.setObjectName("FindingWindowDescriptionTextEdit")
        self.verticalLayout.addWidget(self.FindingWindowDescriptionTextEdit)
        self.FindingWindowRemediationLBL = QtWidgets.QLabel(FindingDetailWindow)
        self.FindingWindowRemediationLBL.setMaximumSize(QtCore.QSize(16777215, 25))
        self.FindingWindowRemediationLBL.setObjectName("FindingWindowRemediationLBL")
        self.verticalLayout.addWidget(self.FindingWindowRemediationLBL)
        self.FindingWindowRemediationTextEdit = QtWidgets.QTextEdit(FindingDetailWindow)
        self.FindingWindowRemediationTextEdit.setMaximumSize(QtCore.QSize(16777215, 150))
        self.FindingWindowRemediationTextEdit.setReadOnly(True)
        self.FindingWindowRemediationTextEdit.setObjectName("FindingWindowRemediationTextEdit")
        self.verticalLayout.addWidget(self.FindingWindowRemediationTextEdit)
        spacerItem = QtWidgets.QSpacerItem(128, 66, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(FindingDetailWindow)
        QtCore.QMetaObject.connectSlotsByName(FindingDetailWindow)

    def retranslateUi(self, FindingDetailWindow):
        _translate = QtCore.QCoreApplication.translate
        FindingDetailWindow.setWindowTitle(_translate("FindingDetailWindow", "Finding Details"))
        self.FindingWindowNameLBL.setText(_translate("FindingDetailWindow", "Finding Name:"))
        self.FindingWindowCriticalityLBL.setText(_translate("FindingDetailWindow", "Finding Criticality:"))
        self.FindingWindowTypeLBL.setText(_translate("FindingDetailWindow", "Finding Type:"))
        self.FindingWindowDescriptionLBL.setText(_translate("FindingDetailWindow", "Finding Description:"))
        self.FindingWindowRemediationLBL.setText(_translate("FindingDetailWindow", "Finding Remediation:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FindingDetailWindow = QtWidgets.QDialog()
    ui = Ui_FindingDetailWindow()
    ui.setupUi(FindingDetailWindow)
    FindingDetailWindow.show()
    sys.exit(app.exec_())
