# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import viewsets
from api.models import UserManager,User
from api.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework import authentication, permissions
import json
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.permissions import AllowAny
from jwtdrf.pagination import CustomPagination
import json

"""
This API for Register User
"""
# class RegisterView(generics.CreateAPIView):

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = UserManager.objects.all()

class RegisterViewNormal(generics.CreateAPIView):
    def get(self, validated_data):
        serializer_class = UserMangerCreateSerializer
        if serializer_class.is_valid():
            serializer_class.save()
        return Response(serializer_class.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class PaginationView(GenericAPIView):
    """
    This API for Pagination View for Order List for easy to get no of data length 
    """
    # serializer_class = OrderSerializer
    queryset = User.objects.all()  # query set data
    pagination_class = CustomPagination

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data  # pagination data
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
        payload = {
            'return_code': '200',
            'return_message': 'Success',
            'data': data
        }
        return Response(data)
