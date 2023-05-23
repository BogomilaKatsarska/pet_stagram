# photos/models/py
from django.core.validators import MinLengthValidator
from django.db import models

from pet_stagram.pets.models import Pet
from pet_stagram.photos.validators import validate_image_less_than_5MB


class Photo(models.Model):
    MAX_LEN_LOCATION = 30
    MIN_LEN_DESCRIPTION = 10
    MAX_LEN_DESCRIPTION = 300
    photo = models.ImageField(
        # upload_to='mediafiles/pet_photos/',
        validators=(validate_image_less_than_5MB,),
        null=False,
        blank=True,
    )
    description = models.CharField(
        max_length=MAX_LEN_DESCRIPTION,
        validators=(
            MinLengthValidator(MIN_LEN_DESCRIPTION),
        ),
        null=True,
        blank=True,
    )
    location = models.CharField(
        max_length=MAX_LEN_LOCATION,
        null=True,
        blank=True,
    )
    publication_date = models.DateField(
        auto_now=True,
        # null=False and blank=True because publication date is auto generated
        null=False,
        blank=True,
    )
    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )