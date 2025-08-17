from tqdm import tqdm
import pandas as pd
import pickle
import numpy as np


def merge_data(crypto_data, coin_data, save_file=True):
    print("🔄 Starting data merging process...")
    print(
        f"📊 Processing {len(crypto_data['date'])} crypto posts across {len(coin_data)} trading days"
    )
    if crypto_data is None:
        with open("./data/processed/sentiment_results.pkl", "rb") as f:
            crypto_data = pickle.load(f)
            print("✅ Crypto data loaded successfully")
    else:
        print("✅ Crypto data loaded successfully")

    finetuned_result = {}
    coin_data_index = pd.to_datetime(coin_data.index).strftime("%Y-%m-%d").tolist()

    print("📅 Initializing data structure for all trading days...")
    for date in tqdm(coin_data_index, desc="Initializing dates", unit="date"):
        finetuned_result[date] = {
            "bullish_sentiment_score": [],
            "bearish_sentiment_score": [],
            "neutral_sentiment_score": [],
            "dominant_sentiment_type": None,
            "sentiment_confidence": 0.0,
            "sentiment_strength": 0.0,
            "open": [],
            "high": [],
            "low": [],
            "close": [],
            "volume": [],
        }

    print("🔗 Merging crypto sentiment data with price data...")
    for i, date in tqdm(
        enumerate(crypto_data["date"]),
        desc="Processing posts",
        unit="post",
        total=len(crypto_data["date"]),
    ):
        if date in finetuned_result:
            sentiment_score = crypto_data["sentiment_score"][i]
            sentiment_type = crypto_data["sentiment_type"][i]

            # Separate sentiments by type
            if sentiment_type == "bullish":
                finetuned_result[date]["bullish_sentiment_score"].append(
                    sentiment_score
                )
            elif sentiment_type == "bearish":
                finetuned_result[date]["bearish_sentiment_score"].append(
                    sentiment_score
                )
            elif sentiment_type == "neutral":
                finetuned_result[date]["neutral_sentiment_score"].append(
                    sentiment_score
                )

            finetuned_result[date]["open"].append(coin_data["Open"][date])
            finetuned_result[date]["high"].append(coin_data["High"][date])
            finetuned_result[date]["low"].append(coin_data["Low"][date])
            finetuned_result[date]["close"].append(coin_data["Close"][date])
            finetuned_result[date]["volume"].append(coin_data["Volume"][date])

    print("🧮 Calculating sentiment metrics and aggregating price data...")
    processed_dates = 0
    for date in tqdm(finetuned_result, desc="Calculating metrics", unit="date"):
        if any(
            [
                finetuned_result[date]["bullish_sentiment_score"],
                finetuned_result[date]["bearish_sentiment_score"],
                finetuned_result[date]["neutral_sentiment_score"],
            ]
        ):  # Only process dates with sentiment data
            processed_dates += 1

            # Calculate weighted averages for each sentiment type
            bullish_avg = (
                np.mean(finetuned_result[date]["bullish_sentiment_score"])
                if finetuned_result[date]["bullish_sentiment_score"]
                else 0
            )
            bearish_avg = (
                np.mean(finetuned_result[date]["bearish_sentiment_score"])
                if finetuned_result[date]["bearish_sentiment_score"]
                else 0
            )
            neutral_avg = (
                np.mean(finetuned_result[date]["neutral_sentiment_score"])
                if finetuned_result[date]["neutral_sentiment_score"]
                else 0
            )

            # Determine dominant sentiment type based on highest average score
            sentiment_scores = {
                "bullish": bullish_avg,
                "bearish": bearish_avg,
                "neutral": neutral_avg,
            }

            dominant_type = max(sentiment_scores, key=sentiment_scores.get)
            sentiment_confidence = sentiment_scores[dominant_type]

            # Calculate sentiment strength (difference between dominant and other sentiments)
            other_scores = [
                v for k, v in sentiment_scores.items() if k != dominant_type
            ]
            sentiment_strength = (
                sentiment_confidence - max(other_scores)
                if other_scores
                else sentiment_confidence
            )

            # Store the results
            finetuned_result[date]["bullish_sentiment_score"] = bullish_avg
            finetuned_result[date]["bearish_sentiment_score"] = bearish_avg
            finetuned_result[date]["neutral_sentiment_score"] = neutral_avg
            finetuned_result[date]["dominant_sentiment_type"] = dominant_type
            finetuned_result[date]["sentiment_confidence"] = sentiment_confidence
            finetuned_result[date]["sentiment_strength"] = sentiment_strength

            # Average the price data
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
                "bullish_sentiment_score": 0,
                "bearish_sentiment_score": 0,
                "neutral_sentiment_score": 0,
                "dominant_sentiment_type": "neutral",
                "sentiment_confidence": 0.0,
                "sentiment_strength": 0.0,
                "open": coin_data["Open"][date],
                "high": coin_data["High"][date],
                "low": coin_data["Low"][date],
                "close": coin_data["Close"][date],
                "volume": coin_data["Volume"][date],
            }

    print("🔧 Finalizing data structure...")
    for date in tqdm(finetuned_result, desc="Finalizing", unit="date"):
        for key in finetuned_result[date]:
            if (
                isinstance(finetuned_result[date][key], list)
                and len(finetuned_result[date][key]) == 1
            ):
                finetuned_result[date][key] = finetuned_result[date][key][0]

    print(f"✅ Data merging completed successfully!")
    print(f"  📊 Processed {processed_dates} dates with sentiment data")
    print(f"  📈 Total trading days: {len(finetuned_result)}")
    print(f"  🎯 Sample sentiment distribution:")

    # Count sentiment types
    sentiment_counts = {}
    for date in finetuned_result:
        sentiment_type = finetuned_result[date]["dominant_sentiment_type"]
        sentiment_counts[sentiment_type] = sentiment_counts.get(sentiment_type, 0) + 1

    for sentiment, count in sentiment_counts.items():
        percentage = (count / len(finetuned_result)) * 100
        print(f"    {sentiment.capitalize()}: {count} days ({percentage:.1f}%)")

    if save_file:
        print("💾 Saving combined data to file...")
        with open("./data/processed/combined_data.pkl", "wb") as f:
            pickle.dump(finetuned_result, f)
        print("✅ Combined data saved successfully")

    return finetuned_result
