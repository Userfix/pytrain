# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    create_group_if_blank(app)
    app.group.modify_first_group(Group(name="New Test Name Group"))


def test_modify_group_header(app):
    create_group_if_blank(app)
    app.group.modify_first_group(Group(header="New Header Group"))


def create_group_if_blank(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))