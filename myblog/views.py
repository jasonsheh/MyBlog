#!/usr/bin/python
# __author__ = 'jasonsheh'
# -*- coding:utf-8 -*-
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Article


def index(request):
    articles = Article.objects.order_by('-id')[0:12]
    return render(request, 'index.html', {'articles': articles})


def articles(request, page):
    if not page:
        page = 1
    articles = Article.objects.order_by('-id')
    paginator = Paginator(articles, 10)
    part_articles = paginator.page(page)
    return render(request, 'articles.html', {'articles': part_articles})


def article(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'article.html', {'article': article})


def about(request):
    return render(request, 'about.html', )


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
    return render(request, 'manage/article_list.html', {'articles': part_articles})


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    content = article.content
    return render(request, 'manage/article_detail.html', {'content': content, 'article_id':article_id})


def alter_article(request):
    article = Article.objects.get(id=request.POST['article_id'])
    article.content = request.POST['content']
    article.save()
    return HttpResponseRedirect('/manage/article/'+request.POST['article_id'])


def delete_article(request, article_id):
    article = Article.objects.get(id=article_id)
    content = article.content
    return render(request, 'manage/article_detail.html', {'content': content})


def admin_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return render(request, 'manage.html')
    else:
        return HttpResponseRedirect('/')

