from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Writers



class WritersSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Writers
        fields = "__all__"




# class WritersModel():
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# def encode():
#     model = WritersModel("Jorge Orwell", "Content: Jorge Orwell")
#     model_sr = WritersSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

# def decode():
#     stream = io.BytesIO(b'{"title": "Jorge Orwell", "content": "Jorge Orwell"}')
#     data = JSONParser().parse(stream)
#     serializer = WritersSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
