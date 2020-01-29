import mysql.connector
from mysql.connector import errorcode
from PyQt5.QtWidgets import QMessageBox


class DatabaseUtility:
    def __init__(self, database, table_name):
        self.db = database
        self.table_name = table_name

        self.cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1')
        self.cursor = self.cnx.cursor()

        self.connect_to_db()
        self.create_table()

    def connect_to_db(self):
        try:
            self.cursor.execute('USE {}'.format(self.db))
            print(f'Connected to {self.db}')
        except mysql.connector.Error as err:
            print('ЕГОРКА')
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_db()
                print(f'Database {self.db} created successfully')
                self.cnx.database = self.db
            else:
                print(err.msg)

    def create_db(self):
        try:
            self.run_command(f"CREATE DATABASE {self.db} DEFAULT CHARACTER SET 'utf8'")
        except mysql.connector.Error as err:
            print(f'Failed creating database: {err}')

    def create_table(self):
        cmd = (f" CREATE TABLE IF NOT EXISTS `{self.table_name}` ("
               " `id` int(4) NOT NULL AUTO_INCREMENT,"
               " `name` char(250) NOT NULL,"
               " `price` char(50),"
               " `link` text,"
               " `comment` varchar(250),"
               " PRIMARY KEY (`id`)"
               ") ENGINE=InnoDB")
        self.run_command(cmd)

    def get_table(self):
        pass

    def get_column(self):
        pass

    # def add_wish_to_table(self, message):
    #     cmd = "INSERT INTO" + self.table_name + " (name, price, link, comment)"
    #     cmd += " VALUES "

    def edit_wish(self, wish):
        pass

    def del_wish(self, wish):
        pass

    def __del__(self):
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()

    def run_command(self, cmd):
        try:
            self.cursor.execute(cmd)
        except mysql.connector.Error as err:
            print('ERROR MESSAGE: ' + str(err.msg))
            print('WITH ' + cmd)
            print(f"Error: {err.args[0]}, {err.args[1]}")
            self.cnx.rollback()
            alert = QMessageBox()
            alert.setText('Что-то пошло не так')
            alert.exec_()
            self.close_window()

        # try:
        #     msg = self.cursor.fetchall()
        # except:
        #     msg = self.cursor.fetchone()
        #
        # return msg


if __name__ == '__main__':
    db = 'wishlistdb'
    table_name = 'wishlist'

    dbu = DatabaseUtility(db, table_name)