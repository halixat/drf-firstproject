from rest_framework import generics, viewsets
from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Writers, Category
from .serializers import WritersSerializer



class WritersViewSet(viewsets.ModelViewSet):
    queryset = Writers.objects.all()[0:3]
    serializer_class = WritersSerializer

    @action(methods=['get'], detail = True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})



# class WritersAPIList(generics.ListCreateAPIView):
#     queryset = Writers.objects.all()
#     serializer_class = WritersSerializer


# class WritersAPIUpdate(generics.UpdateAPIView):
#     queryset = Writers.objects.all()
#     serializer_class = WritersSerializer


# class WritersAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Writers.objects.all()
#     serializer_class = WritersSerializer
