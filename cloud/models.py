from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=500)
    credit = models.CharField(max_length=500)

class Word(models.Model):
    text = models.CharField(max_length=50)
    occurances = models.IntegerField()
    songs = models.ManyToManyField(Word)
