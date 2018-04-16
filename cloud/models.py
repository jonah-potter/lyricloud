from django.db import models

class Word(models.Model):
    text = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.text

class Song(models.Model):
    title = models.CharField(max_length=500)
    credit = models.CharField(max_length=500)
    lyrics = models.TextField()
    words = models.ManyToManyField(Word, through='SongWord')

    def __str__(self):
        return self.title+" by "+self.credit

class SongWord(models.Model):
    count = models.IntegerField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

    def __str__(self):
        return 'The word "'+str(self.word)+'" appears '+str(self.count)+' times in '+str(self.song)
