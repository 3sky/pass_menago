import random
import string


class UserInfo:
    def __init__(self):
        self.user_name = 'No_one'
        self.user_passwd = ''

    def sing_user(self, user_name, user_passwd):
        self.user_name = user_name
        self.user_passwd = user_passwd


def weak_gen():
    global pwlist
    pwlist = []
    gen_pass(5)
    random.shuffle(pwlist)
    pwstring = "".join(pwlist)
    return pwstring


def strong_gen():
    global pwlist
    pwlist = []
    gen_pass(8)
    random.shuffle(pwlist)
    pwstring = "".join(pwlist)
    return pwstring


def unix_pass_gen():
    global pwlist
    pwlist = []
    gen_pass(8)
    gen_random(string.digits)
    gen_random(string.punctuation)
    random.shuffle(pwlist)
    pwstring = "".join(pwlist)
    return pwstring


def gen_pass(sing):
    while len(pwlist) < sing:
        word = random.choice(string.ascii_letters)
        if word.lower() not in pwlist:
            if word.upper() not in pwlist:
                pwlist.append(word)


def gen_random(string_type):
    pwlist.append(random.choice(string_type))
