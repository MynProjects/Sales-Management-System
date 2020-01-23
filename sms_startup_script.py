import os, sys
from PyQt5.QtWidgets import QApplication, QStyleFactory
from login import Login
from startup_login_setup import StartupLoginSetup


def resource_path(relative_path):  # argument types: String
    """
    This method genrates the relative paths to all the resources used in the application
    including image files, source file, media files and what have you. It is very
    necessary because it preserves the path to the resources after producing the
    executable for the application
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


if __name__=="__main__":
    # set the GUI style
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    # start the application
    app = QApplication(sys.argv)
    # check if the firm name exists, if yes, start the application from the login
    # else start it from the login setup
    try:
        firm_name_file = open(resource_path("data_files" + os.sep + "firm_info.txt"), "r")
        data = firm_name_file.read()
        firm_name_file.close()
        if data.strip() != "":
            login_window = Login()
            login_window.show()
        else:
            startup_login_setup_window = StartupLoginSetup()
            startup_login_setup_window.show()
    except:
        startup_login_setup_window = StartupLoginSetup()
        startup_login_setup_window.show()
    sys.exit(app.exec_())
