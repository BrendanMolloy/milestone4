from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """
    This model will contain all of a user's key information, apart from what is required for
    authentication (username, password and email). The fields are:
    - description (a text field the user can fill in giving personal or other information, tp
    describe to other users what they are looking for)
    - address
    We also of course use a OneToOneField to link it to a specific user!
    """
    user = models.OneToOneField(User)
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)

    def __unicode__(self):
        return self.user.username