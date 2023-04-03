from django.urls import path
from . import views

urlpatterns = [
    path("setURL", views.set_url),
    path("getURL", views.get_url),
    path("deleteURL",views.delete_url)
]