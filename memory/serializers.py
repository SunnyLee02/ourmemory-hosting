from rest_framework import serializers
from memory.models import Memory
from drf_extra_fields.fields import Base64ImageField

# Memory Serializer을 만드는 클래스.
class MemorySerializer(serializers.HyperlinkedModelSerializer):
    image = Base64ImageField(use_url=True)
    
    class Meta:
        model = Memory
        fields = ['id', 'placeName', 'placeRoad', 'placeAddress', 'placeX', 'placeY', 'placeUrl', 'feedDate', 'description', 'image']
    
