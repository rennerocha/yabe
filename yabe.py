# -*- coding: utf-8 -*-
from bottle import (abort, get, route, run, view)
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


@get('/<year:int>/<month:int>/<slug>')
@view('post')
def specific_post(year, month, slug):
    try:
        last_post = Post.select().where(Post.published==True).where(Post.slug==slug).where(Post.date.year==year).where(Post.date.month==month).get()
        page_title = last_post.title
    except Post.DoesNotExist:
        abort(404, "POST not found.")

    return {'post': last_post, 'page_title': page_title}


@get('/new/post')
@view('new_post')
def new_post_form():
    return {}



run(host='localhost', port=8080, debug=True, reloader=True)

