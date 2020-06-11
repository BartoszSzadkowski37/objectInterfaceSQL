# DataBase class

import sqlite3

class DataBase():
    def __init__(self, name):
        self.name = name
        con = sqlite3.connect(name+'.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()


    def showTables(self):
        con = sqlite3.connect(self.name+'.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute('SELECT name FROM ' + self.name + ' WHERE type = "table"')
        tables = cur.fetchall()
        print(tables)
