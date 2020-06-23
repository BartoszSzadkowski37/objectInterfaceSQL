# DataBase class

import sqlite3
import pyinputplus as pyip
from Table import Table
from Column import Column


class DataBase():
    def __init__(self, name, tables = []):
        self.name = name
        self.tables = tables
        con = sqlite3.connect(name+'.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()


    def createTable(self):
        con = sqlite3.connect(self.name+'.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        print('1. CREATE FROM DB STUDIO LEVEL') 
        print('2. CREATE BY SQL QUERY')
        userChoice = pyip.inputChoice(['1', '2'], ('(1/2)'))
        if userChoice == '1':
            tableName = pyip.inputStr('Table name:')
            # CREATING TABLE OBJECT
            table = Table(tableName)
            columnsAmount = pyip.inputInt('Columns amount:')
            for i in range(columnsAmount):
                columnName = pyip.inputStr('Column name: ')
                columnType = pyip.inputStr('Column type: ')
                # CREATING COLUMN OBJECT
                column = Column(columnName, columnType)
                # ADDING COLUMN OBJECT TO THE COLUMNS PROPERTY IN TABLE OBJECT
                table.columns.append(column)
        # ADDING TABLE TO THE TABLES PROPERTY IN DATABASE OBJECT
        self.tables.append(table)
        # CREATING SQL QUERY
        query = 'CREATE TABLE ' + table.name + ' (\n'
        for i in range(len(table.columns)):
            query += table.columns[i].name + table.columns[i].type + ',\n'
            # HEREEEE

            for i in range(len(table.columns)):
                print(table.columns[i].name, table.columns[i].type, table.columns[i].value)
        
        
