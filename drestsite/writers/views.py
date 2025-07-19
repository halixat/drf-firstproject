from rest_framework import generics
from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Writers
from .serializers import WritersSerializer

class WritersAPIView(APIView):
    def get(self, request):
        w = Writers.objects.all()
        return Response({'posts': WritersSerializer(w, many=True).data})
    
    def post(self, request):
        serializer = WritersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response({"error": "Method PUT not allowed"})
        
        try:
            instance = Writers.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        
        serializer = WritersSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response({"error": "Method Delete not allowed"})
        
        try:
            instance = Writers.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        
        instance.delete()
        
        return Response({"post": "deleted post " + str(pk)})

# class WritersAPIView(generics.ListAPIView):
#     queryset = Writers.objects.all()
#     serializer_class = WritersSerializer