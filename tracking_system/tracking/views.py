from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import transaction
from .models import TrackingNumber
from .serializers import TrackingNumberSerializer

class TrackingNumberGenerateView(APIView):
    def post(self, request, *args, **kwargs):
        '''Generate a new tracking number'''
        try:
            with transaction.atomic():
                tracking_number = TrackingNumber.objects.create()
                serializer = TrackingNumberSerializer(tracking_number)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
