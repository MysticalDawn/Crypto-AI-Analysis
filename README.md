# Crypto-AI-Analysis

A comprehensive cryptocurrency analysis platform that combines sentiment analysis, market data scraping, and machine learning models to provide insights into cryptocurrency markets.

> **⚠️ Work in Progress** - This project is still under active development with lots and lots of work remaining. Many features are experimental and the codebase is continuously evolving.

## 🚀 Features

- **Multi-Source Data Collection**: Scrapes data from Reddit, news APIs, and Google Trends
- **Sentiment Analysis**: Uses fine-tuned CryptoBERT models for cryptocurrency-specific sentiment classification
- **Market Data Integration**: Fetches historical price data using Yahoo Finance API
- **Data Fusion**: Combines sentiment and market data for comprehensive analysis
- **Machine Learning Models**: Includes time series forecasting and classification models
- **Visualization Tools**: Interactive charts and market trend analysis

## 📁 Project Structure

```
Crypto-AI-Analysis/
├── data/                          # Data storage directory
│   ├── combined_data.pkl         # Merged sentiment and market data
│   ├── data.csv                  # Processed dataset
│   ├── news_results.pkl          # Scraped news data
│   └── reddit_results.pkl        # Scraped Reddit data
├── data_scrapers/                # Data collection modules
│   ├── news_scraper.py          # News API integration (NewsAPI, GNews, CryptoPanic)
│   └── reddit_scraper.py        # Reddit data collection from crypto subreddits
├── models/                       # Trained ML models
├── ai_models.ipynb              # Jupyter notebook with ML model training
├── combine_data.py              # Data fusion and preprocessing
├── crypto_sentiment_analysis.py # Sentiment analysis using CryptoBERT
├── fetch_coin.py                # Cryptocurrency price data fetching
├── merge_data.py                # Data merging utilities
├── prepare_dataframe.py         # DataFrame preparation utilities
├── trend_search.py              # Google Trends integration
└── visualize_market.py          # Market data visualization
```

## 🛠️ Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd Crypto-AI-Analysis
```

2. Install required dependencies:

```bash
pip install transformers torch pandas numpy scikit-learn seaborn matplotlib yfinance praw newsapi-python pytrends tqdm python-dotenv
```

## 📊 Data Sources

### News APIs

- **NewsAPI**: BBC News, The Verge, WSJ, NYT, CNBC, Reuters, Bloomberg
- **GNews**: Global news coverage
- **CryptoPanic**: Cryptocurrency-specific news and sentiment

### Reddit Communities

- r/CryptoCurrency
- r/Bitcoin
- r/CryptoMarkets
- r/Crypto
- r/CryptoTrading
- r/CryptoAnalysis
- r/CryptoNews

### Market Data

- **Yahoo Finance**: Historical price data (OHLCV)
- **Google Trends**: Search interest over time

## 🔍 Sentiment Analysis

The platform uses a fine-tuned CryptoBERT model (`ElKulako/cryptobert`) specifically trained for cryptocurrency sentiment classification. The model categorizes text into three sentiment classes and provides confidence scores.

## 🤖 Machine Learning Models

- **Time Series Forecasting**: Volume prediction using LSTM networks
- **Classification Models**: Decision trees for sentiment classification
- **Regression Models**: Random forest for market prediction
- **Cross-validation**: Robust model evaluation

## 📈 Usage Examples

### Fetching Cryptocurrency Data

```python
from fetch_coin import get_more_history

# Get 1 year of Bitcoin data
btc_data = get_more_history('BTC-USD', days=365)
```

### Running Sentiment Analysis

```python
from crypto_sentiment_analysis import classify

# Analyze sentiment of crypto-related text
sentiment_results = classify(data)
```

### Scraping Reddit Data

```python
from data_scrapers.reddit_scraper import fetch_reddit

# Fetch 500 posts from crypto subreddits
reddit_data = fetch_reddit(limit=500)
```

### Combining Data Sources

```python
from combine_data import merge_data

# Merge sentiment and market data
combined_data = merge_data(crypto_data, coin_data)
```

## 📊 Visualization

The platform includes visualization tools for:

- Volume vs. sentiment analysis
- Market trend visualization
- Time series plots
- Sentiment distribution charts

## 🔧 Configuration

### API Keys Required

- **NewsAPI**: Get your key from [newsapi.org](https://newsapi.org/)
- **Reddit**: Create a Reddit app at [reddit.com/prefs/apps](https://reddit.com/prefs/apps)
- **GNews**: Get your key from [gnews.io](https://gnews.io/)
- **CryptoPanic**: Get your token from [cryptopanic.com](https://cryptopanic.com/)

### Environment Setup

1. Copy the example environment file:

```bash
cp .env.example .env
```

2. Update the `.env` file with your actual API keys and credentials:

```bash
# News API Configuration
NEWSAPI_KEY=your_actual_newsapi_key
GNEWS_API_KEY=your_actual_gnews_api_key
CRYPTOPANIC_AUTH_TOKEN=your_actual_cryptopanic_token

# Reddit API Configuration
REDDIT_CLIENT_ID=your_actual_reddit_client_id
REDDIT_CLIENT_SECRET=your_actual_reddit_client_secret
REDDIT_USERNAME=your_actual_reddit_username
REDDIT_PASSWORD=your_actual_reddit_password
```

**⚠️ Important**: Never commit your `.env` file to version control. It's already included in `.gitignore`.

## 📝 Data Output

The platform generates:

- **Combined Dataset**: Merged sentiment and market data in CSV format
- **Pickle Files**: Serialized data for efficient processing
- **Visualizations**: Interactive charts and plots
- **Model Predictions**: ML model outputs and forecasts

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This tool is for educational and research purposes. Cryptocurrency investments carry significant risk. Always do your own research and consult with financial advisors before making investment decisions.

## 🔗 Dependencies

- **Core ML**: PyTorch, scikit-learn, transformers
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Data Sources**: yfinance, praw, newsapi-python, pytrends
- **Utilities**: tqdm, pickle, python-dotenv

---
