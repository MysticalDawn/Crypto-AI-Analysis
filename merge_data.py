from data_scrapers.reddit_scraper import fetch_reddit
from crypto_sentiment_analysis import classify
from fetch_coin import fetch_coin, get_more_history
from tqdm import tqdm
from datetime import datetime
import pandas as pd
import csv
import pickle
import collections


def merge_data(crypto_data, coin_data, save_file=True):
    finetuned_result = {}
    coin_data_index = pd.to_datetime(coin_data.index).strftime("%Y-%m-%d").tolist()
    for date in coin_data_index:
        finetuned_result[date] = {
            "avg_sentiment_score": [],
            "avg_sentiment_type": [],
            "open": [],
            "high": [],
            "low": [],
            "close": [],
            "volume": [],
        }

    for i, date in tqdm(enumerate(crypto_data["date"])):
        if date in finetuned_result:
            finetuned_result[date]["avg_sentiment_score"].append(
                crypto_data["sentiment_score"][i]
            )
            finetuned_result[date]["avg_sentiment_type"].append(
                crypto_data["sentiment_type"][i]
            )
            finetuned_result[date]["open"].append(coin_data["Open"][date])
            finetuned_result[date]["high"].append(coin_data["High"][date])
            finetuned_result[date]["low"].append(coin_data["Low"][date])
            finetuned_result[date]["close"].append(coin_data["Close"][date])
            finetuned_result[date]["volume"].append(coin_data["Volume"][date])

    for date in finetuned_result:
        if finetuned_result[date][
            "avg_sentiment_score"
        ]:  # Only process dates with sentiment data
            finetuned_result[date]["avg_sentiment_score"] = [
                sum(finetuned_result[date]["avg_sentiment_score"])
                / len(finetuned_result[date]["avg_sentiment_score"])
            ]
            finetuned_result[date]["avg_sentiment_type"] = [
                max(
                    set(finetuned_result[date]["avg_sentiment_type"]),
                    key=finetuned_result[date]["avg_sentiment_type"].count,
                )
            ]
            finetuned_result[date]["open"] = [
                sum(finetuned_result[date]["open"])
                / len(finetuned_result[date]["open"])
            ]
            finetuned_result[date]["high"] = [
                sum(finetuned_result[date]["high"])
                / len(finetuned_result[date]["high"])
            ]
            finetuned_result[date]["low"] = [
                sum(finetuned_result[date]["low"]) / len(finetuned_result[date]["low"])
            ]
            finetuned_result[date]["close"] = [
                sum(finetuned_result[date]["close"])
                / len(finetuned_result[date]["close"])
            ]
            finetuned_result[date]["volume"] = [
                sum(finetuned_result[date]["volume"])
                / len(finetuned_result[date]["volume"])
            ]
        else:
            finetuned_result[date] = {
                "avg_sentiment_score": -1,
                "avg_sentiment_type": -1,
                "open": coin_data["Open"][date],
                "high": coin_data["High"][date],
                "low": coin_data["Low"][date],
                "close": coin_data["Close"][date],
                "volume": coin_data["Volume"][date],
            }

    finetuned_result = {
        k: v for k, v in finetuned_result.items() if v["avg_sentiment_score"]
    }

    for date in finetuned_result:
        for key in finetuned_result[date]:
            if (
                isinstance(finetuned_result[date][key], list)
                and len(finetuned_result[date][key]) == 1
            ):
                finetuned_result[date][key] = finetuned_result[date][key][0]

    finetuned_result = collections.OrderedDict(
        sorted(finetuned_result.items(), reverse=True)
    )

    print("After averaging:", finetuned_result)

    if save_file:
        with open("./data/combined_data.pkl", "wb") as f:
            pickle.dump(finetuned_result, f)

    return finetuned_result
