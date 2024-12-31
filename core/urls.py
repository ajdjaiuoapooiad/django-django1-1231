
from django.urls import path

from core import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('post/<int:pk>',views.detail,name='detail'),
    path('create',views.create,name='create'),
    path('update/<int:pk>',views.update,name='update'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('like/<int:pk>',views.like,name='like'),


]
