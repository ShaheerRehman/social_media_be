from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    building_name = models.CharField(max_length=100, null=True, blank=True)
    apartment_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username + " " + self.building_name + " " + str(self.apartment_number)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
