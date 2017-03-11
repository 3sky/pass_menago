import sqlite3
import re
import hashlib
import getpass


def show_data(user_name, description):
    conn = sqlite3.connect('meango.db')
    cursor = conn.cursor()
    cursor.execute("SELECT PASSWORD FROM APP_DB WHERE USER = '%s' and DESCRIPTION = '%s'" %
                   (user_name, description))
    query_output = str(cursor.fetchone())
    password = ''.join(query_output.split())[2:-3]
    return password
    conn.close()


def select_user(user_name):
    conn = sqlite3.connect('meango.db')
    cursor = conn.cursor()
    cursor.execute("SELECT MASTER_PASS FROM SEC WHERE USER = '%s'" %
                   user_name)
    query_output = str(cursor.fetchone())
    password = re.sub('[^A-Za-z0-9]+', '', query_output)
    return password
    conn.close()


def insert_data(user_name, user_pass, description):
    conn = sqlite3.connect('meango.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO APP_DB (user,password,description) VALUES ('%s','%s','%s')" %
                   (user_name, user_pass, description))
    conn.commit()
    conn.close()


def insert_user(user_name, hash_pass):
    conn = sqlite3.connect('meango.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO SEC (USER,MASTER_PASS) VALUES ('%s','%s')" %
                   (user_name, hash_pass))
    conn.commit()
    conn.close()


def update_password(user_name, description, new_password):
    conn = sqlite3.connect('meango.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE APP_DB SET PASSWORD = '%s' WHERE USER = '%s' and DESCRIPTION = '%s'" %
                   (new_password, user_name, description))
    conn.commit()
    conn.close()


def init_table():
    conn = sqlite3.connect('meango.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS APP_DB
         (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             USER text,
             PASSWORD text,
             DESCRIPTION real)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS SEC
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             USER text,
             MASTER_PASS text)''')
    conn.commit()
    conn.close()


def check_pass(user_name, user_passwd):
    conn = sqlite3.connect('meango.db')
    cursor = conn.cursor()
    cursor.execute("SELECT MASTER_PASS FROM SEC WHERE USER = '%s'" %
                   user_name)
    query_output = str(cursor.fetchone())
    db_pass = re.sub('[^A-Za-z0-9]+', '', query_output)
    conn.close()
    user_hash = hashlib.sha512(user_passwd.encode())
    if user_hash.hexdigest() == db_pass:
        return True


def create_user():
    user_name = input("Insert username: \n"
                      ">>> ")
    if user_name == '.exit':
        print("")
    elif (select_user(user_name)) == 'None':
        user_password = getpass.getpass(prompt='Insert yours master password: ')
        hash_passwd = hashlib.sha512(user_password.encode())
        insert_user(user_name, hash_passwd.hexdigest())
    else:
        print('This user already exists')
        create_user()


def del_data(user_name, description):
    conn = sqlite3.connect('meango.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM APP_DB WHERE description='%s' and user='%s'" % (description, user_name))
    conn.commit()
    conn.close()



