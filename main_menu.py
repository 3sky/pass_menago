import db_tool as db
import pass_gen as ps


def welcome():
    ps.clear()
    print('|====================================================|')
    print('|                                                    |')
    print('|              Welcome in Pass Menago                |')
    print('|                                                    |')
    print('|====================================================|')


def main():
    main_actiity = input("\nWhat you want to do?         \n"
                         "\n  Create account - 1 \n"
                         "  Use yours data - 2 \n"
                         "  Generate password - 3 \n"
                         "  Need help ? - 4 \n"
                         "  .exit to quit \n"
                         "\n"
                         ">>> ")
    if main_actiity == '1':
        db.create_user()
        welcome()
        main()
    elif main_actiity == '2':
        menage_date()
        main()
    elif main_actiity == '3':
        ps.generator_menu()
        main()
    elif main_actiity == '4':
        print('Sam se napisz manual')
        welcome()
        main()
    elif main_actiity == '.exit':
        print('Nara frajerze')
        exit()
    elif main_actiity == '':
        print('Nara frajerze')
    else:
        welcome()
        main()


def menage_date():
    welcome()
    main_actiity = input("\nWhat you want to do?         \n"
                         "\n  Add data - 1 \n"
                         "  Delete date - 2 \n"
                         "  Modify data - 3 \n"
                         "  Show data - 4 \n"
                         "  .back to back \n"
                         "\n"
                         ">>> ")
    if main_actiity == '1':
        db.insert_data()
    elif main_actiity == '2':
        db.del_data()
    elif main_actiity == '3':
        db.update_password()
    elif main_actiity == '4':
        db.show_data()
    elif main_actiity == '.back':
        print('Nara frajerze')
    else:
        welcome()
        main()


welcome()
main()

