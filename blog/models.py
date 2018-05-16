from django.db import models
import pymysql
# Create your models here.


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    content = models.TextField()
    title = models.TextField()
    post_url = models.TextField()
