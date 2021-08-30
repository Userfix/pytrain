# -*- coding: utf-8 -*-
from random import randrange

from model.group import Group


def test_modify_group_name(app):
    create_group_if_blank(app)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New Test Name Group")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#     create_group_if_blank(app)
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New Header Group"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)


def create_group_if_blank(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
