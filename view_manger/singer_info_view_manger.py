from PyQt5 import QtWidgets, QtGui
from views import singer_info_view
import os


class SingerInfoManger(singer_info_view.Ui_Form, QtWidgets.QWidget):
    def __init__(self, singer_name: str, songs_num: int, image_path: str = "none"):
        super(SingerInfoManger, self).__init__()
        self.setupUi(self)
        self.set_singer_info(singer_name, songs_num, image_path)

    def set_singer_image(self, image_path: str):
        if os.path.isfile(image_path):
            pix_map = QtGui.QPixmap(image_path)
            self.singer_image_lbl.setPixmap(pix_map)
        else:
            pix_map = QtGui.QPixmap(":/icons/icons/icons8-person-80.png")
            self.singer_image_lbl.setPixmap(pix_map)

    def set_singer_name(self, singer_name: str):
        self.singer_name_lbl.setText(singer_name.title())

    def set_num_of_songs(self, songs_num: int):
        self.songs_num_lbl.setText(str(songs_num))

    def set_singer_info(self, singer_name: str, songs_num: int, image_path: str = "none"):
        if image_path == "none":
            pix_map = QtGui.QPixmap(":/icons/icons/icons8-person-80.png")
            self.singer_image_lbl.setPixmap(pix_map)
        else:
            self.set_singer_image(image_path)

        self.set_singer_name(singer_name)
        self.set_num_of_songs(songs_num)

def __Test__():
    app = QtWidgets.QApplication([])
    o = SingerInfoManger("mohamed", "25", r"")
    o.show()
    app.exec_()

if __name__ == "__main__":
    __Test__()
