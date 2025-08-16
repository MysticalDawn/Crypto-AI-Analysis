from newsapi import NewsApiClient
import pickle
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


if __name__ == "__main__":
    fetch_newsapi()
