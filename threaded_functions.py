import os, sys, socket, sqlite3, pymysql, pickle, time, matplotlib.pyplot as plt, matplotlib as mpl, shutil
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication
import psword_encrypter


# this character sequence is used to separate different queries in the backup
# file
query_sep = "<?+/*-=?>"

def internet_conn_available():
    """
    This method checks if there is internet connection
    """
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except:
        pass
    return False

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

def record_backup_query(query): # argument: str
    """
    This method records an executed query to a file for backup purposes
    """
    try:
        backup_file = open(resource_path("data_files" + os.sep + "backup.txt"), "a")
        backup_file.write(query)
        backup_file.close()
    except:
        pass

def get_backup_script():
    """
    This method gets the backup script from the backup file and returns
    """
    try:
        backup_file = open(resource_path("data_files" + os.sep + "backup.txt"), "r")
        query = backup_file.read()
        backup_file.close()
        return query
    except:
        return ""

def get_db_conn_info(): # return [str, int, str, str, str]
    """
    This method gets the database connection info
    """
    try:
        db_conn_info_file = open(resource_path("data_files" + os.sep + "db_config.pkl"), "rb")
        db_conn_info = pickle.load(db_conn_info_file)
        db_hostname = db_conn_info["db_hostname"]
        db_port = db_conn_info["db_port"]
        db_username = db_conn_info["db_username"]
        db_password = db_conn_info["db_password"]
        db_name = db_conn_info["db_name"]
        db_conn_info_file.close()
        return [db_hostname, db_port, db_username, db_password, db_name]
    except:
        return ["", 3306, "", "", "sms_db"]

###################LOGIN###################

class LoginThread(QThread):
    """
    This thread logs the user into SMS
    """

    login_success_signal = pyqtSignal(list)
    login_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def set_parameters(self, username, password, date_time):
        """
        This method sets the parameters
        """
        self.username = username
        self.password = password
        self.date_time = date_time

    def run(self):
        try:
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            query = 'SELECT * FROM credentials WHERE USERNAME="' + self.username + '"'
            cursor = conn.execute(query)
            result = cursor.fetchone()
            if result:
                uname = result[0]
                psword = result[1]
                if psword_encrypter.decrypt(psword) == self.password:
                    # insert into the login records table
                    insert_login_record_query = 'INSERT INTO login_records VALUES("' + self.username + '","' + self.date_time + '");'
                    conn.execute(insert_login_record_query)
                    conn.commit()
                    conn.close()
                    # save the command for backup
                    record_backup_query(insert_login_record_query + query_sep)
                    # send the success signal
                    self.login_success_signal.emit([uname, psword])
                else:
                    self.login_error_signal.emit("wrong_credentials")
            else:
                self.login_error_signal.emit("wrong_credentials")
        except:
            self.login_error_signal.emit("error")

###################LOGIN SETUP###################

class LoginSetupThread(QThread):
    """
    This thread logs the user into SMS
    """

    login_setup_success_signal = pyqtSignal(list)
    login_setup_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def set_parameters(self, username, password, firm_name, firm_contact, firm_address, date_time):
        """
        This method sets the parameters
        """
        self.username = username
        self.password = password
        self.firm_name = firm_name
        self.firm_contact = firm_contact
        self.firm_address = firm_address
        self.date_time = date_time

    def run(self):
        try:
            # save the firm name to a file
            firm_info_file = open(resource_path("data_files" + os.sep + "firm_info.txt"), "w")
            firm_info = self.firm_name + query_sep + self.firm_contact + query_sep + self.firm_address
            firm_info_file.write(firm_info)
            firm_info_file.close()
            # submit username and password to database
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            # create items and credentials table
            try:
                create_items_table_query = "CREATE TABLE IF NOT EXISTS items (ITEM_NAME TEXT NOT NULL UNIQUE,UNIT_PRICE REAL NOT NULL," + \
                                           "QUANTITY INTEGER NOT NULL DEFAULT 0,PRIMARY KEY(ITEM_NAME));"
                create_credentials_table_query = "CREATE TABLE IF NOT EXISTS credentials (USERNAME TEXT NOT NULL UNIQUE,PASSWORD TEXT NOT " + \
                                                 "NULL UNIQUE,PRIMARY KEY(USERNAME,PASSWORD));"
                create_login_records_table_query = "CREATE TABLE IF NOT EXISTS login_records (USERNAME TEXT NOT NULL,LOGIN_TIME TEXT NOT NULL);"
                create_firm_info_table_query = "CREATE TABLE IF NOT EXISTS firm_info (ID INTEGER NOT NULL,FIRM_NAME TEXT NOT NULL,FIRM_CONTACT " + \
                                               "TEXT NOT NULL,FIRM_ADDRESS TEXT NOT NULL);"
                commands_list = []
                commands_list.append(create_items_table_query)
                commands_list.append(create_credentials_table_query)
                commands_list.append(create_login_records_table_query)
                commands_list.append(create_firm_info_table_query)
                for command in commands_list:
                    conn.execute(command)
            except:
                pass
            insert_credentials_query = 'INSERT INTO credentials VALUES("' + self.username + '","' + psword_encrypter.encrypt(self.password) + '");'
            insert_login_record_query = 'INSERT INTO login_records VALUES("' + self.username + '","' + self.date_time + '");'
            insert_firm_info_query = 'INSERT INTO firm_info VALUES(1,"firm_name","firm_contact","firm_address");'
            update_firm_info_query = 'UPDATE firm_info SET FIRM_NAME="' + self.firm_name + '",FIRM_CONTACT="' + self.firm_contact + '",FIRM_ADDRESS="' + \
                                     self.firm_address + '" WHERE ID=1;'
            conn.execute(insert_credentials_query)
            conn.execute(insert_login_record_query)
            conn.execute(insert_firm_info_query)
            conn.execute(update_firm_info_query)
            conn.commit()
            conn.close()
            # save the command for backup
            record_backup_query(insert_credentials_query + query_sep + insert_login_record_query + query_sep + update_firm_info_query + query_sep)
            # send success signal
            self.login_setup_success_signal.emit([self.username, self.password])
        except:
            self.login_setup_error_signal.emit("error")

