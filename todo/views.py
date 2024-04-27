
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
# import django response
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class TodoView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response("Hello, World!")
@api_view(['GET'])    
def index(request):
    print(234)
    return Response({"message": "Hello, World!"})