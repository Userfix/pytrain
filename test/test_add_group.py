# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="New Group 1",
                           header="New Group 1",
                           footer="New Group 1"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
