# -*- coding: utf-8 -*-
from bottle import (get, route, run, view)
from models import Post


@get('/')
@view('post')
def index():
    try:
        last_post = Post.select().where(Post.published==True).order_by(Post.date).limit(1).get()
        page_title = last_post.title
    except Post.DoesNotExist:
        last_post = None
        page_title = 'Nothing posted yet.'
        
    return {'post': last_post, 'page_title': page_title}


run(host='localhost', port=8080, debug=True, reloader=True)

