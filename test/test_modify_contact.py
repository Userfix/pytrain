# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.contact.modify_first_contact(Contact(firstname="123Updated FirstName", middlename="Updated MiddleName",
                                             lastname="Updated LastName", nickname="UpdNickname",
                                             title="ABC", company="Solar", address="Gogolya 2",
                                             phone="+7499000000", email="quest@test.com",
                                             bday="11", bmonth="July", byear="1862"))


def test_modify_contact(app):
    app.contact.modify_first_contact(Contact(firstname="Updated FirstName"))
