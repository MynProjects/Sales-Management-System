import sys, os, sqlite3, time, numpy, pickle, datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QStyleFactory, QListWidgetItem,
                             QMessageBox, QTableWidgetItem, QPushButton, QCompleter, QMenu,
                             QAction, QLineEdit)
from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PyQt5.QtGui import (QPixmap, QPainter, QIcon, QFont, QTextDocument, QTextCursor, QTextTableFormat, QPageSize, QMovie)
from PyQt5.QtCore import Qt, QSizeF, QDate
from msg_template import NotifMsgTemplate
from sms_main_ui import Ui_SMSMainWindow
from threaded_functions import (SalesLoadItems, SubmitSalesRecord, UpdateItemQuantity, SalesLoadRecords,
                                LoadCredentialsNames, SalesHistoryLoadRecords, GetDailySalesData, GetMonthlySalesData,
                                GetYearlySalesData, AddSalesPerson, RemoveSalesPerson, EditSalesPerson, EditAdmin,
                                AddNewItem, RemoveItem, EditItem, BackupNow, AutoBackup, UpdateFirmInfo, RestoreData)
from daily_graph_window import DailyGraphWindow
from monthly_graph_window import MonthlyGraphWindow
from yearly_graph_window import YearlyGraphWindow
from all_items import ViewAllItemsWindow
from all_sales_persons import ViewAllSalesPersonsDialog


# this character sequence is used to separate different queries in the backup
# file
query_sep = "<?+/*-=?>"


