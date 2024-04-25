from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PeselValidationSerializer
from .utils import Pesel


class PeselValidationView(APIView):
    def post(self, request):
        serializer = PeselValidationSerializer(data=request.data)
        if serializer.is_valid():
            pesel = serializer.validated_data.get('pesel')
            is_valid = Pesel.validate(pesel)
            if is_valid:
                gender = Pesel.get_gender(pesel)
                birth_date = Pesel.get_birth_date(pesel)

                return Response({'message': "Pesel jest prawidowy",
                                 'gender': gender,
                                 'birth_date': birth_date},
                                status.HTTP_200_OK)
            return Response({'message': 'Pesel jest nieprawidowy'},
                            status.HTTP_200_OK)
