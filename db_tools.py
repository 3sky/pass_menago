import sqlite3
import re
import hashlib
import getpass


def select_password(user_name, function):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("SELECT PASSWORD FROM APP_DB WHERE USER = '%s' and FUNCTION = '%s'"
                   % (user_name, function))
    query_output = str(cursor.fetchone())
    user_name = ''.join(filter(str.isalpha, query_output))
    return (user_name)
    conn.close()


def select_user(user_name):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("SELECT MASTER_PASS FROM SEC WHERE USER = '%s'"
                   % (user_name))
    query_output = str(cursor.fetchone())
    password = re.sub('[^A-Za-z0-9]+', '', query_output)
    return (password)
    conn.close()


def insert_data(user_name, user_pass, user_func):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO APP_DB2 (user,password,function) VALUES ('%s','%s','%s')" %
                   (user_name, user_pass, user_func))
    conn.commit()
    conn.close()


def insert_user(name, hash_pass):
    user_name = name.lower()
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO SEC (USER,MASTER_PASS) VALUES ('%s','%s')" %
                   (user_name, hash_pass))
    conn.commit()
    conn.close()


def update_password(user_name, user_func, new_password):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE APP_DB SET PASSWORD = '%s' WHERE USER = '%s' and FUNCTION = '%s'" %
                   (new_password, user_name, user_func))
    conn.commit()
    conn.close()


def init_table():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS APP_DB
         (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             USER text,
             PASSWORD text,
             FUNCTION real)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS SEC
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             USER text,
             MASTER_PASS text)''')
    conn.commit()
    conn.close()


def check_pass(user_name, user_input):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("SELECT MASTER_PASS FROM SEC WHERE USER = '%s'" %
                   (user_name))
    query_output = str(cursor.fetchone())
    db_pass = re.sub('[^A-Za-z0-9]+', '', query_output)
    conn.close()
    user_hash = hashlib.sha512(user_input.encode())
    print(db_pass)
    print(user_hash.hexdigest())
    if user_hash.hexdigest() == db_pass:
        return True


def create_user():
    #     init_table()
    name = input("Insert yours username: \n"
                 "Q to exit \n "
                 ">>> ")
    user_name = name.lower()
    if user_name == 'q':
        print("")
    elif (select_user(user_name)) == 'None':
        user_password = getpass.getpass(prompt='Insert yours master password: ')
        insert_user(user_name, user_password)
    else:
        print('This user already exists')
        create_user()


# user input question
#     hash pass
#     insert_user(user, password)

create_user()

# if check_pass('ADAM', 'Superjaja'):
#     print('Hura dziala')

# print (select_password('Greg', 'DB'))
# insert_row('Jim','ZXCVASDF','OS')
# update_password('Eva','OS','Nowe_haslo4')
# init_table()