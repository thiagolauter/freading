from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from libgen_api import LibgenSearch


# Create your views here.
@api_view(['GET'])
def index(request):
    return Response(request.data)


@api_view(['GET'])
def search(request):
    s = LibgenSearch()
    results = s.search_title(request.data['title'])
    return Response(results)