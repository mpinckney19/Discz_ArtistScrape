#FUNCTIONS TO VISUALIZE THE DATA IN EXCEL
# TO USE THE FUNCTIONS, UNCOMMENT THEN POPULATE THE ARGUMENTS WITH YOUR DESIRED DATABASE/TABLE/EXCEL FILE

import sqlite3
import pandas as pd
from constants import databaseName, tableName, xlFileName

#Delete a table in a given database
def delTable(dbName, tblName):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    dropTable = f'''DROP TABLE {tblName}'''
    c.execute(dropTable)

#RUNNING THIS FUNCTION MIGHT DELETE ALL ARTIST INFO FROM DATABASE
#delTable(databaseName, tableName)

#Remove duplicate rows from a database
def removeDups(dbName, tblName):
    removeDupCommand = f'''
        DELETE FROM {tblName}
        WHERE rowid NOT IN (
            SELECT MIN(rowid)
            FROM {tblName}
            GROUP BY id
        )
        '''
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    c.execute(removeDupCommand)
    conn.commit()

#removeDups(databaseName, tableName)

#Output data in order found to excel file
def outExcel(dbName, tblName, fileName):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    command_string = f'SELECT * FROM {tblName}'
    dataFrame = pd.read_sql_query(command_string, conn)
    dataFrame.to_excel(fileName, index=False)

#outExcel(databaseName, tableName, xlFileName)

#Output alphabetically by name to excel file
#   To reverse order: change 'ASC' to 'DESC'
def outAlphabName(dbName, tblName, fileName):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    command_string = f'SELECT * FROM {tblName} ORDER BY name ASC, id ASC'
    dataFrame = pd.read_sql_query(command_string, conn)
    dataFrame.to_excel(fileName, index=False)

#outAlphabName(databaseName, tableName, xlFileName)

#Output by increasing popularity
#   To reverse order: change 'ASC' to 'DESC'
def outPopularity(dbName, tblName, fileName):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    command_string = f'SELECT * FROM {tblName} ORDER BY popularity ASC, name ASC'
    dataFrame = pd.read_sql_query(command_string, conn)
    dataFrame.to_excel(fileName, index=False)

#outPopularity(databaseName, tableName, xlFileName)
