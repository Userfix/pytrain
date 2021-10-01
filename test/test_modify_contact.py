# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="NewFirstName 1"))
    old_contacts = db.get_contact_list()
    index = random.randrange(len(old_contacts))
    contact = Contact(firstname="Updated FirstName", middlename="Updated MiddleName", lastname="Updated LastName",
                          nickname="UpdNickname", title="ABC", company="Solar", address="Gogolya 2",
                          homephone="84953333333", mobilephone="+7499000000", email1="quest@test.com",
                          bday="11", bmonth="July", byear="1862")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
