#!/usr/bin/python
# __author__ = 'jasonsheh'
# -*- coding:utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Article

import time


def index(request):
    articles = Article.objects.order_by('-id')[0:12]
    return render(request, 'index.html', {'articles': articles})


def about(request):
    return render(request, 'about.html', )


def articles(request, page):
    if not page:
        page = 1
    articles = Article.objects.order_by('-id')
    paginator = Paginator(articles, 10)
    part_articles = paginator.page(page)
    return render(request, 'articles.html', {'articles': part_articles, 'total_pages': paginator.num_pages})


def article(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'article.html', {'article': article})


def manage(request):
    if request.user.is_authenticated:
        return render(request, 'manage.html')
    return render(request, 'login.html', )


def manage_articles(request, page):
    if not page:
        page = 1
    articles = Article.objects.order_by('-id')
    paginator = Paginator(articles, 8)
    part_articles = paginator.page(page)
    return render(request, 'manage/article_list.html', {'articles': part_articles, 'total_pages': paginator.num_pages})


def alter_article_interface(request, article_id):
    article = Article.objects.get(id=article_id)
    content = article.content
    title = article.title
    return render(request, 'manage/article_alter.html', {'content': content, 'title': title, 'article_id': article_id})


def add_article_interface(request):
    return render(request, 'manage/article_add.html')


def add_article_logic(request):
    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    modified_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    content = request.POST['content']
    html_content = request.POST['html_content']
    post_url = title = request.POST['title']
    Article.objects.get_or_create(
        create_time=create_time,
        content=content,
        html_content=html_content,
        title=title,
        post_url=post_url,
        modified_time=modified_time
    )
    return HttpResponseRedirect('/manage/articles/')


def alter_article_logic(request):
    article = Article.objects.get(id=request.POST['article_id'])
    article.content = request.POST['content']
    article.html_content = request.POST['html_content']
    article.title = request.POST['title']
    # article.modified_time = time.strftime("%Y-%m-%d %H:%M:%S", now)
    article.save()
    return HttpResponseRedirect('/manage/article/'+request.POST['article_id'])


def delete_article_logic(request, article_id):
    Article.objects.get(id=article_id).delete()
    return HttpResponseRedirect('/manage/articles/')


def admin_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return render(request, 'manage.html')
    else:
        return HttpResponseRedirect('/')


def admin_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
