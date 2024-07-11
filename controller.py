import json
import os
import ssl
import sys
from pathlib import Path
from urllib import request
from zipfile import ZipFile, is_zipfile

import certifi
from PySide6 import QtGui, QtWidgets
from PySide6.QtWidgets import QMessageBox

from ui_file.AboutUI import Ui_AboutWindow
from ui_file.CustomWidgets import QListWidgetItemPlus
from ui_file.MainUI import Ui_MainWindow


class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.version = "1.0"

        self.setup_control()

    def setup_control(self):
        """
        initialize global variable and connect slot functions
        """
        self.ui.menu_about_about.triggered.connect(self.show_about_window)
        self.ui.menu_about_update.triggered.connect(self.check_update)
        self.ui.path_btn.clicked.connect(self.show_select_path_window)
        self.ui.naming_ignore_rtn.toggled.connect(self.change_naming_mode)
        self.ui.clear_zip_list_btn.clicked.connect(self.clear_zip_list)
        self.ui.start_btn.clicked.connect(self.start_combine)
        self.ui.exit_btn.clicked.connect(self.app_exit)
        self.ui.zip_items_list.send_new_item.connect(self.add_drop_files)
        self.ui.number_start_value.valueChanged.connect(self.update_new_list)
        self.ui.number_gap_value.valueChanged.connect(self.update_new_list)
        self.ui.number_zero_value.valueChanged.connect(self.update_new_list)

    def check_update(self):
        github_release_url: str = (
            "https://github.com/scbmark/zip_combine/releases/latest"
        )
        github_release_url_api: str = (
            "https://api.github.com/repos/scbmark/zip_combine/releases/latest"
        )

        req = request.Request(github_release_url_api)

        try:
            context = ssl.create_default_context(cafile=certifi.where())
            with request.urlopen(req, context=context) as response:
                res = json.load(response)
                latest_version = res["tag_name"]
        except:
            messagebox = QMessageBox(self)
            messagebox.warning(self, "更新", "網路連線失敗")
            return

        if latest_version != self.version:
            messagebox = QMessageBox(self)
            messagebox.setWindowTitle("更新")
            messagebox.setText(
                f"發現更新\n目前版本： {self.version}\n最新版本： {res['tag_name']}"
            )
            messagebox.setIcon(QMessageBox.Icon.Information)
            messagebox.addButton("現在更新", QMessageBox.ButtonRole.AcceptRole)
            messagebox.addButton("不要更新", QMessageBox.ButtonRole.RejectRole)

            result = messagebox.exec()
            if result == 0:
                import webbrowser

                webbrowser.open(github_release_url)
            else:
                pass
        else:
            messagebox = QMessageBox(self)
            messagebox.information(
                self, "檢查更新", f"目前為最新版本\n目前版本： {self.version}"
            )

    def show_about_window(self):
        """
        open about window
        """
        self.AboutWindows = QtWidgets.QWidget()
        self.about_ui = Ui_AboutWindow()
        self.about_ui.setupUi(self.AboutWindows)
        self.about_ui.version_lb.setText(f"Version: {self.version}")
        self.AboutWindows.setFixedSize(400, 600)
        self.about_ui.exit_btn.clicked.connect(lambda: self.AboutWindows.close())
        self.AboutWindows.show()

    def show_select_path_window(self):
        """
        show the file dialog and get the folder's path
        """
        dir_path = QtWidgets.QFileDialog.getExistingDirectory(caption="選取資料夾")
        self.ui.path_value.setText(dir_path)

    def show_error_window(self, error_message):
        messagebox = QMessageBox(self)
        messagebox.warning(self, "錯誤", error_message)

    def change_naming_mode(self):
        if self.ui.naming_ignore_rtn.isChecked():
            self.ui.number_start_value.setEnabled(False)
            self.ui.number_gap_value.setEnabled(False)
            self.ui.number_zero_value.setEnabled(False)
        else:
            self.ui.number_start_value.setEnabled(True)
            self.ui.number_gap_value.setEnabled(True)
            self.ui.number_zero_value.setEnabled(True)
        self.update_old_list()
        self.update_new_list()

    def add_drop_files(self, files: list):
        for file in files:
            if is_zipfile(file):
                self.add_file_to_list(file)

        self.update_old_list()
        self.update_new_list()

    def clear_zip_list(self):
        self.ui.zip_items_list.clear()
        self.update_old_list()
        self.update_new_list()

    def add_file_to_list(self, file: str):
        item = QListWidgetItemPlus(file)
        item_widget = QtWidgets.QWidget()

        name_lb = QtWidgets.QLabel()
        name_lb.setText(Path(file).name)
        item_layout = QtWidgets.QHBoxLayout()

        delete_button = QtWidgets.QPushButton("")
        delete_button.setIcon(QtGui.QIcon(QtGui.QPixmap(":/statics/close.svg")))
        delete_button.clicked.connect(lambda: self.delete_item(item))

        item_layout.addWidget(name_lb)
        item_layout.addStretch()
        item_layout.addWidget(delete_button)

        item_widget.setLayout(item_layout)
        item.setSizeHint(item_widget.sizeHint())

        self.ui.zip_items_list.addItem(item)
        self.ui.zip_items_list.setItemWidget(item, item_widget)
        self.ui.zip_items_list.repaint()

    def delete_item(self, item: QListWidgetItemPlus):
        """
        get the QListWidgetItem and remove it from QListWidget
        """
        index = self.ui.zip_items_list.row(item)
        self.ui.zip_items_list.takeItem(index)
        self.update_old_list()
        self.update_new_list()

    def update_old_list(self):
        self.ui.files_old_list.clear()
        for index_name in range(self.ui.zip_items_list.count()):
            zipitem: QListWidgetItemPlus = self.ui.zip_items_list.item(index_name)
            zip_filename = zipitem.text
            with ZipFile(zip_filename, "r") as f:
                file_list = f.namelist()
            for file in file_list:
                self.ui.files_old_list.addItem(file)

    def update_new_list(self):
        self.ui.files_new_list.clear()

        start_num = self.ui.number_start_value.value()
        gap_num = self.ui.number_gap_value.value()
        zero_num = self.ui.number_zero_value.value()

        for index_name in range(self.ui.zip_items_list.count()):
            zipitem: QListWidgetItemPlus = self.ui.zip_items_list.item(index_name)
            zip_filename = zipitem.text
            with ZipFile(zip_filename, "r") as f:
                file_list = f.namelist()
            if self.ui.naming_ignore_rtn.isChecked():
                for file in file_list:
                    self.ui.files_new_list.addItem(file)
            else:
                for file in file_list:
                    suffix = Path(file).suffix
                    self.ui.files_new_list.addItem(
                        f"{str(start_num).zfill(zero_num)}{suffix}"
                    )
                    start_num += gap_num

    def check_new_zip_file_path(self):
        new_zip_file_path = os.path.join(
            self.ui.path_value.text(), f"{self.ui.output_filename_value.text()}.zip"
        )
        if os.path.exists(new_zip_file_path):
            messagebox = QMessageBox(self)
            messagebox.setWindowTitle("檔案重覆")
            messagebox.setText(f"檔案衝突： {new_zip_file_path}")
            messagebox.setIcon(QMessageBox.Icon.Information)
            messagebox.addButton("檔案覆蓋", QMessageBox.ButtonRole.DestructiveRole)
            messagebox.addButton("加後綴", QMessageBox.ButtonRole.RejectRole)
            messagebox.addButton("取消", QMessageBox.ButtonRole.RejectRole)

            messagebox.exec()
            result = messagebox.clickedButton().text()
            if result == "加後綴":
                times = 1
                while True:
                    new_zip_file_path = os.path.join(
                        self.ui.path_value.text(),
                        f"{self.ui.output_filename_value.text()}-{times}.zip",
                    )
                    if os.path.exists(new_zip_file_path):
                        times += 1
                    else:
                        return new_zip_file_path
            elif result == "檔案覆蓋":
                return new_zip_file_path
            else:
                return ""
        else:
            return new_zip_file_path

    def start_combine(self):
        if not self.ui.output_filename_value.text():
            error_message = "請輸入檔案名稱"
            self.show_error_window(error_message)
            return
        if not self.ui.path_value.text():
            self.show_select_path_window()

        new_zip_file_path = self.check_new_zip_file_path()

        if not new_zip_file_path:
            return

        zip_list = [
            self.ui.zip_items_list.item(index).text
            for index in range(self.ui.zip_items_list.count())
        ]

        new_name_list = [
            self.ui.files_new_list.item(index).text()
            for index in range(self.ui.files_new_list.count())
        ]

        combine_result = self.combine_zips(new_zip_file_path, zip_list, new_name_list)
        if combine_result:
            messagebox = QMessageBox(self)
            messagebox.information(self, "合併完成", "合併完成")
        else:
            messagebox = QMessageBox(self)
            messagebox.warning(self, "合併失敗", "合併失敗")

    def combine_zips(self, new_zip_file_path, zip_list, new_name_list):
        name_count = 0

        try:
            with ZipFile(new_zip_file_path, "w") as output_zf:
                for zip_filename in zip_list:
                    with ZipFile(zip_filename, "r") as zip:
                        for file_name in zip.namelist():
                            with zip.open(file_name) as f:
                                new_file_name = new_name_list[name_count]
                                output_zf.writestr(new_file_name, f.read())
                                name_count += 1
            return True
        except:
            return False

    def app_exit(self):
        """
        close this program
        """
        sys.exit()
