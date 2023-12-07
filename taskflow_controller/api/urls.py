from django.urls import path
from .views import TeamView #made up function

urlpatterns = [
    path('', TeamView.as_view())
]