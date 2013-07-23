# -*- coding: utf-8 -*-
from bottle import (abort, get, post, redirect, request, route, run, view, static_file)
from models import Comment, Post
from utils import slugify


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


@get('/archive/')
@view('archive')
def archive():
    posts = Post.select()
    return {'posts': posts, 'page_title': 'Archive'}


@get('/<year:int>/<month:int>/<slug>')
@view('post')
def specific_post(year, month, slug):
    try:
        last_post = Post.select().where(Post.published==True).where(Post.slug==slug).where(Post.date.year==year).where(Post.date.month==month).get()
        page_title = last_post.title
    except Post.DoesNotExist:
        abort(404, "POST not found.")

    return {'post': last_post, 'page_title': page_title}


@get('/new/')
@view('new_post')
def new_post_form():
    return {}


@post('/new/')
def create_post():
    title = request.forms.get('post_title')
    content = request.forms.get('post_content')
    author = request.forms.get('post_author')
    slug = slugify(title)
    new_post = Post(title=title, slug=slug, content=content, author=author)
    new_post.save()

    redirect('/{0}/{1}/{2}'.format(new_post.date.year, new_post.date.month, slug))


@post('/new/comment/')
def create_comment():
    comment = request.forms.get('comment')
    author = request.forms.get('author')
    post_id = request.forms.get('post_id')
    post = Post.select().where(Post.id==int(post_id)).get()

    new_comment = Comment(comment=comment, author=author, post=post)
    new_comment.save()

    redirect('/{0}/{1}/{2}'.format(post.date.year, post.date.month, post.slug))

# Static Routes
@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/img')


run(host='localhost', port=8080, debug=True, reloader=True)

