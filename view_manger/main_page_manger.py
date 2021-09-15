import os

from PyQt5 import QtWidgets, QtGui, QtCore
from views import main_page_view
from view_manger.add_singer_dialog import AddSingerDialog
from view_manger.singer_page_view_manger import SingerPageManger
from models import SongLoader
import qdarkstyle

class MainPageManger(QtWidgets.QWidget, main_page_view.Ui_Form):
    MoveToSinger = QtCore.pyqtSignal(object)
    LogOut = QtCore.pyqtSignal(object)
    def __init__(self, user_id):
        super(MainPageManger, self).__init__()
        self.setupUi(self)
        self.__current_user_id = user_id
        #install signals
        self.add_singer_btn.clicked.connect(self.display_add_singer_dialog)
        self.log_out_btn.clicked.connect(self.log_out)
        self.__song_counter = -1
        self.__singer_buttons_container = []
        #load songs
        for singer_name, singer_image in SongLoader.get_singers(self.__current_user_id):
            self.add_new_song(singer_name, singer_image)

    def display_add_singer_dialog(self):
        add_dialog = AddSingerDialog()
        if add_dialog.exec_():
            singer_name = add_dialog.get_singer_name()
            singer_image_path = add_dialog.get_image_location()
            singer_songs_path = add_dialog.get_stored_location()
            songs = []
            for file_name in os.listdir(singer_songs_path):
                if file_name.endswith(".mp3"):
                    mp3_file_path = os.path.join(singer_songs_path, file_name)
                    songs.append(mp3_file_path)
            SongLoader.add_new_singer(self.__current_user_id, singer_name, singer_image_path, songs)
            self.add_new_song(singer_name, singer_image_path)

    def add_new_song(self, singer_name: str, singer_image_path: str):
        self.__song_counter += 1
        row_count = self.__song_counter // 4
        col_count = self.__song_counter % 4
        tool_btn = QtWidgets.QToolButton(self)
        tool_btn.setMinimumSize(QtCore.QSize(150, 170))
        tool_btn.setMaximumSize(QtCore.QSize(150, 170))
        tool_btn.setText(singer_name.title())
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(singer_image_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tool_btn.setIcon(icon)
        tool_btn.setIconSize(QtCore.QSize(150, 150))
        tool_btn.setAutoRaise(True)
        tool_btn.setObjectName("tool_btn")
        tool_btn.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.singer_buttons_layout.addWidget(tool_btn, row_count, col_count)
        self.__singer_buttons_container.append(tool_btn)
        self.__singer_buttons_container[-1].clicked.connect(self.lamda_factory(self.__song_counter))

    def lamda_factory(self, counter):
        return lambda: self.load_songs(counter)

    def load_songs(self, singer_id):
        singer_name, singer_image_path, songs = SongLoader.get_songs_list(self.__current_user_id, singer_id)
        self.__singer_page_manger = SingerPageManger(singer_name, songs, singer_image_path)
        self.MoveToSinger.emit(self.__singer_page_manger)

    def log_out(self):
        self.LogOut.emit(self.__current_user_id)



def __Test__():
    app = QtWidgets.QApplication([])
    o = MainPageManger("1")
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    o.show()
    app.exec_()

if __name__ == "__main__":
    __Test__()