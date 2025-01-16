from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
# Create your models here.
class Board(models.Model):
    name =models.CharField(max_length=100,unique=True)
    description=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Topic(models.Model):
    subject=models.CharField(max_length=100)
    board=models.ForeignKey(Board,related_name='topics',on_delete=models.CASCADE)
    created_by=models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject
class Post(models.Model):
    message=models.TextField(max_length=4000)
    topic=models.ForeignKey(Topic,related_name='posts',on_delete=models.CASCADE)
    created_by=models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        msg=Truncator(self.message)
        return msg.chars(30)