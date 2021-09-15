from PyQt5 import QtWidgets, QtCore
from views import singer_page_view
from view_manger.playlist_view_manger import PlayListManger
from view_manger.singer_info_view_manger import SingerInfoManger

import qdarkstyle



class SingerPageManger(singer_page_view.Ui_Form, QtWidgets.QWidget):
    def __init__(self, singer_name: str, songs: list, image_path: str = "none"):
        super(SingerPageManger, self).__init__()
        self.setupUi(self)
        self.playlist_manger = PlayListManger(songs)
        self.singer_info_manger = SingerInfoManger(singer_name, len(songs), image_path)
        self.page_singer_info_layout.addWidget(self.singer_info_manger)
        self.page_playlist_layout.addWidget(self.playlist_manger)

    def kill(self):
        self.playlist_manger.kill_all()

def __Test__():
    app = QtWidgets.QApplication([])
    songs = [
        ("sample", r"C:\Users\Mohamed\Desktop\sample.mp3"),
        ("sample_1", r"C:\Users\Mohamed\Desktop\sample_1.mp3"),
    ]
    o = SingerPageManger("mohamed", songs, "")
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    o.show()
    app.exec_()

if __name__ == "__main__":
    __Test__()