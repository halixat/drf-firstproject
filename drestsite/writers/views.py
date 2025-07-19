from rest_framework import generics, viewsets
from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Writers
from .serializers import WritersSerializer



class WritersViewSet(viewsets.ModelViewSet):
    queryset = Writers.objects.all()
    serializer_class = WritersSerializer



# class WritersAPIList(generics.ListCreateAPIView):
#     queryset = Writers.objects.all()
#     serializer_class = WritersSerializer


# class WritersAPIUpdate(generics.UpdateAPIView):
#     queryset = Writers.objects.all()
#     serializer_class = WritersSerializer


# class WritersAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Writers.objects.all()
#     serializer_class = WritersSerializer
