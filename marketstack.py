import requests
import json
import os
#MARKETSTACK_API = os.environ.get('MARKETSTACK_API')
MARKETSTACK_API='c7e3d8a9bc8230dabe81d7cc7341759b'
BASE_URL='http://api.marketstack.com/v1/'

def get_stock_price(stock_symbol):
    params ={
        "access_key":MARKETSTACK_API
    }
    end_point=''.join([BASE_URL,"tickers/",stock_symbol,"/intraday/latest"])
    api_result=requests.get(end_point,params)
    json_result=json.loads(api_result.text)
    return json.dumps(json_result)

#result=get_stock_price("uuuubhbhvhv")
#print(result)