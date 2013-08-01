# -*- coding: utf-8 -*-
import datetime
from peewee import (Model, ForeignKeyField, CharField, DateTimeField, 
    TextField, BooleanField, SqliteDatabase)

db = SqliteDatabase('yabe.db')


class Post(Model):
    title = CharField()
    slug = CharField(unique=True)
    date = DateTimeField(default=datetime.datetime.now)
    content = TextField()
    author = CharField(default=u'Renne Rocha')
    published = BooleanField(default=True)

    class Meta:
        database = db


class Comment(Model):
    author = CharField()
    date = DateTimeField(default=datetime.datetime.now)
    comment = TextField()
    post = ForeignKeyField(Post, related_name='comments')

    class Meta:
        database = db

Post.create_table(fail_silently=True)
Comment.create_table(fail_silently=True)