###################SALES###################

class SalesLoadItems(QThread):
    """
    This thread loads the sales items
    """

    items_success_signal = pyqtSignal(dict)
    items_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        try:
            # connect to database
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            # select all the items from the local database
            query = "SELECT * FROM items"
            cursor = conn.execute(query)
            result = cursor.fetchall()
            items = dict()
            for row in result:
                # parse the results
                name = row[0]
                price = row[1]
                qty = row[2]
                # add the items to the items dictionary
                items[name] = [price, qty]
            # return items dictionary
            self.items_success_signal.emit(items)
            # close connection
            conn.close()
        except:
            self.items_error_signal.emit("error")


class SubmitSalesRecord(QThread):
    """
    This thread submits the sales record to the database
    """

    submit_sales_success_signal = pyqtSignal(list)
    submit_sales_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def set_parameters(self, item_names, item_qtys, overall_cost, date_time, login_name, cur_date, cur_year):
        # arguments: str, str, float, str, str, list
        """
        This method gets the data from the main thread
        """
        self.item_names = item_names
        self.item_qtys = item_qtys
        self.overall_cost = overall_cost
        self.date_time = date_time
        self.login_name = login_name
        self.cur_date = cur_date
        self.cur_year = cur_year

    def run(self):
        try:
            # connect to database
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            # submit the data
            create_table_query = "CREATE TABLE IF NOT EXISTS sales_records_" + str(self.cur_year) + \
                                 " (ITEMS_SOLD TEXT NOT NULL, QUANTITY TEXT NOT NULL," + \
                                 " TOTAL_COST REAL NOT NULL, DATE_TIME TEXT NOT NULL, " + \
                                 "SALES_PERSON TEXT NOT NULL);"
            insert_query = 'INSERT INTO sales_records_' + str(self.cur_year) + ' VALUES("' + self.item_names + '","' +\
                    self.item_qtys + '",' + str(self.overall_cost) + ',"' + self.date_time + '","' + self.login_name + '");'
            query = create_table_query + insert_query
            conn.executescript(query)
            conn.commit()
            conn.close()
            # emit the success signal
            self.submit_sales_success_signal.emit([self.item_names, self.item_qtys, self.overall_cost, self.date_time, self.cur_date])
            # save the command for backup after editing the create table query
            create_table_query = "CREATE TABLE IF NOT EXISTS sales_records_" + str(self.cur_year) + " (ITEMS_SOLD VARCHAR(500) NOT NULL, " + \
                                 "QUANTITY VARCHAR(200) NOT NULL, TOTAL_COST FLOAT(20) NOT NULL, DATE_TIME VARCHAR(30) NOT NULL, " + \
                                 "SALES_PERSON VARCHAR(50) NOT NULL);"
            insert_query = insert_query.replace("₵", "c")
            query = create_table_query + query_sep + insert_query + query_sep
            record_backup_query(query)
        except:
            self.submit_sales_error_signal.emit("error")


class UpdateItemQuantity(QThread):
    """
    This thread updates the item quantity after a sale
    """

    update_item_qty_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def set_parameters(self, item_names, item_qtys_left):   #argument: list, int
        """
        This method gets the items names and quantities
        """
        self.item_names = item_names
        self.item_qtys_left = item_qtys_left

    def run(self):
        try:
            # connect to database
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            # submit the data
            query = ""
            backup_query = ""
            for i in range(0, len(self.item_names)):
                query += 'UPDATE items SET QUANTITY=' + str(self.item_qtys_left[i]) + ' WHERE ITEM_NAME="' + self.item_names[i] + '";'
                backup_query += 'UPDATE items SET QUANTITY=' + str(self.item_qtys_left[i]) + ' WHERE ITEM_NAME="' + self.item_names[i] + '";' + query_sep
            if len(self.item_names) > 1:
                conn.executescript(query)
            else:
                conn.execute(query)
            conn.commit()
            conn.close()
            # emit the success signal
            self.update_item_qty_signal.emit("success")
            # save the command for backup
            record_backup_query(backup_query)
        except:
            self.update_item_qty_signal.emit("error")


class SalesLoadRecords(QThread):
    """
    This thread loads the sales records into the table
    """

    sales_load_records_success_signal = pyqtSignal(list)
    sales_load_records_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def set_parameters(self, date, cur_year): #argument: str, int
        """
        This method gets the parameters from the main thread
        """
        self.date = date
        self.cur_year = cur_year

    def run(self):
        try:
            # connect to database
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            # submit the data
            query = "SELECT * FROM sales_records_" + str(self.cur_year) + " WHERE DATE_TIME LIKE '%" + self.date + "%'"
            cursor = conn.execute(query)
            results = cursor.fetchall()
            conn.close()
            # get the overall cost
            overall_cost = 0.0
            if len(results) > 0:
                for row in results:
                    total_cost = row[2]
                    overall_cost += total_cost
            # emit the success signal
            self.sales_load_records_success_signal.emit([results, overall_cost])
        except:
            pass


