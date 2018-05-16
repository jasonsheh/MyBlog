#!/usr/bin/python
# __author__ = 'jasonsheh'
# -*- coding:utf-8 -*-
import os
import pymysql
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")
import django
django.setup()
from blog.models import Article

db = pymysql.connect(host="localhost", user="root", password="root", db="wordpress", port=3306, charset='utf8')
cur = db.cursor()
sql = 'select * from wp_posts'
cur.execute(sql)
results = cur.fetchall()
id = 0
for result in results:
    id += 1
    create_time = result[2]
    content = result[4]
    title = result[5]
    post_url = result[11]
    modified_time = result[14]

    Article.objects.get_or_create(
        id=id,
        create_time=create_time,
        content=content,
        title=title,
        post_url=post_url,
        modified_time=modified_time
    )
    print(id, create_time, title, modified_time)
