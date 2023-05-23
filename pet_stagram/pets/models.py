# pets/models.py
from django.db import models
from django.utils.text import slugify


class Pet(models.Model):
    MAX_NAME = 30
    name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,
    )
    personal_photo = models.URLField(
        null=False,
        blank=False,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id} - {self.name}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id}-{self.name}'
