# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/main_app_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.user_name_line = QtWidgets.QLineEdit(self.groupBox)
        self.user_name_line.setObjectName("user_name_line")
        self.gridLayout_2.addWidget(self.user_name_line, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.password_line = QtWidgets.QLineEdit(self.groupBox)
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setObjectName("password_line")
        self.gridLayout_2.addWidget(self.password_line, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.login_btn = QtWidgets.QPushButton(self.groupBox)
        self.login_btn.setMinimumSize(QtCore.QSize(130, 40))
        self.login_btn.setMaximumSize(QtCore.QSize(130, 40))
        self.login_btn.setStyleSheet("border:3px solid #52BFA1;\n"
"font: 14pt \"Times New Roman\";\n"
"border-radius:20px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_btn.setIcon(icon1)
        self.login_btn.setIconSize(QtCore.QSize(40, 40))
        self.login_btn.setObjectName("login_btn")
        self.verticalLayout.addWidget(self.login_btn)
        self.signup_btn = QtWidgets.QPushButton(self.groupBox)
        self.signup_btn.setMinimumSize(QtCore.QSize(130, 40))
        self.signup_btn.setMaximumSize(QtCore.QSize(130, 40))
        self.signup_btn.setStyleSheet("border:3px solid #C0E5E4;\n"
"font: 14pt \"Times New Roman\";\n"
"border-radius:20px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/sign_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.signup_btn.setIcon(icon2)
        self.signup_btn.setIconSize(QtCore.QSize(40, 40))
        self.signup_btn.setObjectName("signup_btn")
        self.verticalLayout.addWidget(self.signup_btn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.horizontalLayout_2.addWidget(self.groupBox)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.reg_user_name_line = QtWidgets.QLineEdit(self.groupBox_2)
        self.reg_user_name_line.setObjectName("reg_user_name_line")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.reg_user_name_line)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.reg_password_line = QtWidgets.QLineEdit(self.groupBox_2)
        self.reg_password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.reg_password_line.setObjectName("reg_password_line")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.reg_password_line)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.reg_repassword_line = QtWidgets.QLineEdit(self.groupBox_2)
        self.reg_repassword_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.reg_repassword_line.setObjectName("reg_repassword_line")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.reg_repassword_line)
        self.gridLayout_4.addLayout(self.formLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.register_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.register_btn.setMinimumSize(QtCore.QSize(130, 40))
        self.register_btn.setMaximumSize(QtCore.QSize(130, 40))
        self.register_btn.setStyleSheet("border:3px solid #C0E5E4;\n"
"font: 14pt \"Times New Roman\";\n"
"border-radius:20px;")
        self.register_btn.setIcon(icon2)
        self.register_btn.setIconSize(QtCore.QSize(40, 40))
        self.register_btn.setObjectName("register_btn")
        self.verticalLayout_3.addWidget(self.register_btn)
        self.back_to_login_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.back_to_login_btn.setMinimumSize(QtCore.QSize(130, 40))
        self.back_to_login_btn.setMaximumSize(QtCore.QSize(130, 40))
        self.back_to_login_btn.setStyleSheet("border:3px solid #52BFA1;\n"
"font: 14pt \"Times New Roman\";\n"
"border-radius:20px;")
        self.back_to_login_btn.setIcon(icon1)
        self.back_to_login_btn.setIconSize(QtCore.QSize(40, 40))
        self.back_to_login_btn.setObjectName("back_to_login_btn")
        self.verticalLayout_3.addWidget(self.back_to_login_btn)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem11)
        self.gridLayout_5.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music World"))
        self.groupBox.setTitle(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "User Name"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.signup_btn.setText(_translate("MainWindow", "SignUp"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Registeration"))
        self.label_3.setText(_translate("MainWindow", "User Name"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.label_5.setText(_translate("MainWindow", "Repeat Password"))
        self.register_btn.setText(_translate("MainWindow", "Register"))
        self.back_to_login_btn.setText(_translate("MainWindow", "Login"))
import app_resource_rc
