from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

monthly_challenges ={
    'january': 'challenge for January!',
    'february': 'Challenge for February!',
    'march': 'Challenge for March!',
    'april': 'Challenge for April!',
    'may': 'Challenge for May!',
    'june': 'Challenge for June!',
    'july': 'Challenge for July!',
    'august': 'Challenge for August!',
    'september': 'Challenge for September!',
    'october': 'Challenge for October!',
    'november': 'Challenge for November!',
    'december': 'Challenge for December!'
}

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound('This month is not supported!')
    return HttpResponse(challenge_text)
