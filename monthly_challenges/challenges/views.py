from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.



def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = 'Eat no sugar for the entire month!'
    elif month == 'february':
        challenge_text = 'Walk for at least 20 minutes daily!'
    elif month == 'march':
        challenge_text = 'Learn Django for 20 minutes a day!'
    else:
        return HttpResponseNotFound('This month is not currently supported!')
    return HttpResponse(challenge_text)
