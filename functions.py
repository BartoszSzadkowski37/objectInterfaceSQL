# functions

# IMPORTING MODULES
from os import system, name
import pyinputplus as pyip
from pathlib import Path
from DataBase import DataBase
import re
import os

# FUNCTION FOR CLEARING THE SCREEN
def clear():
    #for windows
    if name == 'nt':
        _ = system('cls')
    #for mac and linux
    else:
        _ = system('clear')
 
 
# FUNCTION TO PRINT MAIN MENU 
def menu():
    print('1. CREATE DATABASE')
    print('2. SHOW DATABASES')
    print('3. EXIT')
    userInput = pyip.inputChoice(['1', '2', '3'], '(1/2/3):')
    return userInput

# CREATING DATABASE
def createDB():
    # clear the screen
    clear()
    print('CREATING DATABASE')
    print('1. CREATE FROM DB STUDIO LEVEL')
    print('2. CREATE MANUALLY BY SQL')
    print('3. EXIT')
    userInput = pyip.inputChoice(['1', '2', '3'], '(1/2/3):')
# IF USER PRESS 3 EXIT 
    if userInput == '3':
        return
# CREATING DB FROM THE DB STUDIO LEVEL
    elif userInput == '1':
        ifExists = True
        # getting db name and checking if such DB exists
        while ifExists:
            DBName = pyip.inputStr('Provide name of the DataBase:')
            path = Path.cwd() / DBName
            if path.exists():
                print('There is DB with this name already!')
            else:
                ifExists = False
# CREATING DB BY SQL QUERY
    else:
        query = pyip.inputStr('Provide SQL query:', allowRegexes=(r'CREATE DATABASE (/w)+;'), blockRegexes=(r'.*'), limit=3)
        DBName = re.sub('CREATE DATABASE ', '', query)
        DBName = re.sub(';', '', DBName)
    DB = DataBase(DBName)


# LIST ALL DATABASES EXISTING IF USER WANT TO MANAGE SOME DB, FUNCTION WILL RETURN THIS DB NAME, ELSE WILL RETURN NONE
def listDBs():
    cwd = str(Path.cwd())
    ls = os.listdir(cwd)
    checkDBReg = re.compile(r'.*\.db')
    existingDB = []
    for i in range(len(ls)):
        match = checkDBReg.search(ls[i])
        if match != None:
            existingDB.append(match.group())
    print('Found DataBases:')
    print(existingDB)

    print('Provide DataBase name for manage or press "q" to exit')

    correctNameOfDB = False
    while correctNameOfDB == False:
        userInput = pyip.inputStr(prompt='Provide valid DB name:')
        if userInput == 'q':
            return
        for i in range(len(existingDB)):
            if existingDB[i] == userInput:
                correctNameOfDB = True
    userInput = re.sub('.db', '', userInput)
    return userInput


#FUNCTION FOR MANAGING DB
def manageDB(DBName):
    DB = DataBase(DBName)
    DB.showTables()

