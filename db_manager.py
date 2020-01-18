import mysql.connector
from mysql.connector import errorcode


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
            self.cnx.database = self.db
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_db()
                self.cnx.database = self.db
            else:
                print(err.msg)

    def create_db(self):
        try:
            self.run_command("CREATE DATABASE %s DEFAULT CHARACTER SET 'utf-8';" % self.db)
        except mysql.connector.Error as err:
            print(f'Failed creating database: {err}')

    def create_table(self):
        cmd = (" CREATE TABLE IF NOT EXISTS " + self.table_name + " ("
               " `ID` int(4) NOT NULL AUTO_INCREMENT,"
               " `name` char(50) NOT NULL,"
               " `price` char(50), "
               " `link` char, "
               "  `comment` char(250), "
               ") ENGINE=InnoDB;")
        self.run_command(cmd)

    def get_table(self):
        pass

    def get_column(self):
        pass

    def add_wish_to_table(self, message):
        cmd = "INSERT INTO" + self.table_name + " (name, price, link, comment)"
        cmd += " VALUES "

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

        try:
            msg = self.cursor.fetchall()
        except:
            msg = self.cursor.fetchone()

        return msg


if __name__ == '__main__':
    db = 'wishlist_db'
    table_name = 'wishlist'

    dbu = DatabaseUtility(db, table_name)