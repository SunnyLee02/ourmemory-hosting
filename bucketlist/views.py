from bucketlist.models import BucketList
from bucketlist.serializers import BucketSerializer
from rest_framework import generics


class BucketListList(generics.ListCreateAPIView):
    queryset = BucketList.objects.all()
    serializer_class = BucketSerializer


class BucketListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BucketList.objects.all()
    serializer_class = BucketSerializer
    
