from pytrends.request import TrendReq


def get_trends(keyword="Bitcoin"):
    pytrends = TrendReq(hl="en-US", tz=360)
    pytrends.build_payload(kw_list=[keyword], timeframe="today 1-y")
    data = pytrends.interest_over_time()
    data = data.drop(columns=["isPartial"])
    return data


data = get_trends()
print(data)
