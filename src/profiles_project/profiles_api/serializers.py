# All serializers of this app are here
from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serialize a name field for test"""

    name = serializers.CharField(max_length=10)
