# Crypto AI Analysis

A comprehensive cryptocurrency analysis platform that combines data collection, sentiment analysis, and AI-powered insights.

## Project Structure

```
Crypto-AI-Analysis/
├── src/
│   ├── data_collection/          # Data collection modules
│   │   ├── scrapers/             # Web scrapers for various sources
│   │   │   ├── crypto_panic.py   # CryptoPanic news scraper
│   │   │   ├── google_news.py    # Google News scraper
│   │   │   ├── news_api.py       # NewsAPI scraper
│   │   │   ├── news_data_io.py   # NewsData.io scraper
│   │   │   ├── reddit.py         # Reddit sentiment scraper
│   │   │   └── coin_gecko.py     # CoinGecko data fetcher
│   │   └── fetchers/             # Data fetching utilities
│   │       ├── news_fetcher.py   # News aggregation fetcher
│   │       └── coin_fetcher.py   # Cryptocurrency data fetcher
│   ├── data_processing/          # Data processing and analysis
│   │   ├── data_merger.py        # Data merging utilities
│   │   ├── data_combiner.py      # Data combination utilities
│   │   ├── dataframe_preparer.py # DataFrame preparation
│   │   └── sentiment_analyzer.py # Sentiment analysis tools
│   ├── analysis/                 # Analysis and visualization
│   │   ├── trend_analyzer.py     # Trend analysis tools
│   │   └── market_visualizer.py  # Market visualization tools
│   └── notebooks/                # Jupyter notebooks
│       └── ai_models.ipynb       # AI model development
├── data/                         # Data storage
│   ├── raw/                      # Raw collected data
│   ├── processed/                # Processed and cleaned data
│   └── external/                 # External data sources
├── config/                       # Configuration files
│   └── .env                      # Environment variables
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

## Features

- **Multi-source Data Collection**: Collects data from CryptoPanic, Google News, NewsAPI, Reddit, and CoinGecko
- **Sentiment Analysis**: Analyzes sentiment from news articles and social media
- **Data Processing**: Comprehensive data cleaning, merging, and preparation
- **Market Analysis**: Trend analysis and market visualization tools
- **AI Integration**: Jupyter notebooks for AI model development

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and configure your API keys
4. Run the desired modules

## Usage

### Data Collection

```python
from src.data_collection.scrapers.crypto_panic import fetch_cryptoPanic
from src.data_collection.scrapers.reddit import fetch_reddit_sentiment

# Collect news data
news_data = fetch_cryptoPanic()

# Collect Reddit sentiment
reddit_data = fetch_reddit_sentiment()
```

### Data Processing

```python
from src.data_processing.sentiment_analyzer import analyze_sentiment
from src.data_processing.data_merger import merge_datasets

# Analyze sentiment
sentiment_results = analyze_sentiment(text_data)

# Merge datasets
combined_data = merge_datasets([dataset1, dataset2])
```

### Analysis

```python
from src.analysis.trend_analyzer import analyze_trends
from src.analysis.market_visualizer import visualize_market

# Analyze trends
trends = analyze_trends(data)

# Visualize market data
visualize_market(data)
```

## Configuration

Set up your API keys in the `config/.env` file:

```
CRYPTOPANIC_AUTH_TOKEN=your_token_here
NEWS_API_KEY=your_key_here
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
```

## Contributing

1. Follow the established project structure
2. Add new scrapers to `src/data_collection/scrapers/`
3. Add new analysis tools to `src/analysis/`
4. Update requirements.txt for new dependencies
5. Document new features in README.md
