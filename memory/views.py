from memory.models import Memory
from memory.serializers import MemorySerializer
from rest_framework import generics


class MemoryList(generics.ListCreateAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer


class MemoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer
    
