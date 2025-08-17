import yfinance as yf
from tqdm import tqdm


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
    print(f"📈 Fetching historical data for {symbol}...")
    print(f"📅 Requesting {days} days of price history...")

    coin = yf.Ticker(symbol)

    # Determine the appropriate period and interval based on days
    if days <= 5:
        period = "5d"
        interval = "1m"
        print("  ⏱️  Using 1-minute intervals for 5-day data")
    elif days <= 30:
        period = "1mo"
        interval = "1h"
        print("  ⏱️  Using 1-hour intervals for 1-month data")
    elif days <= 90:
        period = "3mo"
        interval = "1d"
        print("  ⏱️  Using daily intervals for 3-month data")
    elif days <= 365:
        period = "1y"
        interval = "1d"
        print("  ⏱️  Using daily intervals for 1-year data")
    elif days <= 365 * 2:
        period = "2y"
        interval = "1d"
        print("  ⏱️  Using daily intervals for 2-year data")
    elif days <= 365 * 3:
        period = "3y"
        interval = "1d"
        print("  ⏱️  Using daily intervals for 3-year data")
    elif days <= 365 * 4:
        period = "4y"
        interval = "1d"
        print("  ⏱️  Using daily intervals for 4-year data")
    elif days <= 365 * 5:
        period = "5y"
        interval = "1d"
        print("  ⏱️  Using daily intervals for 5-year data")
    else:
        period = "max"
        interval = "1d"
        print("  ⏱️  Using daily intervals for maximum available data")

    print(f"  🔄 Fetching {period} of data with {interval} intervals...")

    try:
        history = coin.history(period=period, interval=interval)
        print(f"✅ Successfully fetched {len(history)} data points for {symbol}")
        print(
            f"  📊 Date range: {history.index[0].strftime('%Y-%m-%d')} to {history.index[-1].strftime('%Y-%m-%d')}"
        )
        print(
            f"  💰 Price range: ${history['Low'].min():.2f} - ${history['High'].max():.2f}"
        )
        return history
    except Exception as e:
        print(f"❌ Error fetching data for {symbol}: {str(e)}")
        raise
