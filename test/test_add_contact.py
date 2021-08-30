# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="NewFirstName", middlename="NewMiddleName",
                      lastname="NewLastName", nickname="AutoTestUser",
                      title="ZXC", company="Romashka", address="Lenina 1",
                      phone="+74991234567", email="test@test.com",
                      bday="3", bmonth="March", byear="2000")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_contact_name_only(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Qwerty 1")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
