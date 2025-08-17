import pandas as pd


def make_dataframe(data):
    df = pd.DataFrame.from_dict(data, orient="index")
    df.index.name = "date"
    df["price_change"] = df["close"] - df["open"]
    df.to_csv("./data/processed/data.csv")
    return df
