import database

# Short main program for testing the database functions

# First time using if __name__ == '__main__' - learned that is preferable to use it
if __name__ == '__main__':
    name = input('Enter the name of the table you gonna create for storing accounts: ')
    database.createTable(name)
    print('')
    database.printTable(name)
    print('')
    database.insertTable(name)
    print('')
    database.printTable(name)
    print('')
    id = input('Enter the id of the account you want to be deleted from the table: ')
    database.deleteById(name,id)
    print('')
    database.printTable(name)
    print('')
    database.deleteTable()

