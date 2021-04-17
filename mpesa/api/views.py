
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