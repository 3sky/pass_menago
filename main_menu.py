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
                         "  Zero to quit - 0 \n"
                         "\n"
                         ">>> ")
    if main_actiity == '1':
        print('Insert you date')
        db.create_user()
#        welcome()
        main()
    elif main_actiity == '2':
        print('Yours data')
        main()
    elif main_actiity == '3':
        ps.generator_menu()
        main()
    elif main_actiity == '4':
        print ('Sam se napisz manual')
        welcome()
        main()
    elif main_actiity == '0':
        print ('Nara frajerze')
        exit()
    elif main_actiity == '':
        print ('Nara frajerze')
    else:
        welcome()
        main()

welcome()
main()

