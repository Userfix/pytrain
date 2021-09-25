# -*- coding: utf-8 -*-
import random
import string
import pytest
from model.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(prefix, maxlen):
    symbols = string.digits + "()-+ "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(prefix, maxlen):
    symbols = string.ascii_lowercase
    return prefix + "".join([(random.choice(symbols)+"@qwerty.com") for i in range(random.randrange(maxlen))])

# testdata = [
#     Contact(firstname=firstname, middlename=middlename, lastname=lastname)
#     for firstname in ["", random_string("firstname", 10)]
#     for middlename in ["", random_string("middlename", 20)]
#     for lastname in ["", random_string("lastname", 15)]
# ]


testdata = [Contact(firstname="",
                    middlename="",
                    lastname="",
                    nickname="",
                    title="",
                    company="",
                    address="",
                    homephone="",
                    email1=""
                    )] + [Contact(firstname=random_string("firstname", 10),
                                  middlename=random_string("middlename", 20),
                                  lastname=random_string("lastname", 15),
                                  nickname=random_string("nickname", 15),
                                  title=random_string("title", 15),
                                  company=random_string("company", 15),
                                  address=random_string("address", 15),
                                  homephone=random_phone("phone-", 15),
                                  email1=random_email("email-", 1)
                                  )
            for i in range(3)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
