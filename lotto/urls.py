from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('form/', views.post),
    path('detail/<int:num>', views.detail2),
    path('detail', views.detail),
]
