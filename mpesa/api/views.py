
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from mpesa.api.serializers import LNMOnlineSerializer
from mpesa.models import LNMOnline

class LNMcallbackurlAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]

    def create(self,request):
        print(request.data,"This is request.data")
       """
        {'Body': 
            {'stkCallback': 
               {'MerchantRequestID': '42432-14242808-1',
                'CheckoutRequestID': 'ws_CO_170420210934368924',
                'ResultCode': 0, 
                'ResultDesc': 'The service request is processed successfully.', 
                'CallbackMetadata': 
                    {'Item': [{'Name': 'Amount', 'Value': 1.0}, 
                    {'Name': 'MpesaReceiptNumber', 'Value': 'PDH1WP9EWT'}, 
                    {'Name': 'Balance'}, {'Name': 'TransactionDate', 'Value': 20210417093515}, 
                    {'Name': 'PhoneNumber', 'Value': 254718282544}]}   
                }   
            }
        } 
        """"
        merchant_request_id = request.data["Body"]["stkCallback"]["MerchantRequestID"]
        print(merchant_request_id, "this should be MerchantRequestID")
        checkout_request_id = request.data["Body"]["stkCallback"]["CheckoutRequestID"]
        result_code = request.data["Body"]["stkCallback"]["ResultCode"]
        result_description = request.data["Body"]["stkCallback"]["ResultDesc"]
        
        amount = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][0]["Value"]
        print(amount, "this should be an amount")

        mpesa_receipt_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][1]["Value"]
        print(mpesa_receipt_number, "this should be an mpesa_receipt_number")

        balance = ""

        transaction_date = request.data["Body"]["stkCallback"]["CallbackMetadata"][ "Item"][3]["Value"]
        print(transaction_date, "this should be an transaction_date")

        phone_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][4]["Value"]
        print(phone_number, "this should be an phone_number")