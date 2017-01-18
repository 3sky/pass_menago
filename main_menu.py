import db_tools as db
import pass_gen as ps
import getpass


def welcome(text):
    ps.clear()
    print('|====================================================|')
    print('|                                                    |')
    print("|              %s                |" % (text))
    print('|                                                    |')
    print('|====================================================|')


def main():
    main_actiity = input("\nWhat you want to do?         \n"
                         "\n  Create account - 1 \n"
                         "  Use yours data - 2 \n"
                         "  Generate password - 3 \n"
                         "  Need help ? - 4 \n"
                         "\n"
                         ">>> ")
    if main_actiity == '1':
        db.create_user()
        welcome('Welcome in Pass Menago')
        main()
    elif main_actiity == '2':
        if log_in():
            welcome('Welcome in Pass Menago')
            menage_date()
            main()
    elif main_actiity == '3':
        ps.generator_menu()
        main()
    elif main_actiity == '4':
        manual()
        welcome('Welcome in Pass Menago')
        main()
    elif main_actiity == '.exit':
        welcome('     To next time     ')
        exit()
    elif main_actiity == '':
        print('Nara frajerze')
    else:
        welcome('Welcome in Pass Menago')
        main()


def log_in():
    global login
    print('Log in please')
    login = input("Username: ")
    user_password = getpass.getpass(prompt="Password: ")
    if login == '.back':
        print("")
    elif db.check_pass(login, user_password):
        return True
    else:
        print('Oh, something go wrong')
        main()


def menage_date():
    welcome('Welcome in Pass Menago')
    print("Hey, %s " % (login))
    main_actiity = input("\nWhat you want to do?         \n"
                         "\n  Add data - 1 \n"
                         "  Delete date - 2 \n"
                         "  Modify data - 3 \n"
                         "  Show data - 4 \n"
                         "\n"
                         ">>> ")
    if main_actiity == '1':
        description = input("Description: ")
        user_pass = input("Password: ")
        db.insert_data(login, user_pass, description)
    elif main_actiity == '2':
        description = input("Description to delete: ")
        db.del_data(login, description)
    elif main_actiity == '3':
        description = input("Description to mod: ")
        new_password = input("New password: ")
        db.update_password(login, description, new_password)
    elif main_actiity == '4':
        user_func = input("Description: ")
        print(db.show_data(login, user_func))
    elif main_actiity == '.back':
        print('')
    else:
        welcome()
        main()


def manual():
    print('Easy to use:')
    print('- .exit to quit')
    print('- .back to go to previous menu')
    print("'Enter' for back to Pass Menago menu")
    man = input()
    if not man == '':
        manual()


db.init_table()
welcome('Welcome in Pass Menago')
main()