class LoadCredentialsNames(QThread):
    """
    This thread loads the names of all users (admin and sales persons)
    """

    load_credentials_names_signal = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def run(self):
        try:
            # connect to database
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            # submit the data
            query = "SELECT USERNAME FROM credentials"
            cursor = conn.execute(query)
            results = cursor.fetchall()
            conn.close()
            # emit the success signal
            self.load_credentials_names_signal.emit(results)
        except:
            pass

###################RECORDS###################

class SalesHistoryLoadRecords(QThread):
    """
    This thread loads the sales records into the table
    """

    sales_history_load_records_success_signal = pyqtSignal(list)
    sales_history_load_records_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def set_parameters(self, date, year): #argument: str, int
        """
        This method gets the parameters from the main thread
        """
        self.date = date
        self.year = year

    def run(self):
        try:
            # connect to database
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            # get the data
            query = "SELECT * FROM sales_records_" + str(self.year) + " WHERE DATE_TIME LIKE '%" + self.date + "%'"
            cursor = conn.execute(query)
            results = cursor.fetchall()
            conn.close()
            # get the overall cost
            overall_cost = 0.0
            if len(results) > 0:
                for row in results:
                    total_cost = row[2]
                    overall_cost += total_cost
            # emit the success signal
            self.sales_history_load_records_success_signal.emit([results, overall_cost])
        except:
            pass


class GetDailySalesData(QThread):
    """
    This method gets the daily sales data
    """

    sales_history_view_daily_graphs_success_signal = pyqtSignal(list)
    sales_history_view_daily_graphs_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        # initialize tuples holding months based on their number of days, excluding february
        self.months_with_30_days = ("Apr", "Jun", "Sep", "Nov")
        self.months_with_31_days = ("Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec")

    def set_parameters(self, month, year, graph_type, fig_index):  # argument: str, str, str, int
        """
        This method gets the parameters
        """
        self.month = month
        self.year = year
        self.graph_type = graph_type
        self.fig_index = fig_index

    def run(self):
        try:
            # connect to database
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            # get the total cost and date and time data
            query = "SELECT TOTAL_COST, DATE_TIME FROM sales_records_" + self.year + \
                    " WHERE DATE_TIME LIKE '%" + self.month + "%" + self.year + "%'"
            cursor = conn.execute(query)
            results = cursor.fetchall()
            conn.close()
            # create a list to hold the plot data and number of days in the selected month
            plot_data = [[], []]
            num_days_in_month = 30
            # get the appropriate number of days for the selected month
            if self.months_with_30_days.__contains__(self.month):
                num_days_in_month = 30
            elif self.months_with_31_days.__contains__(self.month):
                num_days_in_month = 31
            else:
                # if the month is February, set the number of days appropriately if leap year or not
                if int(self.year)/4 == 0:
                    num_days_in_month = 29
                else:
                    num_days_in_month = 28
            # get the plot data
            x_vals = [i for i in range(1, num_days_in_month + 1)]
            y_vals = []
            day_total_income = 0  # store a day's total income
            overall_total_income = 0  # store the overall income for the selected period of time
            for i in range(1, num_days_in_month + 1):
                for row in results:
                    date_time = row[1]
                    date_time = date_time.replace(",", "")
                    day_of_month = date_time.split()[2]
                    if i == int(day_of_month):
                        day_total_income += row[0]
                y_vals.append(round(day_total_income, 2))
                overall_total_income += day_total_income
                day_total_income = 0
            plot_data = [x_vals, y_vals, overall_total_income, self.graph_type, self.fig_index, self.month, self.year]
            if len(plot_data[0]) > 0:
                # display the graph
                mpl.rcParams['toolbar'] = "None"
                plt.style.use('seaborn')
                plt.figure()
                plt.title(self.month + " " + self.year)
                if self.graph_type == "line_graph":
                    plt.xlim(1, len(x_vals))
                    plt.xticks(x_vals)
                    plt.xlabel("DAYS")
                    plt.ylabel("GROSS INCOME (GH CEDIS)")
                    plt.plot(x_vals, y_vals)
                elif self.graph_type == "bar_chart":
                    plt.xticks(x_vals)
                    plt.ylabel("GROSS INCOME (GH CEDIS)")
                    plt.xlabel("DAYS")
                    plt.bar(x_vals, height=y_vals)
                plt.savefig("data_files" + os.sep + "figures" + os.sep + "figure" + str(self.fig_index) + ".png")
                # emit the success signal
                self.sales_history_view_daily_graphs_success_signal.emit(plot_data)
            else:
                # emit the error
                self.sales_history_view_daily_graphs_error_signal.emit("error")
        except:
            # emit the error
            self.sales_history_view_daily_graphs_error_signal.emit("error")


