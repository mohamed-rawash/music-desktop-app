from views import media_playlist_view
from PyQt5 import QtWidgets, QtMultimedia, QtCore
from view_manger.song_view_manger import SongManger
import qdarkstyle


class PlayListManger(media_playlist_view.Ui_Form, QtWidgets.QScrollArea):
    def __init__(self, songs_list: list):
        """
        :param songs:
        [(name, path), (name, path)]
        """
        super(PlayListManger, self).__init__()
        self.setupUi(self)
        self.__songs_info = songs_list
        self.__songs_info.reverse()
        self.__songs_player = []
        for name, path in self.__songs_info:
            self.__songs_player.append(SongManger(name, path))
            self.__songs_player[-1].SongStarted.connect(self.new_song_started)
            self.__songs_player[-1].SongPaused.connect(self.new_song_paused)
            self.__songs_player[-1].SongStoped.connect(self.new_song_Stoped)
            self.playlist_v_layout.insertWidget(0, self.__songs_player[-1])
        self.__shared_player = QtMultimedia.QMediaPlayer()
        self.__shared_player.durationChanged.connect(self.update_duration)
        self.__shared_player.positionChanged.connect(self.update_postion)
        self.__loaded_file_path = ""
        self.__is_paused = False
        self.__current_song = None

    def new_song_started(self, played_song):
        self.__current_song = played_song
        self.__current_song.volume_slider.valueChanged.connect(self.__shared_player.setVolume)
        if self.__is_paused:
            self.__shared_player.play()
            self.__is_paused = False
        else:
            for song in self.__songs_player:
                if not (song is played_song):
                    song.stop()
            song_path = played_song.get_song_path()
            if song_path != self.__loaded_file_path:
                self.__loaded_file_path = song_path
                self.__shared_player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl(f"file:{song_path}")))
                self.__shared_player.play()

    def new_song_paused(self):
        self.__shared_player.pause()
        self.__is_paused = True

    def new_song_Stoped(self):
        self.__shared_player.stop()

    def update_duration(self, duration):
        self.__current_song.time_slider.setRange(0, duration)

    def update_postion(self, postion):
        self.__current_song.time_slider.setValue(postion)

    def kill_all(self):
        self.__shared_player.stop()

def __Test__():
    app = QtWidgets.QApplication([])
    o = PlayListManger([
        ("sample", r"C:\Users\Mohamed\Desktop\sample.mp3"),
        ("sample_1", r"C:\Users\Mohamed\Desktop\sample_1.mp4a"),
        ("sample_2", r"C:\Users\Mohamed\Desktop\sample_2.mp3"),
        ("sample_3", r"C:\Users\Mohamed\Desktop\sample_3.mp3"),
        ("sample_4", r"C:\Users\Mohamed\Desktop\sample_4.mp3"),
        ("sample_5", r"C:\Users\Mohamed\Desktop\sample_5.mp3"),
        ("sample_6", r"C:\Users\Mohamed\Desktop\sample_6.mp3"),
        ("sample_7", r"C:\Users\Mohamed\Desktop\sample_7.mp3"),
        ("sample_8", r"C:\Users\Mohamed\Desktop\sample_8.mp3"),
        ("sample_9", r"C:\Users\Mohamed\Desktop\sample_9.mp3"),
    ])
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    o.show()
    app.exec_()

if __name__ == "__main__":
    __Test__()
