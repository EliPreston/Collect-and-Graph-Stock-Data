import requests
import json
import os

from dotenv import load_dotenv
from tickers import symbols_valid


load_dotenv()




def request_json_data(ticker):
    try:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&outputsize=full&datatype=json&apikey={os.getenv('API_KEY')}'
        r = requests.get(url)
    except Exception as e:
        print(e)
        return 0
    
    data = r.json()

    f_name = f'data/{ticker}-data-daily.json'
    with open(f_name, 'w') as f_data: 
        json.dump(data, f_data)
    f_name.close()

    return 1


def download_data():

    downloaded = []
    
    for symbol in symbols_valid:
        try:
            if request_json_data(symbol) == 1:
                downloaded.append(symbol)
        except Exception as e:
            print(f'**{symbol} -- {e}')
            break

    print(downloaded)

download_data()