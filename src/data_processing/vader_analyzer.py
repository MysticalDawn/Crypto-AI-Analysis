from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def analyze_vader(data):
    analyzer = SentimentIntensityAnalyzer()
    data["sentiment_score"] = [
        analyzer.polarity_scores(text)["compound"] for text in data["full_text"]
    ]
    return data
