import requests
from bs4 import BeautifulSoup

def scrape_coinmarketcap():
    # Make a request to the coinmarketcap website.
    response = requests.get("https://coinmarketcap.com/")

    # Parse the response as HTML.
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table of cryptocurrency data.
    table = soup.find("table", class_="cmc-table")

    # Get the data from the table.
    data = []
    for row in table.find_all("tr"):
        cells = row.find_all("td")
        data.append({
            "name": cells[0].text if len(cells) > 0 else "",
            "price": cells[1].text if len(cells) > 1 else "",
            "1h%": cells[2].text if len(cells) > 2 else "",
            "24h%": cells[3].text if len(cells) > 3 else "",
            "7d%": cells[4].text if len(cells) > 4 else "",
            "market_cap": cells[5].text if len(cells) > 5 else "",
            "volume(24h)": cells[6].text if len(cells) > 6 else "",
            "circulating_supply": cells[7].text if len(cells) > 7 else ""
        })

    print(data)
    return data
