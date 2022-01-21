from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from .models import Customers
from .serializers import CustomersSerializer
# Create your views here.
from django.http import HttpResponse




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class CustomerList(APIView):
    def get(self, request):
        queryset = Customers.objects.all()
        serializer = CustomersSerializer(queryset, many=True)
        return Response(serializer.data)

class CustomerGet(APIView):
    def get(self, request, customers_id):
        queryset = Customers.objects.filter(id=customers_id)
        serializer = CustomersSerializer(queryset, many=True)
        return Response(serializer.data)

class CustomerCreate(CreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer

class CustomerUpdate(UpdateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer

class CustomerDelete(DestroyAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
