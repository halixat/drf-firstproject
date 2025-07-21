from rest_framework import generics, viewsets
from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Writers, Category
from .permissions import IsAdminUserOrReadOnly, IsOwnerOrReadOnly
from .serializers import WritersSerializer



class WritersAPIList(generics.ListCreateAPIView):
    queryset = Writers.objects.all()
    serializer_class = WritersSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class WritersAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Writers.objects.all()
    serializer_class = WritersSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class WritersAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Writers.objects.all()
    serializer_class = WritersSerializer
    permission_classes = (IsAdminUserOrReadOnly, )
