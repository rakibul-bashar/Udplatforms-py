from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import Address, User
from common.enums import UserTypes


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = (
            'id',
        )

class AddressMinifiedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = (
            'id',
            'alias',
            'street',
            'city',
            'state',
            'zip_code'
        )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = (
            'id',
        )


class UsersListSerializer(serializers.ModelSerializer):
    addresses = AddressMinifiedSerializer()
    class Meta:
        model = User
        fields = (
            'id', 
            'alias', 
            'first_name', 
            'last_name', 
            'user_type', 
            'addresses',
            'created_at', 
            'updated_at'
        )

        read_only_fields = (
            'id',
        )