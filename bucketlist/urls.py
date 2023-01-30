from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from bucketlist import views

urlpatterns = [
    path('bucketlist/', views.BucketListList.as_view()),
    path('bucketlist/<int:pk>/', views.BucketListDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)