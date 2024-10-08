import requests
import json
import os

from dotenv import load_dotenv
from tickers import symbols_valid


load_dotenv()




def request_json_data(ticker):
    try:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}.TRT&outputsize=full&datatype=json&apikey={os.getenv('API_KEY')}'
        print(url)
        r = requests.get(url)

        data = r.json()
        f_name = f'data/{ticker}-data-daily.json'
        with open(f_name, 'w') as f_data: 
            json.dump(data, f_data)

        return 1

    except Exception as e:
        print(e)
        return 0
    
   

def download_data(symbols = symbols_valid):

    downloaded = []
    
    for symbol in symbols:
        
        try:
            if request_json_data(symbol) == 1:
                downloaded.append(symbol)
        except Exception as e:
            print(f'**{symbol} -- {e}')
            break
        
    print(downloaded)

download_data()