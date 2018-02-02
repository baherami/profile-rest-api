from django.shortcuts import render

# adding view for user profile
from rest_framework.views import APIView
from rest_framework.response import Response

#import for serializers
from . import serializers
#import HTTP status
from rest_framework import status

# adding viewset
from rest_framework import viewsets

# Create your views here.

class HelloApiView(APIView):
    """Test API View method in django"""

    #adding serializer to APIView
    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """ list of what this APIView does"""
        apiview_example = [
            'Use HTTP methods as function',
            'get, post, patch, put, delete',
        ]
        # return a response object via a dictionary
        return Response(
        {'message':'Testing APIView', 'apiview_example':apiview_example})

    def post(self, request):
        """ Create a hello response with name"""
        #passing the data to serializer
        serializer = serializers.HelloSerializer(data=request.data)
        # validation check in for data
        if serializer.is_valid():
            name = serializer.data.get('name')
            #create a string message for response
            message = 'hello {0}'.format(name)
            # make a response object via a dictionary
            return Response({'message':message})
        # if data is not validate, return an error message
        else:
            return Response(
                serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Update objects, logics are not implemented yet"""

        return Response({'method':'put'})

    def patch(self, request, pk=None):
        """update partially some fields, logics are not implemented yet"""

        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        """delete an object, logics are not implemented yet"""

        return Response({'method':'delete'})

class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSets"""

    def list(self, request):
        """ return a hello message"""
        viewset_example = [
            'Use actions',
            'list, create, retrieve, update, partial_update',
        ]
        # return a response object via a dictionary
        return Response({'message':'Testing ViewSet', 'viewset_example':viewset_example})
