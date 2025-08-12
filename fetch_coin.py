import yfinance as yf


def fetch_coin(symbol: str):
    coin = yf.Ticker(symbol)
    return coin


def get_more_history(symbol: str, days: int = 365):
    """
    Get more historical data for a cryptocurrency.

    Args:
        symbol (str): The cryptocurrency symbol (e.g., 'BTC-USD', 'ETH-USD')
        days (int): Number of days of history to fetch (default: 365)

    Returns:
        DataFrame: Historical price data
    """
    coin = yf.Ticker(symbol)

    if days <= 5:
        history = coin.history(period="5d", interval="1m")
    elif days <= 30:
        history = coin.history(period="1mo", interval="1h")
    elif days <= 90:
        history = coin.history(period="3mo", interval="1d")
    elif days <= 365:
        history = coin.history(period="1y", interval="1d")
    elif days <= 365 * 2:
        history = coin.history(period="2y", interval="1d")
    elif days <= 365 * 3:
        history = coin.history(period="3y", interval="1d")
    elif days <= 365 * 4:
        history = coin.history(period="4y", interval="1d")
    elif days <= 365 * 5:
        history = coin.history(period="5y", interval="1d")
    else:
        history = coin.history(period="max", interval="1d")

    return history
