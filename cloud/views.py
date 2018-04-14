from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    return HttpResponse("Hello, World!")

def song(request):
    s = models.Song(title='Find Your Cloud', credit='Papadosio')
    s.save()
    w = models.Word(text='dream')
    w.save()
    sw = models.SongWord.objects.create(song=s, word=w, count=1)
    response = s.title+" by "+s.credit+" contains the word(s) \""+w.text+"\" "+str(sw.count)+" time(s)."
    return HttpResponse(response)
