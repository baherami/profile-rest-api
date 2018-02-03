from django.shortcuts import render

# adding view for user profile
from rest_framework.views import APIView
from rest_framework.response import Response

#import for serializers
from . import serializers
from . import models

from . import permissions

#import HTTP status
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
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

    serializer_class= serializers.HelloSerializer

    def list(self, request):
        """ return a hello message"""
        viewset_example = [
            'Use actions',
            'list, create, retrieve, update, partial_update'
        ]
        # return a response object via a dictionary
        return Response({'message' : 'Testing ViewSet', 'viewset_example' : viewset_example})

    def create(self, request):
        """ Create a new hello message"""
        # same logic as explained in post method of HelloApiView
        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
            serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles retrieving(getting) an object."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles deleting an object."""

        return Response({'http_method': 'PATCH'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handles CRUD for profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # adding token Authentication tuple
    authentication_classes= (TokenAuthentication,)
    # adding permissions
    permission_classes=(permissions.UpdateOwnProfile,)
