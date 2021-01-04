# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(925, 625)
        MainWindow.setMinimumSize(QtCore.QSize(775, 562))
        MainWindow.setMaximumSize(QtCore.QSize(925, 625))
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background: orange;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setStyleSheet("QFrame{\n"
"    background: orange;\n"
"\n"
"}")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.main_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.buy_items = QtWidgets.QPushButton(self.main_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.buy_items.setFont(font)
        self.buy_items.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buy_items.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background: red;\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"    height: 18px;\n"
"}\n"
"QPushButton:hover{\n"
"    color: black;\n"
"    background:orange;\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"    height: 18px;\n"
"}")
        self.buy_items.setObjectName("buy_items")
        self.gridLayout.addWidget(self.buy_items, 2, 2, 1, 1)
        self.item_list = QtWidgets.QListWidget(self.main_frame)
        self.item_list.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.item_list.setFont(font)
        self.item_list.setStyleSheet("QListWidget{\n"
"    background: #333;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    color: #717072;    \n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.item_list.setObjectName("item_list")
        item = QtWidgets.QListWidgetItem()
        self.item_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.item_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.item_list.addItem(item)
        self.gridLayout.addWidget(self.item_list, 1, 2, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.main_frame)
        self.tabWidget.setStyleSheet("QTabBar::tab:selected {\n"
"    background: orange;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"    font-size: 15px;\n"
"    height: 20px;\n"
"    width: 110px;\n"
"    font-family: \"Century Gothic\";\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: red;\n"
"    color: white;\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"    font-size: 15px;\n"
"    height: 20px;\n"
"    width: 110px;\n"
"    font-family: \"Century Gothic\";\n"
"}\n"
"\n"
"QTabWidget::pane{\n"
"    border: 0;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.card_ifo_frame = QtWidgets.QFrame(self.tab_2)
        self.card_ifo_frame.setStyleSheet("QFrame{\n"
"    background: #333;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"}")
        self.card_ifo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card_ifo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card_ifo_frame.setObjectName("card_ifo_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.card_ifo_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.name_label = QtWidgets.QLabel(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setUnderline(False)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;    \n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.name_label.setObjectName("name_label")
        self.horizontalLayout_6.addWidget(self.name_label)
        self.name_lineEdit = QtWidgets.QLineEdit(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(10)
        self.name_lineEdit.setFont(font)
        self.name_lineEdit.setStyleSheet("QLineEdit{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"}")
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.horizontalLayout_6.addWidget(self.name_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.email_label = QtWidgets.QLabel(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setUnderline(False)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;    \n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.email_label.setObjectName("email_label")
        self.horizontalLayout_7.addWidget(self.email_label)
        self.email_lineEdit = QtWidgets.QLineEdit(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(10)
        self.email_lineEdit.setFont(font)
        self.email_lineEdit.setStyleSheet("QLineEdit{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"}")
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.horizontalLayout_7.addWidget(self.email_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tel_label = QtWidgets.QLabel(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setUnderline(False)
        self.tel_label.setFont(font)
        self.tel_label.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;    \n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.tel_label.setObjectName("tel_label")
        self.horizontalLayout_8.addWidget(self.tel_label)
        self.tel_lineEdit = QtWidgets.QLineEdit(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(10)
        self.tel_lineEdit.setFont(font)
        self.tel_lineEdit.setStyleSheet("QLineEdit{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"}")
        self.tel_lineEdit.setObjectName("tel_lineEdit")
        self.horizontalLayout_8.addWidget(self.tel_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.address_label = QtWidgets.QLabel(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setUnderline(False)
        self.address_label.setFont(font)
        self.address_label.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;    \n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.address_label.setObjectName("address_label")
        self.horizontalLayout_9.addWidget(self.address_label)
        self.address_lineEdit = QtWidgets.QLineEdit(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(10)
        self.address_lineEdit.setFont(font)
        self.address_lineEdit.setStyleSheet("QLineEdit{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"}")
        self.address_lineEdit.setObjectName("address_lineEdit")
        self.horizontalLayout_9.addWidget(self.address_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.city_label = QtWidgets.QLabel(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setUnderline(False)
        self.city_label.setFont(font)
        self.city_label.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;    \n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.city_label.setObjectName("city_label")
        self.horizontalLayout_10.addWidget(self.city_label)
        self.city_lineEdit = QtWidgets.QLineEdit(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(10)
        self.city_lineEdit.setFont(font)
        self.city_lineEdit.setStyleSheet("QLineEdit{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"}")
        self.city_lineEdit.setObjectName("city_lineEdit")
        self.horizontalLayout_10.addWidget(self.city_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.postcode_label = QtWidgets.QLabel(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setUnderline(False)
        self.postcode_label.setFont(font)
        self.postcode_label.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;    \n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.postcode_label.setObjectName("postcode_label")
        self.horizontalLayout_11.addWidget(self.postcode_label)
        self.postcode_lineEdit = QtWidgets.QLineEdit(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(10)
        self.postcode_lineEdit.setFont(font)
        self.postcode_lineEdit.setStyleSheet("QLineEdit{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"}")
        self.postcode_lineEdit.setObjectName("postcode_lineEdit")
        self.horizontalLayout_11.addWidget(self.postcode_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.country_label = QtWidgets.QLabel(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setUnderline(False)
        self.country_label.setFont(font)
        self.country_label.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;    \n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.country_label.setObjectName("country_label")
        self.horizontalLayout_12.addWidget(self.country_label)
        self.coutry_comboBox = QtWidgets.QComboBox(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.coutry_comboBox.setFont(font)
        self.coutry_comboBox.setStyleSheet("QComboBox{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.coutry_comboBox.setObjectName("coutry_comboBox")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.coutry_comboBox.addItem("")
        self.horizontalLayout_12.addWidget(self.coutry_comboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.cardtype_label = QtWidgets.QLabel(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setUnderline(False)
        self.cardtype_label.setFont(font)
        self.cardtype_label.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;    \n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.cardtype_label.setObjectName("cardtype_label")
        self.horizontalLayout_13.addWidget(self.cardtype_label)
        self.card_type_comboBox = QtWidgets.QComboBox(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.card_type_comboBox.setFont(font)
        self.card_type_comboBox.setStyleSheet("QComboBox{\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.card_type_comboBox.setObjectName("card_type_comboBox")
        self.card_type_comboBox.addItem("")
        self.card_type_comboBox.addItem("")
        self.card_type_comboBox.addItem("")
        self.card_type_comboBox.addItem("")
        self.horizontalLayout_13.addWidget(self.card_type_comboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.card_nuber_label = QtWidgets.QLabel(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setUnderline(False)
        self.card_nuber_label.setFont(font)
        self.card_nuber_label.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;    \n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.card_nuber_label.setObjectName("card_nuber_label")
        self.horizontalLayout_14.addWidget(self.card_nuber_label)
        self.card_number_lineEdit = QtWidgets.QLineEdit(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(10)
        self.card_number_lineEdit.setFont(font)
        self.card_number_lineEdit.setStyleSheet("QLineEdit{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"}")
        self.card_number_lineEdit.setObjectName("card_number_lineEdit")
        self.horizontalLayout_14.addWidget(self.card_number_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.card_month_label = QtWidgets.QLabel(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setUnderline(False)
        self.card_month_label.setFont(font)
        self.card_month_label.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;    \n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.card_month_label.setObjectName("card_month_label")
        self.horizontalLayout_15.addWidget(self.card_month_label)
        self.card_month_comboBox = QtWidgets.QComboBox(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.card_month_comboBox.setFont(font)
        self.card_month_comboBox.setStyleSheet("QComboBox{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.card_month_comboBox.setObjectName("card_month_comboBox")
        self.card_month_comboBox.addItem("")
        self.card_month_comboBox.addItem("")
        self.card_month_comboBox.addItem("")
        self.card_month_comboBox.addItem("")
        self.card_month_comboBox.addItem("")
        self.card_month_comboBox.addItem("")
        self.card_month_comboBox.addItem("")
        self.card_month_comboBox.addItem("")
        self.card_month_comboBox.addItem("")
        self.card_month_comboBox.addItem("")
        self.card_month_comboBox.addItem("")
        self.card_month_comboBox.addItem("")
        self.horizontalLayout_15.addWidget(self.card_month_comboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.card_year_label = QtWidgets.QLabel(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setUnderline(False)
        self.card_year_label.setFont(font)
        self.card_year_label.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;    \n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.card_year_label.setObjectName("card_year_label")
        self.horizontalLayout_16.addWidget(self.card_year_label)
        self.card_year_comboBox = QtWidgets.QComboBox(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.card_year_comboBox.setFont(font)
        self.card_year_comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.card_year_comboBox.setStyleSheet("QComboBox{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.card_year_comboBox.setObjectName("card_year_comboBox")
        self.card_year_comboBox.addItem("")
        self.card_year_comboBox.addItem("")
        self.card_year_comboBox.addItem("")
        self.card_year_comboBox.addItem("")
        self.card_year_comboBox.addItem("")
        self.card_year_comboBox.addItem("")
        self.card_year_comboBox.addItem("")
        self.card_year_comboBox.addItem("")
        self.card_year_comboBox.addItem("")
        self.card_year_comboBox.addItem("")
        self.card_year_comboBox.addItem("")
        self.card_year_comboBox.addItem("")
        self.horizontalLayout_16.addWidget(self.card_year_comboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.card_cvv_label = QtWidgets.QLabel(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setUnderline(False)
        self.card_cvv_label.setFont(font)
        self.card_cvv_label.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;    \n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.card_cvv_label.setObjectName("card_cvv_label")
        self.horizontalLayout_17.addWidget(self.card_cvv_label)
        self.cvv_lineEdit = QtWidgets.QLineEdit(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(10)
        self.cvv_lineEdit.setFont(font)
        self.cvv_lineEdit.setStyleSheet("QLineEdit{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"}")
        self.cvv_lineEdit.setObjectName("cvv_lineEdit")
        self.horizontalLayout_17.addWidget(self.cvv_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.save_btn = QtWidgets.QPushButton(self.card_ifo_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background: red;\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"    height: 18px;\n"
"}\n"
"QPushButton:hover{\n"
"    color: black;\n"
"    background:orange;\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"    height: 18px;\n"
"}")
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_18.addWidget(self.save_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_3.addLayout(self.horizontalLayout_19)
        self.verticalLayout_4.addWidget(self.card_ifo_frame)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = QtWidgets.QFrame(self.tab_1)
        self.frame.setStyleSheet("QFrame{\n"
"    background: orange;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 401, 251))
        self.frame_2.setStyleSheet("QFrame{\n"
"    background: #333;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.coat_label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setUnderline(False)
        self.coat_label.setFont(font)
        self.coat_label.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;    \n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.coat_label.setObjectName("coat_label")
        self.horizontalLayout.addWidget(self.coat_label)
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.kw1_label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setUnderline(False)
        self.kw1_label.setFont(font)
        self.kw1_label.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;    \n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.kw1_label.setObjectName("kw1_label")
        self.horizontalLayout_2.addWidget(self.kw1_label)
        self.kw1_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.kw1_lineEdit.setFont(font)
        self.kw1_lineEdit.setStyleSheet("QLineEdit{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.kw1_lineEdit.setObjectName("kw1_lineEdit")
        self.horizontalLayout_2.addWidget(self.kw1_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.kw2_label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setUnderline(False)
        self.kw2_label.setFont(font)
        self.kw2_label.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;    \n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.kw2_label.setObjectName("kw2_label")
        self.horizontalLayout_3.addWidget(self.kw2_label)
        self.kw2_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.kw2_lineEdit.setFont(font)
        self.kw2_lineEdit.setStyleSheet("QLineEdit{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.kw2_lineEdit.setObjectName("kw2_lineEdit")
        self.horizontalLayout_3.addWidget(self.kw2_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.colour_label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setUnderline(False)
        self.colour_label.setFont(font)
        self.colour_label.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;    \n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.colour_label.setObjectName("colour_label")
        self.horizontalLayout_4.addWidget(self.colour_label)
        self.colour_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.colour_lineEdit.setFont(font)
        self.colour_lineEdit.setStyleSheet("QLineEdit{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.colour_lineEdit.setObjectName("colour_lineEdit")
        self.horizontalLayout_4.addWidget(self.colour_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.size_label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setUnderline(False)
        self.size_label.setFont(font)
        self.size_label.setStyleSheet("QLabel{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;    \n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.size_label.setObjectName("size_label")
        self.horizontalLayout_5.addWidget(self.size_label)
        self.size_combo = QtWidgets.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.size_combo.setFont(font)
        self.size_combo.setStyleSheet("QComboBox{\n"
"    background: transparent;\n"
"    border: none;    \n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"    font-family: \"Century Gothic\";\n"
"}")
        self.size_combo.setObjectName("size_combo")
        self.size_combo.addItem("")
        self.size_combo.addItem("")
        self.size_combo.addItem("")
        self.size_combo.addItem("")
        self.horizontalLayout_5.addWidget(self.size_combo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.add_item = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.add_item.setFont(font)
        self.add_item.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background: red;\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"    height: 18px;\n"
"}\n"
"QPushButton:hover{\n"
"    color: black;\n"
"    background:orange;\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"    height: 18px;\n"
"}")
        self.add_item.setObjectName("add_item")
        self.verticalLayout_2.addWidget(self.add_item)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background: red;\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"    height: 18px;\n"
"}\n"
"QPushButton:hover{\n"
"    color: black;\n"
"    background:orange;\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"    height: 18px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_5.addWidget(self.frame)
        self.tabWidget.addTab(self.tab_1, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 5, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        self.buying_list = QtWidgets.QTreeWidget(self.main_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.buying_list.setFont(font)
        self.buying_list.setStyleSheet("QTreeWidget{\n"
"    background: #333;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    font-family: \"Century Gothic\";\n"
"    color: #717072;    \n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #333;\n"
"    color: #717072;    \n"
"}")
        self.buying_list.setFrameShape(QtWidgets.QFrame.Box)
        self.buying_list.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buying_list.setObjectName("buying_list")
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setKerning(True)
        self.buying_list.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.buying_list.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.buying_list.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.buying_list.headerItem().setFont(3, font)
        self.buying_list.headerItem().setBackground(3, QtGui.QColor(85, 170, 127))
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.buying_list.headerItem().setForeground(3, brush)
        item_0 = QtWidgets.QTreeWidgetItem(self.buying_list)
        self.gridLayout.addWidget(self.buying_list, 4, 2, 1, 1)
        self.verticalLayout.addWidget(self.main_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionREAD_ME = QtWidgets.QAction(MainWindow)
        self.actionREAD_ME.setObjectName("actionREAD_ME")
        self.actionContact = QtWidgets.QAction(MainWindow)
        self.actionContact.setObjectName("actionContact")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buy_items.setText(_translate("MainWindow", "Buy Item(s)"))
        __sortingEnabled = self.item_list.isSortingEnabled()
        self.item_list.setSortingEnabled(False)
        item = self.item_list.item(0)
        item.setText(_translate("MainWindow", "dsadas"))
        item = self.item_list.item(1)
        item.setText(_translate("MainWindow", "dsadas"))
        item = self.item_list.item(2)
        item.setText(_translate("MainWindow", "dsadas"))
        self.item_list.setSortingEnabled(__sortingEnabled)
        self.name_label.setText(_translate("MainWindow", "Name :"))
        self.email_label.setText(_translate("MainWindow", "E-Mail"))
        self.tel_label.setText(_translate("MainWindow", "Tel. :"))
        self.address_label.setText(_translate("MainWindow", "Address :"))
        self.city_label.setText(_translate("MainWindow", "City :"))
        self.postcode_label.setText(_translate("MainWindow", "Postcode :"))
        self.country_label.setText(_translate("MainWindow", "Country :"))
        self.coutry_comboBox.setItemText(0, _translate("MainWindow", "UK"))
        self.coutry_comboBox.setItemText(1, _translate("MainWindow", "UK (N. IRELAND)"))
        self.coutry_comboBox.setItemText(2, _translate("MainWindow", "AUSTRIA"))
        self.coutry_comboBox.setItemText(3, _translate("MainWindow", "BELARUS"))
        self.coutry_comboBox.setItemText(4, _translate("MainWindow", "BELGIUM"))
        self.coutry_comboBox.setItemText(5, _translate("MainWindow", "BULGARIA"))
        self.coutry_comboBox.setItemText(6, _translate("MainWindow", "CROATIA"))
        self.coutry_comboBox.setItemText(7, _translate("MainWindow", "CZECH REPUBLIC"))
        self.coutry_comboBox.setItemText(8, _translate("MainWindow", "DENMARK"))
        self.coutry_comboBox.setItemText(9, _translate("MainWindow", "ESTONIA"))
        self.coutry_comboBox.setItemText(10, _translate("MainWindow", "FINLAND"))
        self.coutry_comboBox.setItemText(11, _translate("MainWindow", "FRANCE"))
        self.coutry_comboBox.setItemText(12, _translate("MainWindow", "GERMANY"))
        self.coutry_comboBox.setItemText(13, _translate("MainWindow", "GREECE"))
        self.coutry_comboBox.setItemText(14, _translate("MainWindow", "HUNGARY"))
        self.coutry_comboBox.setItemText(15, _translate("MainWindow", "ICELAND"))
        self.coutry_comboBox.setItemText(16, _translate("MainWindow", "IRELAND"))
        self.coutry_comboBox.setItemText(17, _translate("MainWindow", "ITALY"))
        self.coutry_comboBox.setItemText(18, _translate("MainWindow", "LATVIA"))
        self.coutry_comboBox.setItemText(19, _translate("MainWindow", "LITHUANIA"))
        self.coutry_comboBox.setItemText(20, _translate("MainWindow", "LUXEMBURG"))
        self.coutry_comboBox.setItemText(21, _translate("MainWindow", "MONACO"))
        self.coutry_comboBox.setItemText(22, _translate("MainWindow", "NETHERLANDS"))
        self.coutry_comboBox.setItemText(23, _translate("MainWindow", "NORWAY"))
        self.coutry_comboBox.setItemText(24, _translate("MainWindow", "POLAND"))
        self.coutry_comboBox.setItemText(25, _translate("MainWindow", "PORTUGAL"))
        self.coutry_comboBox.setItemText(26, _translate("MainWindow", "ROMANIA"))
        self.coutry_comboBox.setItemText(27, _translate("MainWindow", "RUSSIA"))
        self.coutry_comboBox.setItemText(28, _translate("MainWindow", "SLOVAKIA"))
        self.coutry_comboBox.setItemText(29, _translate("MainWindow", "SLOVENIA"))
        self.coutry_comboBox.setItemText(30, _translate("MainWindow", "SPAIN"))
        self.coutry_comboBox.setItemText(31, _translate("MainWindow", "SWEDEN"))
        self.coutry_comboBox.setItemText(32, _translate("MainWindow", "SWITZERLAND"))
        self.coutry_comboBox.setItemText(33, _translate("MainWindow", "TURKEY"))
        self.cardtype_label.setText(_translate("MainWindow", "Card type :"))
        self.card_type_comboBox.setItemText(0, _translate("MainWindow", "Visa"))
        self.card_type_comboBox.setItemText(1, _translate("MainWindow", "American Express"))
        self.card_type_comboBox.setItemText(2, _translate("MainWindow", "Mastercard"))
        self.card_type_comboBox.setItemText(3, _translate("MainWindow", "Solo"))
        self.card_nuber_label.setText(_translate("MainWindow", "Card number :"))
        self.card_month_label.setText(_translate("MainWindow", "Card month :"))
        self.card_month_comboBox.setItemText(0, _translate("MainWindow", "01"))
        self.card_month_comboBox.setItemText(1, _translate("MainWindow", "02"))
        self.card_month_comboBox.setItemText(2, _translate("MainWindow", "03"))
        self.card_month_comboBox.setItemText(3, _translate("MainWindow", "04"))
        self.card_month_comboBox.setItemText(4, _translate("MainWindow", "05"))
        self.card_month_comboBox.setItemText(5, _translate("MainWindow", "06"))
        self.card_month_comboBox.setItemText(6, _translate("MainWindow", "07"))
        self.card_month_comboBox.setItemText(7, _translate("MainWindow", "08"))
        self.card_month_comboBox.setItemText(8, _translate("MainWindow", "09"))
        self.card_month_comboBox.setItemText(9, _translate("MainWindow", "10"))
        self.card_month_comboBox.setItemText(10, _translate("MainWindow", "11"))
        self.card_month_comboBox.setItemText(11, _translate("MainWindow", "12"))
        self.card_year_label.setText(_translate("MainWindow", "Card year :"))
        self.card_year_comboBox.setItemText(0, _translate("MainWindow", "2019"))
        self.card_year_comboBox.setItemText(1, _translate("MainWindow", "2020"))
        self.card_year_comboBox.setItemText(2, _translate("MainWindow", "2021"))
        self.card_year_comboBox.setItemText(3, _translate("MainWindow", "2022"))
        self.card_year_comboBox.setItemText(4, _translate("MainWindow", "2023"))
        self.card_year_comboBox.setItemText(5, _translate("MainWindow", "2024"))
        self.card_year_comboBox.setItemText(6, _translate("MainWindow", "2025"))
        self.card_year_comboBox.setItemText(7, _translate("MainWindow", "2026"))
        self.card_year_comboBox.setItemText(8, _translate("MainWindow", "2027"))
        self.card_year_comboBox.setItemText(9, _translate("MainWindow", "2028"))
        self.card_year_comboBox.setItemText(10, _translate("MainWindow", "2029"))
        self.card_year_comboBox.setItemText(11, _translate("MainWindow", "2030"))
        self.card_cvv_label.setText(_translate("MainWindow", "Card CVV :"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Checkout"))
        self.coat_label.setText(_translate("MainWindow", "Coat :"))
        self.comboBox.setItemText(0, _translate("MainWindow", "jackets"))
        self.comboBox.setItemText(1, _translate("MainWindow", "shirts"))
        self.comboBox.setItemText(2, _translate("MainWindow", "tops/sweaters"))
        self.comboBox.setItemText(3, _translate("MainWindow", "sweatshirts"))
        self.comboBox.setItemText(4, _translate("MainWindow", "pants"))
        self.comboBox.setItemText(5, _translate("MainWindow", "shorts"))
        self.comboBox.setItemText(6, _translate("MainWindow", "hats"))
        self.comboBox.setItemText(7, _translate("MainWindow", "bags"))
        self.kw1_label.setText(_translate("MainWindow", "KeyWord1 :"))
        self.kw2_label.setText(_translate("MainWindow", "KeyWord2 :"))
        self.colour_label.setText(_translate("MainWindow", "Colour : "))
        self.size_label.setText(_translate("MainWindow", "Size :"))
        self.size_combo.setItemText(0, _translate("MainWindow", "Small"))
        self.size_combo.setItemText(1, _translate("MainWindow", "Medium"))
        self.size_combo.setItemText(2, _translate("MainWindow", "Large"))
        self.size_combo.setItemText(3, _translate("MainWindow", "XLarge"))
        self.add_item.setText(_translate("MainWindow", "Add Item"))
        self.pushButton.setText(_translate("MainWindow", "Add cart"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Items"))
        self.buying_list.setSortingEnabled(False)
        self.buying_list.headerItem().setText(0, _translate("MainWindow", "Item Name"))
        self.buying_list.headerItem().setText(1, _translate("MainWindow", "Status"))
        self.buying_list.headerItem().setText(2, _translate("MainWindow", "Start time"))
        self.buying_list.headerItem().setText(3, _translate("MainWindow", "End time"))
        __sortingEnabled = self.buying_list.isSortingEnabled()
        self.buying_list.setSortingEnabled(False)
        self.buying_list.topLevelItem(0).setText(0, _translate("MainWindow", "Upland Fleece"))
        self.buying_list.topLevelItem(0).setText(1, _translate("MainWindow", "In Progress"))
        self.buying_list.topLevelItem(0).setText(2, _translate("MainWindow", "18:08:20:02552"))
        self.buying_list.topLevelItem(0).setText(3, _translate("MainWindow", "18:08:21:50525"))
        self.buying_list.setSortingEnabled(__sortingEnabled)
        self.actionREAD_ME.setText(_translate("MainWindow", "READ ME"))
        self.actionContact.setText(_translate("MainWindow", "Contact"))
#import icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
