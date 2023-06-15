from django import forms

from pet_stagram.pets.models import Pet


class PetCreateForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ('slug',)
        # fields = '__all__' -> not our case, we want to skip 'slug' field
        # fields = ('name', 'personal_photo', 'date_of_birth') -> this IS option 1
        labels = {
            'name': 'Pet Name',
            'personal_photo': 'Link to Image',
            'date_of_birth': 'Date of Birth',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet name'
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy'
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image'
                }
            )
        }


class PetEditForm:
    pass

class PetDeleteForm:
    pass