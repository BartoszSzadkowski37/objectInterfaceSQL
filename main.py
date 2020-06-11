# main file

from DataBase import DataBase
import functions as func

# MAIN LOOP
loop = True
 
while loop:
   #func.clear()
   action = func.menu() 
   if action == '1':
       func.clear()
       func.createDB()
   elif action == '2':
       func.clear()
       dbName = func.listDBs()
       print(dbName)
       func.manageDB(dbName)
   elif action == '3':
       func.clear()
       loop = False
