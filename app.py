import yfinance as yf

appl = yf.Ticker("AAPL")

def get_stock_news(ticker):
    # Get the stock ticker
    stock = yf.Ticker(ticker)

    # Fetch recent news
    news = stock.news

    # Display the news articles
    if news:
        print(f"Recent news for {ticker}:")
        for article in news:
            print(f"\nTitle: {article['title']}")
            print(f"Publisher: {article['publisher']}")
            print(f"Link: {article['link']}")
            print(f"Publish Time: {article['providerPublishTime']}")
    else:
        print(f"No recent news found for {ticker}.")

import json
def save_to_json(my_dict):
    with open(f"{my_dict['id']}.json", "w") as json_file:
        json.dump(my_dict, json_file)


for item in appl.news:
    save_to_json(item)



   