class GetMonthlySalesData(QThread):
    """
    This method gets the monthly sales data
    """

    sales_history_view_monthly_graphs_success_signal = pyqtSignal(list)
    sales_history_view_monthly_graphs_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def set_parameters(self, year, graph_type, fig_index):  # argument: str, str, int
        """
        This method gets the parameters
        """
        self.year = year
        self.graph_type = graph_type
        self.fig_index = fig_index

    def run(self):
        try:
            # connect to database
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            # get the total cost and date and time data
            query = "SELECT TOTAL_COST, DATE_TIME FROM sales_records_" + self.year
            cursor = conn.execute(query)
            results = cursor.fetchall()
            conn.close()
            # create a list to hold the plot data
            plot_data = [[], []]
            # get the plot data
            x_vals = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            y_vals = []
            month_total_income = 0  # store a month's total income
            overall_total_income = 0  # store the overall income for the selected period of time
            for m in x_vals:
                for row in results:
                    date_time = row[1]
                    date_time = date_time.replace(",", "")
                    month = date_time.split()[1]
                    if m == month:
                        month_total_income += row[0]
                y_vals.append(round(month_total_income, 2))
                overall_total_income += month_total_income
                month_total_income = 0
            plot_data = [x_vals, y_vals, overall_total_income, self.graph_type, self.fig_index, self.year]
            if len(plot_data[0]) > 0:
                # display the graph
                x_vals_enc = [i for i in range(1, len(x_vals) + 1)]
                mpl.rcParams['toolbar'] = "None"
                plt.style.use('seaborn')
                plt.figure()
                plt.title(self.year)
                if self.graph_type == "line_graph":
                    plt.xlim(1, len(x_vals))
                    plt.xticks(x_vals_enc, x_vals)
                    plt.xlabel("MONTHS")
                    plt.ylabel("GROSS INCOME (GH CEDIS)")
                    plt.plot(x_vals_enc, y_vals)
                elif self.graph_type == "bar_chart":
                    plt.xticks(x_vals_enc, x_vals)
                    plt.ylabel("GROSS INCOME (GH CEDIS)")
                    plt.xlabel("MONTHS")
                    plt.bar(x_vals_enc, height=y_vals)
                plt.savefig("data_files" + os.sep + "figures" + os.sep + "figure" + str(self.fig_index) + ".png")
                # emit the success signal
                self.sales_history_view_monthly_graphs_success_signal.emit(plot_data)
            else:
                # emit the error
                self.sales_history_view_monthly_graphs_error_signal.emit("error")
        except:
            # emit the error
            self.sales_history_view_monthly_graphs_error_signal.emit("error")


class GetYearlySalesData(QThread):
    """
    This method gets the monthly sales data
    """

    sales_history_view_yearly_graphs_success_signal = pyqtSignal(list)
    sales_history_view_yearly_graphs_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def set_parameters(self, from_year, to_year, graph_type, fig_index):  # argument: str, str, int
        """
        This method gets the parameters
        """
        self.from_year = from_year
        self.to_year = to_year
        self.graph_type = graph_type
        self.fig_index = fig_index

    def run(self):
        try:
            # connect to database
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            # create a list to hold the plot data
            plot_data = [[], []]
            # get the plot data
            x_vals = [i for i in range(self.from_year, self.to_year + 1)]
            y_vals = []
            year_total_income = 0  # store a year's total income
            overall_total_income = 0  # store the overall income for the selected period of time
            for year in x_vals:
                try:
                    query = "SELECT SUM(TOTAL_COST) FROM sales_records_" + str(year)
                    cursor = conn.execute(query)
                    result = cursor.fetchone()
                    year_total_income = result[0]
                except:
                    year_total_income = 0.0
                y_vals.append(year_total_income)
                overall_total_income += year_total_income
            conn.close()
            plot_data = [x_vals, y_vals, overall_total_income, self.graph_type, self.fig_index, str(self.from_year), str(self.to_year)]
            if len(plot_data[0]) > 0:
                # display the graph
                x_vals_enc = [i for i in range(1, len(x_vals) + 1)]
                mpl.rcParams['toolbar'] = "None"
                plt.style.use('seaborn')
                plt.figure()
                plt.title(str(self.from_year) + " - " + str(self.to_year))
                if self.graph_type == "line_graph":
                    plt.xlim(1, len(x_vals))
                    plt.xticks(x_vals_enc, x_vals)
                    plt.xlabel("YEARS")
                    plt.ylabel("GROSS INCOME (GH CEDIS)")
                    plt.plot(x_vals_enc, y_vals)
                elif self.graph_type == "bar_chart":
                    plt.xticks(x_vals_enc, x_vals)
                    plt.ylabel("GROSS INCOME (GH CEDIS)")
                    plt.xlabel("YEARS")
                    plt.bar(x_vals_enc, height=y_vals)
                plt.savefig("data_files" + os.sep + "figures" + os.sep + "figure" + str(self.fig_index) + ".png")
                # emit the success signal
                self.sales_history_view_yearly_graphs_success_signal.emit(plot_data)
            else:
                # emit the error
                self.sales_history_view_yearly_graphs_error_signal.emit("error")
        except:
            # emit the error
            self.sales_history_view_yearly_graphs_error_signal.emit("error")

###################SETTINGS###################

class AddSalesPerson(QThread):
    """
    This method adds a sales person
    """

    add_sales_person_success_signal = pyqtSignal(str)
    add_sales_person_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def set_parameters(self, username, password): # argument: str, str
        """
        This method gets the parameters
        """
        self.username = username
        self.password = password

    def run(self):
        try:
            # check if the username or password exists before adding
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            select_query = 'SELECT * FROM credentials WHERE USERNAME="' + self.username + '"'
            cursor = conn.execute(select_query)
            results = cursor.fetchall()
            if len(results) == 0:
                insert_query = 'INSERT INTO credentials VALUES("' + self.username + '","' + psword_encrypter.encrypt(self.password) + '");'
                conn.execute(insert_query)
                conn.commit()
                self.add_sales_person_success_signal.emit(self.username)
                # save the command for backup
                record_backup_query(insert_query + query_sep)
            else:
                self.add_sales_person_error_signal.emit("uname_exists")
            conn.close()
        except:
            self.add_sales_person_error_signal.emit("error")


