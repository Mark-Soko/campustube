from django.contrib import admin
from mpesa.models import LNMOnline

# Register your models here.
   

class myLNMOnlineAdmin(admin.ModelAdmin):
    list_display =("PhoneNumber","Amount","MpesaReceiptNumber", "TransactionDate")



admin.site.register(LNMOnline,myLNMOnlineAdmin) 