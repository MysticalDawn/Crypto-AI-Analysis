import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def fetch_gnews(
    api_key=None,
    query="bitcoin",
    page=1,
    max_pages=100,
):
    # Use environment variable if no API key provided
    if api_key is None:
        api_key = os.getenv("GNEWS_API_KEY")
        if not api_key:
            raise ValueError("GNEWS_API_KEY environment variable not set")

    url = f"https://gnews.io/api/v4/search?q={query}&page={page}&max={max_pages}&lang=en&from=2024-08-08&to=2025-08-08&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    refined_articles = {
        "date": [],
        "full_text": [],
        "sentiment_score": [],
        "sentiment_type": [],
    }

    for article in data["articles"]:
        refined_articles["date"].append(article["publishedAt"][:10])
        refined_articles["full_text"].append(
            article["title"] + " " + article["description"]
        )

    print(refined_articles)
    return refined_articles


if __name__ == "__main__":
    fetch_gnews()
