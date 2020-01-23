import os, sys, numpy
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QCompleter, QStyleFactory
from PyQt5.QtCore import Qt
from all_items_ui import Ui_AllItemsMainWindow
from threaded_functions import ViewAllItems


class ViewAllItemsWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_AllItemsMainWindow()
        self.ui.setupUi(self)
        # variable to hold the items data
        self.items = []
        # get all the items
        self.get_all_items()
        # connect methods to buttons
        self.ui.salesLoadTableButton.clicked.connect(self.get_all_items)
        self.ui.itemSearchButton.clicked.connect(self.search_item)
        self.ui.itemSearchField.returnPressed.connect(self.search_item)

    def get_all_items(self):
        """
        This method starts the thread that gets all the items from the database
        """
        self.view_all_items_thread = ViewAllItems()
        self.view_all_items_thread.view_all_items_success_signal.connect(self.get_all_items_success)
        self.view_all_items_thread.view_all_items_error_signal.connect(self.get_all_items_error)
        self.view_all_items_thread.start()

    def get_all_items_success(self, get_all_items_success_signal): #argument: list
        """
        This method gets the success signal from the get all items thread
        """
        self.sort_items(get_all_items_success_signal)
        # set the auto completion data for the search field
        item_names = []
        for row in get_all_items_success_signal:
            item_names.append(row[0])
        self.search_autocomplete_data(item_names)

    def get_all_items_error(self, get_all_items_error_signal): # argument: str
        """
        This method gets the error signal from the get all items thread
        """
        pass

    def search_autocomplete_data(self, auto_completion_data): #argument: list
        """
        This method sets the auto completion data into the search field
        """
        auto_completion_data = list(set(auto_completion_data))
        completer = QCompleter(auto_completion_data, self.ui.itemSearchField)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.itemSearchField.setCompleter(completer)

    def sort_items(self, items_data): # argument: list
        """
        This method sorts the items data
        """
        # sort items by name
        items_list = []
        items_names = []
        for row in items_data:
            items_names.append(row[0])
        items_array = numpy.array(items_names, dtype=str)
        sorted_items_array = numpy.argsort(items_array)
        for index in sorted_items_array:
            items_list.insert(0, items_data[index])
        # add items to table widget
        self.ui.itemsTableWidget.setRowCount(0)
        for row in items_list:
            self.add_row_to_items_table_widget(row[0], row[1], row[2])
            QApplication.processEvents()
        # set the items list
        items_list.reverse()
        self.items = items_list

    def search_item(self):
        """
        This method searches for an item
        """
        # get the text to search and search column index
        item_to_search = self.ui.itemSearchField.text().strip()
        search_column_index = 0
        match_found = False     # notify for a match
        punc_chars = ["/", ",", ".", ";", "\\", "\\\\", "?", "!", ":", "*", "#"]
        # remove punctuation symbols from the item to be searched
        for ch in punc_chars:
            item_to_search = item_to_search.replace(ch, "")     # remove all puntuation marks before search
            item_to_search = item_to_search.replace("  ", " ")   # replace double spaces with single spaces
        if item_to_search.strip() != "":
            if self.ui.itemsTableWidget.rowCount() > 0:
                try:
                    # create a search data list to hold the list of items that serve as the dictionary
                    search_data_list = []
                    # extract the item descriptions from the items table data
                    for row in self.items:
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
                            name_item = self.ui.itemsTableWidget.takeItem(row_index_of_item, 0)
                            qty_item = self.ui.itemsTableWidget.takeItem(row_index_of_item, 1)
                            price_item = self.ui.itemsTableWidget.takeItem(row_index_of_item, 2)
                            # add all the selected rows with their items to a list
                            selected_rows.append([name_item, qty_item, price_item])
                        # remove the selected rows from their previous positions
                        for row_index_of_item in row_indices_of_items:
                            if row_shift_count == 0:
                                self.ui.itemsTableWidget.removeRow(row_index_of_item)
                                self.items.pop(row_index_of_item)
                                row_shift_count += 1
                            else:
                                try:
                                    self.ui.itemsTableWidget.removeRow(row_index_of_item - row_shift_count)
                                    self.items.pop(row_index_of_item - row_shift_count)
                                    row_shift_count += 1
                                except:
                                    self.ui.itemsTableWidget.removeRow(row_index_of_item)
                                    self.items.pop(row_index_of_item)
                                    row_shift_count += 1
                        # reverse the selected rows so as to obtain the same order after adding to the table
                        selected_rows.reverse()
                        # clear the table of the other data which are not included in the search results.
                        # this is to ensure that only the search results are displayed in the table
                        self.ui.itemsTableWidget.setRowCount(0)
                        self.items.clear()
                        # get the selected rows to the top and rearrange the table
                        for row in selected_rows:
                            row_data = (row[0].text(), int(row[1].text()), float(row[2].text()))
                            self.items.insert(0, row_data)
                        # sort the table data according to the present sorting parameter selected
                        self.sort_items(self.items)
                    else:
                        QMessageBox.information(self, 'Done', item_to_search + " not found!!!")
                except ValueError:
                    QMessageBox.information(self, 'Done', item_to_search + " not found!!!")
            else:
                QMessageBox.information(self, 'Done', item_to_search + " not found!!!")
        else:
            QMessageBox.information(self, 'Alert', "No search query has been provided!!!")

    def add_row_to_items_table_widget(self, name, price, qty):  #argument: str, float, int
        """
        This method adds a row to the items table widget
        """
        # add the item to the cart table
        self.ui.itemsTableWidget.insertRow(0)
        desc_item = QTableWidgetItem(name)
        qty_item = QTableWidgetItem(str(qty))
        price_item = QTableWidgetItem("{0:.2f}".format(float(price)))
        # make rows uneditable
        desc_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        qty_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        price_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        # add the table widget items to the table
        self.ui.itemsTableWidget.setItem(0, 0, desc_item)
        self.ui.itemsTableWidget.setItem(0, 1, qty_item)
        self.ui.itemsTableWidget.setItem(0, 2, price_item)


if __name__=="__main__":
    # set the GUI style
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    # start the application
    app  = QApplication(sys.argv)
    view_all_items_window = ViewAllItemsWindow()
    view_all_items_window.show()
    sys.exit(app.exec_())
