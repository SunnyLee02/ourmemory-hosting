from django.db import models

# Bucketlist Model을 만드는 클래스.
class BucketList(models.Model):
    id = models.AutoField(primary_key=True)
    bucket = models.TextField(blank=False, default='')
    isFinished = models.BooleanField(default=False)

    class Meta:
        ordering = ('-isFinished',)