class RemoveSalesPerson(QThread):
    """
    This thread removes a sales person
    """

    remove_sales_person_success_signal = pyqtSignal(str)
    remove_sales_person_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def set_parameters(self, username):
        """
        This method sets the parameters
        """
        self.username = username

    def run(self):
        try:
            # check if the username exists before deleting
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            select_query = 'SELECT * FROM credentials WHERE USERNAME="' + self.username + '"'
            cursor = conn.execute(select_query)
            results = cursor.fetchall()
            if len(results) > 0:
                delete_query = 'DELETE FROM credentials WHERE USERNAME="' + self.username + '";'
                conn.execute(delete_query)
                conn.commit()
                self.remove_sales_person_success_signal.emit(self.username)
                # save the command for backup
                record_backup_query(delete_query + query_sep)
            else:
                self.remove_sales_person_error_signal.emit("not_exist")
            conn.close()
        except:
            self.remove_sales_person_error_signal.emit("error")


class EditSalesPerson(QThread):
    """
    This thread edits the sales person's data
    """

    edit_sales_person_success_signal = pyqtSignal(list)
    edit_sales_person_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def set_parameters(self, cur_username, new_username, cur_password, new_password): # argument: str, str, str, str
        """
        This method sets the parameters
        """
        self.cur_username = cur_username
        self.new_username = new_username
        self.cur_password = cur_password
        self.new_password = new_password

    def run(self):
        try:
            # get the sales persons credentials and verify if current password since the username already exists
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            select_query = 'SELECT * FROM credentials WHERE USERNAME="' + self.cur_username + '"'
            cursor = conn.execute(select_query)
            results = cursor.fetchone()
            if psword_encrypter.decrypt(results[1]) == self.cur_password:
                # if new password does not exist already for another person, update the sales person's info
                update_query = 'UPDATE credentials SET USERNAME="' + self.new_username + '", PASSWORD="' + psword_encrypter.encrypt(self.new_password) + \
                               '" WHERE USERNAME="' + self.cur_username + '";'
                conn.execute(update_query)
                self.edit_sales_person_success_signal.emit([self.cur_username, self.new_username])
                # save the command for backup
                record_backup_query(update_query + query_sep)
            else:
                self.edit_sales_person_error_signal.emit("wrong_password")
            conn.commit()
            conn.close()
        except:
            self.edit_sales_person_error_signal.emit("error")


class ViewAllSalesPersons(QThread):
    """
    This thread loads all the sales persons in the view all sales persons table
    """

    view_all_sales_persons_success_signal = pyqtSignal(list)
    view_all_sales_persons_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        try:
            # connect to database
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            # select all the items from the local database
            query = "SELECT * FROM credentials"
            cursor = conn.execute(query)
            result = cursor.fetchall()
            # return items dictionary
            self.view_all_sales_persons_success_signal.emit(result)
            # close connection
            conn.close()
        except:
            self.view_all_sales_persons_error_signal.emit("error")


class EditAdmin(QThread):
    """
    This thread edits the admin info
    """

    edit_admin_success_signal = pyqtSignal(str)
    edit_admin_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def set_parameters(self, cur_password, new_password):
        """
        This method sets the parameters
        """
        self.cur_password = cur_password
        self.new_password = new_password

    def run(self):
        try:
            # check if the password exists before updating
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            select_query = 'SELECT * FROM credentials WHERE USERNAME="Admin"'
            cursor = conn.execute(select_query)
            results = cursor.fetchone()
            if psword_encrypter.decrypt(results[1]) == self.cur_password:
                update_query = 'UPDATE credentials SET PASSWORD="' + psword_encrypter.encrypt(self.new_password) + '" WHERE USERNAME="Admin";'
                conn.execute(update_query)
                self.edit_admin_success_signal.emit("success")
                # save the command for backup
                record_backup_query(update_query + query_sep)
            else:
                self.edit_admin_error_signal.emit("wrong_password")
            conn.commit()
            conn.close()
        except:
            self.edit_admin_error_signal.emit("error")


class AddNewItem(QThread):
    """
    This thread adds a new item to the stock
    """

    add_new_item_success_signal = pyqtSignal(list)
    add_new_item_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def set_parameters(self, item_name, price, quantity): # argument: str, str, str
        """
        This method sets the parameters
        """
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

    def run(self):
        try:
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            query = 'INSERT INTO items VALUES("' + self.item_name + '",' + self.price + ',' + self.quantity + ');'
            conn.execute(query)
            conn.commit()
            conn.close()
            self.add_new_item_success_signal.emit([self.item_name, self.price, self.quantity])
            # save the command for backup
            record_backup_query(query + query_sep)
        except:
            self.add_new_item_error_signal.emit("error")


class ViewAllItems(QThread):
    """
    This thread loads all the items in the view all items table
    """

    view_all_items_success_signal = pyqtSignal(list)
    view_all_items_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        try:
            # connect to database
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            # select all the items from the local database
            query = "SELECT * FROM items"
            cursor = conn.execute(query)
            result = cursor.fetchall()
            # return items dictionary
            self.view_all_items_success_signal.emit(result)
            # close connection
            conn.close()
        except:
            self.view_all_items_error_signal.emit("error")


