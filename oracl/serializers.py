from rest_framework import serializers
from .models import Passport, Client, Address


class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    passport = PassportSerializer(many=False)
    address = AddressSerializer(many=False)

    class Meta:
        model = Client
        fields = ['name', 'surname', 'passport', 'address']


class ClientINNSerializer(serializers.ModelSerializer):
    inn = serializers.CharField()
    otp = serializers.CharField()

    class Meta:
        model = Client
        fields = ['inn', 'otp']
