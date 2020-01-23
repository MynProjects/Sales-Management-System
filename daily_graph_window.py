import os, sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import Qt
from daily_graph_window_ui import Ui_DailyGraphMainWindow
from display_graph import DisplayGraphDialog


class DailyGraphWindow(QMainWindow):

    def __init__(self, x_vals, y_vals, overall_total_income, graph_type, fig_index, month, year):
        # argument: list(int), list(float), float, str, int, str, str
        super().__init__()
        self.ui = Ui_DailyGraphMainWindow()
        self.ui.setupUi(self)
        self.win_title = month + " " + year
        if graph_type == "line_graph":
            self.win_title = "Daily Sales Line Graph - " + month + " " + year
        else:
            self.win_title = "Daily Sales Bar Chart - " + month + " " + year
        self.setWindowTitle(self.win_title)
        # initialize variables
        self.x_vals = x_vals
        self.y_vals = y_vals
        self.overall_total_income = overall_total_income
        self.graph_type = graph_type
        self.fig_path = self.resource_path("data_files" + os.sep + "figures" + os.sep + \
                                           "figure" + str(fig_index) + ".png")
        # display the overall gross income
        self.ui.grossIncomeLabel.setText("GROSS INCOME: GH₵ " + "{0:.2f}".format(overall_total_income))
        # populate the table widget
        self.populate_table_widget()
        # add show function to view button
        self.ui.viewGraphButton.clicked.connect(self.show_graph)

    def populate_table_widget(self):
        """
        This method adds rows to the table widget
        """
        for i in range(0, len(self.x_vals)):
            # add the item to the cart table
            self.ui.graphDataTableWidget.insertRow(i)
            day_item = QTableWidgetItem(str(self.x_vals[i]))
            income_item = QTableWidgetItem("{0:.2f}".format(self.y_vals[i]))
            # make rows uneditable
            day_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            income_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            # add the table widget items to the table
            self.ui.graphDataTableWidget.setItem(i, 0, day_item)
            self.ui.graphDataTableWidget.setItem(i, 1, income_item)
            QApplication.processEvents()

    def show_graph(self):
        """
        This method shows the graph
        """
        self.display_graph_dialog = DisplayGraphDialog(self.win_title, self.fig_path)
        self.display_graph_dialog.show()

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

    def closeEvent(self, event):
        """
        This method wraps up everything before the app closes
        """
        try:
            #delete the figure
            os.remove(self.fig_path)
        except:
            pass
