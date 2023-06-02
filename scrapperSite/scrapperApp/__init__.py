import requests
from bs4 import BeautifulSoup
from scrapperApp.scraper import scrape_coinmarketcap

def scrape_data(url):
  """
  Scrapes the data from the given URL.

  Args:
    url: The URL of the website to scrape.

  Returns:
    A dictionary containing the scraped data.
  """

  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'lxml')

  data = {}
  for row in soup.find_all('tr'):
    cols = row.find_all('td')
    data[cols[0].text] = cols[1].text

  return data

def send_data(data, url):
  """
  Sends the given data to the given URL via an HTTP POST request.

  Args:
    data: The data to send.
    url: The URL to send the data to.
  """

  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.post(url, data=json.dumps(data), headers=headers)

  if response.status_code != 200:
    raise Exception('Error sending data: {}'.format(response.status_code))

def main():
    """
    The main function.
    """

    url = "https://coinmarketcap.com/"
    post_url = "http://127.0.0.1:8000/app/update_data/"
    # Scrape the data from the website.
  

    # Send the data to the Django/Flask backend every 5 seconds.
    while True:
        data = scrape_data(url)
        send_data(data, post_url)
        time.sleep(5)

if __name__ == '__main__':
    main()
