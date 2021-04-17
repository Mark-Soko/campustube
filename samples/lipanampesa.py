import requests
from access_token import generate_access_token
from encode import generate_password
from utils import generate_timestamp
import keys



def lipa_na_mpesa():
        
    formarted_time = generate_timestamp()
    decode_string = generate_password(formarted_time)
    access_token = generate_access_token()        #Calling a generated access tokem from access_token file
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "BusinessShortCode": keys.business_shortCode,
        "Password": decode_string,
        "Timestamp": formarted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": keys.phone_number,
        "PartyB": keys.business_shortCode,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://fast-retreat-95570.herokuapp.com/api/payments/lnm",
        "AccountReference": "25718282544",
        "TransactionDesc": "Pay for this content "
    }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)
     
lipa_na_mpesa()


