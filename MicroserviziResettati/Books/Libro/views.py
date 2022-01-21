from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from .models import Books
from .serializers import BookSerializer
# Create your views here.
from django.http import HttpResponse




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class BookList(APIView):
    def get(self, request):
        queryset = Books.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

class BookGet(APIView):
    def get(self, request, book_id):
        queryset = Books.objects.filter(id=book_id)
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

class BookCreate(CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BookUpdate(UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BookDelete(DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer