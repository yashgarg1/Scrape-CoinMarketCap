# CoinMarketCap Data Scraper and Display
This project is a web application that scrapes data from CoinMarketCap.com and displays it in a tabular format on a web page. It provides real-time updates of cryptocurrency information such as name, price, percentage changes, market cap, volume, and circulating supply.

# Features
Web scraper to extract cryptocurrency data from CoinMarketCap.com.
Django backend to handle HTTP requests and update the database with scraped data.
MySQL database to store the cryptocurrency information.
HTTP GET request to retrieve the latest data from the database.
React frontend to display the data in a tabular format.
Automatic data refresh every 3 seconds.

# Technologies Used
Python,
Django,
MySQL,
React,
JavaScript,
HTML/CSS

# Some Useful Commands
django-admin startproject scrapperSite,
cd ./scrapperSite/,
python3 ./manage.py startapp scrapperApp,
python3 ./manage.py migrate,
python3 ./manage.py runserver,

for migration
python3 ./manage.py makemigrations,
python3 ./manage.py migrate,

Used basic run commands for creating ract app and running it using npm start

Project Doc - https://docs.google.com/document/d/1GJFDcqAGq4XaKlfGTpIAvZtKcybGToQ0BcuiqtguEoY/edit?usp=sharing