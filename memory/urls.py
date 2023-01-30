from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from memory import views

urlpatterns = [
    path('memory/', views.MemoryList.as_view()),
    path('memory/<int:pk>/', views.MemoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)