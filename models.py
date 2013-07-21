# -*- coding: utf-8 -*-
from peewee import (Model, CharField, DateTimeField, 
    TextField, BooleanField, SqliteDatabase)

db = SqliteDatabase('yabe.db')


class Post(Model):
    title = CharField()
    slug = CharField(unique=True)
    date = DateTimeField()
    content = TextField()
    author = CharField(default=u'Renne Rocha')
    published = BooleanField(default=False)

    class Meta:
        database = db

Post.create_table(fail_silently=True)

