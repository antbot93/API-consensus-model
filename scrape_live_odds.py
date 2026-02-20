import requests
from config import API_KEY, SPORT, REGIONS, MARKETS, ODDS_FORMAT, BASE_URL

def scrape_live_odds():

    url = f"{BASE_URL}/{SPORT}/odds"

    params = {
        "apiKey": API_KEY,
        "regions": REGIONS,
        "markets": MARKETS,
        "oddsFormat": ODDS_FORMAT
    }

    response = requests.get(url, params=params)

    return response.json()