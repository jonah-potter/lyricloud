from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    return HttpResponse("Hello, World!")

def song(request):
    # i know this is gross but it's dummy data
    s = models.Song(title='Find Your Cloud',
                    credit='Papadosio',
                    lyrics="Dream out loud and make no sound\nFind your cloud and ride it 'round")
    s.save()
    wordStrings = s.lyrics.replace('\n', ' ').split(' ')
    for wordString in wordStrings:
        wordString = wordString.lower()
        # get_or_create returns a tuple with the object gotten or created and a boolean value reflecting whether it was created
        w = models.Word.objects.get_or_create(text=wordString)[0]
        # normally you could just use s.words.add(w),
        # but Song and Word relate through an intermediate join table with fields of its own
        sw = models.SongWord.objects.create(song=s, word=w, count=wordStrings.count(wordString))
        w.save()
        sw.save()
    return HttpResponse(s.title+" by "+s.credit+" contains the word(s) \""+w.text+"\" "+str(sw.count)+" time(s).")
