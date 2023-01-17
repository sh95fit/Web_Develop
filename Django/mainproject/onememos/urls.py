from django.urls import path
from . import views

urlpatterns = [
    # onememos의 루트 경로
    path('', views.index, name="index"),
]