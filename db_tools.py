import sqlite3
import re
import hashlib
import getpass


def show_data(user_name, function):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("SELECT PASSWORD FROM APP_DB WHERE USER = '%s' and FUNCTION = '%s'"
            % (user_name, function))
    query_output = str(cursor.fetchone())
    password = re.sub('[^A-Za-z0-9]+', '', query_output)
    return (password)
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
    if user_hash.hexdigest() == db_pass:
        return True


def create_user():
    init_table()
    name = input("Insert yours username: \n"
                 ">>> ")
    user_name = name.lower()
    if user_name == 'exit()':
        print("")
    elif (select_user(user_name)) == 'None':
        user_password = getpass.getpass(prompt='Insert yours master password: ')
        hash_passwd = hashlib.sha512(user_password.encode())
        insert_user(user_name, hash_passwd.hexdigest())
    else:
        print('This user already exists')
        create_user()


def del_data(user_func):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM APP_DB WHERE function='%s'" % (user_func))
    conn.commit()
    conn.close()



