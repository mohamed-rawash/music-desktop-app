from PyQt5 import QtWidgets
from views import add_singer_dialog_view


class AddSingerDialog(QtWidgets.QDialog, add_singer_dialog_view.Ui_Dialog):
    def __init__(self):
        super(AddSingerDialog, self).__init__()
        self.setupUi(self)
        self.setModal(True)
        self.ok_btn.clicked.connect(self.validate_info)
        self.cancel_btn.clicked.connect(self.reject)
        self.browse_songs_btn.clicked.connect(self.select_folder_path)
        self.browse_image_btn.clicked.connect(self.select_image_path)
        self.__chosen_path = ''
        self.__singer_name = ''
        self.__singer_image_path = ''

    def validate_info(self):
        self.__singer_name = self.singer_name_line.text()
        if len(self.__singer_name.strip()) > 0 and len(self.__chosen_path) > 0:
            self.accept()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("You have to chose file location and enter the singer name")
            msg.exec_()

    def select_folder_path(self):
        dialog = QtWidgets.QFileDialog(self, 'chose singer songs folder')
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.DirectoryOnly)
        if dialog.exec_() == QtWidgets.QFileDialog.Accepted:
            self.__chosen_path = dialog.selectedFiles()[0]
            self.stores_songs_location_lbl.setText(self.__chosen_path)

    def select_image_path(self):
        dialog = QtWidgets.QFileDialog(self, 'chose singer image folder')
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.AnyFile)
        if dialog.exec_() == QtWidgets.QFileDialog.Accepted:
            self.__singer_image_path = dialog.selectedFiles()[0]
            self.stores_image_location_lbl.setText(self.__singer_image_path)

    def get_stored_location(self):
        return self.__chosen_path

    def get_image_location(self):
        return self.__singer_image_path

    def get_singer_name(self):
        return self.__singer_name.title()

def __Test__():
    app = QtWidgets.QApplication([])
    o = AddSingerDialog()
    o.show()
    app.exec_()

if __name__ == "__main__":
    __Test__()