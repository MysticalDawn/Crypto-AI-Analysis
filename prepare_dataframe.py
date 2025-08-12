import pandas as pd


def make_dataframe(data):
    df = pd.DataFrame.from_dict(data, orient="index")
    df.index.name = "date"
    df["price_change"] = df["close"] - df["open"]
    df.drop(df[df["avg_sentiment_score"] == -1].index, inplace=True)
    col_drop = pd.get_dummies(df["avg_sentiment_type"], dtype=int)
    df = pd.concat([df, col_drop], axis=1)
    df.drop(columns=["avg_sentiment_type"], inplace=True)
    df.to_csv("./data/data.csv")
    return df
