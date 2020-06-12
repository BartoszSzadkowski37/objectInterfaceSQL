# DataBase class

import sqlite3
import pyinputplus as pyip

class DataBase():
    def __init__(self, name):
        self.name = name
        con = sqlite3.connect(name+'.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute('SHOW DATABASES;')


    def createTable(self):
        con = sqlite3.connect(self.name+'.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        print('1. CREATE FROM DB STUDIO LEVEL') 
        print('2. CREATE BY SQL QUERY')
        userChoice = pyip.inputChoice(['1', '2'], ('(1/2)'))
        if userChoice == '1':
            # HERE SHOULD BE CREATE TABLE OBJECT
            tableName = pyip.inputStr('Table name:')
            columnsAmount = pyip.inputInt('Columns amount:')
            columns = []

        
        
