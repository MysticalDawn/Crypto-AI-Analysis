import praw
import re
import datetime
import pickle
import os


def process_submission(submission, results):
    """Helper function to process a single submission and add it to results"""
    if (
        submission.selftext == "[removed]"
        or submission.selftext == "[deleted]"
        or len(submission.selftext) >= 800
    ):
        return

    # convert the date to day/month/year
    results["date"].append(
        datetime.datetime.fromtimestamp(submission.created_utc).strftime("%Y-%m-%d")
    )
    results["title"].append(submission.title)
    results["score"].append(submission.score)
    results["selftext"].append(submission.selftext)
    results["sentiment_score"].append(0)
    results["full_text"].append(
        re.sub(r"http\S+|www\S+|https\S+", "", submission.title.lower().strip())
        + " "
        + re.sub(r"http\S+|www\S+|https\S+", "", submission.selftext.lower().strip())
    )
    results["sentiment_type"].append("Nan")


def reddit_scrapper(
    reddit: praw.Reddit,
    subreddit: str = "CryptoCurrency",
    subreddit_2="Bitcoin",
    subreddit_3="CryptoMarkets",
    subreddit_4="Crypto",
    subreddit_5="CryptoTrading",
    subreddit_6="CryptoAnalysis",
    subreddit_7="CryptoNews",
    subreddit_8="CryptoTrading",
    subreddit_9="CryptoAnalysis",
    subreddit_10="CryptoNews",
    limit: int = 500,
):
    results = {
        "date": [],
        "title": [],
        "score": [],
        "selftext": [],
        "sentiment_score": [],
        "full_text": [],
        "sentiment_type": [],
    }

    # List of subreddits to process
    subreddits = [
        subreddit,
        subreddit_2,
        subreddit_3,
        subreddit_4,
        subreddit_5,
        subreddit_6,
        subreddit_7,
        subreddit_8,
        subreddit_9,
        subreddit_10,
    ]

    # Process each subreddit
    for subreddit_name in subreddits:
        for submission in reddit.subreddit(subreddit_name).hot(limit=limit):
            process_submission(submission, results)

    print(len(results["date"]))
    return results


def fetch_reddit(limit=500, save_file=True, load_file=False):
    if load_file and os.path.exists("./data/reddit_results.pkl"):
        with open("./data/reddit_results.pkl", "rb") as f:
            results = pickle.load(f)
            return results
    reddit = praw.Reddit(
        client_id="Oa6lXOm8M_5rGVdvahmdfQ",
        client_secret="F9QLcAh8dbClNz7z8LwK-o4dqAOseQ",
        user_agent="Crypto for the people",
        username="Dry_Line_4031",
        password="4WQ#b3mI3!^o",
    )
    results = reddit_scrapper(reddit, limit=limit)
    if save_file:
        with open("./data/reddit_results.pkl", "wb") as f:
            pickle.dump(results, f)
    return results
