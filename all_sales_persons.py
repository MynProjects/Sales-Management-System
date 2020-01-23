import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QStyleFactory
from PyQt5.QtCore import Qt
from all_sales_persons_ui import Ui_AllSalesPersonsDialog
from threaded_functions import ViewAllSalesPersons
from login_records import LoginRecords


class ViewAllSalesPersonsDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_AllSalesPersonsDialog()
        self.ui.setupUi(self)
        # variable to hold the sales persons data
        self.get_all_sales_persons()
        # connect widgets to methods
        self.ui.refreshButton.clicked.connect(self.get_all_sales_persons)
        self.ui.loginRecordsButton.clicked.connect(self.open_login_records_window)

    def get_all_sales_persons(self):
        """
        This method starts the thread that gets all the sales persons from the database
        """
        self.view_all_sales_persons_thread = ViewAllSalesPersons()
        self.view_all_sales_persons_thread.view_all_sales_persons_success_signal.connect(self.get_all_sales_persons_success)
        self.view_all_sales_persons_thread.view_all_sales_persons_error_signal.connect(self.get_all_sales_persons_error)
        self.view_all_sales_persons_thread.start()

    def get_all_sales_persons_success(self, get_all_sales_persons_success_signal): #argument: list
        """
        This method gets the success signal from the get all sales persons thread
        """
        self.sort_sales_persons(get_all_sales_persons_success_signal)

    def get_all_sales_persons_error(self, get_all_sales_persons_error_signal): # argument: str
        """
        This method gets the error signal from the get all sales persons thread
        """
        pass

    def sort_sales_persons(self, sales_persons_data): # argument: list
        """
        This method sorts the sales persons data
        """
        # sort items by name
        sales_persons_names = []
        for row in sales_persons_data:
            name = row[0]
            if name.lower() != "admin":
                sales_persons_names.append(name)
        sales_persons_names.sort()
        sales_persons_names.reverse()
        # add items to table widget
        self.ui.salesPersonsTableWidget.setRowCount(0)
        for name in sales_persons_names:
            self.add_row_to_sales_persons_table_widget(name)
            QApplication.processEvents()

    def add_row_to_sales_persons_table_widget(self, name):  #argument: str
        """
        This method adds a row to the sales persons table widget
        """
        # add the item to the cart table
        self.ui.salesPersonsTableWidget.insertRow(0)
        name_item = QTableWidgetItem(name)
        # make rows uneditable
        name_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        # add the table widget items to the table
        self.ui.salesPersonsTableWidget.setItem(0, 0, name_item)

    def open_login_records_window(self):
        """
        This method opens the login records window
        """
        self.login_records_window = LoginRecords()
        self.login_records_window.show()


if __name__=="__main__":
    # set the GUI style
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    # start the application
    app = QApplication(sys.argv)
    all_sales_persons_dialog = ViewAllSalesPersonsDialog()
    all_sales_persons_dialog.show()
    sys.exit(app.exec_())
