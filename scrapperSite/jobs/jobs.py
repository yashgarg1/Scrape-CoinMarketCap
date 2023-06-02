from django.conf import settings
import json
from scrapperApp.scraper import update_values

def schedule_api():
    print("hello there")
    update_values()