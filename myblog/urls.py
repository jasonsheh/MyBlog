"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from myblog.views import index, articles, article, about, manage, manage_articles, article_detail, alter_article, admin_login

urlpatterns = [
    path('', index),
    re_path('^articles/(\d*)', articles),
    re_path('^article/(\d*)', article),
    path('about/', about),
    path('manage/', manage),
    path('edit_article/alter/', alter_article),
    re_path('^manage/article/(\d*)', article_detail),
    re_path('^manage/articles/(\d*)', manage_articles),
    path('login/', admin_login),
]
