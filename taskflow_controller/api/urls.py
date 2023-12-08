from django.urls import path
from .views import TeamView #made up function

urlpatterns = [
    path('home', TeamView.as_view())
]