from views import song_view
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtMultimedia import *
import qdarkstyle

class SongManger(song_view.Ui_Form, QtWidgets.QWidget):
    SongStarted = QtCore.pyqtSignal(object)
    SongPaused = QtCore.pyqtSignal(object)
    SongStoped = QtCore.pyqtSignal(object)
    def __init__(self, song_name: str, song_path: str):
        super(SongManger, self).__init__()
        self.setupUi(self)
        self.song_name_lpl.setText(song_name)
        self.__song_name = song_name
        self.__song_path = song_path
        self.player = QMediaPlayer()
        self.play_pause_btn.clicked.connect(self.play_pause)
        #set all slider and volume control invisable state
        self.time_slider.setVisible(False)
        self.volume_slider.setVisible(False)
        self.is_runinig = False

    def get_song_path(self) -> str:
        return  self.__song_path

    def play_pause(self):
        if self.is_runinig:
            self.pause()
        else:
            self.play()
        self.is_runinig = not self.is_runinig

    def play(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/paus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_pause_btn.setIcon(icon)
        self.play_pause_btn.setIconSize(QtCore.QSize(45, 45))
        self.play_pause_btn.setAutoRaise(True)
        self.time_slider.setVisible(True)
        self.volume_slider.setVisible(True)
        self.SongStarted.emit(self)

    def stop(self):
        self.time_slider.setVisible(False)
        self.volume_slider.setVisible(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/play_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_pause_btn.setIcon(icon)
        self.play_pause_btn.setIconSize(QtCore.QSize(45, 45))
        self.play_pause_btn.setAutoRaise(True)
        self.SongStoped.emit(self)
        self.is_runinig = False

    def pause(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/play_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_pause_btn.setIcon(icon)
        self.play_pause_btn.setIconSize(QtCore.QSize(45, 45))
        self.play_pause_btn.setAutoRaise(True)
        self.SongPaused.emit(self)

    def update_duration(self, duration):
        self.time_slider.setRange(0, duration)

    def update_postion(self, postion):
        self.time_slider.setValue(postion)

def __Test__():
    app = QtWidgets.QApplication([])
    o = SongManger("moahemd",r"C:\Users\Mohamed\Desktop\sample.mp3")
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    o.show()
    app.exec_()

if __name__ == "__main__":
    __Test__()