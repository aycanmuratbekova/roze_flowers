from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ClientSerializer, ClientINNSerializer
from .models import Passport, Client


class ClientAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(request_body=ClientINNSerializer)
    def post(self, request, format=None):
        inn = request.data.get('inn')
        otp = request.data.get('otp')
        try:
            passport = Passport.objects.get(inn=inn)
        except Passport.objects.get(inn=inn).DoesNotExist:
            raise Http404
        client = Client.objects.get(passport=passport)

        serializer = ClientSerializer(client, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
