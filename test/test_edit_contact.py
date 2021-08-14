# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(f_name="Updated FirstName", m_name="Updated MiddleName",
                                           l_name="Updated LastName", nickname="UpdatedAutoTestUser",
                                           phone="+7499000000", email="quest@test.com",
                                           bday="11", bmonth="July", byear="1862"))
    app.session.logout()
