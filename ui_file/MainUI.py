# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QButtonGroup, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)
import resources_rc
from .CustomWidgets import DropListWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 800)
        icon = QIcon()
        icon.addFile(u":/statics/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.menu_about_about = QAction(MainWindow)
        self.menu_about_about.setObjectName(u"menu_about_about")
        self.menu_about_manual = QAction(MainWindow)
        self.menu_about_manual.setObjectName(u"menu_about_manual")
        self.menu_about_update = QAction(MainWindow)
        self.menu_about_update.setObjectName(u"menu_about_update")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.v_main_layout = QVBoxLayout()
        self.v_main_layout.setObjectName(u"v_main_layout")
        self.v_main_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.v_main_layout.setContentsMargins(10, 10, 10, 10)
        self.setting_layout = QVBoxLayout()
        self.setting_layout.setObjectName(u"setting_layout")
        self.setting_layout.setContentsMargins(5, 5, 5, 5)
        self.path_layout = QHBoxLayout()
        self.path_layout.setObjectName(u"path_layout")
        self.path_layout.setContentsMargins(0, 0, 0, 0)
        self.output_filename_lb = QLabel(self.centralwidget)
        self.output_filename_lb.setObjectName(u"output_filename_lb")

        self.path_layout.addWidget(self.output_filename_lb)

        self.output_filename_value = QLineEdit(self.centralwidget)
        self.output_filename_value.setObjectName(u"output_filename_value")

        self.path_layout.addWidget(self.output_filename_value)

        self.path_lb = QLabel(self.centralwidget)
        self.path_lb.setObjectName(u"path_lb")

        self.path_layout.addWidget(self.path_lb)

        self.path_value = QLineEdit(self.centralwidget)
        self.path_value.setObjectName(u"path_value")
        self.path_value.setReadOnly(True)

        self.path_layout.addWidget(self.path_value)

        self.path_btn = QPushButton(self.centralwidget)
        self.path_btn.setObjectName(u"path_btn")

        self.path_layout.addWidget(self.path_btn)


        self.setting_layout.addLayout(self.path_layout)


        self.v_main_layout.addLayout(self.setting_layout)

        self.veiw_layout = QVBoxLayout()
        self.veiw_layout.setObjectName(u"veiw_layout")
        self.veiw_layout.setContentsMargins(5, 5, 5, 5)
        self.zip_items_list = DropListWidget(self.centralwidget)
        self.zip_items_list.setObjectName(u"zip_items_list")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zip_items_list.sizePolicy().hasHeightForWidth())
        self.zip_items_list.setSizePolicy(sizePolicy)
        self.zip_items_list.setDragEnabled(True)
        self.zip_items_list.setDragDropMode(QAbstractItemView.InternalMove)
        self.zip_items_list.setDefaultDropAction(Qt.MoveAction)
        self.zip_items_list.setIconSize(QSize(50, 50))
        self.zip_items_list.setMovement(QListView.Free)
        self.zip_items_list.setProperty("isWrapping", False)
        self.zip_items_list.setWordWrap(True)

        self.veiw_layout.addWidget(self.zip_items_list)

        self.clear_layout = QHBoxLayout()
        self.clear_layout.setObjectName(u"clear_layout")
        self.clear_layout.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.clear_layout.addItem(self.horizontalSpacer)

        self.item_list_info_lb = QLabel(self.centralwidget)
        self.item_list_info_lb.setObjectName(u"item_list_info_lb")
        self.item_list_info_lb.setAlignment(Qt.AlignCenter)

        self.clear_layout.addWidget(self.item_list_info_lb)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.clear_layout.addItem(self.horizontalSpacer_4)

        self.clear_zip_list_btn = QPushButton(self.centralwidget)
        self.clear_zip_list_btn.setObjectName(u"clear_zip_list_btn")
        icon1 = QIcon()
        icon1.addFile(u":/statics/clear_all.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_zip_list_btn.setIcon(icon1)

        self.clear_layout.addWidget(self.clear_zip_list_btn)


        self.veiw_layout.addLayout(self.clear_layout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.veiw_layout.addWidget(self.line)

        self.naming_layout = QHBoxLayout()
        self.naming_layout.setObjectName(u"naming_layout")
        self.naming_layout.setContentsMargins(0, 0, 0, 0)
        self.naming_mode_lb = QLabel(self.centralwidget)
        self.naming_mode_lb.setObjectName(u"naming_mode_lb")

        self.naming_layout.addWidget(self.naming_mode_lb)

        self.naming_ignore_rtn = QRadioButton(self.centralwidget)
        self.naming_mode = QButtonGroup(MainWindow)
        self.naming_mode.setObjectName(u"naming_mode")
        self.naming_mode.addButton(self.naming_ignore_rtn)
        self.naming_ignore_rtn.setObjectName(u"naming_ignore_rtn")
        self.naming_ignore_rtn.setChecked(False)

        self.naming_layout.addWidget(self.naming_ignore_rtn)

        self.naming_number_rtn = QRadioButton(self.centralwidget)
        self.naming_mode.addButton(self.naming_number_rtn)
        self.naming_number_rtn.setObjectName(u"naming_number_rtn")
        self.naming_number_rtn.setChecked(True)

        self.naming_layout.addWidget(self.naming_number_rtn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.naming_layout.addItem(self.horizontalSpacer_3)

        self.number_start_lb = QLabel(self.centralwidget)
        self.number_start_lb.setObjectName(u"number_start_lb")

        self.naming_layout.addWidget(self.number_start_lb)

        self.number_start_value = QSpinBox(self.centralwidget)
        self.number_start_value.setObjectName(u"number_start_value")
        self.number_start_value.setMaximum(999)
        self.number_start_value.setValue(1)

        self.naming_layout.addWidget(self.number_start_value)

        self.number_gap_lb = QLabel(self.centralwidget)
        self.number_gap_lb.setObjectName(u"number_gap_lb")

        self.naming_layout.addWidget(self.number_gap_lb)

        self.number_gap_value = QSpinBox(self.centralwidget)
        self.number_gap_value.setObjectName(u"number_gap_value")
        self.number_gap_value.setMinimum(-999)
        self.number_gap_value.setMaximum(999)
        self.number_gap_value.setValue(1)

        self.naming_layout.addWidget(self.number_gap_value)

        self.number_zero_lb = QLabel(self.centralwidget)
        self.number_zero_lb.setObjectName(u"number_zero_lb")

        self.naming_layout.addWidget(self.number_zero_lb)

        self.number_zero_value = QSpinBox(self.centralwidget)
        self.number_zero_value.setObjectName(u"number_zero_value")
        self.number_zero_value.setMaximum(10)

        self.naming_layout.addWidget(self.number_zero_value)


        self.veiw_layout.addLayout(self.naming_layout)

        self.filename_layout = QHBoxLayout()
        self.filename_layout.setObjectName(u"filename_layout")
        self.filename_layout.setContentsMargins(5, 5, 5, 5)
        self.files_old_list = QListWidget(self.centralwidget)
        self.files_old_list.setObjectName(u"files_old_list")

        self.filename_layout.addWidget(self.files_old_list)

        self.arrow_lb = QLabel(self.centralwidget)
        self.arrow_lb.setObjectName(u"arrow_lb")

        self.filename_layout.addWidget(self.arrow_lb)

        self.files_new_list = QListWidget(self.centralwidget)
        self.files_new_list.setObjectName(u"files_new_list")

        self.filename_layout.addWidget(self.files_new_list)


        self.veiw_layout.addLayout(self.filename_layout)

        self.veiw_layout.setStretch(0, 1)
        self.veiw_layout.setStretch(4, 3)

        self.v_main_layout.addLayout(self.veiw_layout)

        self.button_layout = QHBoxLayout()
        self.button_layout.setObjectName(u"button_layout")
        self.button_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.button_layout.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.button_layout.addItem(self.horizontalSpacer_2)

        self.start_btn = QPushButton(self.centralwidget)
        self.start_btn.setObjectName(u"start_btn")
        icon2 = QIcon()
        icon2.addFile(u":/statics/play_arrow.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.start_btn.setIcon(icon2)
        self.start_btn.setIconSize(QSize(30, 30))

        self.button_layout.addWidget(self.start_btn)

        self.exit_btn = QPushButton(self.centralwidget)
        self.exit_btn.setObjectName(u"exit_btn")
        icon3 = QIcon()
        icon3.addFile(u":/statics/logout.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn.setIcon(icon3)
        self.exit_btn.setIconSize(QSize(28, 28))
        self.exit_btn.setFlat(False)

        self.button_layout.addWidget(self.exit_btn)


        self.v_main_layout.addLayout(self.button_layout)


        self.gridLayout.addLayout(self.v_main_layout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 720, 32))
        self.menu_about = QMenu(self.menubar)
        self.menu_about.setObjectName(u"menu_about")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_about.menuAction())
        self.menu_about.addAction(self.menu_about_update)
        self.menu_about.addAction(self.menu_about_about)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ZIP Combine", None))
        self.menu_about_about.setText(QCoreApplication.translate("MainWindow", u"\u95dc\u65bc", None))
        self.menu_about_manual.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u8aaa\u660e", None))
        self.menu_about_update.setText(QCoreApplication.translate("MainWindow", u"\u6aa2\u67e5\u66f4\u65b0", None))
        self.output_filename_lb.setText(QCoreApplication.translate("MainWindow", u"\u8f38\u51fa\u540d\u7a31\uff1a", None))
        self.path_lb.setText(QCoreApplication.translate("MainWindow", u"\u8f38\u51fa\u8def\u5f91\uff1a", None))
        self.path_btn.setText(QCoreApplication.translate("MainWindow", u"\u9078\u64c7", None))
        self.item_list_info_lb.setText(QCoreApplication.translate("MainWindow", u"\u62d6\u66f3\u58d3\u7e2e\u6a94\u4ee5\u65b0\u589e\u6216\u6392\u5e8f", None))
        self.clear_zip_list_btn.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u5217\u8868", None))
        self.naming_mode_lb.setText(QCoreApplication.translate("MainWindow", u"\u6a94\u540d\u8a2d\u8a08\uff1a", None))
        self.naming_ignore_rtn.setText(QCoreApplication.translate("MainWindow", u"\u5ffd\u7565", None))
        self.naming_number_rtn.setText(QCoreApplication.translate("MainWindow", u"\u5e8f\u5217\u5316", None))
        self.number_start_lb.setText(QCoreApplication.translate("MainWindow", u"\u8d77\u59cb", None))
        self.number_gap_lb.setText(QCoreApplication.translate("MainWindow", u"\u9593\u9694", None))
        self.number_zero_lb.setText(QCoreApplication.translate("MainWindow", u"\u586b\u88dc", None))
        self.arrow_lb.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"\u958b\u59cb", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"\u96e2\u958b", None))
        self.menu_about.setTitle(QCoreApplication.translate("MainWindow", u"\u8aaa\u660e", None))
    # retranslateUi

