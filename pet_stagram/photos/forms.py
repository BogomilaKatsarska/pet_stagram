from django import forms
from django.core.exceptions import ValidationError

from pet_stagram.core.form_mixins import DisabledFormMixin
from pet_stagram.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('publication_date',)


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'photo')


class PhotoDeleteForm(PhotoBaseForm, DisabledFormMixin):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def clean_tagged_pets(self):
        tagged_pets = self.cleaned_data['tagged_pets']
        if tagged_pets:
            raise ValidationError('Pets are tagged in this photo!')