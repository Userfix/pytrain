# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(f_name="NewFirstName", m_name="NewMiddleName",
                               l_name="NewLastName", nickname="AutoTestUser",
                               phone="+74991234567", email="test@test.com",
                               bday="3", bmonth="March", byear="2000"))
    app.session.logout()
