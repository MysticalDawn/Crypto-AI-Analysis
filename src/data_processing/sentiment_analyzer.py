from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TextClassificationPipeline as TCP,
)
import os
import pickle


def classify_finbert(pipe: TCP, text: str, result) -> str:
    all_pred = pipe(text)
    for pred in all_pred:
        result["sentiment_score"].append(pred["score"])
        result["sentiment_type"].append(pred["label"])
    return result


def classify_cryptobert(data, save_file=False, load_file=False):
    if load_file and os.path.exists("./data/processed/sentiment_results.pkl"):
        with open("./data/processed/sentiment_results.pkl", "rb") as f:
            data = pickle.load(f)
            return data
    model_name = "ElKulako/cryptobert"
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)
    pipe = TCP(
        model=model,
        tokenizer=tokenizer,
        max_length=512,
        truncation=True,
        padding="max_length",
    )
    posts = data["full_text"]
    classify_finbert(pipe, posts, data)
    filtered_sentiments = []
    filtered_scores = []
    for label, score in zip(data["sentiment_type"], data["sentiment_score"]):
        if label != "Nan" and score != 0:
            filtered_sentiments.append(label)
            filtered_scores.append(score)

    data["sentiment_type"] = filtered_sentiments
    data["sentiment_score"] = filtered_scores
    if save_file:
        with open("./data/processed/sentiment_results.pkl", "wb") as f:
            pickle.dump(data, f)
            print("✅ Sentiment results saved successfully")
    return data
