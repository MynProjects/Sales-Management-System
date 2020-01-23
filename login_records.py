import sys, numpy, datetime, time
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QStyleFactory, QMessageBox, QCompleter
from PyQt5.QtCore import Qt
from login_records_ui import Ui_LoginRecordsWindow
from threaded_functions import LoadLoginRecordsThread


class LoginRecords(QMainWindow):
    """
    This class shows all the login records
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginRecordsWindow()
        self.ui.setupUi(self)
        # hide the search date widget
        self.search_param_effect()
        # initialize the login records list
        self.login_records = []
        # create days and months tuples
        self.days_list = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
        self.months_list = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
        # initialize external classes
        self.initialize_external_classes()
        # connect method to signals
        self.connect_methods_to_signals()
        # connect widgets to methods
        self.connect_widgets_to_methods()
        # set the year to the current year
        cur_date_time = time.localtime()
        cur_year = cur_date_time.tm_year
        self.ui.yearSpinBox.setValue(cur_year)
        # load all the login records
        self.load_login_records()

    def initialize_external_classes(self):
        """
        This method initializes external classes
        """
        self.load_login_records_thread = LoadLoginRecordsThread()

    def connect_methods_to_signals(self):
        """
        This method connects methods to signals from external classes
        """
        self.load_login_records_thread.load_login_records_success_signal.connect(self.load_login_records_success)
        self.load_login_records_thread.load_login_records_error_signal.connect(self.load_login_records_error)

    def connect_widgets_to_methods(self):
        """
        The method connects the widgets to their methods
        """
        self.ui.loginRecordsSearchParamComboBox.currentTextChanged.connect(self.search_param_effect)
        self.ui.loginRecordsLoadTableButton.clicked.connect(self.load_login_records)
        self.ui.loginRecordsFlipTableButton.clicked.connect(self.flip_login_records_table)
        self.ui.loginRecordsSortComboBox.currentTextChanged.connect(self.sort_login_records)
        self.ui.yearSpinBox.valueChanged.connect(self.load_login_records)
        self.ui.loginRecordsSearchButton.clicked.connect(self.search_login_records)
        self.ui.loginRecordsSearchField.returnPressed.connect(self.search_login_records)

    def search_param_effect(self):
        """
        This method reacts to the selected search parameter
        """
        selected_text = self.ui.loginRecordsSearchParamComboBox.currentText().lower().strip()
        if selected_text == "search by:":
            self.ui.loginRecordsSearchField.show()
            self.ui.monthComboBox.hide()
            self.ui.loginRecordsSearchField.setPlaceholderText("Type query here")
        elif selected_text == "username":
            self.ui.loginRecordsSearchField.show()
            self.ui.monthComboBox.hide()
            self.ui.loginRecordsSearchField.setPlaceholderText("Type username here")
        elif selected_text == "month":
            self.ui.loginRecordsSearchField.hide()
            self.ui.monthComboBox.show()

    def load_login_records(self):
        """
        This method calls the thread that loads all the login records
        """
        year = self.ui.yearSpinBox.value()
        self.load_login_records_thread.set_parameters(year)
        self.load_login_records_thread.start()

    def load_login_records_success(self, load_login_records_success_signal):
        """
        This method gets the success signal from the load all login records thread
        """
        self.login_records = load_login_records_success_signal
        self.sort_login_records()

    def load_login_records_error(self, load_login_records_error_signal):
        """
        This method gets the error signal from the load all login records thread
        """
        QMessageBox.critical(self, "Error", "Failed to load login records!")

    def sort_login_records(self):
        """
        This method sorts the login records according to the selected parameter
        """
        param = self.ui.loginRecordsSortComboBox.currentText().lower().strip()
        if param == "username":
            self.sort_by_username()
        else:
            self.sort_by_login_time()
        # create list to hold usernames for autocompletion
        autocompletion_data = []
        # clear the table
        self.ui.loginRecordsTableWidget.setRowCount(0)
        # add the sorted data to the table
        for row in self.login_records:
            name = row[0]
            login_time = row[1]
            self.add_row_to_login_records_table_widget(0, name, login_time)
            autocompletion_data.append(name.upper())
            QApplication.processEvents()
        # reverse table data to get the same order as in the table
        self.login_records.reverse()
        # set the autocompletion data
        self.search_autocomplete_data(autocompletion_data)

    def sort_by_username(self):
        """
        This method sorts the login records by username
        """
        # get the sorting data in the table
        list_of_data = []
        col_index = 0
        for row in self.login_records:
            list_of_data.append(row[col_index])
        # put the sorting data in a numpy array
        array_of_data = numpy.array(list_of_data, dtype=str)
        # sort the data in alphabetical order and get the indices of their rows
        sorted_data_indices = numpy.argsort(array_of_data)
        # create a copy of the table data
        table_data_copy = self.login_records.copy()
        # clear the table data
        self.login_records.clear()
        # set the table data in the sorted form
        for index in sorted_data_indices:
            self.login_records.insert(0, table_data_copy[index])

    def sort_by_login_time(self):
        """
        This method sorts the login records by time
        """
        # get the sorting data in the table
        list_of_data = []
        col_index = 1
        for row in self.login_records:
            list_of_data.append(row[col_index])
        # get the login time into and datetime object
        list_of_login_date_time = []
        for login_time in list_of_data:
            year, month, day_of_month, hour, minute = self.parse_date_time(login_time)
            date_time = datetime.datetime(year, month, day_of_month, hour, minute)
            list_of_login_date_time.append(date_time)
        # create copy of the login datetime objects list
        list_of_login_date_time_copy = list_of_login_date_time.copy()
        # sort the login datetime and get the sorted indices
        list_of_login_date_time_copy.sort()
        list_of_login_date_time_sorted_indices = []
        for date_time in list_of_login_date_time_copy:
            index = list_of_login_date_time.index(date_time)
            list_of_login_date_time_sorted_indices.append(index)
        # copy the login records data and clear it
        login_records_copy = self.login_records.copy()
        self.login_records.clear()
        # add the sorted data to the login records list
        for index in list_of_login_date_time_sorted_indices:
            self.login_records.insert(0, login_records_copy[index])

    def search_autocomplete_data(self, auto_completion_data): #argument: list
        """
        This method sets the auto completion data into the search field
        """
        auto_completion_data = list(set(auto_completion_data))
        completer = QCompleter(auto_completion_data, self.ui.loginRecordsSearchField)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.loginRecordsSearchField.setCompleter(completer)

    def search_login_records(self):
        """
        This method searches the records for a query
        """
        # check if a search parameter is selected before proceeding
        if self.ui.loginRecordsSearchParamComboBox.currentText() != "Search By:":
            # get the search parameter
            search_param = self.ui.loginRecordsSearchParamComboBox.currentText()
            item_search_param = search_param.strip().lower()
            # get the text to search and search column index
            item_to_search = ""
            search_column_index = -1
            if item_search_param == "username":
                item_to_search = self.ui.loginRecordsSearchField.text().strip()
                search_column_index = 0
            elif item_search_param == "month":
                item_to_search = self.ui.monthComboBox.currentText().strip()
                search_column_index = 1
            match_found = False     # notify for a match
            punc_chars = ["/", ",", ".", ";", "\\", "\\\\", "?", "!", ":", "*", "#"]
            # remove punctuation symbols from the item to be searched
            for ch in punc_chars:
                item_to_search = item_to_search.replace(ch, "")     # remove all puntuation marks before search
                item_to_search = item_to_search.replace("  ", " ")   # replace double spaces with single spaces
            if item_to_search.strip() != "":
                if self.ui.loginRecordsTableWidget.rowCount() > 0:
                    try:
                        # create a search data list to hold the list of items that serve as the dictionary
                        search_data_list = []
                        if search_column_index >= 0:
                            # extract the item descriptions from the items table data
                            for row in self.login_records:
                                search_data_list.append(row[search_column_index])
                            # remove punctuation symbols from the search list data
                            for item in search_data_list:
                                for ch in punc_chars:
                                    item = item.replace(ch, "")     # remove all puntuation marks before search
                                    item = item.replace("  ", " ")   # replace double spaces with single spaces
                                # split the search item into parts and search for each part
                                query_parts = item_to_search.strip().lower().split()
                                for part in query_parts:
                                    if item.lower().__contains__(part):
                                        match_found = True
                                        break
                            # create object to hold previous index to avoid repetitions
                            prev_index = -1
                            # create object to hold the number of matches found for a single item in the search list
                            # this helps arrange the search results according to the best to least match
                            cur_num_of_matches = 1
                            prev_num_of_matches = 0
                            # if a match is found for the search query, proceed search
                            if match_found:
                                row_indices_of_items = []
                                for index, search_data in enumerate(search_data_list):
                                    for ch in punc_chars:
                                        search_data = search_data.replace(ch, " ")    # remove all puntuation marks before search
                                        search_data = search_data.replace("  ", " ")  # replace double spaces with single spaces
                                    # get the search item and split it into parts and search for each part
                                    query_text = item_to_search.strip().lower()
                                    query_parts = query_text.split()
                                    # use the partial match algorithm else use the exact match algorithm
                                    for part in query_parts:
                                        # if the previous item is not equal to the current item, set the prev index to the
                                        # current one
                                        if search_data.lower().__contains__(part) and prev_index != index:
                                            prev_index = index
                                            # if the number of matches for the current item, is greater than that of the
                                            # previous one, add it the the end of the list else add it to the beginning of
                                            # the list
                                            if cur_num_of_matches > prev_num_of_matches:
                                                row_indices_of_items.append(index)
                                            else:
                                                row_indices_of_items.insert(0, index)
                                        # if the previous item is the same as the current on and another match is found,
                                        # increase the number of matches by 1
                                        if search_data.lower().__contains__(part) and prev_index == index:
                                            cur_num_of_matches += 1
                                        # if the previous item is different from the current one, reset the number of matches to 1
                                        # and set the previous number of matches to the value of the current one
                                        if prev_index != index:
                                            prev_num_of_matches = cur_num_of_matches
                                            cur_num_of_matches = 1
                                # get the the contents of the row
                                selected_rows = []
                                row_shift_count = 0
                                for row_index_of_item in row_indices_of_items:
                                    name_item = self.ui.loginRecordsTableWidget.takeItem(row_index_of_item, 0)
                                    time_item = self.ui.loginRecordsTableWidget.takeItem(row_index_of_item, 1)
                                    # add all the selected rows with their items to a list
                                    selected_rows.append([name_item, time_item])
                                # remove the selected rows from their previous positions
                                for row_index_of_item in row_indices_of_items:
                                    if row_shift_count == 0:
                                        self.ui.loginRecordsTableWidget.removeRow(row_index_of_item)
                                        self.login_records.pop(row_index_of_item)
                                        row_shift_count += 1
                                    else:
                                        try:
                                            self.ui.loginRecordsTableWidget.removeRow(row_index_of_item - row_shift_count)
                                            self.login_records.pop(row_index_of_item - row_shift_count)
                                            row_shift_count += 1
                                        except:
                                            self.ui.loginRecordsTableWidget.removeRow(row_index_of_item)
                                            self.login_records.pop(row_index_of_item)
                                            row_shift_count += 1
                                # reverse the selected rows so as to obtain the same order after adding to the table
                                selected_rows.reverse()
                                # clear the table of the other data which are not included in the search results.
                                # this is to ensure that only the search results are displayed in the table
                                self.ui.loginRecordsTableWidget.setRowCount(0)
                                self.login_records.clear()
                                # get the selected rows to the top and rearrange the table
                                for row in selected_rows:
                                    row_data = (row[0].text(), row[1].text())
                                    self.login_records.insert(0, row_data)
                                # sort the table data according to the present sorting parameter selected
                                self.sort_login_records()
                            else:
                                QMessageBox.information(self, 'Done', item_to_search + " not found!!!")
                        else:
                            QMessageBox.information(self, 'Done', item_to_search + " not found!!!")
                    except ValueError:
                        QMessageBox.information(self, 'Done', item_to_search + " not found!!!")
                else:
                    QMessageBox.information(self, 'Done', item_to_search + " not found!!!")
            else:
                QMessageBox.information(self, 'Alert', "No search query has been provided!!!")
        else:
            QMessageBox.critical(self, "Alert", "Please select a search parameter!")

    def flip_login_records_table(self):
        """
        This method flips/reverses the records table
        """
        # clear the table
        self.ui.loginRecordsTableWidget.setRowCount(0)
        # add the data to the table in the reverse order
        for row in self.login_records:
            name = row[0]
            login_time = row[1]
            self.add_row_to_login_records_table_widget(0, name, login_time)
            QApplication.processEvents()
        # reverse table data to get the same order as in the table
        self.login_records.reverse()

    def add_row_to_login_records_table_widget(self, next_row, username, login_time):
        #argument: int, str, str
        """
        This method adds a row to the login records table widget
        """
        # add the item to the records table
        self.ui.loginRecordsTableWidget.insertRow(next_row)
        name_item = QTableWidgetItem(username)
        time_item = QTableWidgetItem(login_time)
        # make rows uneditable
        name_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        time_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        # add the table widget items to the table
        self.ui.loginRecordsTableWidget.setItem(next_row, 0, name_item)
        self.ui.loginRecordsTableWidget.setItem(next_row, 1, time_item)

    def parse_date_time(self, date_time):   #argument: str
        """
        This method parses date and time string
        """
        date_time = date_time.replace(",", "")
        day_of_week, month, day_of_month, year, time, gmt = date_time.split()
        month = self.months_list.index(month) + 1
        hour, minute = time.split(":")
        return [int(year), month, int(day_of_month), int(hour), int(minute)]


if __name__=="__main__":
    # set the GUI style
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    # start the application
    app = QApplication(sys.argv)
    login_records_window = LoginRecords()
    login_records_window.show()
    sys.exit(app.exec_())
