from django.contrib.auth import get_user_model
from django.db import models
import uuid


class UuidCreateUpdateAbstractModel(models.Model):
    """Abstract model that has uuid as primary key"""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserInfo(UuidCreateUpdateAbstractModel):
    """Additional user info model"""
    user = models.OneToOneField(get_user_model(), null=False, blank=False, on_delete=models.CASCADE)
    email = models.EmailField(null=False, blank=False, max_length=255)
    first_name = models.CharField(null=True, blank=True, max_length=100)
    last_name = models.CharField(null=True, blank=True, max_length=150)
    birth_date = models.DateField(null=True, blank=True)
