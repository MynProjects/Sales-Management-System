from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
from display_graph_ui import Ui_DisplayGraphDialog


class DisplayGraphDialog(QDialog):
    """
    This class displays the graph
    """

    def __init__(self, win_title, fig_path):
        # argument: str, str
        super().__init__()
        self.ui = Ui_DisplayGraphDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(win_title)
        self.ui.graphLabel.setPixmap(QPixmap(fig_path))
