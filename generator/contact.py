# -*- coding: utf-8 -*-
import string
import random
import os
import jsonpickle
import getopt
import sys
from model.contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(prefix, maxlen):
    symbols = string.digits + "()-+ "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(prefix, maxlen):
    symbols = string.ascii_lowercase + string.digits + "-+_."*10
    return prefix + "".join([(random.choice(symbols)+"@qwerty.com") for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="",
                    title="", company="", address="", homephone="", email1=""
                    )] + [Contact(firstname=random_string("firstname", 10),
                                  middlename=random_string("middlename", 20),
                                  lastname=random_string("lastname", 15),
                                  nickname=random_string("nickname", 15),
                                  title=random_string("title", 15),
                                  company=random_string("company", 15),
                                  address=random_string("address", 15),
                                  homephone=random_phone("phone-", 15),
                                  email1=random_email("email-", 2)
                                  )
            for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
