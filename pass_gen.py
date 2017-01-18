import os
import random
import string


def generator_menu():
    pwlist = []
    global pwlist
    clear()
    main_actiity = (input("\nWhat strong password do you need \n"
                          "\n  # Weak - 1 \n"
                          " # Strong - 2\n"
                          "  # Unix like - 3 \n"
                          ">>> "))
    if main_actiity == '1':
        weak_gen()
    elif main_actiity == '2':
        clear()
        [strong_gen() for _ in range(8)]
    elif main_actiity == '3':
        clear()
        [unix_pass_gen() for _ in range(8)]
    elif main_actiity == '.back':
        clear()
    else:
        generator_menu()


def weak_gen():
    weak_req = input("Do you really need gen weak password(Y/n): ")
    weak_req.lower()
    if weak_req == "y":
        clear()
        for _ in range(8):
            gen_pass(5)
            random.shuffle(pwlist)
            pwstring = "".join(pwlist)
            print (pwstring)
    elif weak_req == "n":
        generator_menu()
    else:
        weak_gen()


def strong_gen():
    gen_pass(8)
    random.shuffle(pwlist)
    pwstring = "".join(pwlist)
    print(pwstring)


def unix_pass_gen():
    pwlist = []
    global pwlist
    gen_pass(8)
    gen_random(string.digits)
    gen_random(string.punctuation)
    random.shuffle(pwlist)
    pwstring = "".join(pwlist)
    print(pwstring)


def gen_pass(sing):
    while len(pwlist) < sing:
        word = random.choice(string.ascii_letters)
        if word.lower() not in pwlist:
            if word.upper() not in pwlist:
                pwlist.append(word)


def gen_random(string_type):
    pwlist.append(random.choice(string_type))


def clear():
    os.system('cls')
