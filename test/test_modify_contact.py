# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="NewFirstName 1"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contactdata = Contact(firstname="Updated FirstName", middlename="Updated MiddleName", lastname="Updated LastName",
                          nickname="UpdNickname", title="ABC", company="Solar", address="Gogolya 2",
                          homephone="84953333333", mobilephone="+7499000000", email1="quest@test.com",
                          bday="11", bmonth="July", byear="1862")
    app.contact.modify_contact_by_id(contact.id, contactdata)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
