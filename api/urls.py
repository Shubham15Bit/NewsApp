from django.urls import path
from . import views

urlpatterns = [
    path("setURL", views.set_url),
]