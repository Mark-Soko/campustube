import keys
import base64
#Generate our password for mpesa transaction. ["BusineessShortCode"+ "lipa na mpesa passkey" +" Timestamp"]
def generate_password(formarted_time):  
    data_to_encode= keys.business_shortCode + keys.lipa_na_mpesa_passkey + formarted_time
    encoded_binary = base64.b64encode(data_to_encode.encode())  # This line returns a binary encoded value of "data_to_encode" 

    #Lets convert the binary encoded value above to string  by decoding it. This will now act as our password
    decode_string = encoded_binary.decode("utf-8")
    return decode_string
