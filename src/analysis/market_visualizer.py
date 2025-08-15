import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def visualize_avg_sentiment_with_volume(data):
    plt.figure(figsize=(20, 10))
    figure_showcase = sns.scatterplot(
        x=list(data.keys()),
        y=[v["volume"] for v in data.values()],
        hue=[v["avg_sentiment_type"] for v in data.values()],
    )
    figure_showcase.set_xlabel("Date")
    figure_showcase.set_ylabel("Volume")
    figure_showcase.set_title("Volume vs Date")
    plt.xticks(ticks=plt.xticks()[0][::10])
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
