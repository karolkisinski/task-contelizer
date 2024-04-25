from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UploadedFileSerializer
from .utils import RandomizeText
from rest_framework.parsers import FileUploadParser


class UploadedFileView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request):
        file_serializer = UploadedFileSerializer(data=request.data)
        if file_serializer.is_valid():
            uploaded_file = file_serializer.save()
            processed_text = RandomizeText.process_file(uploaded_file.file)
            uploaded_file.processed_text = processed_text
            uploaded_file.save()
            return Response({'processed_text': processed_text},
                            status=status.HTTP_200_OK)
        return Response(file_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
