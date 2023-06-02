# Scrape-CoinMarketCap
This project scrapes cryptocurrency data from coinmarketcap.com and displays it in a tabular format on a web page using a Django/Flask backend and a JavaScript framework frontend.

django-admin startproject scrapperSite
cd ./scrapperSite/
python3 ./manage.py startapp scrapperApp
python3 ./manage.py migrate
python3 ./manage.py runserver

python3 ./manage.py makemigrations 
python3 ./manage.py migrate