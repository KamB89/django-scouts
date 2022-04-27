from django.urls import path
from .import views


urlpatterns = [
    path("", views.index, name="scouts"),
    path("john", views.john, name="john"),
    path("jack", views.jack),
    path("bill", views.bill),
    path("description/<scout>", views.description, name="scout_desc")
]
