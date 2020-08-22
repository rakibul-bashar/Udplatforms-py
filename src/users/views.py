from django.shortcuts import render
from django.db import IntegrityError, transaction

from rest_framework import generics, viewsets

from .models import Address, User
from .serializers import AddressSerializer, UserSerializer, UsersListSerializer

from common.enums import UserTypes
from rest_framework import serializers, status
from rest_framework.response import Response



class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by('id')
    serializer_class = AddressSerializer
    lookup_field = 'alias'


class UserCreateApiView(generics.CreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        data = request.data
        user_type = request.data.get('user_type')
        address = request.data.get('addresses')

        try:
            with transaction.atomic():
                if user_type == UserTypes.CHILD and address:
                    raise serializers.ValidationError(
                    'CHILD_USER_ADDRESS_MUST_BE_EMPTY'
                )

                serializer =  self.get_serializer(
                    data=data,
                    context= {'request': request}
                )

                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                    
        except IntegrityError as exception:
            content = {'error': '{}'.format(exception)}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

                



class UserListApiView(generics.ListAPIView):

    queryset =  User.objects.all().order_by('id')
    serializer_class = UsersListSerializer


class UserRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'alias'
    queryset =  User.objects.all().order_by('id')
    serializer_class = UserSerializer

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        data = request.data
        user_type = request.data.get('user_type')
        address = request.data.get('addresses')

        try:
            with transaction.atomic():

                if user_type == UserTypes.CHILD and address:
                    raise serializers.ValidationError(
                    'CHILD_USER_ADDRESS_MUST_BE_EMPTY'
                )

                serializer = self.get_serializer(
                    self.get_object(),
                    data = data
                )
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                    
        except IntegrityError as exception:
            content = {'error': '{}'.format(exception)}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)