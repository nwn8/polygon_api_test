
import requests
#from dotenv import load_dotenv
import pickle

load_dotenv()

api_key=os.getenv("NEW_API_KEY")

def get_aapl_price():
    url=f"https://api.twelvedata.com/price?symbol=AAPL&apikey={api_key}"
    response = requests.get(url)

    #print(f"Status Code: {response.status_code}")
    #print(f"Response Body: {response.json()}")

    price_aapl=response.json()
 
    """
    The following is to create a list of ongoing prices saved as a pickle file

    price_aa=round(float(price_aapl['price']),2)
    with open("aapl_log.pkl","rb") as file2:
         a=pickle.load(file2)

    
    a.append(price_aa)
    
    with open("aapl_log.pkl", "wb") as file:
        pickle.dump(a, file)

    """
    print(price_aapl)
    return price_aapl['price']

def get_nvda_price():
    url=f"https://api.twelvedata.com/price?symbol=nvda&apikey={api_key}"
    response = requests.get(url)

    #print(f"Status Code: {response.status_code}")
    #print(f"Response Body: {response.json()}")

    price_nvda=response.json()

    """
    The following is to create and read a list as a pickle file for ongoing prices

    price_nn=round(float(price_nvda['price']),2)
    with open("nvda_log.pkl","rb") as filer:
         x=pickle.load(filer)

    x.append(price_nn)
    

    with open("nvda_log.pkl", "wb") as file:
        pickle.dump(x, file)
    """


    return price_nvda['price']

get_aapl_price()
get_nvda_price()
