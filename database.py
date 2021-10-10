# Importing a module for sqlite3 that is included in python3
import sqlite3

# The name of the database will be account.db

# With the help of the cursor.execute I can execute some sqlite commands. Also using "*6 helps to write commands in new line
# Creating a table, that has 4 cols, name, entity, id_account, amount_money
# This is a function for creating Table
def createTable(tableName):

    # Making connection to the database named accounts.db, if it's not created, it will be created with that name
    conn = sqlite3.connect('database.sqlite')

    # Cursor that is used to work with the database
    cursor = conn.cursor()

    # Defining the command for creating a table with a tableName, that has atributes name, entity, id_account, amount_money
    table = f""" CREATE TABLE {tableName}(
            name text,
            entity text,
            id_account int,
            amount_money real
    )"""

    # Executing the command
    cursor.execute(table)

    # Sending the changes for the database
    conn.commit()

    # Closing the connection
    conn.close()

# This is a function for inserting accounts into the database
def insertTable(tableName):
    # Making connection to the database named accounts.db, if it's not created, it will be created with that name
    conn = sqlite3.connect('database.sqlite')

    # Cursor that is used to work with the database
    cursor = conn.cursor()

    # Defining a list that will store all the accounts till they are inserted into the database
    acc = []
    print('How many accounts you want to insert into the database: ')
    n = int(input())

    for i in range(n):
        # Inserting account by account
        account = (input('Enter the name of the entity: ').capitalize(), input('Enter what kind of entity are you inserting(Person/Company): ').capitalize(), int(input('Enter the ID of the account: ')),float(input('Enter the amount of money on the account: ')))
        # Appending the account into the list
        acc.append(account)

    # Inserting all the accounts into the database, to be precise to the table that is defined with tableName
    cursor.executemany(f"INSERT INTO {tableName} VALUES (?,?,?,?)", acc)

    # Sending the changes for the database
    conn.commit()

    # Closing the connection
    conn.close()

# This is a function for printing the table from the database
def printTable(tableName):
    # Making connection to the database named accounts.db, if it's not created, it will be created with that name
    conn = sqlite3.connect('database.sqlite')

    # Cursor that is used to work with the database
    cursor = conn.cursor()

    # Defining the command that needs to be executed on the table with tableName
    table = f"SELECT rowid, * from {tableName}"

    # Selecting everything from the database from table accounts with their primary key
    cursor.execute(table)

    # Fetching all and all that is fetched, store in a variable
    accounts = cursor.fetchall()

    # Going through that variable(probably list) and printing all the elements one by one
    for account in accounts:
        print(account)
        print()
    print("Done !")

    # Sending the changes for the database
    conn.commit()

    # Closing the connection
    conn.close()

# This is a function for deleting(dropping) a table from the database
def deleteTable(tableName):

    # Making connection to the database named accounts.db, if it's not created, it will be created with that name
    conn = sqlite3.connect('database.sqlite')

    # Cursor that is used to work with the database
    cursor = conn.cursor()

    # Defining the command that needs to be executed on the table with tableName
    table = f"DROP TABLE {tableName}"

    # Dropping the table, deleting it
    cursor.execute(table)

    # Sending the changes for the database
    conn.commit()

    # Closing the connection
    conn.close()

    print('TABLE DELETED !!!')

def deleteById(tableName, id):

    # Making connection to the database named accounts.db, if it's not created, it will be created with that name
    conn = sqlite3.connect('database.sqlite')

    # Cursor that is used to work with the database
    cursor = conn.cursor()

    # Defining the command
    table = f"DELETE from {tableName} WHERE rowid = {id}"

    # Executing the command
    cursor.execute(table)

    # Sending the changes for the database
    conn.commit()

    # Closing the connection
    conn.close()

printTable('proba')