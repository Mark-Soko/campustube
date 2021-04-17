from django.contrib import admin
from django.urls import path,include

from mpesa.api.views import LNMcallbackurlAPIView

urlpatterns = [
    path('lnm/', LNMcallbackurlAPIView.as_view(),name="lnm-callbackurl"),
    
]
