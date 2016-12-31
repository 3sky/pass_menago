import getpass
import uuid
import hashlib

def main_menu():
    print("Witaj w Pass Menago")
    what_to_do = input("\nCo chcesz zrobic? \n   "
                       "* Chce zobaczyc moje hasła - wpisz 1 \n   "
                       "* Chce dodac nowe hasło - wpisz 2 \n   "
                       "* Jesli chcesz wyjść - wpisz 3 \n   "
                       "* Jezeli potrzebujesz pomocy - wpisz help \n"
                       "\n Co wybierasz: ")
    if what_to_do == '1':
        see_pass()
    elif what_to_do == '2':
        add_pass()
    elif what_to_do == '3':
        print ("Do zobaczenia")
        exit()
    elif what_to_do == 'help':
        help_page()
    else:
        main_menu


def hash_password(passwd):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + passwd.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


def login_panel():
    name = input("Podaj zwojego uzytkownika: ")
    passwd = getpass.getpass(prompt="Podaj haslo: ")
    passwd_2 = getpass.getpass(prompt="Podaj haslo: ")
    hashed_password = hash_password(passwd)
    hashed_password_2 = hash_password(passwd_2)
    if check_password(hashed_password, hashed_password_2):
        print('You entered the right password')
    else:
        print('I am sorry but the password does not match')
