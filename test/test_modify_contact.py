# -*- coding: utf-8 -*-
from random import randrange

from model.contact import Contact


def test_modify_contact(app):
    create_contact_if_blank(app)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Updated FirstName", middlename="Updated MiddleName", lastname="Updated LastName",
                      nickname="UpdNickname", title="ABC", company="Solar", address="Gogolya 2",
                      homephone="84953333333", mobilephone="+7499000000", email="quest@test.com",
                      bday="11", bmonth="July", byear="1862")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_contact_name_only(app):
#     create_contact_if_blank(app)
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="Only Updated FirstName", lastname="")
#     app.contact.modify_first_contact(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)


def create_contact_if_blank(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="NewFirstName 1"))
