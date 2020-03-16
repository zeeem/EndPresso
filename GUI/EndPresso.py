# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\zeeem\Desktop\EndPresso.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 603)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(40, 120, 331, 231))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 390, 331, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 450, 161, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.quality_horizontalSlider = QtWidgets.QSlider(Dialog)
        self.quality_horizontalSlider.setGeometry(QtCore.QRect(50, 480, 141, 21))
        self.quality_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.quality_horizontalSlider.setObjectName("quality_horizontalSlider")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 450, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(420, 380, 311, 161))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setObjectName("label_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(410, 120, 331, 231))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(150, 80, 111, 31))
        self.label_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_3.setLineWidth(1)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(520, 80, 111, 31))
        self.label_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_4.setLineWidth(1)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(280, 20, 211, 31))
        self.label_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_5.setLineWidth(1)
        self.label_5.setMidLineWidth(1)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "UPLOAD IMAGE TO COMPRESS"))
        self.pushButton_2.setText(_translate("Dialog", "COMPRESS NOW"))
        self.label.setText(_translate("Dialog", "Compression Quality"))
        self.label_2.setText(_translate("Dialog", "RESULT: "))
        self.label_3.setText(_translate("Dialog", "Source Image"))
        self.label_4.setText(_translate("Dialog", "Output Image"))
        self.label_5.setText(_translate("Dialog", "EndPresso - Intelligent Image Compressor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
