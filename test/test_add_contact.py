# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(f_name="FirstName", m_name="MiddleName",
                               l_name="LastName", nickname="AutoTestUser",
                               phone="+74991234567", email="test@test.com",
                               bday="3", bmonth="March", byear="2000"))
    app.session.logout()
