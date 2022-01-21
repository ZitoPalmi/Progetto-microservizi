from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
# Create your views here.
from django.http import HttpResponse




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class OrderList(APIView):
    def get(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

class OrderGet(APIView):
    def get(self, request, order_id):
        queryset = Order.objects.filter(id=order_id)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

class OrderCreate(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderUpdate(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDelete(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
