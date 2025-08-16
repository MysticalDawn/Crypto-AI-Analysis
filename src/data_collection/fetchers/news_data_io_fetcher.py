import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()


def fetch_newsdataio(api_key=None, query="btc"):
    if api_key is None:
        api_key = os.getenv("NEWSDATAIO_API_KEY")
        if not api_key:
            raise ValueError("Newsdataio API key environment variable not set")
    request = requests.get(
        url=f"https://newsdata.io/api/1/crypto?apikey={api_key}&coin={query}&from_date=2024-08-13&to_date=2025-08-14"
    )
    data = request.json()
    print(data)
    refined_articles = {
        "full_text": [],
        "date": [],
    }
    for article in data["results"]:
        if article["title"] is None and article["description"] is None:
            continue
        title = article["title"] or ""
        description = article["description"] or ""
        refined_articles["full_text"].append(title + " " + description)
        refined_articles["date"].append(article["pubDate"])

    return refined_articles


print(fetch_newsdataio())
