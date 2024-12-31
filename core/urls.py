
from django.urls import path

from core import views

urlpatterns = [
    path('index',views.index),
    path('post/<int:pk>',views.detail,name='detail'),
]
