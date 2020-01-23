import os, sys, time, datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QSplashScreen, QProgressBar, QStyleFactory
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from login_ui import Ui_LoginMainWindow
from threaded_functions import LoginThread
from sms_main import SMS


class Login(QMainWindow):
    """
    This method logs into SMS
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginMainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        try:
            self.hide_icon = self.resource_path("icons" + os.sep + "hide.png")
            self.show_icon = self.resource_path("icons" + os.sep + "show.png")
        except:
            pass
        self.password_hidden = True
        # connect the buttons to their functions
        self.ui.hideShowPasswordButton.clicked.connect(self.hide_show_password)
        self.ui.loginButton.clicked.connect(self.login_to_sms)
        self.ui.usernameLineEdit.returnPressed.connect(self.login_to_sms)
        self.ui.passwordLineEdit.returnPressed.connect(self.login_to_sms)
        self.ui.cancelButton.clicked.connect(self.close)
        # connect signals to functions
        self.login_thread = LoginThread()
        self.login_thread.login_success_signal.connect(self.login_to_sms_success)
        self.login_thread.login_error_signal.connect(self.login_to_sms_error)
        # create days and months tuples
        self.days_list = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
        self.months_list = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
                            "Aug", "Sep", "Oct", "Nov", "Dec")

    def hide_show_password(self):
        """
        This method hides the password
        """
        try:
            if self.password_hidden:
                self.ui.passwordLineEdit.setEchoMode(QLineEdit.Normal)
                self.ui.hideShowPasswordButton.setIcon(QIcon(self.hide_icon))
                self.ui.hideShowPasswordButton.setToolTip("Hide Password")
                self.password_hidden = False
            else:
                self.ui.passwordLineEdit.setEchoMode(QLineEdit.Password)
                self.ui.hideShowPasswordButton.setIcon(QIcon(self.show_icon))
                self.ui.hideShowPasswordButton.setToolTip("Show Password")
                self.password_hidden = True
        except:
            pass

    def login_to_sms(self):
        """
        This method calls the thread that logs the user into SMS
        """
        username = self.ui.usernameLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        date_time = self.get_cur_date_time()
        if username.strip() != "" and password.strip() != "":
            if os.path.exists(self.resource_path("data_files" + os.sep + "date_time_checker.txt")):
                # check if the time of sale is valid before submitting the registration
                date_valid, cur_date, year = self.verify_date_time(date_time)
                if date_valid:
                    # disable the login button before login
                    self.ui.loginButton.setDisabled(True)
                    self.login_thread.set_parameters(username, password, date_time)
                    self.login_thread.start()
                    # update the date time checker
                    self.update_date_time_checker(date_time)
                else:
                    QMessageBox.critical(self, "Error", "Invalid date and time.\nPlease set system date and time.")
            else:
                # disable the login button before login
                self.ui.loginButton.setDisabled(True)
                self.login_thread.set_parameters(username, password, date_time)
                self.login_thread.start()
                # update the date time checker
                self.update_date_time_checker(date_time)
        else:
            QMessageBox.critical(self, "Error", "Provide both username and password!")

    def login_to_sms_success(self, login_success_signal):
        """
        This method receives the success signal from the login thread
        """
        self.ui.loginButton.setEnabled(True)
        # hide this window
        self.hide()
        # login to sms main window
        username, password = login_success_signal
        # show splash screen
        img = QPixmap(self.resource_path("icons" + os.sep + "sms_icon900x900.png"))
        img = img.scaled(300, 300)
        splash_screen = QSplashScreen(img)
        # adding progress bar to splash screen
        progressBar = QProgressBar(splash_screen)
        progressBar.setMaximum(10)
        progressBar.setValue(0)
        progressBar.setTextVisible(False)
        progressBar.setStyleSheet("QProgressBar {border-radius: 5px;background-color: #63b946;}QProgressBar::chunk {border: 1px solid white;border-radius: 5px;background-color: white;}")
        progressBar.setGeometry(50, img.height() - 5, img.width() - 100, 5)
        progressBar.show()
        QApplication.processEvents()
        # continue preparing progressbar
        splash_screen.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        splash_screen.show()
        QApplication.processEvents()
##        splash_screen.showMessage("<h3><font color='white'>Loading Resources ...</font></h3>", Qt.AlignTop, Qt.white)
        # open sms main window
        self.sms_main_window = SMS()
        self.sms_main_window.get_login_data(self, username, password)
        QApplication.processEvents()
        for i in range(1, 11):
            progressBar.setValue(i)
            time.sleep(1)
            QApplication.processEvents()
        # close splash screen
        splash_screen.close()
        # show main window
        self.sms_main_window.show()
        # clear the username and password fields and close the login window
        self.ui.usernameLineEdit.clear()
        self.ui.passwordLineEdit.clear()
        # set the focus to the username field
        self.ui.usernameLineEdit.setFocus(True)
        self.close()

    def login_to_sms_error(self, login_error_signal):
        """
        This method receives the error signal from the login thread
        """
        self.ui.loginButton.setEnabled(True)
        if login_error_signal == "wrong_credentials":
            QMessageBox.critical(self, "Error", "Wrong credentials!")
        else:
            QMessageBox.critical(self, "Error", "Login failed!")

    def get_cur_date_time(self):
        """
        This method gets the current date and time in the format that the app stores for reference
        """
        # get the current time
        date_time = time.localtime()
        # get the date and time values
        year = str(date_time.tm_year)
        month = self.months_list[date_time.tm_mon-1]
        day_of_month = str(date_time.tm_mday)
        day_of_week = self.days_list[date_time.tm_wday]
        hour = str(date_time.tm_hour)
        minute = str(date_time.tm_min)
        if len(minute) < 2:
            minute = "0" + minute
        date = day_of_week + ", " + month + " " + day_of_month + ", " + year
        _time = hour + ":" + minute
        date_time = date + "  " + _time + " GMT"
        return date_time

    def update_date_time_checker(self, date_time):  #argument: str
        """
        This method updates the date and time of the most recent sale
        """
        try:
            checker_file_path = self.resource_path("data_files" + os.sep + "date_time_checker.txt")
            checker_file = open(checker_file_path, 'w')
            checker_file.write(date_time)
            checker_file.close()
        except:
            pass

    def parse_date_time(self, date_time):   #argument: str
        """
        This method parses date and time string
        """
        date_time = date_time.replace(",", "")
        day_of_week, month, day_of_month, year, time, gmt = date_time.split()
        month = self.months_list.index(month) + 1
        hour, minute = time.split(":")
        return [int(year), month, int(day_of_month), int(hour), int(minute)]

    def verify_date_time(self, date_time):  #argument: str
        """
        This method verifies if the date and time of a sale is valid
        """
        # set a variable to hold bool for time validity
        time_valid = False
        # set a list to hold the current date if the current date is greater than the previous one
        cur_date = []
        try:
            # parse the time of the current sale
            year, month, day_of_month, hour, minute = self.parse_date_time(date_time)
            # get and parse the time of the previous sale
            checker_file_path = self.resource_path("data_files" + os.sep + "date_time_checker.txt")
            checker_file = open(checker_file_path, 'r')
            prev_date_time = checker_file.read()
            checker_file.close()
            prev_year, prev_month, prev_day_of_month, prev_hour, prev_minute = self.parse_date_time(prev_date_time)
            # verify date and time
            date = datetime.date(year, month, day_of_month)
            prev_date = datetime.date(prev_year, prev_month, prev_day_of_month)
            _time = datetime.time(hour, minute)
            prev_time = datetime.time(prev_hour, prev_minute)
            if date > prev_date:
                time_valid = True
                cur_date = [year, month, day_of_month]
            elif date == prev_date:
                if _time >= prev_time:
                    time_valid = True
        except:
            time_valid = False
        return (time_valid, cur_date, year)

    def resource_path(self, relative_path):  # argument types: String
        """
        This method genrates the relative paths to all the resources used in the application
        including image files, source file, media files and what have you. It is very
        necessary because it preserves the path to the resources after producing the
        executable for the application
        """
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)
            


if __name__ == "__main__":
    # set the GUI style
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    # start the application
    app = QApplication(sys.argv)
    sms_login = Login()
    sms_login.show()
    sys.exit(app.exec_())
