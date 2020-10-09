import requests
import json
import os
#receiving the marketstack api from the virtual machine
MARKETSTACK_API = os.environ.get('MARKETSTACK_API')
#MARKETSTACK_API='c7e3d8a9bcXXXXXXXX81d7cc7341759b'
BASE_URL='http://api.marketstack.com/v1/'
#method to get the stock market data from market stack
def get_stock_price(stock_symbol):
    params ={
        "access_key":MARKETSTACK_API
    }
    #documentaion found on marketstack.com
    end_point=''.join([BASE_URL,"tickers/",stock_symbol,"/intraday/latest"])
    api_result=requests.get(end_point,params)
    json_result=json.loads(api_result.text)
    #returning the json file received as a string
    return json.dumps(json_result)

#result=get_stock_price("uuuubhbhvhv")
#print(result)
