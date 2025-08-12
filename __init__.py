from merge_data import merge_data
from crypto_sentiment_analysis import classify
from fetch_coin import get_more_history
from data_scrapers.reddit_scraper import fetch_reddit
import os
import pickle
from visualize_market import visualize_avg_sentiment_with_volume
from prepare_dataframe import make_dataframe


def main(visualize=False, reiterate=False):
    if os.path.exists("./data/combined_data.pkl") and not reiterate:
        with open("./data/combined_data.pkl", "rb") as f:
            combined_data = pickle.load(f)
    else:
        reddit_data = fetch_reddit(limit=5000, save_file=True, load_file=not reiterate)
        # news_data = fetch_news(save_file=True)
        coin_data = get_more_history("BTC-USD", days=365 * 5)
        classified_reddit_data = classify(reddit_data)
        # classified_news_data = classify(news_data)
        combined_data = merge_data(classified_reddit_data, coin_data, save_file=True)
    if visualize:
        visualize_avg_sentiment_with_volume(combined_data)

    return make_dataframe(combined_data)


if __name__ == "__main__":
    data = main(reiterate=False)
