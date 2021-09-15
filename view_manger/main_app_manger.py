from PyQt5 import QtWidgets
from views import main_app_view
from models import User
from view_manger.main_page_manger import MainPageManger
import qdarkstyle


class MusicWorld(QtWidgets.QMainWindow, main_app_view.Ui_MainWindow):
    def __init__(self):
        super(MusicWorld, self).__init__()
        self.setupUi(self)
        self.login_btn.clicked.connect(self.signin_to_app)
        self.signup_btn.clicked.connect(self.goto_register_win)
        self.back_to_login_btn.clicked.connect(self.goto_login_win)
        self.register_btn.clicked.connect(self.add_new_account)

    def signin_to_app(self):
        user_name = self.user_name_line.text()
        user_password = self.password_line.text()
        if len(user_name) == 0:
            self.display_error("Login Error", "You can't leave user name empty")
            self.user_name_line.setFocus()
            return
        if len(user_password) == 0:
            self.display_error("Login Error", "You can't leave password empty")
            self.password_line.setFocus()
            return
        user = User(user_name, user_password)
        if user.login():
            self.load_user_page(user.get_user_id())
        else:
            self.display_error("Error", "User not define or incorrect password ")

    def goto_register_win(self):
        self.clear_line_edit()
        self.stackedWidget.setCurrentIndex(1)

    def goto_login_win(self):
        self.clear_line_edit()
        self.stackedWidget.setCurrentIndex(0)

    def add_new_account(self):
        user_name = self.reg_user_name_line.text()
        password_1 = self.reg_password_line.text()
        password_2 = self.reg_repassword_line.text()
        if len(user_name) == 0:
            self.display_error("Register Error", "You can't leave user name empty")
            self.user_name_line.setFocus()
            return
        if len(password_1) == 0:
            self.display_error("Register Error", "You can't leave password empty")
            self.reg_user_name_line.setFocus()
            return
        if len(password_1) < 9:
            self.display_error("Register Error", "Password is too short should enter at least 8 char")
            self.reg_user_name_line.setFocus()
            return
        if len(password_2) == 0:
            self.display_error("Register Error", "You have enter password again")
            self.reg_repassword_line.setFocus()
            return
        if password_1 != password_2:
            self.display_error("Register Error", "Password didn't match")
            return
        user = User(user_name, password_1)
        if user.register():
            self.display_info_dialog("Account Created", "Your register successfully")
        else:
            self.display_info_dialog("Account Failed", "Oops something went wrong")


    def display_error(self, title: str, body: str):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle(title)
        msg.setText(body)
        msg.exec_()

    def display_info_dialog(self, title: str, body: str):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle(title)
        msg.setText(body)
        msg.exec_()

    def load_user_page(self, user_id):
        self.main_profile_page = MainPageManger(str(user_id))
        self.main_profile_page.MoveToSinger.connect(self.load_singer_page)
        self.stackedWidget.addWidget(self.main_profile_page)
        self.stackedWidget.setCurrentIndex(2)
        self.main_profile_page.LogOut.connect(self.log_out)



    def load_singer_page(self, widget):
        self.stackedWidget.addWidget(widget)
        self.stackedWidget.setCurrentIndex(3)
        widget.back_btn.clicked.connect(lambda: self.back_to_singers(widget))

    def back_to_singers(self, widget):
        widget.kill()
        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget.removeWidget(widget)
        widget.deleteLater()

    def log_out(self):
        self.stackedWidget.setCurrentIndex(0)
        self.clear_line_edit()

    def clear_line_edit(self):
        self.user_name_line.setText("")
        self.password_line.setText("")
        self.reg_user_name_line.setText("")
        self.reg_password_line.setText("")
        self.reg_repassword_line.setText("")


def __Test__():
    app = QtWidgets.QApplication([])
    o = MusicWorld()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    o.show()
    app.exec_()

if __name__ == "__main__":
    __Test__()