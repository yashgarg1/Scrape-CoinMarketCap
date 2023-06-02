import requests
from bs4 import BeautifulSoup

def scrape_coinmarketcap(url):
    # Make a request to the coinmarketcap website.
    response = requests.get(url)

    # Parse the response as HTML.
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table of cryptocurrency data.
    table = soup.find("table", class_="cmc-table")

    # Get the data from the table.
    data = {"data": []}
    for row in table.find_all("tr"):
        cells = row.find_all("td")
        # TODO: correct the order of these cells to get correct data
        # TODO: Handle the update data case (no duplicates)
        data["data"].append({
            "name": cells[2].text if len(cells) > 2 else "",
            "price": cells[3].text if len(cells) > 3 else "",
            "1h%": cells[4].text if len(cells) > 4 else "",
            "24h%": cells[5].text if len(cells) > 5 else "",
            "7d%": cells[6].text if len(cells) > 6 else "",
            "market_cap": cells[7].text if len(cells) > 7 else "",
            "volume(24h)": cells[8].text if len(cells) > 8 else "",
            "circulating_supply": cells[9].text if len(cells) > 9 else ""
        })

    return data


def send_data(data, url):
    headers = {
        'Content-Type': 'application/json'
    }
    requests.post(url, json=data, headers=headers)


def update_values():
    """
    The main function.
    """
    print("hello abc")
    url = "https://coinmarketcap.com/"
    post_url = "http://127.0.0.1:8000/app/update_data/"
  
    data = scrape_coinmarketcap(url)
    send_data(data, post_url)