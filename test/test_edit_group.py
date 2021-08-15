# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="Updated Name Group",
                                     header="Updated Group Header",
                                     footer="Updated Group Footer"))
