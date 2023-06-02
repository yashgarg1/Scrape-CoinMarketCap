from django.shortcuts import render
from django.http import HttpResponse
from scrapperApp.scraper import scrape_coinmarketcap
from scrapperApp.updateData import *

# Create your views here.
def index(request):
    data = scrape_coinmarketcap()
    request.data = data
    update_data(request)
    return HttpResponse(data)