class RemoveItem(QThread):
    """
    This thread removes an item from the stock
    """

    remove_item_success_signal = pyqtSignal(str)
    remove_item_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def set_parameters(self, item_name):
        """
        This method sets the parameters
        """
        self.item_name = item_name

    def run(self):
        try:
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            query = 'DELETE FROM items WHERE ITEM_NAME="' + self.item_name + '";'
            conn.execute(query)
            conn.commit()
            conn.close()
            self.remove_item_success_signal.emit(self.item_name)
            # save the command for backup
            record_backup_query(query + query_sep)
        except:
            self.remove_item_error_signal.emit("error")


class EditItem(QThread):
    """
    This thread edits an item
    """

    edit_item_success_signal = pyqtSignal(list)
    edit_item_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def set_parameters(self, item_name, quantity, unit_price): # argument: str, str, str
        """
        This method sets the parameters
        """
        self.item_name = item_name
        self.quantity = quantity
        self.unit_price = unit_price

    def run(self):
        try:
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            query = 'UPDATE items SET UNIT_PRICE=' + self.unit_price + ',QUANTITY=' + self.quantity + \
                    ' WHERE ITEM_NAME="' + self.item_name + '";'
            conn.execute(query)
            conn.commit()
            conn.close()
            self.edit_item_success_signal.emit([self.item_name, self.unit_price, self.quantity])
            # save the command for backup
            record_backup_query(query + query_sep)
        except:
            self.edit_item_error_signal.emit("error")


class BackupNow(QThread):
    """
    This thread manually backs up the data
    """

    backup_now_success_signal = pyqtSignal(str)
    backup_now_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        self.backup_now_success_signal.emit("backing_up")
        # check for internet connection
        if internet_conn_available():
            try:
                # backup data
                # hostname, username, password, dbname
                db_hostname, db_port, db_username, db_password, db_name = get_db_conn_info()
                conn = pymysql.connect(host=db_hostname, port=db_port, user=db_username, password=db_password, db=db_name)
                try:
                    cursor = conn.cursor()
                    query = get_backup_script()
                    if query != "":
                        commands_list = query.split(query_sep)
                        commands_list = commands_list[:-1]
                        # insert create table commands to create the tables if they do not exist
                        disable_warnings_query = "SET sql_notes=0"
                        enable_warnings_query = "SET sql_notes=1"
                        create_item_table_query = "CREATE TABLE IF NOT EXISTS items (ITEM_NAME VARCHAR(100) NOT NULL, " + \
                                                  "UNIT_PRICE FLOAT(10) NOT NULL, QUANTITY INT(10) NOT NULL);"
                        create_credentials_table_query = "CREATE TABLE IF NOT EXISTS credentials (USERNAME VARCHAR(100) NOT NULL, " + \
                                                         "PASSWORD VARCHAR(100) NOT NULL, PRIMARY KEY(USERNAME,PASSWORD));"
                        create_login_records_table_query = "CREATE TABLE IF NOT EXISTS login_records (USERNAME VARCHAR(100) NOT NULL, " + \
                                                                     "LOGIN_TIME VARCHAR(50) NOT NULL);"
                        create_firm_info_table_query = "CREATE TABLE IF NOT EXISTS firm_info (ID INTEGER(1) NOT NULL,FIRM_NAME VARCHAR(100) NOT NULL," + \
                                                 "FIRM_CONTACT VARCHAR(50) NOT NULL,FIRM_ADDRESS VARCHAR(50) NOT NULL);"
                        insert_firm_info_query = 'INSERT INTO firm_info VALUES(1,"firm_name","firm_contact","firm_address");'
                        # get the row count in the firm table
                        firm_info_row_count = 0
                        try:
                            firm_info_table_row_count_query = 'SELECT COUNT(*) FROM firm_info;'
                            firm_info_cursor = conn.cursor()
                            firm_info_cursor.execute(firm_info_table_row_count_query)
                            firm_info_row_count = firm_info_cursor.fetchone()[0]
                        except:
                            pass
                        # add the create table commands to the commands list
                        commands_list.insert(0, create_item_table_query)
                        commands_list.insert(0, create_credentials_table_query)
                        commands_list.insert(0, create_login_records_table_query)
                        if firm_info_row_count == 0:
                            commands_list.insert(0, insert_firm_info_query)
                        commands_list.insert(0, create_firm_info_table_query)
                        commands_list.insert(0, disable_warnings_query)
                        commands_list.append(enable_warnings_query)
                        for command in commands_list:
                            try:
                                cursor.execute(command)
                            except:
                                pass
                        conn.commit()
                        # send success signal
                        self.backup_now_success_signal.emit("backup_success")
                    else:
                        self.backup_now_error_signal.emit("not_backup_data")
                except:
                    self.backup_now_error_signal.emit("backup_error")
                conn.close()
            except:
                self.backup_now_error_signal.emit("backup_failed")
        else:
            self.backup_now_error_signal.emit("internet_error")