class SMS(QMainWindow):
    """
    This is the main window for the sales management system
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_SMSMainWindow()
        self.ui.setupUi(self)
        # load the hide and show icons and set hide/show booleans
        try:
            self.hide_icon = self.resource_path("icons" + os.sep + "hide.png")
            self.show_icon = self.resource_path("icons" + os.sep + "show.png")
        except:
            pass
        self.add_sales_person_password_hidden = True
        self.add_sales_person_confirm_password_hidden = True
        self.edit_sales_person_current_password_hidden = True
        self.edit_sales_person_new_password_hidden = True
        self.edit_sales_person_confirm_password_hidden = True
        self.edit_admin_current_password_hidden = True
        self.edit_admin_new_password_hidden = True
        self.edit_admin_confirm_password_hidden = True
        # instantiate all external classes
        self.instantiate_extern_classes()
        # connect methods to their signals
        self.connect_methods_to_signals()
        # connect methods to their widgets
        self.connect_methods_to_widgets()
        # create days and months tuples
        self.days_list = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
        self.months_list = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
                            "Aug", "Sep", "Oct", "Nov", "Dec")
        # create items dictionary, cart list, sales records list, receipt dictionary
        # and credentials names list
        self.items = dict() # {item_name(str): [price(float), quantity(int)]}
        self.cart = []
        self.sales_records = []
        self.receipt_content = dict()
        self.credentials_names = []
        # create a variable to hold the overall sales and the current history sales
        self.sales_cur_day_overall_cost = 0.0
        # create a list to hold the records history
        self.sales_records_history = []
        # create lists to hold the notification message names and info
        self.notif_msgs = [] # names(date and time)
        self.notif_msgs_details = [] # details (date and time, title, section)
        self.notif_filename = ""
        # initialize the variable to store the current search history index for sales
        self.sales_cur_records_history_file_index = -1
        self.sales_history_records_history_file_index = -1
        # create a list to hold the search history file names
        self.list_of_sales_cur_records_history_files = []
        self.list_of_sales_history_records_history_files = []
        # initialize a variable to hold the figure index and dictionary to hold the graph windows
        self.fig_index = 0
        self.graph_windows = dict()
        # hide the notification list widget
        self.ui.notifMsgListWidget.hide()
        # load all startup data
        self.load_data_on_startup()
        # notify that logout has been clicked
        self.logout_clicked = False

    def load_data_on_startup(self):
        """
        This method loads all required data on startup
        """
        # get login name
##        self.get_login_data()
        # load settings
        self.load_settings()
        # load items
        self.sales_load_items()
        # load sales records for current day
        date_time = time.localtime()
        year = date_time.tm_year
        month = date_time.tm_mon
        day_of_month = date_time.tm_mday
        self.ui.salesSearchDateEdit.setDate(QDate(year, month, day_of_month))
        self.ui.recordsSearchDateEdit.setDate(QDate(year, month, day_of_month))
        # load the names of all credentials
        self.load_credentials_names()
        # load today's notifications
        self.load_today_notif_msgs()
        # add menus to view graphs buttons
        self.add_menus_to_view_graphs_btns()
        # load the loading animations
        self.set_loading_anim_to_labels()

    def get_login_data(self, login_window_obj, name="Admin", password="1234"): #argument: Login, str, str
        """
        This method gets the login name
        """
        self.login_window_obj = login_window_obj  # get the login class instance
        self.login_name = name
        self.login_password = password
        # disable settings button if not admin
        if name.strip() != "Admin":
            self.ui.settingsMenuButton.setDisabled(True)

    def instantiate_extern_classes(self):
        """
        This method instantiates all external classes
        """
        # sales
        self.sales_load_items_thread = SalesLoadItems()
        self.submit_sales_record_thread = SubmitSalesRecord()
        self.update_item_qty_thread = UpdateItemQuantity()
        self.sales_load_records_thread = SalesLoadRecords()
        self.load_credentials_names_thread = LoadCredentialsNames()
        # records
        self.sales_history_load_records_thread = SalesHistoryLoadRecords()
        self.get_daily_sales_data_thread = GetDailySalesData()
        self.get_monthly_sales_data_thread = GetMonthlySalesData()
        self.get_yearly_sales_data_thread = GetYearlySalesData()
        # settings
        self.add_sales_person_thread = AddSalesPerson()
        self.remove_sales_person_thread = RemoveSalesPerson()
        self.edit_sales_person_thread = EditSalesPerson()
        self.edit_admin_thread = EditAdmin()
        self.add_new_item_thread = AddNewItem()
        self.remove_item_thread = RemoveItem()
        self.edit_item_thread = EditItem()
        self.backup_now_thread = BackupNow()
        self.auto_backup_thread = AutoBackup()
        self.update_firm_info_thread = UpdateFirmInfo()
        self.restore_data_thread = RestoreData()

    def connect_methods_to_signals(self):
        """
        This method connects methods to signals from external threads
        """
        # sales
        self.sales_load_items_thread.items_success_signal.connect(self.sales_load_items_success)
        self.sales_load_items_thread.items_error_signal.connect(self.sales_load_items_error)
        self.submit_sales_record_thread.submit_sales_success_signal.connect(self.sell_items_success)
        self.submit_sales_record_thread.submit_sales_error_signal.connect(self.sell_items_error)
        self.update_item_qty_thread.update_item_qty_signal.connect(self.update_item_qty)
        self.sales_load_records_thread.sales_load_records_success_signal.connect(self.sales_load_records_success)
        self.sales_load_records_thread.sales_load_records_error_signal.connect(self.sales_load_records_error)
        self.load_credentials_names_thread.load_credentials_names_signal.connect(self.load_credentials_names_success)
        # records
        self.sales_history_load_records_thread.sales_history_load_records_success_signal.connect(self.sales_history_load_records_success)
        self.sales_history_load_records_thread.sales_history_load_records_error_signal.connect(self.sales_history_load_records_error)
        self.get_daily_sales_data_thread.sales_history_view_daily_graphs_success_signal.connect(self.sales_history_view_daily_graphs_success)
        self.get_daily_sales_data_thread.sales_history_view_daily_graphs_error_signal.connect(self.sales_history_view_daily_graphs_error)
        self.get_monthly_sales_data_thread.sales_history_view_monthly_graphs_success_signal.connect(self.sales_history_view_monthly_graphs_success)
        self.get_monthly_sales_data_thread.sales_history_view_monthly_graphs_error_signal.connect(self.sales_history_view_monthly_graphs_error)
        self.get_yearly_sales_data_thread.sales_history_view_yearly_graphs_success_signal.connect(self.sales_history_view_yearly_graphs_success)
        self.get_yearly_sales_data_thread.sales_history_view_yearly_graphs_error_signal.connect(self.sales_history_view_yearly_graphs_error)
        # settings
        self.add_sales_person_thread.add_sales_person_success_signal.connect(self.add_sales_person_success)
        self.add_sales_person_thread.add_sales_person_error_signal.connect(self.add_sales_person_error)
        self.remove_sales_person_thread.remove_sales_person_success_signal.connect(self.remove_sales_person_success)
        self.remove_sales_person_thread.remove_sales_person_error_signal.connect(self.remove_sales_person_error)
        self.edit_sales_person_thread.edit_sales_person_success_signal.connect(self.edit_sales_person_success)
        self.edit_sales_person_thread.edit_sales_person_error_signal.connect(self.edit_sales_person_error)
        self.edit_admin_thread.edit_admin_success_signal.connect(self.edit_admin_success)
        self.edit_admin_thread.edit_admin_error_signal.connect(self.edit_admin_error)
        self.add_new_item_thread.add_new_item_success_signal.connect(self.add_new_item_success)
        self.add_new_item_thread.add_new_item_error_signal.connect(self.add_new_item_error)
        self.remove_item_thread.remove_item_success_signal.connect(self.remove_item_success)
        self.remove_item_thread.remove_item_error_signal.connect(self.remove_item_error)
        self.edit_item_thread.edit_item_success_signal.connect(self.edit_item_success)
        self.edit_item_thread.edit_item_error_signal.connect(self.edit_item_error)
        self.backup_now_thread.backup_now_success_signal.connect(self.backup_now_success)
        self.backup_now_thread.backup_now_error_signal.connect(self.backup_now_error)
        self.auto_backup_thread.auto_backup_success_signal.connect(self.auto_backup_success)
        self.auto_backup_thread.auto_backup_error_signal.connect(self.auto_backup_error)
        self.update_firm_info_thread.update_firm_info_success_signal.connect(self.update_firm_info_success)
        self.update_firm_info_thread.update_firm_info_error_signal.connect(self.update_firm_info_error)
        self.restore_data_thread.restore_data_success_signal.connect(self.restore_data_success)
        self.restore_data_thread.restore_data_error_signal.connect(self.restore_data_error)

    def connect_methods_to_widgets(self):
        """
        This method connects widgets to their respective methods or functions
        """
        # menu
        self.ui.salesMenuButton.clicked.connect(self.switch_to_sales)
        self.ui.notifMenuButton.clicked.connect(self.switch_to_notification)
        self.ui.recordsMenuButton.clicked.connect(self.switch_to_records)
        self.ui.settingsMenuButton.clicked.connect(self.switch_to_settings)
        # sales
        self.ui.salesItemComboBox.currentTextChanged.connect(self.get_selected_item_data)
        self.ui.salesQtyOfItemsSpinBox.valueChanged.connect(self.get_selected_item_data)
        self.ui.addToCartButton.clicked.connect(self.add_to_cart)
        self.ui.removeFromCartButton.clicked.connect(self.remove_from_cart)
        self.ui.reloadItemsButton.clicked.connect(self.sales_load_items)
        self.ui.salesResetAllButton.clicked.connect(self.abort_sale)
        self.ui.sellButton.clicked.connect(self.sell_items)
        self.ui.salesRecordsTableWidget.doubleClicked.connect(self.load_record_into_cart)
        self.ui.salesPrintReceiptButton.clicked.connect(self.sales_print_receipt)
        self.ui.salesSearchDateEdit.dateChanged.connect(self.sales_load_records)
        self.ui.salesLoadTableButton.clicked.connect(self.sales_load_records)
        self.ui.salesFlipTableButton.clicked.connect(self.sales_flip_records_table)
        self.ui.salesSortComboBox.currentTextChanged.connect(self.sales_sort_records_table)
        self.ui.salesSearchParamComboBox.currentTextChanged.connect(self.sales_search_records_param_effect)
        self.ui.salesSearchButton.clicked.connect(self.sales_search_records)
        self.ui.salesSearchField.returnPressed.connect(self.sales_search_records)
        self.ui.salesPrevSearchButton.clicked.connect(self.sales_previous_records_search)
        self.ui.salesNextSearchButton.clicked.connect(self.sales_next_records_search)
        # notification
        self.ui.todayNotifButton.clicked.connect(self.switch_to_today)
        self.ui.historyNotifButton.clicked.connect(self.switch_to_history)
        self.ui.notifMsgListWidget.currentRowChanged.connect(self.show_notif)
        self.ui.todayNotifButton.clicked.connect(self.load_today_notif_msgs)
        self.ui.historyNotifButton.clicked.connect(self.load_notif_history)
        # records
        self.ui.recordsSearchDateEdit.dateChanged.connect(self.sales_history_load_records)
        self.ui.recordsLoadTableButton.clicked.connect(self.sales_history_load_records)
        self.ui.recordsFlipTableButton.clicked.connect(self.sales_history_flip_records_table)
        self.ui.recordsSortComboBox.currentTextChanged.connect(self.sales_history_sort_records_table)
        self.ui.recordsSearchParamComboBox.currentTextChanged.connect(self.sales_history_search_records_param_effect)
        self.ui.recordsSearchButton.clicked.connect(self.sales_history_search_records)
        self.ui.recordsSearchField.returnPressed.connect(self.sales_history_search_records)
        self.ui.recordsPrevSearchButton.clicked.connect(self.sales_history_previous_records_search)
        self.ui.recordsNextSearchButton.clicked.connect(self.sales_history_next_records_search)
        # settings
        self.ui.accountSettingsButton.clicked.connect(self.switch_to_account_settings)
        self.ui.stockSettingsButton.clicked.connect(self.switch_to_stock_settings)
        self.ui.otherSettingsButton.clicked.connect(self.switch_to_other_settings)
        self.ui.addSalesPersonSubmitButton.clicked.connect(self.add_sales_person)
        self.ui.addSalesPersonHideShowPasswordButton.clicked.connect(self.add_sales_person_hide_show_password)
        self.ui.addSalesPersonShowHideConfirmPasswordButton.clicked.connect(self.add_sales_person_hide_show_confirm_password)
        self.ui.removeSalesPersonConfirmButton.clicked.connect(self.remove_sales_person)
        self.ui.removeSalesPersonRevokeButton.clicked.connect(self.remove_sales_person_clear_username_combobox)
        self.ui.editSalesPersonSaveButton.clicked.connect(self.edit_sales_person)
        self.ui.editSalesPerosnCancelButton.clicked.connect(self.edit_sales_person_clear_username_combobox)
        self.ui.editSalesPersonShowHideCurrentPasswordButton.clicked.connect(self.edit_sales_person_hide_show_current_password)
        self.ui.editSalesPersonShowHideNewPasswordButton.clicked.connect(self.edit_sales_person_hide_show_new_password)
        self.ui.editSalesPersonShowHideConfirmPasswordButton.clicked.connect(self.edit_sales_person_hide_show_confirm_password)
        self.ui.viewAllSalesPersonsButton.clicked.connect(self.view_all_sales_persons)
        self.ui.editAdminShowHideCurrentPasswordButton.clicked.connect(self.edit_admin_hide_show_current_password)
        self.ui.editAdminShowHideNewPasswordButton.clicked.connect(self.edit_admin_hide_show_new_password)
        self.ui.editAdminShowHideConfirmPasswordButton.clicked.connect(self.edit_admin_hide_show_confirm_password)
        self.ui.editAdminSaveButton.clicked.connect(self.edit_admin)
        self.ui.addNewItemAddButton.clicked.connect(self.add_new_item)
        self.ui.addNewItemClearButton.clicked.connect(self.reset_add_new_item_fields)
        self.ui.viewAllItemsButton.clicked.connect(self.open_all_items_window)
        self.ui.removeItemRemoveButton.clicked.connect(self.remove_item)
        self.ui.removeItemChooseItemComboBox.currentTextChanged.connect(self.remove_item_get_price_and_qty)
        self.ui.editItemUpdateButton.clicked.connect(self.edit_item)
        self.ui.editItemChooseItemComboBox.currentTextChanged.connect(self.edit_item_get_price_and_qty)
        self.ui.editItemClearButton.clicked.connect(self.edit_item_reset_fields_button)
        self.ui.saveNotifSettingsButton.clicked.connect(self.save_notif_settings)
        self.ui.saveBackupSettingsButton.clicked.connect(self.save_backup_settings)
        self.ui.backupDataBackupNowButton.clicked.connect(self.backup_now)
        self.ui.backupMenuButton.clicked.connect(self.backup_now)
        self.ui.logoutMenuButton.clicked.connect(self.log_out)
        self.ui.updateFirmInfoButton.clicked.connect(self.update_firm_info)
        self.ui.loadFirmInfoButton.clicked.connect(self.load_firm_info)
        self.ui.restoreDataButton.clicked.connect(self.restore_data)

###################MENU BAR###################

    def switch_to_sales(self):
        """
        This method switches view to the sales
        """
        self.ui.salesMenuButton.setChecked(True)
        self.ui.notifMenuButton.setChecked(False)
        self.ui.recordsMenuButton.setChecked(False)
        self.ui.settingsMenuButton.setChecked(False)
        self.ui.contentStackedWidget.setCurrentWidget(self.ui.salesPage)

    def switch_to_notification(self):
        """
        This method switches view to the notification
        """
        self.ui.salesMenuButton.setChecked(False)
        self.ui.notifMenuButton.setChecked(True)
        self.ui.recordsMenuButton.setChecked(False)
        self.ui.settingsMenuButton.setChecked(False)
        self.ui.contentStackedWidget.setCurrentWidget(self.ui.notificationPage)

    def switch_to_records(self):
        """
        This method switches view to the records
        """
        self.ui.salesMenuButton.setChecked(False)
        self.ui.notifMenuButton.setChecked(False)
        self.ui.recordsMenuButton.setChecked(True)
        self.ui.settingsMenuButton.setChecked(False)
        self.ui.contentStackedWidget.setCurrentWidget(self.ui.recordsPage)

    def switch_to_settings(self):
        """
        This method switches view to the settings
        """
        self.ui.salesMenuButton.setChecked(False)
        self.ui.notifMenuButton.setChecked(False)
        self.ui.recordsMenuButton.setChecked(False)
        self.ui.settingsMenuButton.setChecked(True)
        self.ui.contentStackedWidget.setCurrentWidget(self.ui.settingsPage)

###################GENERAL###################

    def set_loading_anim_to_labels(self):
        """
        This method sets the loading animation to all the appropriate labels
        """
        # load and set the loading animation
        self.loading_anim = QMovie(self.resource_path("icons" + os.sep + "loading_anim.gif"))
        self.ui.backupMenuAnimLabel.setMovie(self.loading_anim)
        self.ui.backupAnimLabel.setMovie(self.loading_anim)
        self.ui.loadingGraphAnimLabel.setMovie(self.loading_anim)
        self.ui.restoreDataAnimLabel.setMovie(self.loading_anim)
        self.loading_anim.start()
        # hide the loading labels
        self.ui.backupMenuAnimLabel.hide()
        self.ui.backupAnimLabel.hide()
        self.ui.loadingGraphAnimLabel.hide()
        self.ui.restoreDataAnimLabel.hide()

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
        if not self.logout_clicked:
            ok_pressed = QMessageBox.question(self, "Confirm Exit", "Do you really want to exit?")
            if ok_pressed == QMessageBox.Yes:
                self.release_resources()
                try:
                    self.loading_anim.stop()
                except:
                    pass
            else:
                event.ignore()
        else:
            self.release_resources()
            try:
                self.loading_anim.stop()
            except:
                pass

    def release_resources(self):
        """
        This method releases all resources before closing
        """
        # close the local database
        try:
            self.close_database()
        except:
            pass
        try:
            # clear search history
            for file in os.listdir(self.resource_path("search_history" + os.sep + "sales")):
                os.remove(self.resource_path("search_history" + os.sep + "sales" + os.sep + file))
            for file in os.listdir(self.resource_path("search_history" + os.sep + "records")):
                os.remove(self.resource_path("search_history" + os.sep + "records" + os.sep + file))
        except:
            pass

###################SALES###################

    def load_credentials_names(self):
        """
        This method loads all the names of people with access to this application
        """
        self.load_credentials_names_thread.start()

    def load_credentials_names_success(self, load_credentials_names_signal):   #argument: list
        """
        This method gets the credentials names
        """
        for name in load_credentials_names_signal:
            self.credentials_names.append(name[0])
        credentials_names_copy = self.credentials_names.copy()
        self.settings_populate_sales_persons_comboboxes(credentials_names_copy)

    def sales_load_items(self):
        """
        This method starts the load sales items thread
        """
        self.sales_load_items_thread.start()

    def sales_load_items_success(self, success_signal): #argument: list
        """
        This method loads the items into a dictionary
        """
        # get the items dictionary
        self.items = success_signal
        # populate the items and quantity comboboxes
        item_names = list(self.items.keys())
        item_names.sort()
        self.sales_populate_item_list(item_names)

    def sales_load_items_error(self, error_signal): #argument: str
        """
        This method receives the error signal from the load sales items thread
        """
        QMessageBox.critical(self, "Error", "Failed to load items")

    def sales_populate_item_list(self, items):     # argument: list
        """
        This method populates the items combobox
        """
        items.sort()
        self.ui.salesItemComboBox.clear()
        self.ui.editItemChooseItemComboBox.clear()
        self.ui.removeItemChooseItemComboBox.clear()
        self.ui.salesItemComboBox.addItems(items)
        self.ui.editItemChooseItemComboBox.addItems(items)
        self.ui.removeItemChooseItemComboBox.addItems(items)
        self.ui.salesItemComboBox.setCurrentText("")
        self.ui.editItemChooseItemComboBox.setCurrentText("")
        self.ui.removeItemChooseItemComboBox.setCurrentText("")
        # set autocompletion data for search field
        self.sales_search_autocomplete_data(items)

    def get_selected_item_data(self):
        """
        This method get the price and quantity of the selected item data and displays them
        """
        item = self.ui.salesItemComboBox.currentText().strip().upper()
        existing_items = list(self.items.keys())
        if existing_items.count(item) > 0:
            price = self.items[item][0]
            qty_available = self.items[item][1]
            qty_selected = self.ui.salesQtyOfItemsSpinBox.value()
            self.ui.totalCostForSelectedItemLineEdit.setText(str(round(price * qty_selected, 2)))
            self.ui.itemQtyLeftLineEdit.setText(str(qty_available))
        else:
            self.ui.totalCostForSelectedItemLineEdit.setText("0.00")
            self.ui.itemQtyLeftLineEdit.setText("0")

    def add_row_to_cart_table_widget(self, next_row, item, qty_purchased, cost, item_index=-1):
        #argument: int, str, int, float, int
        """
        This method adds a row to the cart table widget
        """
        # add the item to the cart items list
        if item_index == -1:
            self.cart.insert(0, (item, cost, qty_purchased))
        else:
            self.cart.insert(item_index, (item, cost, qty_purchased))
        # add the item to the cart table
        self.ui.cartTableWidget.insertRow(next_row)
        item_desc = QTableWidgetItem(item)
        item_quantity = QTableWidgetItem(str(qty_purchased))
        item_cost = QTableWidgetItem("{0:.2f}".format(float(cost)))
        # make rows uneditable
        item_desc.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        item_quantity.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        item_cost.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        # add the table widget items to the table
        self.ui.cartTableWidget.setItem(next_row, 0, item_desc)
        self.ui.cartTableWidget.setItem(next_row, 1, item_quantity)
        self.ui.cartTableWidget.setItem(next_row, 2, item_cost)

    def add_to_cart(self, item_index=-1):   #argument: int
        """
        This method add a selected item to the cart
        """
        item = self.ui.salesItemComboBox.currentText().strip().upper()
        if item != "":
            if item.find(";") <= 0:
                existing_items = list(self.items.keys())
                # check if item is in the items list
                if existing_items.count(item) > 0:
                    # check if item already exists in the cart before proceeding
                    item_exists_in_cart = False
                    if len(self.cart) > 0:
                        for row in self.cart:
                            if item.lower() == row[0].lower():
                                item_exists_in_cart = True
                                break
                    # get the sales info
                    qty_purchased = int(self.ui.salesQtyOfItemsSpinBox.value())
                    cost = float(self.ui.totalCostForSelectedItemLineEdit.text())
                    qty_available = self.items[item][1]
                    overall_cost = float(self.ui.salesTotalCostLineEdit.text())
                    overall_cost += cost
                    # check if the quantity purchased exceeds the quantity available before proceeding
                    if qty_purchased > qty_available:
                        QMessageBox.critical(self, "Alert", "Insufficient " + item + " available!")
                    else:
                        # if the item is not in the cart, add it to the cart
                        if not item_exists_in_cart:
                            # get next table row index
                            if item_index == -1:
                                next_row = self.ui.cartTableWidget.rowCount()
                            else:
                                next_row = item_index
                            # add item to cart table widget
                            self.add_row_to_cart_table_widget(next_row, item, qty_purchased, cost, item_index)
                            # set the total cost
                            self.ui.salesTotalCostLineEdit.setText("{0:.2f}".format(overall_cost))
                            # reset the items combobox, the item cost and quantity left
                            self.ui.salesItemComboBox.setCurrentText("")
                            self.ui.salesQtyOfItemsSpinBox.setValue(1)
                            self.ui.itemQtyLeftLineEdit.setText("0")
                        else:
                            ret_val = QMessageBox.question(self, "Alert",
                                                           "Item already exists in the cart!\nDo you want to replace it?")
                            if ret_val == QMessageBox.Yes:
                                self.replace_cart_item()
                            else:
                                pass
                else:
                    QMessageBox.critical(self, "Error", "Item does not exist!")
                    self.sales_populate_item_list(list(self.items.keys()))
            else:
                QMessageBox.critical(self, "Error", "Semi-colon(;) is not allowed!")
        else:
            QMessageBox.critical(self, "Error", "No item selected!")

    def replace_cart_item(self):
        """
        This method replaces an item in the cart
        """
        # get index of item to be replaced
        item = self.ui.salesItemComboBox.currentText().strip()
        item_index = -1
        for index in range(0, len(self.cart)):
            if item.lower() == self.cart[index][0].lower():
                item_index = index
                break
        if item_index >= 0:
            # remove the item from the cart table and re-calculate
            self.ui.cartTableWidget.removeRow(item_index)
            # recalculate the total cost
            overall_cost = float(self.ui.salesTotalCostLineEdit.text())
            overall_cost -= float(self.cart[item_index][1])
            self.ui.salesTotalCostLineEdit.setText("{0:.2f}".format(overall_cost))
            # remove the item from the cart items list
            self.cart.pop(item_index)
            # add replacement to cart in the same position
            self.add_to_cart(item_index)

    def remove_from_cart(self):
        """
        This method removes a selected item from the cart
        """
        if self.ui.cartTableWidget.rowCount() > 0:
            # get the selected row's index
            selected_row_index = self.ui.cartTableWidget.currentRow()
            if selected_row_index >= 0:
                # remove the item from the cart table and re-calculate
                self.ui.cartTableWidget.removeRow(selected_row_index)
                # recalculate the total cost
                overall_cost = float(self.ui.salesTotalCostLineEdit.text())
                overall_cost -= float(self.cart[selected_row_index][1])
                self.ui.salesTotalCostLineEdit.setText("{0:.2f}".format(overall_cost))
                # remove the item from the cart items list
                self.cart.pop(selected_row_index)
            else:
                QMessageBox.critical(self, "Alert", "No item selected!!!")
        else:
            QMessageBox.critical(self, "Alert", "Cart is empty!!!")

    def abort_sale(self):
        """
        This method clears all the fields in the sales form
        """
        self.ui.salesItemComboBox.setCurrentText("")
        self.ui.salesQtyOfItemsSpinBox.setValue(1)
        self.ui.totalCostForSelectedItemLineEdit.setText("0.00")
        self.ui.itemQtyLeftLineEdit.setText("0")
        self.ui.cartTableWidget.setRowCount(0)
        self.ui.salesTotalCostLineEdit.setText("0.00")

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
##            date = datetime.date(year, month, day_of_month)
##            prev_date = datetime.date(prev_year, prev_month, prev_day_of_month)
##            _time = datetime.time(hour, minute)
##            prev_time = datetime.time(prev_hour, prev_minute)
##            if date > prev_date:
##                time_valid = True
##                cur_date = [year, month, day_of_month]
##            elif date == prev_date:
##                if _time >= prev_time:
##                    time_valid = True
            date_time_obj = datetime.datetime(year, month, day_of_month, hour, minute)
            prev_date_time_obj = datetime.datetime(prev_year, prev_month, prev_day_of_month, prev_hour, prev_minute)
            if date_time_obj >= prev_date_time_obj:
                time_valid = True
        except:
            time_valid = False
        return (time_valid, cur_date, year)

    def sell_items(self):
        """
        This method sells the items
        """
        num_of_cart_rows = self.ui.cartTableWidget.rowCount()
        if num_of_cart_rows > 0:
            # get the item names, quantities, costs of each set of items, overall cost, date and time
            item_names = []
            item_qtys = []
            for row in self.cart:
                item_names.append(row[0])
                item_qtys.append(str(row[2]) + "(GH₵" + str(row[1]) + ")")
            # join the item names and quantities in strings
            item_names = "; ".join(item_names)
            item_qtys = "; ".join(item_qtys)
            overall_cost = float(self.ui.salesTotalCostLineEdit.text())
            # get the current time
            date_time = self.get_cur_date_time()
            # check if the time of sale is valid before submitting the sale
            date_valid, cur_date, year = self.verify_date_time(date_time)
            if date_valid:
                # start the submit sales record thread
                self.submit_sales_record_thread.set_parameters(item_names, item_qtys, overall_cost, date_time, self.login_name, cur_date, year)
                self.submit_sales_record_thread.start()
            else:
                QMessageBox.critical(self, "Error", "Invalid date and time.\nPlease set system date and time.")
        else:
            QMessageBox.critical(self, "Error", "Cart is empty!")

    def sell_items_success(self, submit_sales_success_signal):  #argument: list
        """
        This method response to a successful submission of the sales record
        """
        item_names, item_qtys, overall_cost, date_time, cur_date = submit_sales_success_signal
        # add the data to the table widget
        if len(cur_date) == 0:
            self.sales_add_record_to_table_widget(item_names, item_qtys, overall_cost, date_time, self.login_name)
            # update the overall cost
            self.sales_cur_day_overall_cost += overall_cost
            self.ui.salesCurrentDayTotalSalesLabel.setText("{0:.2f}".format(self.sales_cur_day_overall_cost))
        else:
            year, month, day_of_month = cur_date
            self.ui.salesSearchDateEdit.setDate(QDate(year, month, day_of_month))
            self.sales_add_record_to_table_widget(item_names, item_qtys, overall_cost, date_time, self.login_name)
            # update the overall cost
            self.sales_cur_day_overall_cost = overall_cost
            self.ui.salesCurrentDayTotalSalesLabel.setText("{0:.2f}".format(self.sales_cur_day_overall_cost))
        # clear cart after sale
        self.ui.cartTableWidget.setRowCount(0)
        self.cart.clear()
        self.ui.salesTotalCostLineEdit.setText("0.00")
        # get item names and quantities and make changes to their quantities left
        item_names = item_names.strip().split("; ")
        item_qtys_costs = item_qtys.strip().split("; ")
        item_qtys = []
        item_costs = []
        item_qtys_left = []
        for qty_cost in item_qtys_costs:
            qtys, costs = qty_cost.split("(GH₵")
            item_costs.append(costs)
            item_qtys.append(int(qtys))
        for i in range(0, len(item_costs)):
            item_costs[i] = item_costs[i][:-1]
        for i in range(0, len(item_names)):
            self.items[item_names[i]][1] -= item_qtys[i]
            item_qtys_left.append(self.items[item_names[i]][1])
        # start the update item quantities thread
        self.update_item_qty_thread.set_parameters(item_names, item_qtys_left)
        self.update_item_qty_thread.start()
        # get the receipt contents
        self.receipt_content['item_names'] = item_names
        self.receipt_content['item_qtys'] = item_qtys
        self.receipt_content['item_costs'] = item_costs
        self.receipt_content['overall_cost'] = overall_cost
        self.receipt_content['date_time'] = date_time
        self.receipt_content['sales_person'] = self.login_name
        # send notification if there is shortage of any of the items
        insufficient_item_names = []
        insufficient_item_qtys = []
        for i in range(0, len(item_names)):
            if self.items[item_names[i]][1] <= self.min_qty_to_notify:
                insufficient_item_names.append(item_names[i])
                insufficient_item_qtys.append(item_qtys_left[i])
        if len(insufficient_item_names) > 0:
            notif_msg = self.compose_shortage_notif_msg(insufficient_item_names, insufficient_item_qtys)
            self.add_notif(date_time, "SHORTAGE OF ITEM(S)!", notif_msg, "today")
        # update the time checker
        self.update_date_time_checker(date_time)

    def update_item_qty(self, update_item_qty_signal):  #argument: str
        """
        This method responds to signals from the item quantity update thread
        """
        if update_item_qty_signal == "success":
            pass
        else:
            pass

    def sell_items_error(self, submit_sales_error_signal):  #argument: str
        """
        This method response to a successful submission of the sales record
        """
        QMessageBox.critical(self, "Error", "Sale was interrupted!")

    def sales_add_record_to_table_widget(self, item_names, item_qtys, overall_cost, date_time, login_name="Admin", set_list=True):
        #argument: str, str, float, str, str, bool
        """
        This method add a row record to the records table widget
        """
        # insert row into sales records list
        if set_list:
            self.sales_records.insert(0, (item_names, item_qtys, overall_cost, date_time, login_name))
        # add the item to the cart table
        self.ui.salesRecordsTableWidget.insertRow(0)
        name_item = QTableWidgetItem(item_names)
        qtys_item = QTableWidgetItem(item_qtys)
        overall_cost_item = QTableWidgetItem("{0:.2f}".format(float(overall_cost)))
        date_time_item = QTableWidgetItem(date_time)
        sales_person_item = QTableWidgetItem(login_name)
        # make rows uneditable
        name_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        qtys_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        overall_cost_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        date_time_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        sales_person_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        # add the table widget items to the table
        self.ui.salesRecordsTableWidget.setItem(0, 0, name_item)
        self.ui.salesRecordsTableWidget.setItem(0, 1, qtys_item)
        self.ui.salesRecordsTableWidget.setItem(0, 2, overall_cost_item)
        self.ui.salesRecordsTableWidget.setItem(0, 3, date_time_item)
        self.ui.salesRecordsTableWidget.setItem(0, 4, sales_person_item)

    def load_record_into_cart(self):
        """
        This method loads a selected record in the sales records table into the cart
        """
        # get the selected row index from records table
        selected_row_index = self.ui.salesRecordsTableWidget.currentRow()
        # load items selected row
        selected_row_data = self.sales_records[selected_row_index]
        item_names = selected_row_data[0].strip().split("; ")
        item_qtys_costs = selected_row_data[1].strip().split("; ")
        item_qtys = []
        item_costs = []
        for qty_cost in item_qtys_costs:
            qtys, costs = qty_cost.split("(GH₵")
            item_qtys.append(qtys)
            item_costs.append(costs)
        for i in range(0, len(item_costs)):
            item_costs[i] = item_costs[i][:-1]
        overall_cost = selected_row_data[2]
        # get the items that are insuficient
        insufficient_items = []
        for i in range(0, len(item_names)):
            if int(item_qtys[i]) > self.items[item_names[i]][1]:
                insufficient_items.append(item_names[i])
        # load the items only if there is sufficient quantities of each of them
        if len(insufficient_items) > 0:
            if len(insufficient_items) > 1:
                QMessageBox.critical(self, "Alert", "Insufficient " + ", ".join(insufficient_items) + " available!")
            else:
                QMessageBox.critical(self, "Alert", "Insufficient " + insufficient_items[0] + " available!")
        else:
            # add data to the cart
            self.ui.cartTableWidget.setRowCount(0)
            self.cart.clear()
            for i in range(0, len(item_names)):
                item = item_names[i]
                qty_purchased = item_qtys[i]
                cost = item_costs[i]
                self.add_row_to_cart_table_widget(0, item, qty_purchased, cost)
            # set overall cost
            self.ui.salesTotalCostLineEdit.setText("{0:.2f}".format(overall_cost))        

    def sales_print_receipt(self):
        """
        This method prints the receipt for a sale
        """
        # check if there is info to be printed before printing
        if len(self.receipt_content) > 0:
            dialog = QPrintPreviewDialog()
            dialog.setWindowTitle("Print Receipt")
            dialog.printer().setPaperSize(QSizeF(80, 100), QPrinter.Millimeter)
##            dialog.printer().setPaperSize(QPrinter.A7)
            dialog.printer().setPageMargins(0.2, 0.2, 0.2, 0.2, QPrinter.Millimeter)
            dialog.paintRequested.connect(self._sales_print_receipt)
            dialog.exec_()
        else:
            QMessageBox.critical(self, "Print Alert", "No data available for printing!!!")

    def _sales_print_receipt(self, printer):  # argument: QPrinter
        """
        This method organizes the data to be printed on the receipt
        """
        # create text document to hold table
        document = QTextDocument()
        # set table dimensions
        p_size = printer.pageRect()
        p_width, p_height = p_size.width(), p_size.height()
        document.setPageSize(QSizeF(p_width, p_height))
        document.setDocumentMargin(5.0)
        font = QFont("Verdana", 7)
        document.setDefaultFont(font)
        # create document's text cursor
        cursor = QTextCursor(document)
        # get the academic division
        firm_name = "SALES MANAGEMENT SOFTWARE"
        try:
            firm_name_file = open("data_files" + os.sep + "firm_info.txt", 'r')
            data = firm_name_file.read()
            firm_name, firm_contact, firm_address = data.strip().upper().split(query_sep)
        except:
            pass
        # set title
        cursor.insertHtml("<html><p align='center'><h3><strong>" + firm_name + "<br></strong></h3></p></html>")
        cursor.insertHtml("<html><p align='center'><h3><strong>CONTACT:" + firm_contact + "<br></strong></h3></p></html>")
        cursor.insertHtml("<html><p align='center'><h3><strong>" + firm_address + "<br></strong></h3></p></html>")
        # add items details to receipt
        textTableFormat = QTextTableFormat()
        textTableFormat.setBorder(0.00)
        textTableFormat.setBorderStyle(QTextTableFormat.BorderStyle_Solid)
        textTableFormat.setCellPadding(2.00)
##        textTableFormat.setCellSpacing(0)
        num_of_rows = len(self.receipt_content['item_names'])
        table = cursor.insertTable(num_of_rows + 1, 3, textTableFormat)
        item_names = self.receipt_content['item_names']  # list to hold the item names
        item_qtys = self.receipt_content['item_qtys']  # list to hold the item quantities
        for i in range(0, len(item_qtys)):
            item_qtys[i] = str(item_qtys[i])
        item_costs = self.receipt_content['item_costs']  # list to hold the total costs
        item_names.insert(0, "ITEM")
        item_qtys.insert(0, "QTY")
        item_costs.insert(0, "COST")
        data_array = numpy.array([item_names, item_qtys, item_costs], dtype=str)  # create numpy array to hold table
        for row in range(table.rows()):
            for col in range(table.columns()):
                if row == 0:
                    cursor.insertHtml("<html><strong>" + data_array[col, row] + "</strong></html>")
                    cursor.movePosition(QTextCursor.NextCell)
                else:
                    cursor.insertText(data_array[col, row])
                    cursor.movePosition(QTextCursor.NextCell)
        cursor.movePosition(QTextCursor.NextBlock)
        # add the total cost
        table = cursor.insertTable(1, 2, textTableFormat)
        cursor.insertHtml("<html><strong>TOTAL COST:</strong></html>")
        cursor.movePosition(QTextCursor.NextCell)
        cursor.insertText("GH₵{0:.2f}".format(self.receipt_content["overall_cost"]))
        cursor.movePosition(QTextCursor.NextBlock)
        # add the sales person's name
        textTableFormat = QTextTableFormat()
        textTableFormat.setBorder(0.00)
        textTableFormat.setCellPadding(2.00)
        table = cursor.insertTable(1, 2, textTableFormat)
        cursor.insertHtml("<html><strong>SALES PERSON:</strong></html>")
        cursor.movePosition(QTextCursor.NextCell)
        cursor.insertText(self.receipt_content["sales_person"])
        cursor.movePosition(QTextCursor.NextBlock)
        # add the date and time
        table = cursor.insertTable(1, 2, textTableFormat)
        cursor.insertHtml("<html><strong>DATE AND TIME:</strong></html>")
        cursor.movePosition(QTextCursor.NextCell)
        cursor.insertText(self.receipt_content["date_time"])
        cursor.movePosition(QTextCursor.NextBlock)
        # print document
        document.print_(printer)

    def sales_load_records(self):
        """
        This method loads the sales records from the database
        """
        # get the date
        date = self.ui.salesSearchDateEdit.text().strip()
        day, month, year = date.split("/")
        month = self.months_list[int(month)-1]
        date = month + " " + day + ", " + year
        cur_year = int(year)  # get the year
        # start the load records thread
        self.sales_load_records_thread.set_parameters(date, cur_year)
        self.sales_load_records_thread.start()

    def sales_load_records_success(self, sales_load_records_success_signal):    #argument: list
        """
        This method gets the success signal after loading sales records
        """
        # get the sales records
        self.sales_records, self.sales_cur_day_overall_cost = sales_load_records_success_signal
        # sort table data and display
        self.sales_sort_records_table()
        # display the overall cost
        self.ui.salesCurrentDayTotalSalesLabel.setText("{0:.2f}".format(self.sales_cur_day_overall_cost))
        # reset the history file
        self.sales_cur_records_history_file_index = 0

    def sales_load_records_error(self, sales_load_records_error_signal):    #argument: str
        """
        This method gets the error signal after loading sales records
        """
        QMessageBox.critical(self, "Error", "Failed to load sales records!")

    def sales_flip_records_table(self):
        """
        This method flips/reverses the records table
        """
        # clear the table
        self.ui.salesRecordsTableWidget.setRowCount(0)
        # add the data to the table in the reverse order
        for row in self.sales_records:
            item_names = row[0]
            item_qtys = row[1]
            overall_cost = str(row[2])
            date_time = row[3]
            login_name = row[4]
            self.sales_add_record_to_table_widget(item_names, item_qtys, overall_cost, date_time, login_name, False)
            QApplication.processEvents()
        # reverse table data to get the same order as in the table
        self.sales_records.reverse()

    def sales_sort_records_table(self):
        """
        This method sorts the sales records based the selected parameter
        """
        param = self.ui.salesSortComboBox.currentText().lower().strip()
        if param == "time":
            col_index = 3
        else:
            col_index = 4
        # get the sorting data in the table
        list_of_data = []
        for row in self.sales_records:
            if col_index == 3:
                time = row[col_index].split()[4]
                list_of_data.append(int(time.replace(":", "")))
            else:
                list_of_data.append(row[col_index])
        # put the sorting data in a numpy array
        if col_index == 3:
            array_of_data = numpy.array(list_of_data, dtype=int)
        else:
            array_of_data = numpy.array(list_of_data, dtype=str)
        # sort the data in alphabetical order and get the indices of their rows
        sorted_data_indices = numpy.argsort(array_of_data)
        # create a copy of the table data
        table_data_copy = self.sales_records.copy()
        # clear the table data
        self.sales_records.clear()
        # set the table data in the sorted form
        for index in sorted_data_indices:
            self.sales_records.insert(0, table_data_copy[index])
        # clear the table
        self.ui.salesRecordsTableWidget.setRowCount(0)
        # add the sorted data to the table
        for row in self.sales_records:
            item_names = row[0]
            item_qtys = row[1]
            overall_cost = str(row[2])
            date_time = row[3]
            login_name = row[4]
            self.sales_add_record_to_table_widget(item_names, item_qtys, overall_cost, date_time, login_name, False)
            QApplication.processEvents()
        # reverse table data to get the same order as in the table
        self.sales_records.reverse()

    def sales_search_autocomplete_data(self, auto_completion_data): #argument: list
        """
        This method sets the auto completion data into the search field
        """
        auto_completion_data = list(set(auto_completion_data))
        completer = QCompleter(auto_completion_data, self.ui.salesSearchField)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.salesSearchField.setCompleter(completer)

    def sales_search_records_param_effect(self):
        """
        This methods reacts to search parameter selection for performing searches
        """
        selected_param = self.ui.salesSearchParamComboBox.currentText().lower().strip()
        if selected_param == "search by:":
            self.ui.salesSearchField.setPlaceholderText("Type query here")
            self.sales_search_autocomplete_data([])
        elif selected_param == "item":
            self.ui.salesSearchField.setPlaceholderText("Type item's name here")
            self.sales_search_autocomplete_data(list(self.items.keys()))
        elif selected_param == "time(hour)":
            self.ui.salesSearchField.setPlaceholderText("Type hour here (0 to 23)")
            self.sales_search_autocomplete_data([])
        elif selected_param == "sales person":
            self.ui.salesSearchField.setPlaceholderText("Type sales person's name here")
            self.sales_search_autocomplete_data(self.credentials_names)

    def sales_search_records(self):
        """
        This method searches the records for a query
        """
        # check if a search parameter is selected before proceeding
        if self.ui.salesSearchParamComboBox.currentText() != "Search By:":
            # get the search parameter
            search_param_for_history = self.ui.salesSearchParamComboBox.currentText()
            item_search_param = search_param_for_history.strip().lower()
            # get the text to search and search column index
            item_to_search = ""
            search_column_index = -1
            if item_search_param == "item":
                item_to_search = self.ui.salesSearchField.text().strip()
                search_column_index = 0
            elif item_search_param == "time(hour)":
                item_to_search = self.ui.salesSearchField.text().strip()
                search_column_index = 3
            elif item_search_param == "sales person":
                item_to_search = self.ui.salesSearchField.text().strip()
                search_column_index = 4
            match_found = False     # notify for a match
            punc_chars = ["/", ",", ".", ";", "\\", "\\\\", "?", "!", ":", "*", "#"]
            # remove punctuation symbols from the item to be searched
            for ch in punc_chars:
                item_to_search = item_to_search.replace(ch, "")     # remove all puntuation marks before search
                item_to_search = item_to_search.replace("  ", " ")   # replace double spaces with single spaces
            if item_to_search.strip() != "":
                if self.ui.salesRecordsTableWidget.rowCount() > 0:
                    try:
                        # create a search data list to hold the list of items that serve as the dictionary
                        search_data_list = []
                        if search_column_index >= 0:
                            # extract the item descriptions from the items table data
                            for row in self.sales_records:
                                search_data_list.append(row[search_column_index])
                            # remove punctuation symbols from the search list data
                            for item in search_data_list:
                                # remove the colon from the punctuation list if search parameter is time
                                try:
                                    if item_search_param == "time(hour)":
                                        punc_chars.remove(":")
                                except:
                                    pass
                                for ch in punc_chars:
                                    item = item.replace(ch, "")     # remove all puntuation marks before search
                                    item = item.replace("  ", " ")   # replace double spaces with single spaces
                                # if the search parameter is time, search and see if the hour exists
                                if item_search_param == "time(hour)":
                                    if item.split()[4].split(":")[0] == item_to_search:
                                        match_found = True
                                        break
                                else:
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
                                    if item_search_param == "time(hour)":
                                        if search_data.split()[4].split(":")[0] == item_to_search:
                                            row_indices_of_items.insert(0, index)
                                    else:
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
                                    name_item = self.ui.salesRecordsTableWidget.takeItem(row_index_of_item, 0)
                                    qty_item = self.ui.salesRecordsTableWidget.takeItem(row_index_of_item, 1)
                                    total_cost_item = self.ui.salesRecordsTableWidget.takeItem(row_index_of_item, 2)
                                    date_item = self.ui.salesRecordsTableWidget.takeItem(row_index_of_item, 3)
                                    sales_person_item = self.ui.salesRecordsTableWidget.takeItem(row_index_of_item, 4)
                                    # add all the selected rows with their items to a list
                                    selected_rows.append([name_item, qty_item, total_cost_item, date_item, sales_person_item])
                                # remove the selected rows from their previous positions
                                for row_index_of_item in row_indices_of_items:
                                    if row_shift_count == 0:
                                        self.ui.salesRecordsTableWidget.removeRow(row_index_of_item)
                                        self.sales_records.pop(row_index_of_item)
                                        row_shift_count += 1
                                    else:
                                        try:
                                            self.ui.salesRecordsTableWidget.removeRow(row_index_of_item - row_shift_count)
                                            self.sales_records.pop(row_index_of_item - row_shift_count)
                                            row_shift_count += 1
                                        except:
                                            self.ui.salesRecordsTableWidget.removeRow(row_index_of_item)
                                            self.sales_records.pop(row_index_of_item)
                                            row_shift_count += 1
                                # reverse the selected rows so as to obtain the same order after adding to the table
                                selected_rows.reverse()
                                # clear the table of the other data which are not included in the search results.
                                # this is to ensure that only the search results are displayed in the table
                                self.ui.salesRecordsTableWidget.setRowCount(0)
                                self.sales_records.clear()
                                # get the selected rows to the top and rearrange the table
                                for row in selected_rows:
                                    row_data = (row[0].text(), row[1].text(), float(row[2].text()), row[3].text(), row[4].text())
                                    self.sales_records.insert(0, row_data)
                                # sort the table data according to the present sorting parameter selected
                                self.sales_sort_records_table()
                                # add search to history
                                self.sales_save_search_history(search_param_for_history, item_to_search, self.sales_records)
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

    def sales_save_search_history(self, search_param, item_searched, search_results):   #argument: str, str, list
        """
        This method saves the history of a search
        """
        # pack the search data into a dictionary
        history_data = {"search_param": search_param, "item_searched": item_searched, "search_results": search_results}
        # count existing history files
        history_file_count = len(os.listdir(self.resource_path("search_history" + os.sep + "sales")))
        # get a list of the names of the history files.
        self.list_of_sales_cur_records_history_files = [str(x) + ".pkl" for x in range(1, history_file_count + 2)]
        self.sales_cur_records_history_file_index = -1
        # save the history to a pickle file
        history_filename = str(history_file_count + 1) + ".pkl"
        history_file = open(self.resource_path("search_history" + os.sep + "sales" + os.sep + history_filename), "wb")
        pickle.dump(history_data, history_file)
        history_file.close()

    def sales_previous_records_search(self):
        """
        This method loads the previous search results
        """
        try:
            # get the previous search history
            self.sales_cur_records_history_file_index -= 1
            history_filename = self.list_of_sales_cur_records_history_files[self.sales_cur_records_history_file_index]
            history_file = open(self.resource_path("search_history" + os.sep + "sales" + os.sep + history_filename), "rb")
            history_data = pickle.load(history_file)
            history_file.close()
            # get the history data items
            search_param = history_data["search_param"]
            item_searched = history_data["item_searched"]
            search_results = history_data["search_results"]
            # insert the search history data items to their respective fields
            self.ui.salesSearchParamComboBox.setCurrentText(search_param)
            self.ui.salesSearchField.setText(item_searched)
            # clear the table and add data to table
            self.ui.salesRecordsTableWidget.setRowCount(0)
            search_results.reverse()
            for row in search_results:
                self.sales_add_record_to_table_widget(*row)
                QApplication.processEvents()
            # set the table data list to the history data
            search_results.reverse()
            self.sales_records = search_results
        except:
            # set current history file to the previously valid one
            self.sales_cur_records_history_file_index += 1
            QMessageBox.information(self, "Search Alert", "No previous search history available")

    def sales_next_records_search(self):
        """
        This method loads the next search results
        """
        try:
            # get the next search history
            if self.sales_cur_records_history_file_index < -1:
                self.sales_cur_records_history_file_index += 1
                history_filename = self.list_of_sales_cur_records_history_files[self.sales_cur_records_history_file_index]
                history_file = open(self.resource_path("search_history" + os.sep + "sales" + os.sep + history_filename), "rb")
                history_data = pickle.load(history_file)
                history_file.close()
                # get the history data items
                search_param = history_data["search_param"]
                item_searched = history_data["item_searched"]
                search_results = history_data["search_results"]
                # insert the search history data items to their respective fields
                self.ui.salesSearchParamComboBox.setCurrentText(search_param)
                self.ui.salesSearchField.setText(item_searched)
                # clear the table and add data to table
                self.ui.salesRecordsTableWidget.setRowCount(0)
                search_results.reverse()
                for row in search_results:
                    self.sales_add_record_to_table_widget(*row)
                    QApplication.processEvents()
                # set the table data list to the history data
                search_results.reverse()
                self.sales_records = search_results
            else:
                QMessageBox.information(self, "Search Alert", "No next search history available")
        except:
            QMessageBox.information(self, "Search Alert", "No next search history available")

###################NOTIFICATION###################

    def switch_to_today(self):
        """
        This method loads the current day's notifications
        """
        self.ui.todayNotifButton.setChecked(True)
        self.ui.historyNotifButton.setChecked(False)

    def switch_to_history(self):
        """
        This method loads all previous notifications
        """
        self.ui.todayNotifButton.setChecked(False)
        self.ui.historyNotifButton.setChecked(True)

    def add_notif(self, date_time="", msg_title="", msg="", section="", notif_msg_filename=""):
        #argument: str, str, str, str
        """
        This method adds a notification
        """
        # when message is not empty, it means it is a new message
        # so add message details to list if only it is a new message
        if msg != "":
            # create date folder if it does not exist before writing notification to file
            shortage_notif_dir_path = self.resource_path("notifications" + os.sep + "shortage")
            year, month, day_of_month, hour, minute = self.parse_date_time(date_time)
            cur_date = str(year) + "_" + str(month) + "_" + str(day_of_month)
            # if the previous messages are not for today, clear them before adding the current one
            if self.ui.todayNotifButton.isChecked():
                if self.ui.notifMsgListWidget.count() > 0:
                    # check the date for one of the items to see if it belongs to today
                    existing_date_time = self.notif_msgs[0].split("_")[1].replace(";", ":")
                    e_year, e_month, e_day_of_month, e_hour, e_minute = self.parse_date_time(existing_date_time)
                    existing_date_obj = datetime.date(e_year, e_month, e_day_of_month)
                    cur_date_obj = datetime.date(year, month, day_of_month)
                    if existing_date_obj != cur_date_obj:
                        # set the current message being viewed to be cleared from the message view
                        self.notif_filename = "new_date"
            notif_msg_dir_path = shortage_notif_dir_path + os.sep + cur_date # get path to the date folder
            notif_dates = os.listdir(shortage_notif_dir_path)
            if notif_dates.count(cur_date) < 1:  # if date does not exist, create a folder for it
                os.mkdir(notif_msg_dir_path)
            notif_files = os.listdir(notif_msg_dir_path)  # get the list of history files in the date's folder
            next_file_index = len(notif_files) + 1 # get the number of files in the date's folder
            notif_msg_filename = str(next_file_index) + "_" + date_time.replace(":", ";") # get the notification message filename
            notif_msg_filename = str(next_file_index) + "_" + date_time.replace(":", ";") # get the notification message filename
            notif_msg_file_path = notif_msg_dir_path + os.sep + notif_msg_filename # get the notification message file path
            # write the notification file
            notif_msg_file = open(notif_msg_file_path, 'w')
            notif_msg_file.write(msg)
            notif_msg_file.close()
        if self.ui.historyNotifButton.isChecked() and self.notif_filename == "new_date":
            pass
        else:
            # if it is a new message, add it to the messages details list
            self.notif_msgs_details.append([date_time, msg_title, section])
            # add message to list widget
            self.ui.noNotifMsgLabel.hide()
            self.ui.notifMsgListWidget.show()
            self.notif_msgs.append(notif_msg_filename)
            msg_index = len(self.notif_msgs) - 1
            self.notif_msg_template = NotifMsgTemplate(date_time, msg_title, section, self.select_notif_msg_row,
                                                       msg_index, self.delete_notif, notif_msg_filename)
            item = QListWidgetItem(self.ui.notifMsgListWidget)
            self.ui.notifMsgListWidget.setItemWidget(item, self.notif_msg_template)

    def compose_shortage_notif_msg(self, item_names, item_qtys): #argument: list, list
        """
        This method composes the shortage of items message
        """
        msg = "<html><body><p align=center><h3>SHORTAGE OF ITEM(S)</h3></p>"
        if len(item_names) == 1:
            msg += "<p>There is shortage of: <b>" + item_names[0] + "</b>; Quantity Left = <b>" + str(item_qtys[0]) + "</b></p>"
        else:
            msg += "<p>The are shortages of: </br><ol>"
            for i in range(0, len(item_names)):
                msg += "<li><b>" + item_names[i] + "</b>; Quantity Left = <b>" + str(item_qtys[i]) + "</b></li>"
            msg += "</ol></p>"
        msg += "</body></html>"
        return msg

    def delete_notif(self, date_time, section, filename): #argument: str, str, str
        """
        This method deletes a notification
        """
        try:
            # get the date folder name
            edited_date_time = filename.split("_")[1].replace(";", ":")
            year, month, day_of_month, hour, minute = self.parse_date_time(edited_date_time)
            dir_name = str(year) + "_" + str(month) + "_" + str(day_of_month)
            # get the path to the file
            msg_file_path = self.resource_path("notifications" + os.sep + "shortage" + os.sep + dir_name + os.sep + filename)
            # delete the file
            os.remove(msg_file_path)
            # clear message view if its message is deleted
            if self.notif_filename == filename:
                self.ui.viewNotifTextEdit.clear()
                # set the currently viewed notification as deleted
                self.notif_filename = "deleted"
            # remove the message from the message details list and refresh the list widget
            msg_names_details_dict = dict()
            for i in range(0, len(self.notif_msgs)):
                msg_names_details_dict[self.notif_msgs[i]] = self.notif_msgs_details[i]
            msg_names_details_dict.pop(filename)
            self.notif_msgs = list(msg_names_details_dict.keys())
            self.notif_msgs_details = list(msg_names_details_dict.values())
            self.ui.notifMsgListWidget.clear()
            # reload all messages
            num_of_msgs = len(self.notif_msgs)  # get the number of notifications minus the removed one
            notif_msgs_copy = self.notif_msgs.copy()
            self.notif_msgs.clear()
            notif_msgs_details_copy = self.notif_msgs_details.copy()
            self.notif_msgs_details.clear()
            if num_of_msgs > 0:
                for i in range(0, num_of_msgs):
                    date_time, msg_title, section = notif_msgs_details_copy[i]
                    fname = notif_msgs_copy[i]
                    self.add_notif(date_time, msg_title, "", section, fname)
            else:
                self.ui.notifMsgListWidget.hide()
                self.ui.noNotifMsgLabel.show()
        except:
            pass

    def select_notif_msg_row(self, msg_index, filename=""):
        """
        This method sets the current row for the notification messages
        """
        self.notif_filename = filename  # get the notification filename from the template message class for reading the notification
        self.ui.notifMsgListWidget.setCurrentRow(msg_index)

    def show_notif(self): # argument: int, str
        """
        This method displays the notification
        """
        try:
            # get the date folder name
            date_time = self.notif_filename.split("_")[1].replace(";", ":")
            year, month, day_of_month, hour, minute = self.parse_date_time(date_time)
            dir_name = str(year) + "_" + str(month) + "_" + str(day_of_month)
            # get the path to the file
            msg_file_path = self.resource_path("notifications" + os.sep + "shortage" + os.sep + dir_name + os.sep + self.notif_filename)
            # read the file
            msg_file = open(msg_file_path, 'r')
            msg = msg_file.read()
            msg_file.close()
            # show the message
            self.ui.viewNotifTextEdit.clear()
            if self.notif_filename != "" or self.notif_filename == "new_date" or self.notif_filename == "deleted":
                self.ui.viewNotifTextEdit.insertHtml(msg)
        except:
            # if the todays section is opened, load today's messages else load the notifications history
            # when a file being viewed is deleted else do nothing
            if self.notif_filename == "":
                pass
            elif self.notif_filename == "new_date":
                self.notif_filename = "old_date"
            elif self.notif_filename == "deleted":
                self.load_today_notif_msgs()
                self.load_notif_history()

    def load_today_notif_msgs(self):
        """
        This method load all the current day's notification messages
        """
        try:
            if self.ui.todayNotifButton.isChecked():
                # clear the messages filenames list and details
                self.notif_msgs.clear()
                self.notif_msgs_details.clear()
                # get the date folder name
                # get the current time
                date_time = time.localtime()
                # get the date and time values
                year = date_time.tm_year
                month = date_time.tm_mon
                day_of_month = date_time.tm_mday
                dir_name = str(year) + "_" + str(month) + "_" + str(day_of_month)
                # get the path to the file
                msgs_dir_path = self.resource_path("notifications" + os.sep + "shortage" + os.sep + dir_name)
                if os.path.exists(msgs_dir_path):
                    # get the list of filenames
                    filenames = os.listdir(msgs_dir_path)
                    # clear the current view notification
                    self.notif_filename = ""
                    # clear the messages list widget and the message view
                    self.ui.viewNotifTextEdit.clear()
                    self.ui.notifMsgListWidget.clear()
                    if len(filenames) > 0:
                        # sort the files in ascending order
                        file_indices_list = []
                        for fname in filenames:
                            file_index = int(fname.split("_")[0])
                            file_indices_list.append(file_index)
                        file_indices_array = numpy.array(file_indices_list, dtype=int)
                        sorted_file_indices = numpy.argsort(file_indices_array)
                        filenames_copy = filenames.copy()
                        filenames.clear()
                        for index in sorted_file_indices:
                            filenames.append(filenames_copy[index])
                        # get the date and time and add the notifications to the messages list widget
                        for fname in filenames:
                            date_time = fname.split("_")[1].replace(";", ":")
                            self.add_notif(date_time, "SHORTAGE OF ITEM(S)", "", "today", fname)
                    else:
                        self.ui.notifMsgListWidget.hide()
                        self.ui.noNotifMsgLabel.show()
                else:
                    # clear the messages filenames list and details
                    self.notif_msgs.clear()
                    self.notif_msgs_details.clear()
                    # clear the messages list widget and the message view
                    self.ui.viewNotifTextEdit.clear()
                    self.ui.notifMsgListWidget.clear()
                    self.ui.notifMsgListWidget.hide()
                    self.ui.noNotifMsgLabel.show()
        except:
            # clear the messages filenames list and details
            self.notif_msgs.clear()
            self.notif_msgs_details.clear()
            # clear the messages list widget and the message view
            self.ui.viewNotifTextEdit.clear()
            self.ui.notifMsgListWidget.clear()
            self.ui.notifMsgListWidget.hide()
            self.ui.noNotifMsgLabel.show()

    def load_notif_history(self):
        """
        This method loads the notification history excluding the current day's data
        """
        try:
            if self.ui.historyNotifButton.isChecked():
                # clear the messages filenames list and details
                self.notif_msgs.clear()
                self.notif_msgs_details.clear()
                # get the date folder name
                # get the current time
                cur_date_time = time.localtime()
                # get the date and time values
                year = cur_date_time.tm_year
                month = cur_date_time.tm_mon
                day_of_month = cur_date_time.tm_mday
                cur_dir_name = str(year) + "_" + str(month) + "_" + str(day_of_month)
                # get the path to the file
                parent_dir_path = self.resource_path("notifications" + os.sep + "shortage")
                # get a list of the notification dates
                notif_dirs = os.listdir(parent_dir_path)
                # get the history directory names by removing the current date
                try:
                    notif_dirs.remove(cur_dir_name)
                except:
                    pass
                if len(notif_dirs) > 0:
                    # sort the history directories in descending order
                    notif_dirs_copy = notif_dirs.copy()
                    notif_dirs.clear()
                    for dir_name in notif_dirs_copy:
                        year, month, day = dir_name.split("_")
                        d = datetime.date(int(year), int(month), int(day))
                        notif_dirs.append(d)
                    notif_dirs.sort()
                    notif_dirs.reverse()
                    notif_dirs_copy = notif_dirs.copy()
                    notif_dirs.clear()
                    for date_obj in notif_dirs_copy:
                        dir_name = str(date_obj.year) + "_" + str(date_obj.month) + "_" + str(date_obj.day)
                        notif_dirs.append(dir_name)
                    # create a list to hold all the history filenames
                    all_history_filenames = []
                    # get all the history filenames
                    for dir_name in notif_dirs:
                        # get the filenames in the directory
                        filenames = os.listdir(parent_dir_path + os.sep + dir_name)
                        # sort the files in ascending order
                        file_indices_list = []
                        for fname in filenames:
                            file_index = int(fname.split("_")[0])
                            file_indices_list.append(file_index)
                        file_indices_array = numpy.array(file_indices_list, dtype=int)
                        sorted_file_indices = numpy.argsort(file_indices_array)
                        filenames_copy = filenames.copy()
                        filenames.clear()
                        for index in sorted_file_indices:
                            filenames.append(filenames_copy[index])
                        all_history_filenames.extend(filenames)
                    # clear the current view notification
                    self.notif_filename = ""
                    # clear the messages list widget and the message view
                    self.ui.viewNotifTextEdit.clear()
                    self.ui.notifMsgListWidget.clear()
                    if len(all_history_filenames) > 0:
                        # add the history to the list widget
                        for fname in all_history_filenames:
                            date_time = fname.split("_")[1].replace(";", ":")
                            self.add_notif(date_time, "SHORTAGE OF ITEM(S)", "", "today", fname)
                    else:
                        self.ui.notifMsgListWidget.hide()
                        self.ui.noNotifMsgLabel.show()
                else:
                    # clear the messages filenames list
                    self.notif_msgs.clear()
                    # clear the messages list widget and the message view
                    self.ui.viewNotifTextEdit.clear()
                    self.ui.notifMsgListWidget.clear()
                    self.ui.notifMsgListWidget.hide()
                    self.ui.noNotifMsgLabel.show()
        except:
            # clear the messages filenames list
            self.notif_msgs.clear()
            # clear the messages list widget and the message view
            self.ui.viewNotifTextEdit.clear()
            self.ui.notifMsgListWidget.clear()
            self.ui.notifMsgListWidget.hide()
            self.ui.noNotifMsgLabel.show()

###################RECORDS###################

    def sales_history_add_record_to_table_widget(self, item_names, item_qtys, overall_cost, date_time, login_name="Admin", set_list=True):
        #argument: str, str, float, str, str, bool
        """
        This method add a row record to the records table widget
        """
        # insert row into sales records list
        if set_list:
            self.sales_records_history.insert(0, (item_names, item_qtys, overall_cost, date_time, login_name))
        # add the item to the cart table
        self.ui.recordsTableWidget.insertRow(0)
        name_item = QTableWidgetItem(item_names)
        qtys_item = QTableWidgetItem(item_qtys)
        overall_cost_item = QTableWidgetItem("{0:.2f}".format(float(overall_cost)))
        date_time_item = QTableWidgetItem(date_time)
        sales_person_item = QTableWidgetItem(login_name)
        # make rows uneditable
        name_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        qtys_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        overall_cost_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        date_time_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        sales_person_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        # add the table widget items to the table
        self.ui.recordsTableWidget.setItem(0, 0, name_item)
        self.ui.recordsTableWidget.setItem(0, 1, qtys_item)
        self.ui.recordsTableWidget.setItem(0, 2, overall_cost_item)
        self.ui.recordsTableWidget.setItem(0, 3, date_time_item)
        self.ui.recordsTableWidget.setItem(0, 4, sales_person_item)

    def sales_history_load_records(self):
        """
        This method loads the sales records from the database
        """
        # get the date
        date = self.ui.recordsSearchDateEdit.text().strip()
        day, month, year = date.split("/")
        month = self.months_list[int(month)-1]
        date = month + " " + day + ", " + year
        cur_year = int(year)  # get the year
        # start the load records thread
        self.sales_history_load_records_thread.set_parameters(date, cur_year)
        self.sales_history_load_records_thread.start()

    def sales_history_load_records_success(self, sales_load_records_history_success_signal):    #argument: list
        """
        This method gets the success signal after loading sales records
        """
        # get the sales records
        self.sales_records_history, history_cur_day_overall_cost = sales_load_records_history_success_signal
        # sort table data and display
        self.sales_history_sort_records_table()
        # display the overall cost
        self.ui.historyCurrentDayTotalSalesLabel.setText("{0:.2f}".format(history_cur_day_overall_cost))
        # reset the history file
        self.sales_history_records_history_file_index = -1
        self.list_of_sales_history_records_history_files.clear()
        # clear the records search history since date is changed
        try:
            for file in os.listdir(self.resource_path("search_history" + os.sep + "records")):
                os.remove(self.resource_path("search_history" + os.sep + "records" + os.sep + file))
        except:
            pass

    def sales_history_load_records_error(self, sales_history_load_records_error_signal):    #argument: str
        """
        This method gets the error signal after loading sales records
        """
        QMessageBox.critical(self, "Error", "Failed to load sales records!")

    def sales_history_flip_records_table(self):
        """
        This method flips/reverses the records table
        """
        # clear the table
        self.ui.recordsTableWidget.setRowCount(0)
        # add the data to the table in the reverse order
        for row in self.sales_records_history:
            item_names = row[0]
            item_qtys = row[1]
            overall_cost = str(row[2])
            date_time = row[3]
            login_name = row[4]
            self.sales_history_add_record_to_table_widget(item_names, item_qtys, overall_cost, date_time, login_name, False)
            QApplication.processEvents()
        # reverse table data to get the same order as in the table
        self.sales_records_history.reverse()

    def sales_history_sort_records_table(self):
        """
        This method sorts the sales records based the selected parameter
        """
        param = self.ui.recordsSortComboBox.currentText().lower().strip()
        if param == "time":
            col_index = 3
        else:
            col_index = 4
        # get the sorting data in the table
        list_of_data = []
        for row in self.sales_records_history:
            if col_index == 3:
                time = row[col_index].split()[4]
                list_of_data.append(int(time.replace(":", "")))
            else:
                list_of_data.append(row[col_index])
        # put the sorting data in a numpy array
        if col_index == 3:
            array_of_data = numpy.array(list_of_data, dtype=int)
        else:
            array_of_data = numpy.array(list_of_data, dtype=str)
        # sort the data in alphabetical order and get the indices of their rows
        sorted_data_indices = numpy.argsort(array_of_data)
        # create a copy of the table data
        table_data_copy = self.sales_records_history.copy()
        # clear the table data
        self.sales_records_history.clear()
        # set the table data in the sorted form
        for index in sorted_data_indices:
            self.sales_records_history.insert(0, table_data_copy[index])
        # clear the table
        self.ui.recordsTableWidget.setRowCount(0)
        # add the sorted data to the table
        for row in self.sales_records_history:
            item_names = row[0]
            item_qtys = row[1]
            overall_cost = str(row[2])
            date_time = row[3]
            login_name = row[4]
            self.sales_history_add_record_to_table_widget(item_names, item_qtys, overall_cost, date_time, login_name, False)
            QApplication.processEvents()
        # reverse table data to get the same order as in the table
        self.sales_records_history.reverse()

    def sales_history_search_autocomplete_data(self, auto_completion_data): #argument: list
        """
        This method sets the auto completion data into the search field
        """
        auto_completion_data = list(set(auto_completion_data))
        completer = QCompleter(auto_completion_data, self.ui.recordsSearchField)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.recordsSearchField.setCompleter(completer)

    def sales_history_search_records_param_effect(self):
        """
        This methods reacts to search parameter selection for performing searches
        """
        selected_param = self.ui.recordsSearchParamComboBox.currentText().lower().strip()
        if selected_param == "search by:":
            self.ui.recordsSearchField.setPlaceholderText("Type query here")
            self.sales_history_search_autocomplete_data([])
        elif selected_param == "item":
            self.ui.recordsSearchField.setPlaceholderText("Type item's name here")
            self.sales_history_search_autocomplete_data(list(self.items.keys()))
        elif selected_param == "time(hour)":
            self.ui.recordsSearchField.setPlaceholderText("Type hour here (0 to 23)")
            self.sales_history_search_autocomplete_data([])
        elif selected_param == "sales person":
            self.ui.recordsSearchField.setPlaceholderText("Type sales person's name here")
            self.sales_history_search_autocomplete_data(self.credentials_names)

    def sales_history_search_records(self):
        """
        This method searches the records for a query
        """
        # check if a search parameter is selected before proceeding
        if self.ui.recordsSearchParamComboBox.currentText() != "Search By:":
            # get the search parameter
            search_param_for_history = self.ui.recordsSearchParamComboBox.currentText()
            item_search_param = search_param_for_history.strip().lower()
            # get the text to search and search column index
            item_to_search = ""
            search_column_index = -1
            if item_search_param == "item":
                item_to_search = self.ui.recordsSearchField.text().strip()
                search_column_index = 0
            elif item_search_param == "time(hour)":
                item_to_search = self.ui.recordsSearchField.text().strip()
                search_column_index = 3
            elif item_search_param == "sales person":
                item_to_search = self.ui.recordsSearchField.text().strip()
                search_column_index = 4
            match_found = False     # notify for a match
            punc_chars = ["/", ",", ".", ";", "\\", "\\\\", "?", "!", ":", "*", "#"]
            # remove punctuation symbols from the item to be searched
            for ch in punc_chars:
                item_to_search = item_to_search.replace(ch, "")     # remove all puntuation marks before search
                item_to_search = item_to_search.replace("  ", " ")   # replace double spaces with single spaces
            if item_to_search.strip() != "":
                if self.ui.recordsTableWidget.rowCount() > 0:
                    try:
                        # create a search data list to hold the list of items that serve as the dictionary
                        search_data_list = []
                        if search_column_index >= 0:
                            # extract the item descriptions from the items table data
                            for row in self.sales_records_history:
                                search_data_list.append(row[search_column_index])
                            # remove punctuation symbols from the search list data
                            for item in search_data_list:
                                # remove the colon from the punctuation list if search parameter is time
                                try:
                                    if item_search_param == "time(hour)":
                                        punc_chars.remove(":")
                                except:
                                    pass
                                for ch in punc_chars:
                                    item = item.replace(ch, "")     # remove all puntuation marks before search
                                    item = item.replace("  ", " ")   # replace double spaces with single spaces
                                # if the search parameter is time, search and see if the hour exists
                                if item_search_param == "time(hour)":
                                    if item.split()[4].split(":")[0] == item_to_search:
                                        match_found = True
                                        break
                                else:
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
                                    if item_search_param == "time(hour)":
                                        if search_data.split()[4].split(":")[0] == item_to_search:
                                            row_indices_of_items.insert(0, index)
                                    else:
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
                                    name_item = self.ui.recordsTableWidget.takeItem(row_index_of_item, 0)
                                    qty_item = self.ui.recordsTableWidget.takeItem(row_index_of_item, 1)
                                    total_cost_item = self.ui.recordsTableWidget.takeItem(row_index_of_item, 2)
                                    date_item = self.ui.recordsTableWidget.takeItem(row_index_of_item, 3)
                                    sales_person_item = self.ui.recordsTableWidget.takeItem(row_index_of_item, 4)
                                    # add all the selected rows with their items to a list
                                    selected_rows.append([name_item, qty_item, total_cost_item, date_item, sales_person_item])
                                # remove the selected rows from their previous positions
                                for row_index_of_item in row_indices_of_items:
                                    if row_shift_count == 0:
                                        self.ui.recordsTableWidget.removeRow(row_index_of_item)
                                        self.sales_records_history.pop(row_index_of_item)
                                        row_shift_count += 1
                                    else:
                                        try:
                                            self.ui.recordsTableWidget.removeRow(row_index_of_item - row_shift_count)
                                            self.sales_records_history.pop(row_index_of_item - row_shift_count)
                                            row_shift_count += 1
                                        except:
                                            self.ui.recordsTableWidget.removeRow(row_index_of_item)
                                            self.sales_records_history.pop(row_index_of_item)
                                            row_shift_count += 1
                                # reverse the selected rows so as to obtain the same order after adding to the table
                                selected_rows.reverse()
                                # clear the table of the other data which are not included in the search results.
                                # this is to ensure that only the search results are displayed in the table
                                self.ui.recordsTableWidget.setRowCount(0)
                                self.sales_records_history.clear()
                                # get the selected rows to the top and rearrange the table
                                for row in selected_rows:
                                    row_data = (row[0].text(), row[1].text(), float(row[2].text()), row[3].text(), row[4].text())
                                    self.sales_records_history.insert(0, row_data)
                                # sort the table data according to the present sorting parameter selected
                                self.sales_history_sort_records_table()
                                # add search to history
                                self.sales_history_save_search_history(search_param_for_history, item_to_search, self.sales_records_history)
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

    def sales_history_save_search_history(self, search_param, item_searched, search_results):   #argument: str, str, list
        """
        This method saves the history of a search
        """
        # pack the search data into a dictionary
        history_data = {"search_param": search_param, "item_searched": item_searched, "search_results": search_results}
        # count existing history files
        history_file_count = len(os.listdir(self.resource_path("search_history" + os.sep + "records")))
        # get a list of the names of the history files.
        self.list_of_sales_history_records_history_files = [str(x) + ".pkl" for x in range(1, history_file_count + 2)]
        self.sales_history_records_history_file_index = -1
        # save the history to a pickle file
        history_filename = str(history_file_count + 1) + ".pkl"
        history_file = open(self.resource_path("search_history" + os.sep + "records" + os.sep + history_filename), "wb")
        pickle.dump(history_data, history_file)
        history_file.close()

    def sales_history_previous_records_search(self):
        """
        This method loads the previous search results
        """
        try:
            # get the previous search history
            self.sales_history_records_history_file_index -= 1
            history_filename = self.list_of_sales_history_records_history_files[self.sales_history_records_history_file_index]
            history_file = open(self.resource_path("search_history" + os.sep + "records" + os.sep + history_filename), "rb")
            history_data = pickle.load(history_file)
            history_file.close()
            # get the history data items
            search_param = history_data["search_param"]
            item_searched = history_data["item_searched"]
            search_results = history_data["search_results"]
            # insert the search history data items to their respective fields
            self.ui.recordsSearchParamComboBox.setCurrentText(search_param)
            self.ui.recordsSearchField.setText(item_searched)
            # clear the table and add data to table
            self.ui.recordsTableWidget.setRowCount(0)
            search_results.reverse()
            for row in search_results:
                self.sales_history_add_record_to_table_widget(*row)
                QApplication.processEvents()
            # set the table data list to the history data
            search_results.reverse()
            self.sales_records_history = search_results
        except:
            # set current history file to the previously valid one
            self.sales_history_records_history_file_index += 1
            QMessageBox.information(self, "Search Alert", "No previous search history available")

    def sales_history_next_records_search(self):
        """
        This method loads the next search results
        """
        try:
            # get the next search history
            if self.sales_history_records_history_file_index < -1:
                self.sales_history_records_history_file_index += 1
                history_filename = self.list_of_sales_history_records_history_files[self.sales_history_records_history_file_index]
                history_file = open(self.resource_path("search_history" + os.sep + "records" + os.sep + history_filename), "rb")
                history_data = pickle.load(history_file)
                history_file.close()
                # get the history data items
                search_param = history_data["search_param"]
                item_searched = history_data["item_searched"]
                search_results = history_data["search_results"]
                # insert the search history data items to their respective fields
                self.ui.recordsSearchParamComboBox.setCurrentText(search_param)
                self.ui.recordsSearchField.setText(item_searched)
                # clear the table and add data to table
                self.ui.recordsTableWidget.setRowCount(0)
                search_results.reverse()
                for row in search_results:
                    self.sales_history_add_record_to_table_widget(*row)
                    QApplication.processEvents()
                # set the table data list to the history data
                search_results.reverse()
                self.sales_records_history = search_results
            else:
                QMessageBox.information(self, "Search Alert", "No next search history available")
        except:
            QMessageBox.information(self, "Search Alert", "No next search history available")

    def add_menus_to_view_graphs_btns(self):
        """
        This method adds menu items the view graphs toolbuttons
        """
        # DAILY SALES
        self.daily_sales_menu = QMenu()
        # daily line graph action
        self.daily_line_graph_action = QAction("Line Graph", self.ui.dailyRecordsViewButton)
        self.daily_line_graph_action.triggered.connect(lambda: self.sales_history_view_daily_graphs("line_graph"))
        self.daily_sales_menu.addAction(self.daily_line_graph_action)
        # daily histogram action
        self.daily_bar_chart_action = QAction("Bar Chart", self.ui.dailyRecordsViewButton)
        self.daily_bar_chart_action.triggered.connect(lambda: self.sales_history_view_daily_graphs("bar_chart"))
        self.daily_sales_menu.addAction(self.daily_bar_chart_action)
        # add actions to button
        self.ui.dailyRecordsViewButton.addActions([self.daily_line_graph_action, self.daily_bar_chart_action])
        # MONTHLY SALES
        self.monthly_sales_menu = QMenu()
        # monthly line graph action
        self.monthly_line_graph_action = QAction("Line Graph", self.ui.monthlyRecordsViewButton)
        self.monthly_line_graph_action.triggered.connect(lambda: self.sales_history_view_monthly_graphs("line_graph"))
        self.monthly_sales_menu.addAction(self.monthly_line_graph_action)
        # monthly histogram action
        self.monthly_bar_chart_action = QAction("Bar Chart", self.ui.monthlyRecordsViewButton)
        self.monthly_bar_chart_action.triggered.connect(lambda: self.sales_history_view_monthly_graphs("bar_chart"))
        self.monthly_sales_menu.addAction(self.monthly_bar_chart_action)
        # add actions to button
        self.ui.monthlyRecordsViewButton.addActions([self.monthly_line_graph_action, self.monthly_bar_chart_action])
        # ANNUAL SALES
        self.yearly_sales_menu = QMenu()
        # annual line graph action
        self.yearly_line_graph_action = QAction("Line Graph", self.ui.yearlyRecordsViewButton)
        self.yearly_line_graph_action.triggered.connect(lambda: self.sales_history_view_yearly_graphs("line_graph"))
        self.yearly_sales_menu.addAction(self.yearly_line_graph_action)
        # annual histogram action
        self.yearly_bar_chart_action = QAction("Bar Chart", self.ui.yearlyRecordsViewButton)
        self.yearly_bar_chart_action.triggered.connect(lambda: self.sales_history_view_yearly_graphs("bar_chart"))
        self.yearly_sales_menu.addAction(self.yearly_bar_chart_action)
        # add actions to button
        self.ui.yearlyRecordsViewButton.addActions([self.yearly_line_graph_action, self.yearly_bar_chart_action])

    def sales_history_view_daily_graphs(self, graph_type): # argument: str
        """
        This method shows the graphs of sales made on a daily basis in a selected month
        """
        # get the selected month and year
        selected_month = self.ui.recordsDailyMonthComboBox.currentText()
        selected_year = str(self.ui.recordsDailyYearSpinBox.value())
        if self.months_list.__contains__(selected_month):
            # show loading label
            self.ui.loadingGraphAnimLabel.show()
            # start the daily sales data thread
            self.fig_index += 1
            self.get_daily_sales_data_thread.set_parameters(selected_month, selected_year, graph_type, self.fig_index)
            self.get_daily_sales_data_thread.start()
        else:
            QMessageBox.critical(self, "Error", "No month selected!")

    def sales_history_view_daily_graphs_success(self, sales_history_view_daily_graphs_success_signal): # argument: list
        """
        This method gets the plotting data for daily sales and plots the data
        """
        x_vals, y_vals, overall_total_income, graph_type, fig_index, month, year = sales_history_view_daily_graphs_success_signal
        # display graph details in a table
        window_dict_key = "daily" + str(fig_index)
        self.graph_windows[window_dict_key] = DailyGraphWindow(x_vals, y_vals, overall_total_income, graph_type, fig_index, month, year)
        self.graph_windows[window_dict_key].show()
        # hide loading label
        self.ui.loadingGraphAnimLabel.hide()

    def sales_history_view_daily_graphs_error(self, sales_history_view_daily_graphs_error_signal): # argument: str
        """
        This method gets the plotting data for daily sales errors
        """
        # hide loading label
        self.ui.loadingGraphAnimLabel.hide()
        QMessageBox.information(self, "Alert", "No data exists for the selected month!")

    def sales_history_view_monthly_graphs(self, graph_type): # argument: str
        """
        This method shows the graphs of sales made on a monthly basis in a selected month
        """
        # show loading label
        self.ui.loadingGraphAnimLabel.show()
        # get the selected year
        selected_year = str(self.ui.recordsMonthlyYearSpinBox.value())
        # start the daily sales data thread
        self.fig_index += 1
        self.get_monthly_sales_data_thread.set_parameters(selected_year, graph_type, self.fig_index)
        self.get_monthly_sales_data_thread.start()

    def sales_history_view_monthly_graphs_success(self, sales_history_view_monthly_graphs_success_signal): # argument: list
        """
        This method gets the plotting data for monthly sales and plots the data
        """
        x_vals, y_vals, overall_total_income, graph_type, fig_index, year = sales_history_view_monthly_graphs_success_signal
        # display graph details in a table
        window_dict_key = "monthly" + str(fig_index)
        self.graph_windows[window_dict_key] = MonthlyGraphWindow(x_vals, y_vals, overall_total_income, graph_type, fig_index, year)
        self.graph_windows[window_dict_key].show()
        # hide loading label
        self.ui.loadingGraphAnimLabel.hide()

    def sales_history_view_monthly_graphs_error(self, sales_history_view_monthly_graphs_error_signal):
        """
        This method gets the plotting data for monthly sales errors
        """
        # hide loading label
        self.ui.loadingGraphAnimLabel.hide()
        QMessageBox.information(self, "Alert", "No data exists for the selected year!")

    def sales_history_view_yearly_graphs(self, graph_type): # argument: str
        """
        This method shows the graphs of sales made on a yearly basis in a selected month
        """
        # get the selected year
        from_year = self.ui.recordsYearlyFromYearSpinBox.value()
        to_year = self.ui.recordsYearlyToYearSpinBox.value()
        if from_year < to_year:
            # show loading label
            self.ui.loadingGraphAnimLabel.show()
            # start the daily sales data thread
            self.fig_index += 1
            self.get_yearly_sales_data_thread.set_parameters(from_year, to_year, graph_type, self.fig_index)
            self.get_yearly_sales_data_thread.start()
        else:
            QMessageBox.critical(self, "Error", "Year 'From' must be less than year 'To'!")

    def sales_history_view_yearly_graphs_success(self, sales_history_view_yearly_graphs_success_signal): # argument: list
        """
        This method gets the plotting data for monthly sales and plots the data
        """
        x_vals, y_vals, overall_total_income, graph_type, fig_index, from_year, to_year = sales_history_view_yearly_graphs_success_signal
        # display graph details in a table
        window_dict_key = "yearly" + str(fig_index)
        self.graph_windows[window_dict_key] = YearlyGraphWindow(x_vals, y_vals, overall_total_income, graph_type, fig_index, from_year, to_year)
        self.graph_windows[window_dict_key].show()
        # hide loading label
        self.ui.loadingGraphAnimLabel.hide()

    def sales_history_view_yearly_graphs_error(self, sales_history_view_monthly_graphs_error_signal):
        """
        This method gets the plotting data for monthly sales errors
        """
        # hide loading label
        self.ui.loadingGraphAnimLabel.hide()
        QMessageBox.critical(self, "Error", "Unable to retrieve data for years!")

###################SETTINGS###################

    def switch_to_account_settings(self):
        """
        This method switches view to the account settings page
        """
        self.ui.accountSettingsButton.setChecked(True)
        self.ui.stockSettingsButton.setChecked(False)
        self.ui.otherSettingsButton.setChecked(False)
        self.ui.settingsStackedWidget.setCurrentWidget(self.ui.accountSettingsPage)

    def switch_to_stock_settings(self):
        """
        This method switches view to the stock settings page
        """
        self.ui.accountSettingsButton.setChecked(False)
        self.ui.stockSettingsButton.setChecked(True)
        self.ui.otherSettingsButton.setChecked(False)
        self.ui.settingsStackedWidget.setCurrentWidget(self.ui.stockSettingsPage)

    def switch_to_other_settings(self):
        """
        This method switches view to the other settings page
        """
        self.ui.accountSettingsButton.setChecked(False)
        self.ui.stockSettingsButton.setChecked(False)
        self.ui.otherSettingsButton.setChecked(True)
        self.ui.settingsStackedWidget.setCurrentWidget(self.ui.otherSettingsPage)

    def add_sales_person(self):
        """
        This method calls the add sales person thread
        """
        username = self.ui.addSalesPersonUsernameLineEdit.text().strip()
        password = self.ui.addSalesPersonPasswordLineEdit.text().strip()
        confirm_password = self.ui.addSalesPersonConfirmPasswordLineEdit.text().strip()
        if username != "" and password != "" and confirm_password != "":
            if password == confirm_password:
                self.add_sales_person_thread.set_parameters(username, password)
                self.add_sales_person_thread.start()
            else:
                QMessageBox.critical(self, "Error", "Password and Confirm Password do not match!")
        else:
            QMessageBox.critical(self, "Error", "Provide both username and password!")

    def add_sales_person_success(self, add_sales_person_success_signal): # argument: str
        """
        This method gets the success signal from the add sales person thread
        """
        # get the sales person's name and add to the autocompletion data
        sales_person_name = add_sales_person_success_signal
        self.credentials_names.append(sales_person_name)
        credentials_names_copy = self.credentials_names.copy()
        self.settings_populate_sales_persons_comboboxes(credentials_names_copy)
        self.sales_search_records_param_effect()
        self.sales_history_search_records_param_effect()
        QMessageBox.information(self, "Alert", "Successfully added " + sales_person_name + " as a sales person!")

    def add_sales_person_error(self, add_sales_person_error_signal): # argument: str
        """
        This method gets the error signal from the add sales person thread
        """
        if add_sales_person_error_signal == "uname_exists":
            QMessageBox.critical(self, "Error", "Username already exists!")
        elif add_sales_person_error_signal == "error":
            QMessageBox.critical(self, "Error", "Failed to add sales person!")

    def add_sales_person_hide_show_password(self):
        """
        This method hides/shows the password in the add sales person password field
        """
        try:
            if self.add_sales_person_password_hidden:
                self.ui.addSalesPersonPasswordLineEdit.setEchoMode(QLineEdit.Normal)
                self.ui.addSalesPersonHideShowPasswordButton.setIcon(QIcon(self.hide_icon))
                self.ui.addSalesPersonHideShowPasswordButton.setToolTip("Hide Password")
                self.add_sales_person_password_hidden = False
            else:
                self.ui.addSalesPersonPasswordLineEdit.setEchoMode(QLineEdit.Password)
                self.ui.addSalesPersonHideShowPasswordButton.setIcon(QIcon(self.show_icon))
                self.ui.addSalesPersonHideShowPasswordButton.setToolTip("Show Password")
                self.add_sales_person_password_hidden = True
        except:
            pass

    def add_sales_person_hide_show_confirm_password(self):
        """
        This method hides/shows the password in the add sales person confirm password field
        """
        try:
            if self.add_sales_person_confirm_password_hidden:
                self.ui.addSalesPersonConfirmPasswordLineEdit.setEchoMode(QLineEdit.Normal)
                self.ui.addSalesPersonShowHideConfirmPasswordButton.setIcon(QIcon(self.hide_icon))
                self.ui.addSalesPersonShowHideConfirmPasswordButton.setToolTip("Hide Password")
                self.add_sales_person_confirm_password_hidden = False
            else:
                self.ui.addSalesPersonConfirmPasswordLineEdit.setEchoMode(QLineEdit.Password)
                self.ui.addSalesPersonShowHideConfirmPasswordButton.setIcon(QIcon(self.show_icon))
                self.ui.addSalesPersonShowHideConfirmPasswordButton.setToolTip("Show Password")
                self.add_sales_person_confirm_password_hidden = True
        except:
            pass

    def settings_populate_sales_persons_comboboxes(self, items):     # argument: list
        """
        This method populates the items combobox
        """
        try:
            items.remove("Admin")
        except:
            pass
        items.sort()
        items.insert(0, "")
        self.ui.removeSalesPersonUsernameComboBox.clear()
        self.ui.editSalesPersonUsernameComboBox.clear()
        self.ui.removeSalesPersonUsernameComboBox.addItems(items)
        self.ui.editSalesPersonUsernameComboBox.addItems(items)
        self.ui.removeSalesPersonUsernameComboBox.setCurrentText("")
        self.ui.editSalesPersonUsernameComboBox.setCurrentText("")

    def remove_sales_person(self):
        """
        This method calls the remove sales person thread
        """
        username = self.ui.removeSalesPersonUsernameComboBox.currentText().strip()
        if username != "":
            self.remove_sales_person_thread.set_parameters(username)
            self.remove_sales_person_thread.start()
        else:
            QMessageBox.critical(self, "Error", "No sales person selected!")

    def remove_sales_person_success(self, remove_sales_person_success_signal): # argument: str
        """
        This method gets the success signal from the remove sales person thread
        """
        # get the sales person's name and remove to the autocompletion data
        sales_person_name = remove_sales_person_success_signal
        self.credentials_names.remove(sales_person_name)
        credentials_names_copy = self.credentials_names.copy()
        self.settings_populate_sales_persons_comboboxes(credentials_names_copy)
        self.sales_search_records_param_effect()
        self.sales_history_search_records_param_effect()
        QMessageBox.information(self, "Alert", "Successfully removed " + sales_person_name + "!")

    def remove_sales_person_error(self, remove_sales_person_error_signal): # argument: str
        """
        This method gets the error signal from the remove sales person thread
        """
        if remove_sales_person_error_signal == "not_exist":
            QMessageBox.critical(self, "Error", "Sales person does not exist!")
        elif remove_sales_person_error_signal == "error":
            QMessageBox.critical(self, "Error", "Failed to remove sales person!")

    def remove_sales_person_clear_username_combobox(self):
        """
        This method clears the remove sales person combobox
        """
        self.ui.removeSalesPersonUsernameComboBox.setCurrentText("")

    def edit_sales_person(self):
        """
        This method calls the edit sales person thread
        """
        cur_username = self.ui.editSalesPersonUsernameComboBox.currentText().strip()
        cur_password = self.ui.editSalesPersonCurrentPasswordLineEdit.text().strip()
        new_username = self.ui.editSalesPersonNewUsernameLineEdit.text().strip()
        new_password = self.ui.editSalesPersonNewPasswordLineEdit.text().strip()
        new_confirm_password = self.ui.editSalesPersonConfirmNewPasswordLineEdit.text().strip()
        if cur_username != "" and new_username != "" and cur_password != "" and new_password != "" and new_confirm_password != "":
            if new_username.lower() != "admin":
                # check if the current username exists
                if self.credentials_names.__contains__(cur_username):
                    # check if the new username already exists
                    if cur_username == new_username:
                        if new_password == new_confirm_password:
                            self.edit_sales_person_thread.set_parameters(cur_username, new_username, cur_password, new_password)
                            self.edit_sales_person_thread.start()
                        else:
                            QMessageBox.critical(self, "Error", "New Password and Confirm Password do not match!")
                    elif cur_username != new_username:
                        credentials_names_copy = self.credentials_names.copy()
                        credentials_names_copy.remove(cur_username)
                        if not credentials_names_copy.__contains__(new_username):
                            if new_password == new_confirm_password:
                                self.edit_sales_person_thread.set_parameters(cur_username, new_username, cur_password, new_password)
                                self.edit_sales_person_thread.start()
                            else:
                                QMessageBox.critical(self, "Error", "New Password and Confirm Password do not match!")
                        else:
                            QMessageBox.critical(self, "Error", "New username already exists!")
                else:
                    QMessageBox.critical(self, "Error", "Sales person does not exist!")
            else:
                QMessageBox.critical(self, "Error", "Invalid sales person username.\n'Admin' or 'admin' not allowed!")
        else:
            QMessageBox.critical(self, "Error", "Provide all the data requested in the form!")

    def edit_sales_person_success(self, edit_sales_person_success_signal): # argument: list
        """
        This method gets the success signal from the edit sales person thread
        """
        # get the sales person's name and add to the autocompletion data
        cur_sales_person_name, new_sales_person_name = edit_sales_person_success_signal
        self.credentials_names.remove(cur_sales_person_name)
        self.credentials_names.append(new_sales_person_name)
        credentials_names_copy = self.credentials_names.copy()
        self.settings_populate_sales_persons_comboboxes(credentials_names_copy)
        self.sales_search_records_param_effect()
        self.sales_history_search_records_param_effect()
        QMessageBox.information(self, "Alert", "Successfully updated " + cur_sales_person_name + " info!")

    def edit_sales_person_error(self, edit_sales_person_error_signal): # argument: str
        """
        This method gets the error signal from the edit sales person thread
        """
        if edit_sales_person_error_signal == "wrong_password":
            QMessageBox.critical(self, "Error", "Incorrect current password!")
        elif edit_sales_person_error_signal == "error":
            QMessageBox.critical(self, "Error", "Failed to update sales person!")

    def edit_sales_person_clear_username_combobox(self):
        """
        This method clears the remove sales person combobox
        """
        self.ui.editSalesPersonUsernameComboBox.setCurrentText("")

    def edit_sales_person_hide_show_current_password(self):
        """
        This method hides/shows the current password in the edit sales person current password field
        """
        try:
            if self.edit_sales_person_current_password_hidden:
                self.ui.editSalesPersonCurrentPasswordLineEdit.setEchoMode(QLineEdit.Normal)
                self.ui.editSalesPersonShowHideCurrentPasswordButton.setIcon(QIcon(self.hide_icon))
                self.ui.editSalesPersonShowHideCurrentPasswordButton.setToolTip("Hide Password")
                self.edit_sales_person_current_password_hidden = False
            else:
                self.ui.editSalesPersonCurrentPasswordLineEdit.setEchoMode(QLineEdit.Password)
                self.ui.editSalesPersonShowHideCurrentPasswordButton.setIcon(QIcon(self.show_icon))
                self.ui.editSalesPersonShowHideCurrentPasswordButton.setToolTip("Show Password")
                self.edit_sales_person_current_password_hidden = True
        except:
            pass

    def edit_sales_person_hide_show_new_password(self):
        """
        This method hides/shows the new password in the edit sales person new password field
        """
        try:
            if self.edit_sales_person_new_password_hidden:
                self.ui.editSalesPersonNewPasswordLineEdit.setEchoMode(QLineEdit.Normal)
                self.ui.editSalesPersonShowHideNewPasswordButton.setIcon(QIcon(self.hide_icon))
                self.ui.editSalesPersonShowHideNewPasswordButton.setToolTip("Hide Password")
                self.edit_sales_person_new_password_hidden = False
            else:
                self.ui.editSalesPersonNewPasswordLineEdit.setEchoMode(QLineEdit.Password)
                self.ui.editSalesPersonShowHideNewPasswordButton.setIcon(QIcon(self.show_icon))
                self.ui.editSalesPersonShowHideNewPasswordButton.setToolTip("Show Password")
                self.edit_sales_person_new_password_hidden = True
        except:
            pass

    def edit_sales_person_hide_show_confirm_password(self):
        """
        This method hides/shows the confirm password in the edit sales person confirm password field
        """
        try:
            if self.edit_sales_person_confirm_password_hidden:
                self.ui.editSalesPersonConfirmNewPasswordLineEdit.setEchoMode(QLineEdit.Normal)
                self.ui.editSalesPersonShowHideConfirmPasswordButton.setIcon(QIcon(self.hide_icon))
                self.ui.editSalesPersonShowHideConfirmPasswordButton.setToolTip("Hide Password")
                self.edit_sales_person_confirm_password_hidden = False
            else:
                self.ui.editSalesPersonConfirmNewPasswordLineEdit.setEchoMode(QLineEdit.Password)
                self.ui.editSalesPersonShowHideConfirmPasswordButton.setIcon(QIcon(self.show_icon))
                self.ui.editSalesPersonShowHideConfirmPasswordButton.setToolTip("Show Password")
                self.edit_sales_person_confirm_password_hidden = True
        except:
            pass

    def view_all_sales_persons(self):
        """
        This method opens the view all sales persons dialog
        """
        self.view_all_sales_persons_dialog = ViewAllSalesPersonsDialog()
        self.view_all_sales_persons_dialog.show()

    def edit_admin(self):
        """
        This method calls the edit admin thread
        """
        cur_password = self.ui.editAdminCurrentPasswordLineEdit.text().strip()
        new_password = self.ui.editAdminNewPasswordLineEdit.text().strip()
        new_confirm_password = self.ui.editAdminConfirmPasswordLineEdit.text().strip()
        if cur_password != "" and new_password != "" and new_confirm_password != "":
            if new_password == new_confirm_password:
                self.edit_admin_thread.set_parameters(cur_password, new_password)
                self.edit_admin_thread.start()
            else:
                QMessageBox.critical(self, "Error", "New Password and Confirm Password do not match!")
        else:
            QMessageBox.critical(self, "Error", "Provide all the data requested in the form!")

    def edit_admin_success(self, edit_admin_success_signal): # argument: str
        """
        This method receives the edit admin success signal
        """
        QMessageBox.information(self, "Alert", "Successfully updated Admin info")

    def edit_admin_error(self, edit_admin_error_signal): # argument: str
        """
        This method receives the edit admin error signal
        """
        if edit_admin_error_signal == "wrong_password":
            QMessageBox.critical(self, "Error", "Incorrect current password!")
        elif edit_admin_error_signal == "error":
            QMessageBox.critical(self, "Error", "Failed to update Admin!")

    def edit_admin_hide_show_current_password(self):
        """
        This method hides/shows the current password in the edit admin current password field
        """
        try:
            if self.edit_admin_current_password_hidden:
                self.ui.editAdminCurrentPasswordLineEdit.setEchoMode(QLineEdit.Normal)
                self.ui.editAdminShowHideCurrentPasswordButton.setIcon(QIcon(self.hide_icon))
                self.ui.editAdminShowHideCurrentPasswordButton.setToolTip("Hide Password")
                self.edit_admin_current_password_hidden = False
            else:
                self.ui.editAdminCurrentPasswordLineEdit.setEchoMode(QLineEdit.Password)
                self.ui.editAdminShowHideCurrentPasswordButton.setIcon(QIcon(self.show_icon))
                self.ui.editAdminShowHideCurrentPasswordButton.setToolTip("Show Password")
                self.edit_admin_current_password_hidden = True
        except:
            pass

    def edit_admin_hide_show_new_password(self):
        """
        This method hides/shows the new password in the edit admin new password field
        """
        try:
            if self.edit_admin_new_password_hidden:
                self.ui.editAdminNewPasswordLineEdit.setEchoMode(QLineEdit.Normal)
                self.ui.editAdminShowHideNewPasswordButton.setIcon(QIcon(self.hide_icon))
                self.ui.editAdminShowHideNewPasswordButton.setToolTip("Hide Password")
                self.edit_admin_new_password_hidden = False
            else:
                self.ui.editAdminNewPasswordLineEdit.setEchoMode(QLineEdit.Password)
                self.ui.editAdminShowHideNewPasswordButton.setIcon(QIcon(self.show_icon))
                self.ui.editAdminShowHideNewPasswordButton.setToolTip("Show Password")
                self.edit_admin_new_password_hidden = True
        except:
            pass

    def edit_admin_hide_show_confirm_password(self):
        """
        This method hides/shows the confirm password in the edit admin confirm password field
        """
        try:
            if self.edit_admin_confirm_password_hidden:
                self.ui.editAdminConfirmPasswordLineEdit.setEchoMode(QLineEdit.Normal)
                self.ui.editAdminShowHideConfirmPasswordButton.setIcon(QIcon(self.hide_icon))
                self.ui.editAdminShowHideConfirmPasswordButton.setToolTip("Hide Password")
                self.edit_admin_confirm_password_hidden = False
            else:
                self.ui.editAdminConfirmPasswordLineEdit.setEchoMode(QLineEdit.Password)
                self.ui.editAdminShowHideConfirmPasswordButton.setIcon(QIcon(self.show_icon))
                self.ui.editAdminShowHideConfirmPasswordButton.setToolTip("Show Password")
                self.edit_admin_confirm_password_hidden = True
        except:
            pass

    def add_new_item(self):
        """
        This method calls the thread that adds a new item to the stock
        """
        item_name = self.ui.addNewItemDescLineEdit.text().strip().upper()
        price = "{0:.2f}".format(self.ui.addNewItemUnitPriceSpinBox.value())
        quantity = str(self.ui.addNewItemQtySpinBox.value())
        all_item_names = list(self.items.keys())
        if item_name != "":
            if not all_item_names.__contains__(item_name):
                self.add_new_item_thread.set_parameters(item_name, price, quantity)
                self.add_new_item_thread.start()
            else:
                QMessageBox.critical(self, "Error", item_name.upper() + " already exists!")
        else:
            QMessageBox.critical(self, "Error", "Provide all the data requested in the form!")

    def add_new_item_success(self, add_new_item_success_signal): # argument: list
        """
        This method gets the success signal from the add new item thread
        """
        item_name, price, quantity = add_new_item_success_signal
        self.items[item_name] = [float(price), int(quantity)]
        # populate the items and quantity comboboxes
        item_names = list(self.items.keys())
        item_names.sort()
        self.sales_populate_item_list(item_names)
        QMessageBox.information(self, "Alert", "Successfully added " + item_name + "!")

    def add_new_item_error(self, add_new_item_error_signal): # argument: str
        """
        This method gets the error signal from the add new item thread
        """
        QMessageBox.critical(self, "Error", "Failed to add item!")

    def reset_add_new_item_fields(self):
        """
        This method clears the add new item fields
        """
        self.ui.addNewItemDescLineEdit.clear()
        self.ui.addNewItemUnitPriceSpinBox.setValue(0.00)
        self.ui.addNewItemQtySpinBox.setValue(1)

    def remove_item(self):
        """
        This method calls the thread that removes an item from the stock
        """
        item_name = self.ui.removeItemChooseItemComboBox.currentText().strip().upper()
        all_item_names = list(self.items.keys())
        if item_name != "":
            if all_item_names.__contains__(item_name):
                self.remove_item_thread.set_parameters(item_name)
                self.remove_item_thread.start()
            else:
                QMessageBox.critical(self, "Error", "Item does not exist in the stock!")
        else:
            QMessageBox.critical(self, "Error", "No item selected!")

    def remove_item_success(self, remove_item_success_signal): # argument: str
        """
        This method gets the success signal from the remove item thread
        """
        item_name = remove_item_success_signal
        self.items.pop(item_name)
        # populate the items and quantity comboboxes
        item_names = list(self.items.keys())
        item_names.sort()
        self.sales_populate_item_list(item_names)
        QMessageBox.information(self, "Alert", "Successfully removed " + item_name + "!")

    def remove_item_error(self, remove_item_error_signal): # argument: str
        """
        This method gets the error signal from the remove item thread
        """
        QMessageBox.critical(self, "Error", "Failed to remove item from the stock!")

    def remove_item_get_price_and_qty(self):
        """
        This method gets the price and quantity of the selected item and displays them if available
        """
        try:
            item_name = self.ui.removeItemChooseItemComboBox.currentText().strip().upper()
            price, qty = self.items[item_name]
            self.ui.removeItemUnitPriceLineEdit.setText(str(price))
            self.ui.removeItemQtyLineEdit.setText(str(qty))
        except:
            self.ui.removeItemUnitPriceLineEdit.clear()
            self.ui.removeItemQtyLineEdit.clear()

    def open_all_items_window(self):
        """
        This method opens the window that contains all the items
        """
        self.view_all_items_window = ViewAllItemsWindow()
        self.view_all_items_window.show()

    def edit_item(self):
        """
        This method calls the thread that edits the items in the stock
        """
        item_name = self.ui.editItemChooseItemComboBox.currentText().strip().upper()
        all_item_names = list(self.items.keys())
        if item_name != "":
            if all_item_names.__contains__(item_name):
                cur_quantity = int(self.ui.editItemCurrentQtyLineEdit.text())
                add_quantity = self.ui.editItemAddQtySpinBox.value()
                new_quantity = cur_quantity + add_quantity
                if new_quantity >= 0:
                    new_quantity = str(new_quantity)
                    new_unit_price = str(self.ui.editItemNewUnitPriceSpinBox.value())
                    # call the edit item thread
                    self.edit_item_thread.set_parameters(item_name, new_quantity, new_unit_price)
                    self.edit_item_thread.start()
                else:
                    QMessageBox.critical(self, "Error", "Invalid quantity!\nQuantity cannot be a negative value!")
            else:
                QMessageBox.critical(self, "Error", "Item does not exist in the stock!")
        else:
            QMessageBox.critical(self, "Error", "No item selected!")

    def edit_item_success(self, edit_item_success_signal): # argument: list
        """
        This method gets the success signal from the edit item thread
        """
        item_name, price, qty = edit_item_success_signal
        self.items[item_name] = [float(price), int(qty)]
        self.ui.editItemChooseItemComboBox.setCurrentText("")
        QMessageBox.information(self, "Alert", "Successfully updated " + item_name + "!")

    def edit_item_error(self, edit_item_error_signal): #argument: str
        """
        This method get the error signal from the edit item thread
        """
        QMessageBox.critical(self, "Error", "Failed to update item!")

    def edit_item_get_price_and_qty(self):
        """
        This method gets the price and quantity of the item selected and displays them
        """
        try:
            item_name = self.ui.editItemChooseItemComboBox.currentText().strip().upper()
            price, qty = self.items[item_name]
            self.ui.editItemCurrentUnitPriceLineEdit.setText(str(price))
            self.ui.editItemCurrentQtyLineEdit.setText(str(qty))
            self.ui.editItemNewUnitPriceSpinBox.setValue(price)
        except:
            self.ui.editItemCurrentUnitPriceLineEdit.clear()
            self.ui.editItemCurrentQtyLineEdit.clear()
            self.ui.editItemNewUnitPriceSpinBox.setValue(0.00)

    def edit_item_reset_fields_button(self):
        """
        This method resets the edit item fields
        """
        self.ui.editItemChooseItemComboBox.setCurrentText("")
        self.ui.editItemCurrentQtyLineEdit.clear()
        self.ui.editItemCurrentUnitPriceLineEdit.clear()
        self.ui.editItemAddQtySpinBox.setValue(0)
        self.ui.editItemNewUnitPriceSpinBox.setValue(0.00)

    def save_notif_settings(self):
        """
        This method saves the notification settings
        """
        try:
            self.min_qty_to_notify = self.ui.notificationMinQtyOfItemsToNotifySpinBox.value()
            self.settings["min_qty_to_notify"] = self.min_qty_to_notify
            settings_file_path = self.resource_path("data_files" + os.sep + "settings.pkl")
            settings_file = open(settings_file_path, "wb")
            pickle.dump(self.settings, settings_file)
            settings_file.close()
            QMessageBox.information(self, "Alert", "Successfully saved notification settings!")
        except:
            QMessageBox.critical(self, "Error", "Failed to save notification settings!")

    def save_backup_settings(self):
        """
        This method saves the backup settings
        """
        try:
            if self.ui.backupDataTurnOnOffAutoBackupCheckBox.isChecked():
                self.auto_backup_state = 1
            else:
                self.auto_backup_state = 0
            self.auto_backup_time_interval = self.ui.backupDataTimeIntervalSpinBox.value()
            self.settings["auto_backup"] = self.auto_backup_state
            self.settings["auto_backup_time_interval"] = self.auto_backup_time_interval
            settings_file_path = self.resource_path("data_files" + os.sep + "settings.pkl")
            settings_file = open(settings_file_path, "wb")
            pickle.dump(self.settings, settings_file)
            settings_file.close()
            QMessageBox.information(self, "Alert", "Successfully saved backup settings!")
        except:
            QMessageBox.critical(self, "Error", "Failed to save backup settings!")

    def load_settings(self):
        """
        This method loads the settings from a file
        """
        try:
            settings_file_path = self.resource_path("data_files" + os.sep + "settings.pkl")
            settings_file = open(settings_file_path, "rb")
            self.settings = pickle.load(settings_file)
            settings_file.close()
        except:
            self.settings = {"min_qty_to_notify": 10, "auto_backup": 0, "auto_backup_time_interval": 5}
        self.min_qty_to_notify = self.settings["min_qty_to_notify"]
        self.auto_backup_state = self.settings["auto_backup"]
        self.auto_backup_time_interval = self.settings["auto_backup_time_interval"]
        # set the backup state and interval in their fields
        if self.auto_backup_state == 1:
            self.ui.backupDataTurnOnOffAutoBackupCheckBox.setChecked(True)
        else:
            self.ui.backupDataTurnOnOffAutoBackupCheckBox.setChecked(False)
        self.ui.backupDataTimeIntervalSpinBox.setValue(self.auto_backup_time_interval)
        # start automatic backup if enabled
        self.auto_backup()

    def backup_now(self):
        """
        This method call the thread that backs up the data
        """
        self.ui.sellButton.setDisabled(True)
        self.ui.backupDataBackupNowButton.setText("Backing up ...")
        self.ui.backupDataBackupNowButton.setDisabled(True)
        self.ui.backupMenuButton.setDisabled(True)
        self.backup_now_thread.start()

    def backup_now_success(self, backup_now_success_signal):
        """
        This method gets the success signal from the backup now thread
        """
        if backup_now_success_signal == "backing_up":
            # show the loading labels
            self.ui.backupMenuAnimLabel.show()
            self.ui.backupAnimLabel.show()
        else:
            self.ui.backupMenuAnimLabel.hide()
            self.ui.backupAnimLabel.hide()
            self.ui.sellButton.setEnabled(True)
            self.ui.backupDataBackupNowButton.setText("Back Up Now")
            self.ui.backupDataBackupNowButton.setEnabled(True)
            self.ui.backupMenuButton.setEnabled(True)
            try:
                os.remove(self.resource_path("data_files" + os.sep + "backup.txt"))
            except:
                pass
            QMessageBox.information(self, "Alert", "Successfully backed up data")

    def backup_now_error(self, backup_now_error_signal):
        """
        This method gets the error signal from the backup now thread
        """
        self.ui.backupMenuAnimLabel.hide()
        self.ui.backupAnimLabel.hide()
        self.ui.sellButton.setEnabled(True)
        self.ui.backupDataBackupNowButton.setText("Back Up Now")
        self.ui.backupDataBackupNowButton.setEnabled(True)
        self.ui.backupMenuButton.setEnabled(True)
        if backup_now_error_signal == "internet_error":
            QMessageBox.critical(self, "Error", "No or poor internet connection!")
        elif backup_now_error_signal == "backup_error":
            QMessageBox.critical(self, "Error", "Backup failed!")
        elif backup_now_error_signal == "backup_failed":
            QMessageBox.critical(self, "Error", "Backup failed!\nUnable to access server!")
        elif backup_now_error_signal == "not_backup_data":
            QMessageBox.information(self, "Alert", "No backup data available!")

    def auto_backup(self):
        """
        This method call the thread that backs up the data automatically
        """
        self.auto_backup_thread.set_parameters(self.auto_backup_state, self.auto_backup_time_interval)
        self.auto_backup_thread.start()

    def auto_backup_success(self, auto_backup_success_signal):
        """
        This method gets the success signal from the auto backup thread
        """
        if auto_backup_success_signal == "backing_up":
            self.ui.backupMenuAnimLabel.show()
            self.ui.backupAnimLabel.show()
            self.ui.sellButton.setDisabled(True)
            self.ui.backupDataBackupNowButton.setText("Backing up ...")
            self.ui.backupDataBackupNowButton.setDisabled(True)
            self.ui.backupMenuButton.setDisabled(True)
        else:
            self.ui.backupMenuAnimLabel.hide()
            self.ui.backupAnimLabel.hide()
            self.ui.sellButton.setEnabled(True)
            self.ui.backupDataBackupNowButton.setText("Back Up Now")
            self.ui.backupDataBackupNowButton.setEnabled(True)
            self.ui.backupMenuButton.setEnabled(True)
            try:
                os.remove(self.resource_path("data_files" + os.sep + "backup.txt"))
            except:
                pass

    def auto_backup_error(self, auto_backup_error_signal):
        """
        This method gets the error signal from the auto backup thread
        """
        self.ui.backupMenuAnimLabel.hide()
        self.ui.backupAnimLabel.hide()
        self.ui.sellButton.setEnabled(True)
        self.ui.backupDataBackupNowButton.setText("Back Up Now")
        self.ui.backupDataBackupNowButton.setEnabled(True)
        self.ui.backupMenuButton.setEnabled(True)
        if auto_backup_error_signal == "internet_error":
            pass
        elif auto_backup_error_signal == "backup_error":
            pass
        elif auto_backup_error_signal == "backup_failed":
            pass
        elif auto_backup_error_signal == "not_backup_data":
            pass

    def load_firm_info(self):
        """
        This method loads the firm's info
        """
        try:
            firm_info_file = open(self.resource_path("data_files" + os.sep + "firm_info.txt"), "r")
            firm_name, firm_contact, firm_address = firm_info_file.read().split(query_sep)
            self.ui.firmNameLineEdit.setText(firm_name)
            self.ui.firmContactLineEdit.setText(firm_contact)
            self.ui.firmAddressLineEdit.setText(firm_address)
        except:
            QMessageBox.critical(self, "Error", "Failed to load the firm's info!")

    def update_firm_info(self):
        """
        This method update the firm's info
        """
        # get the firm info
        firm_name = self.ui.firmNameLineEdit.text().strip().upper()
        firm_contact = self.ui.firmContactLineEdit.text().strip()
        firm_address = self.ui.firmAddressLineEdit.text().strip().upper()
        if firm_name != "" and firm_contact != "" and firm_address != "":
            self.update_firm_info_thread.set_parameters(firm_name, firm_contact, firm_address)
            self.update_firm_info_thread.start()
        else:
            QMessageBox.critical(self, "Error", "Please complete the form!")

    def update_firm_info_success(self, update_firm_info_success_signal):
        """
        This method gets the success signal from the update firm info thread
        """
        QMessageBox.information(self, "Alert", "Successfully updated firm's info!")

    def update_firm_info_error(self, update_firm_info_error_signal):
        """
        This method gets the error signal from the update firm info thread
        """
        QMessageBox.critical(self, "Error", "Failed to update firm's info!")

    def restore_data(self):
        """
        This method starts the thread that restores the backed up data
        """
        ok_pressed = QMessageBox.question(self, "Alert", "Click YES to restore data!")
        if ok_pressed:
            self.ui.restoreDataButton.setText("Restoring Data ...")
            self.ui.restoreDataButton.setDisabled(True)
            self.ui.restoreDataAnimLabel.show()
            self.restore_data_thread.start()

    def restore_data_success(self, restore_data_success_signal):
        """
        This method gets the success signal from the restore data thread
        """
        self.ui.restoreDataButton.setText("Restore Data")
        self.ui.restoreDataButton.setEnabled(True)
        self.ui.restoreDataAnimLabel.hide()
        QMessageBox.information(self, "Alert", "Successfully restored data!\nRestart application to effect changes.")
        # log out of applicatioon
        self.logout_clicked = True
        self.close()
        self.login_window_obj.show()
##        ok_pressed = QMessageBox.question(self, "Alert", "Successfully restored data!\nDo you want to restart application?")
##        if ok_pressed == QMessageBox.Yes:
##            print("restart")

    def restore_data_error(self, restore_data_restore_signal):
        """
        This method gets the error signal from the restore data thread
        """
        self.ui.restoreDataButton.setText("Restore Data")
        self.ui.restoreDataButton.setEnabled(True)
        self.ui.restoreDataAnimLabel.hide()
        QMessageBox.critical(self, "Error", "Failed to restore data!")

    def log_out(self):
        """
        This method exits this window and opens the login window
        """
        ok_pressed = QMessageBox.question(self, "Confirm Log Out", "Do you really want to log out?")
        if ok_pressed == QMessageBox.Yes:
            self.logout_clicked = True
            self.close()
            self.login_window_obj.show()


if __name__=="__main__":
    # set the GUI style
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    # start the application
    app = QApplication(sys.argv)
    sms_window = SMS()
    sms_window.show()
    sys.exit(app.exec_())
