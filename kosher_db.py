__author__ = 'student'

import sqlite3


class DbManager:

    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)
        self.cursor = self.con.cursor()

    def create_app_table(self):

        self.cursor.execute("""CREATE TABLE if not exists apps
        (
        'ID' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL  ,
        'name' TEXT NOT NULL,
        'description' TEXT,
        'link' TEXT
        )""")

    def add_data(self, *args):

        self.cursor.execute("INSERT INTO apps('name','description','link') VALUES('{}','{}','{}')".format(*args))
        self.con.commit()

    def get_data(self):
        self.cursor.execute("select * from apps")
        return self.cursor.fetchall()


def push_to_db(name, description, link):
    my_apps = DbManager("kosher_app_db")
    my_apps.create_app_table()
    my_apps.add_data(name, description, link)
    my_apps.con.close()


def get_all_data():
    my_apps = DbManager("kosher_app_db")
    data = my_apps.get_data()
    return data


def main():
    push_to_db('moshe', 'dd', 'ggg')
    print(get_all_data())

if __name__ == '__main__':
    main()