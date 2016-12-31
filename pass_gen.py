import os
import random
import string


def main():
     main_actiity = input("\nWhat strong password do you need \n"
                         "\n  * Weak \n"
                         "  * Strong \n"
                         "  * Unix like\n"
                         "  Press exit for exit \n"
                         "What do you need(weak/strong/unix)? ")
     main_actiity.lower()
     if main_actiity == 'weak':
         weak_gen()
         main()
     elif main_actiity == 'strong':
         clear()
         [strong_gen() for _ in range(8)]
         main()
     elif main_actiity == 'unix':
         clear()
         [unix_pass_gen() for _ in range(8)]
         main()
     elif main_actiity == 'exit':
         print("\nTo next time man")
         exit()
     else:
         main()


def weak_gen():
    weak_req = input("Do you really need gen weak password(yes/no): ")
    if weak_req == "yes":
        clear()
        for _ in range(8):
            gen_pass(5)
            random.shuffle(pwlist)
            pwstring = "".join(pwlist)
            print(pwstring)
    elif weak_req == "no":
        main()
    else:
        weak_gen()


def strong_gen():
    gen_pass(8)
    random.shuffle(pwlist)
    pwstring = "".join(pwlist)
    print(pwstring)


def unix_pass_gen():
    global pwlist
    pwlist = []
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


clear()
pwlist = []
main()