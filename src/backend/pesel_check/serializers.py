from rest_framework import serializers


class PeselValidationSerializer(serializers.Serializer):
    pesel = serializers.CharField(max_length=11)
