import mysql.connector
from mysql.connector import errorcode
from PyQt5.QtWidgets import QMessageBox


class DatabaseUtility:
    def __init__(self, database, table_name):
        self.db = database
        self.table_name = table_name

        self.cnx = mysql.connector.connect(user='root', password='123123', host='127.0.0.1')
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
        self.create_table()
        return self.run_command(f"SELECT * FROM `{self.table_name}`")

    def get_columns(self):
        return self.run_command(f"SHOW COLUMNS FROM `{self.table_name}`")

    def add_wish(self, name, price, link, comment):
        cmd = f"INSERT INTO `{self.table_name}` (`name`, `price`, `link`, `comment`)"
        cmd += f" VALUES ('{name}', '{price}', '{link}', '{comment}')"
        self.run_command(cmd)

    def get_wish(self, id):
        cmd = f"SELECT * from `{self.table_name}` WHERE `id`={int(id)}"
        item = self.run_command(cmd)[0]
        return item

    def edit_wish(self, wish_id, *fields):
        cmd = f"UPDATE `{self.table_name}` SET "
        cmd += f"`name`= '{fields[0]}', `price`='{fields[1]}', " \
               f"`link`='{fields[2]}', `comment`='{fields[3]}'"
        cmd += f" WHERE `id`={wish_id}"
        self.run_command(cmd)

    def del_wish(self, wish):
        self.run_command(f"DELETE FROM `{self.table_name}` WHERE `id`={int(wish)}")

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

        try:
            msg = self.cursor.fetchall()
        except:
            msg = self.cursor.fetchone()

        return msg


if __name__ == '__main__':
    db = 'wishlistdb'
    table_name = 'wishlist'

    dbu = DatabaseUtility(db, table_name)