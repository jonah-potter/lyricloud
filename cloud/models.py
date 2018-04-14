from django.db import models

class Word(models.Model):
    text = models.CharField(max_length=50)

class Song(models.Model):
    title = models.CharField(max_length=500)
    credit = models.CharField(max_length=500)
    words = models.ManyToManyField(Word, through='SongWord')

class SongWord(models.Model):
    count = models.IntegerField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
