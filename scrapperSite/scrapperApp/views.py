from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from scrapperApp.scraper import *
from scrapperApp.models import *
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
import requests

# Create your views here.
def index(request):
    
    url = "https://coinmarketcap.com/"
    data = scrape_coinmarketcap(url)

    post_url = "http://127.0.0.1:8000/app/update_data/"
    send_data(data, post_url)
    return HttpResponse(data)


def send_data(data, url):

    headers = {
        'Content-Type': 'application/json'
    }
    requests.post(url, json=data, headers=headers)

    # if response.status_code != 200:
    #     raise Exception('Error sending data: {}'.format(response.status_code))

# Create a view that accepts the HTTP POST request and updates the data in the database.
@csrf_exempt 
def update_data(request):
    # Get the data from the request.
    data = json.loads(request.body)
    data_list = data["data"]
    
    # Create a cryptocurrency object for each piece of data.
    for row in data_list:
        cryptocurrency, created = Cryptocurrency.objects.update_or_create(name=row["name"], defaults={"price": row["price"],
            "one_h_percent":row["1h%"],
            "twentyFour_h_percent":row["24h%"],
            "seven_d_percent":row["7d%"],
            "market_cap":row["market_cap"],
            "volume_24h": row["volume(24h)"],
            "circulating_supply": row["circulating_supply"],
        })
        print(cryptocurrency, created)

    return HttpResponse("Data updated successfully.")


def get_latest_data(request):
    # Get the latest cryptocurrency data from the database.
    cryptocurrency_data = Cryptocurrency.objects.all()

    data = serializers.serialize('json', cryptocurrency_data)

    return JsonResponse(data, safe=False)
