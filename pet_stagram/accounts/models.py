from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models

from pet_stagram.core.validators import validate_only_letters

'''
Naming the User model
1. Something generic: 
- AppUser
- ApplicationUser
- AuthUser
2. Prefix with application name - PetstagramUser
'''


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    DoNotShow = 'Do not show'


class AppUser(AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        )
    )
    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        )
    )
    email = models.EmailField(
        unique=True,
    )
    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
    )

