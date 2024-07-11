from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    'january': 'Practice Django for 20 minutes a day - January!',
    'february': 'Practice Django for 20 minutes a day - February!',
    'march': 'Practice Django for 20 minutes a day - March!',
    'april': 'Practice Django for 20 minutes a day - April!',
    'may': 'Practice Django for 20 minutes a day - May!',
    'june': 'Practice Django for 20 minutes a day - June!',
    'july': 'Practice Django for 20 minutes a day - July!',
    'august': 'Practice Django for 20 minutes a day - August!',
    'september': 'Practice Django for 20 minutes a day - September!',
    'october': 'Practice Django for 20 minutes a day - October!',
    'november': 'Practice Django for 20 minutes a day - November!',
    'december': 'Practice Django for 20 minutes a day - December!'
}


def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f'<li><a href=\'{month_path}\'>{capitalized_month}</a></li>'
        response_data = f'<ul>{list_items}</ul'
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('<h1>Invalid Month: This month is not supported!</h1>')
    redirect_month = months[month - 1]
    # build /challenge/[month] dynamically
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,'challenges/challenge.html',{
            'text': challenge_text,
            'month_name':month.capitalize()
        })
    except:
        return HttpResponseNotFound('<h1>This month is not supported!</h1>')
    return HttpResponse(challenge_text)
