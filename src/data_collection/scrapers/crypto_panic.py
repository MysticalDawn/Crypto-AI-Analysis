import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def fetch_cryptoPanic(
    auth_token=None,
    currencies="BTC",
    region="en",
):
    # Use environment variable if no auth token provided
    if auth_token is None:
        auth_token = os.getenv("CRYPTOPANIC_AUTH_TOKEN")
        if not auth_token:
            raise ValueError("CRYPTOPANIC_AUTH_TOKEN environment variable not set")

    url = f"https://cryptopanic.com/api/developer/v2/posts/?auth_token={auth_token}&currencies={currencies}&region={region}"
    response = requests.get(url)
    data = response.json()

    refined_articles = {
        "date": [],
        "full_text": [],
        "sentiment_score": [],
        "sentiment_type": [],
    }

    for article in data["results"]:
        if article["title"] is not None and article["description"] is not None:
            refined_articles["date"].append(article["published_at"][:10])
            refined_articles["full_text"].append(
                article["title"] + " " + article["description"]
            )

    print(refined_articles)
    return refined_articles


if __name__ == "__main__":
    fetch_cryptoPanic()
