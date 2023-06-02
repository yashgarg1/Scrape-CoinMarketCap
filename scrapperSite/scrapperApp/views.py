from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from scrapperApp.scraper import *
from scrapperApp.models import *
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
import requests

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

    return HttpResponse("Data updated successfully.")


def get_latest_data(request):
    # Get the latest cryptocurrency data from the database.
    cryptocurrency_data = Cryptocurrency.objects.all()

    data = serializers.serialize('json', cryptocurrency_data)

    return JsonResponse(data, safe=False)
