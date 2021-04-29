import requests
from requests.auth import HTTPBasicAuth
import keys


#Request for access token
def generate_access_token():
    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    #Converting the result into json in order to access it as a dictionary
    json_response =r.json()
    my_access_token = json_response['access_token']

    return my_access_token

