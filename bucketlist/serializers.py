from rest_framework import serializers
from bucketlist.models import BucketList

# Memory Serializer을 만드는 클래스.
class BucketSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = BucketList
        fields = ['id', 'bucket', 'isFinished']
    
