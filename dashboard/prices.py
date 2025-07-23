import os
import requests
from dotenv import load_dotenv
import pickle

load_dotenv()

api_key=os.getenv("NEW_API_KEY")
print(api_key)
def get_aapl_price():
    url=f"https://api.twelvedata.com/price?symbol=AAPL&apikey={api_key}"
    response = requests.get(url)

    #print(f"Status Code: {response.status_code}")
    #print(f"Response Body: {response.json()}")

    price_aapl=response.json()
 
    print(price_aapl)
    return price_aapl['price']

def get_nvda_price():
    url=f"https://api.twelvedata.com/price?symbol=nvda&apikey={api_key}"
    response = requests.get(url)

    #print(f"Status Code: {response.status_code}")
    #print(f"Response Body: {response.json()}")

    price_nvda=response.json()




    return price_nvda['price']

get_aapl_price()
get_nvda_price()
