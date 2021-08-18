# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="NewFirstName", middlename="NewMiddleName",
                               lastname="NewLastName", nickname="AutoTestUser",
                               title="ZXC", company="Romashka", address="Lenina 1",
                               phone="+74991234567", email="test@test.com",
                               bday="3", bmonth="March", byear="2000"))


def test_add_contact(app):
    app.contact.create(Contact(firstname="NewFirstName 1"))
