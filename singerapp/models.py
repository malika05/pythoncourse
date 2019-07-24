from django.db import models

# Create your models here.

class Labels(models.Model):
    name = models.CharField(max_length = 50)
    date = models.IntegerField(default=True)
    people = models.IntegerField(default=True)
    def __str__(self):
        return self.name

class Groups(models.Model):
    name = models.CharField(max_length = 50)
    date = models.IntegerField(default=True)
    people = models.IntegerField(default=True)
    labels = models.CharField(max_length = 50)
    def __str__(self):
        return self.name

class Feedback(models.Model):
    ch = (
        (0, 'like'),
        (1, 'dislike'),
    )
    like_dislike = models.CharField(max_length=1, choices=ch)
    comments =  models.CharField(max_length = 50)
    #owner = models.ForeignKey('auth.User', related_name='feedback', on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.comments

class Singers(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField(default=True)
    nationality = models.CharField(max_length = 50)
    groups = models.CharField(max_length = 50)
    rate = models.FloatField(default=True)
    comments = models.CharField(max_length=200, default=True)
    def __str__(self):
        return self.name

class Solo_singer(models.Model):
    name = models.CharField(max_length = 50)
    date = models.IntegerField(default=True)
    people = models.IntegerField(default=True)
    labels = models.CharField(max_length = 50)
    def __str__(self):
        return self.name

