from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    """
    This model will contain all of a user's profile information,
    apart from what is required for
    authentication (username, password and email).
    The user does not *need* to fill in these details,
    but they can be used to auto-populate the form found on checkout.html
    The fields are:
    - full_name: The user's full name
    - phone_number: The user's phone number,
        to be used if there is a problem with ther order
    - country: The user's country of residence
    - postcode: The user's postcode
    - town_or_city: The name of the user's town or city
    - street_address1: The user's street address
    - street_address2: An additional line for the user's street address
    - county: The user's county of residence; not to be confused with country!
    We also use a OneToOneField to link it to a specific user!
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
