from django.urls import path
from ex_1 import views

urlpatterns = [
    path("index/", views.index, name="index")
]
