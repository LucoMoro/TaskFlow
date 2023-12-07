from django.urls import path
from .views import main #made up function

urlpatterns = [
    path('', main)
]