from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests
import json
import datetime


def index(request):
    db = []
    for i in range(10):
        data = requests.get('https://random-data-api.com/api/restaurant/random_restaurant')
        db.append(json.loads(str(data.text)))

    # doing stuff for web
    current_timestamp = datetime.datetime.now()
    day = current_timestamp.weekday()
    correct_data = []
    for data in db:
        hotel_time = data['hours'][list(data['hours'].keys())[day]]
        opens_at =  datetime.datetime.strptime(hotel_time['opens_at'], '%I:%M %p')
        opens_at = opens_at.replace(year=current_timestamp.year,month=current_timestamp.month,day=current_timestamp.day)
        closes_at = datetime.datetime.strptime(hotel_time['closes_at'], '%I:%M %p')
        closes_at = closes_at.replace(year=current_timestamp.year,month=current_timestamp.month,day=current_timestamp.day)
        if current_timestamp > opens_at and current_timestamp < closes_at:
            correct_data.append(data)

    return_data = ''
    if correct_data:
        for i in correct_data:
            return_data += '<br><br><br><br>' + json.dumps(i)
    else:
        return_data = 'No hotels found'

    return HttpResponse(return_data)
