from django.db import models

from common.models import CreatedAtUpdatedAtBaseModel
from common.enums import UserTypes

    

class Address(CreatedAtUpdatedAtBaseModel):
    street  = models.CharField(max_length=30)
    city  = models.CharField(max_length=30, blank=False, null=False)
    state  = models.CharField(max_length=30)
    zip_code  = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return self.city


class User(CreatedAtUpdatedAtBaseModel):
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name  = models.CharField(max_length=30)
    addresses = models.ForeignKey(Address, null=True, related_name="users_address", on_delete=models.DO_NOTHING)
    user_type = models.CharField(max_length=6, choices=UserTypes.choices)
    
    class Meta: 
        verbose_name_plural = "Users"

    def __str__(self):
        return self.first_name