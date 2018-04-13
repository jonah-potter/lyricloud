from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    s = Song(title='Find Your Cloud', credit='Papadosio')
    s.save()
    w = Word(text='dream')
    w.save()
    s.words.add(w)
    response = s.title+" by "+s.credit+" contains word(s): "+w.text+"("+w.occurances+")"
    return HttpResponse(response)
