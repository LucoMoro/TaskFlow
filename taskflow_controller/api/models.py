from django.db import models
import string
import random

#randomly generates a name for the Team
def generate_unique_name():
    length = 6

    while True:
        name = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Team.objects.filter(name=name).count() == 0:
            break

    return name

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=25, default="", unique=True)
    project_manager = models.CharField(max_length=50, unique=True)
    team_member = models.CharField(max_length=50, unique=False)
    num_of_members = models.IntegerField(null=False, default=5)
    created_at = models.DateTimeField(auto_now_add=True)