class AutoBackup(QThread):
    """
    This thread automatically backs up the data
    """

    auto_backup_success_signal = pyqtSignal(str)
    auto_backup_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def set_parameters(self, auto_backup_state, time_interval):
        """
        This method sets the parameters
        """
        self.auto_backup_state = auto_backup_state
        self.time_interval = time_interval

    def load_settings(self):
        """
        This method loads the settings from a file
        """
        try:
            settings_file_path = resource_path("data_files" + os.sep + "settings.pkl")
            settings_file = open(settings_file_path, "rb")
            self.settings = pickle.load(settings_file)
            settings_file.close()
        except:
            self.settings = {"min_qty_to_notify": 10, "auto_backup": 0, "auto_backup_time_interval": 5}
        self.auto_backup_state = self.settings["auto_backup"]
        self.time_interval = self.settings["auto_backup_time_interval"]

    def run(self):
        # get the current time
        prev_time = time.time()  # in float seconds
        load_settings_prev_time = time.time()
        # find the difference in seconds, convert to minutes and check if it is up to the backup time interval before updating
        while(True):
            QApplication.processEvents()
            # load the settings after every minute
            load_settings_cur_time = time.time()
            load_settings_minute_diff = (load_settings_cur_time - load_settings_prev_time) / 60.0
            if load_settings_minute_diff >= 0.5: # load settings after every minute
                self.load_settings()
                load_settings_prev_time = load_settings_cur_time
            # if the auto backup is enabled, backup at the set time interval
            if self.auto_backup_state == 1: # 1 means ON and 0 means OFF
                cur_time = time.time()
                minute_diff = (cur_time - prev_time) / 60.0
                if minute_diff >= self.time_interval:
                    # check for internet connection
                    if internet_conn_available():
                        try:
                            # send the backing up notice
                            self.auto_backup_success_signal.emit("backing_up")
                            # backup data
                            conn = None
                            try:
                                # hostname, username, password, dbname
                                db_hostname, db_port, db_username, db_password, db_name = get_db_conn_info()
                                conn = pymysql.connect(host=db_hostname, port=db_port, user=db_username, password=db_password, db=db_name)
                                cursor = conn.cursor()
                                query = get_backup_script()
                                if query != "":
                                    commands_list = query.split(query_sep)
                                    commands_list = commands_list[:-1]
                                    # insert create table commands to create the tables if they do not exist
                                    disable_warnings_query = "SET sql_notes=0"
                                    enable_warnings_query = "SET sql_notes=1"
                                    create_item_table_query = "CREATE TABLE IF NOT EXISTS items (ITEM_NAME VARCHAR(100) NOT NULL, " + \
                                                              "UNIT_PRICE FLOAT(10) NOT NULL, QUANTITY INT(10) NOT NULL);"
                                    create_credentials_table_query = "CREATE TABLE IF NOT EXISTS credentials (USERNAME VARCHAR(100) NOT NULL, " + \
                                                                     "PASSWORD VARCHAR(100) NOT NULL, PRIMARY KEY(USERNAME,PASSWORD));"
                                    create_login_records_table_query = "CREATE TABLE IF NOT EXISTS login_records (USERNAME VARCHAR(100) NOT NULL, " + \
                                                                     "LOGIN_TIME VARCHAR(50) NOT NULL);"
                                    create_firm_info_table_query = "CREATE TABLE IF NOT EXISTS firm_info (ID INTEGER(1) NOT NULL,FIRM_NAME VARCHAR(100) NOT NULL," + \
                                                                   "FIRM_CONTACT VARCHAR(50) NOT NULL,FIRM_ADDRESS VARCHAR(50) NOT NULL);"
                                    insert_firm_info_query = 'INSERT INTO firm_info VALUES(1,"firm_name","firm_contact","firm_address");'
                                    # get the row count in the firm table
                                    firm_info_row_count = 0
                                    try:
                                        firm_info_table_row_count_query = 'SELECT COUNT(*) FROM firm_info;'
                                        firm_info_cursor = conn.cursor()
                                        firm_info_cursor.execute(firm_info_table_row_count_query)
                                        firm_info_row_count = firm_info_cursor.fetchone()[0]
                                    except:
                                        pass
                                    # add the create table commands to the commands list
                                    commands_list.insert(0, create_item_table_query)
                                    commands_list.insert(0, create_credentials_table_query)
                                    commands_list.insert(0, create_login_records_table_query)
                                    if firm_info_row_count == 0:
                                        commands_list.insert(0, insert_firm_info_query)
                                    commands_list.insert(0, create_firm_info_table_query)
                                    commands_list.insert(0, disable_warnings_query)
                                    commands_list.append(enable_warnings_query)
                                    for command in commands_list:
                                        try:
                                            cursor.execute(command)
                                        except:
                                            pass
                                    conn.commit()
                                    # send success signal
                                    self.auto_backup_success_signal.emit("backup_success")
                                else:
                                    self.auto_backup_error_signal.emit("not_backup_data")
                            except:
                                self.auto_backup_error_signal.emit("backup_error")
                            conn.close()
                        except:
                            self.auto_backup_error_signal.emit("backup_failed")
                    else:
                        self.auto_backup_error_signal.emit("internet_error")
                    # reset previous time to current one
                    prev_time = cur_time


class UpdateFirmInfo(QThread):
    """
    This thread updates the firm's info
    """

    update_firm_info_success_signal = pyqtSignal(str)
    update_firm_info_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def set_parameters(self, firm_name, firm_contact, firm_address):
        """
        This method sets the parameters
        """
        self.firm_name = firm_name
        self.firm_contact = firm_contact
        self.firm_address = firm_address

    def run(self):
        try:
            # update the firm name in the file
            firm_info_file = open(resource_path("data_files" + os.sep + "firm_info.txt"), "w")
            firm_info = self.firm_name + query_sep + self.firm_contact + query_sep + self.firm_address
            firm_info_file.write(firm_info)
            firm_info_file.close()
            # update the firm info in the database
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            update_firm_info_query = 'UPDATE firm_info SET FIRM_NAME="' + self.firm_name + '",FIRM_CONTACT="' + self.firm_contact + '",FIRM_ADDRESS="' + \
                                     self.firm_address + '" WHERE ID=1;'
            conn.execute(update_firm_info_query)
            conn.commit()
            conn.close()
            # save the command for backup
            record_backup_query(update_firm_info_query + query_sep)
            # send success signal
            self.update_firm_info_success_signal.emit("success")
        except:
            self.update_firm_info_error_signal.emit("error")


