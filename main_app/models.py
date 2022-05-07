from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=250)
    img = models.CharField(max_length=1000)
    cast = models.CharField(max_length=1000)
    trailer = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Play(models.Model):
    title = models.CharField(max_length=250)
    img = models.CharField(max_length=1000)
    director = models.CharField(max_length=250)
    cast = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Book(models.Model):
    title = models.CharField(max_length=250)
    img = models.CharField(max_length=1000)
    author = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    preview = models.CharField(max_length=1000)
    movies = models.ManyToManyField(Movie)
    plays = models.ManyToManyField(Play)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']



