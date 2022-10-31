from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Task1Serializer
from .models import Task1

@api_view(['GET'])
def task1List(request):
    task1s = Task1.objects.all()
    serializer = Task1Serializer(task1s, many = True)
    return Response(serializer.data)

"""
API Overview
"""
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/task1-list/',
    }
    return Response(api_urls)