class RestoreData(QThread):
    """
    This thread restores the data
    """

    restore_data_success_signal = pyqtSignal(str)
    restore_data_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        try:
            # hostname, username, password, dbname
            db_hostname, db_port, db_username, db_password, db_name = get_db_conn_info()
            conn = pymysql.connect(host=db_hostname, port=db_port, user=db_username, password=db_password, db=db_name)
            cursor = conn.cursor()
            # get table names
            table_names_query = 'SHOW TABLES'
            cursor.execute(table_names_query)
            result = cursor.fetchall()
            table_names = []
            for row in result:
                table_names.append(row[0])
            try:
                # create a backup for the local database if any exists
                shutil.move(resource_path("dbs" + os.sep + "sms_db.db"), resource_path("dbs" + os.sep + "db_backup" + os.sep + "sms_db.db"))
            except:
                pass
            # create local database and tables
            local_conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            create_table_query = ""
            for table in table_names:
                if table == "items":
                    create_table_query = "CREATE TABLE IF NOT EXISTS items (ITEM_NAME TEXT NOT NULL UNIQUE,UNIT_PRICE REAL NOT NULL," + \
                                               "QUANTITY INTEGER NOT NULL DEFAULT 0,PRIMARY KEY(ITEM_NAME));"
                elif table == "credentials":
                    create_table_query = "CREATE TABLE IF NOT EXISTS credentials (USERNAME TEXT NOT NULL UNIQUE,PASSWORD TEXT NOT " + \
                                                     "NULL UNIQUE,PRIMARY KEY(USERNAME,PASSWORD));"
                elif table == "login_records":
                    create_table_query = "CREATE TABLE IF NOT EXISTS login_records (USERNAME TEXT NOT NULL,LOGIN_TIME TEXT NOT NULL);"
                elif table == "firm_info":
                    create_table_query = "CREATE TABLE IF NOT EXISTS firm_info (ID INTEGER NOT NULL,FIRM_NAME TEXT NOT NULL,FIRM_CONTACT " + \
                                                   "TEXT NOT NULL,FIRM_ADDRESS TEXT NOT NULL);"
                else:
                    create_table_query = "CREATE TABLE IF NOT EXISTS " + table + " (ITEMS_SOLD TEXT NOT NULL, QUANTITY TEXT NOT NULL," + \
                                         " TOTAL_COST REAL NOT NULL, DATE_TIME TEXT NOT NULL,SALES_PERSON TEXT NOT NULL);"
                local_conn.execute(create_table_query)
            # download all the data into the local database
            insert_query = ""
            for table in table_names:
                # select data
                select_query = "SELECT * FROM " + table + ";"
                cursor.execute(select_query)
                result = cursor.fetchall()
                # insert data
                for row in result:
                    if table == "items":
                        insert_query = 'INSERT INTO items VALUES("' + row[0] + '",' + str(row[1]) + ',' + str(row[2]) + ');'
                    elif table == "credentials":
                        insert_query = 'INSERT INTO credentials VALUES("' + row[0] + '","' + row[1] + '");'
                    elif table == "login_records":
                        insert_query = 'INSERT INTO login_records VALUES("' + row[0] + '","' + row[1] + '");'
                    elif table == "firm_info":
                        insert_query = 'INSERT INTO firm_info VALUES(' + str(row[0]) + ',"' + row[1] + '","' + row[2] + '","' + row[3] + '");'
                    else:
                        insert_query = 'INSERT INTO ' + table + ' VALUES("' + row[0] + '","' + row[1] + '",' + str(row[2]) + ',"' + row[3] + '","' + row[4] + '");'
                    local_conn.execute(insert_query)
            # save the data
            local_conn.commit()
            # close all the database connections
            conn.close()
            local_conn.close()
            # send success signal
            self.restore_data_success_signal.emit("success")
        except:
            try:
                # restore backup for the local database
                shutil.move(resource_path("dbs" + os.sep + "db_backup" + os.sep + "sms_db.db"), resource_path("dbs" + os.sep + "sms_db.db"))
            except:
                pass
            # send error signal
            self.restore_data_error_signal.emit("error")

###################LOGIN RECORDS###################

class LoadLoginRecordsThread(QThread):
    """
    This thread loads all the login records for a sales person
    """

    load_login_records_success_signal = pyqtSignal(list)
    load_login_records_error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def set_parameters(self, year): #argument: int
        """
        This method sets the parameters
        """
        self.year = year

    def run(self):
        try:
            conn = sqlite3.connect(resource_path("dbs" + os.sep + "sms_db.db"))
            query = 'SELECT * FROM login_records WHERE LOGIN_TIME LIKE "%' + str(self.year) + '%"'
            cursor = conn.execute(query)
            result = cursor.fetchall()
            conn.close()
            self.load_login_records_success_signal.emit(result)
        except:
            self.load_login_records_error_signal.emit("error")
