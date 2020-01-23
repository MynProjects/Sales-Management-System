from PyQt5.QtWidgets import QWidget
from msg_template_ui import Ui_NotifMsgWidget


class NotifMsgTemplate(QWidget):
    """
    This class is the template for the notification message
    """

    def __init__(self, date_time, msg_title, section, select_notif_msg_row, msg_index, del_func, filename):
        #argument: str, str, str, func, int, func, str
        super().__init__()
        self.ui = Ui_NotifMsgWidget()
        self.ui.setupUi(self)
        self.ui.notifDateTimeLabel.setText(date_time)
        self.ui.notifMsgPreviewLabel.setText(msg_title)
        self.select_notif_msg_row = select_notif_msg_row
        self.msg_index = msg_index
        self.filename = filename
        # connect widgets to methods
        self.ui.deleteMsgFromListButton.clicked.connect(lambda: del_func(date_time, section, filename))

    def mousePressEvent(self, event):
        self.select_notif_msg_row(self.msg_index, self.filename)
