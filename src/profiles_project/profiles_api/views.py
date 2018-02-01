from django.shortcuts import render

# adding view for user profile
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View method in django"""
    def get(self, request, format=None):
        """ list of what this APIView does"""
        apiview_example = [
            'Use HTTP methods as function',
            'get, post, patch, put, delete',
        ]

        return Response({'message':'Testing APIView', 'apiview_example':apiview_example})
