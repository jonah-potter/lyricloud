from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    return HttpResponse("Hello, World!")

def song(request):
    s = models.Song(title='Find Your Cloud', credit='Papadosio')
    s.save()
    w = models.Word(text='dream', occurances=1)
    w.save()
    w.songs.add(s)
    response = s.title+" by "+s.credit+" contains the word(s) \""+w.text+"\" "+str(w.occurances)+" time(s)."
    return HttpResponse(response)
