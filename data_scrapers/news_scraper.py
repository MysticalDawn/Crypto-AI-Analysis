from newsapi import NewsApiClient
import pickle
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def fetch_newsapi(
    api_key=None,
    query="+bitcoin",
    sources="bbc-news,the-verge,the-wall-street-journal,the-new-york-times,cnbc,reuters,reuters,bloomberg",
    language="en",
    sort_by="relevancy",
    page=1,
    page_size=100,
    save_file=True,
):
    # Use environment variable if no API key provided
    if api_key is None:
        api_key = os.getenv("NEWSAPI_KEY")
        if not api_key:
            raise ValueError("NEWSAPI_KEY environment variable not set")
    newsapi = NewsApiClient(api_key=api_key)
    all_articles = newsapi.get_everything(
        q=query,
        sources=sources,
        language=language,
        sort_by=sort_by,
        page=page,
        page_size=page_size,
    )
    if save_file:
        with open("./data/news_results.pkl", "wb") as f:
            pickle.dump(all_articles, f)
    refined_articles = {
        "date": [],
        "full_text": [],
        "sentiment_score": [],
        "sentiment_type": [],
    }
    for article in all_articles["articles"]:
        refined_articles["date"].append(article["publishedAt"][:10])
        refined_articles["full_text"].append(
            article["title"] + " " + article["description"]
        )
    print(refined_articles)
    return refined_articles


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
