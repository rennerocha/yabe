# -*- coding: utf-8 -*-
from bottle import (route, run, view)
from models import Post


@route('/')
@view('post')
def index():
    post = Post.select().where(Post.published==True).order_by(Post.date).limit(1).get()
    return {'post': post}


run(host='localhost', port=8080, debug=True, reloader=True)

