from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    #allows us to input a max length 10 character field
    name = serializers.CharField(max_length=10)