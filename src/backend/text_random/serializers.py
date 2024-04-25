from rest_framework import serializers
from .models import UploadedFile


class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = '__all__'

    def save(self, **kwargs):
        if self.validated_data['file'].name.endswith('.txt'):
            return super().save(**kwargs)
        else:
            raise serializers.ValidationError("Only .txt files are allowed")
