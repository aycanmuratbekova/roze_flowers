import requests
import xmltodict
from rest_framework import generics
from rest_framework.exceptions import NotAcceptable
from rest_framework.response import Response
from rest_framework.views import APIView

from main.settings import MERCHANT_ID
from .config.confirmations import is_real_signature, get_sig, get_salt, get_params
from .models import Transaction
from .serializers import TransactionSerializer


class TransactionView(generics.CreateAPIView):
    # queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        payment = serializer.save()
        params = get_params(payment)
        params['pg_sig'] = get_sig(params)
        response = requests.post('https://api.paybox.money/init_payment.php', params=params)
        payload = xmltodict.parse(response.content).get('response', {})
        if payload.get('pg_status') != 'ok':
            raise NotAcceptable
        return Response({"url": payload.get('pg_redirect_url')})


class TransactionSuccessView(APIView):

    def get(self, request):
        if is_real_signature(request):
            order_id = request.GET.get('pg_order_id')
            payment = Transaction.objects.get(id=order_id)
            payment.payment_success = True
            payment.save()

        return Response({"pg_transaction_status": 'OK'})


class FailureView(APIView):

    def get(self, request):
        if is_real_signature(request):
            payment_id = request.GET.get('pg_payment_id')
            order_id = request.GET.get('pg_order_id')

            params = dict(
                pg_merchant_id=MERCHANT_ID,
                pg_payment=payment_id,
                pg_order_id=order_id,
                pg_salt=get_salt(),
            )
            params['pg_sig'] = get_sig(params)
            response = requests.post('https://api.paybox.money/get_status2.php', params=params)
            payload = xmltodict.parse(response.content).get('response', {})
            return Response({
                "pg_transaction_status": payload.get('pg_status'),
                "pg_failure_code": payload.get('pg_error_code'),
                "pg_failure_description": payload.get('pg_error_description'),
            })

