from django.shortcuts import render, redirect

from pet_stagram.core.photo_utils import apply_likes_count
from pet_stagram.pets.forms import PetCreateForm
from pet_stagram.pets.utils import get_pet_by_name_and_username
from pet_stagram.photos.models import Photo


def add_pet(request):
    if request.method == 'GET':
        form = PetCreateForm()
    else:
        form = PetCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details user', pk=1)
        #TODO: fix this when auth

    context = {
        'form': PetCreateForm(),
    }
    return render(request, 'pets/pet-add-page.html', context)


def delete_pet(request, username, pet_slug):
    return render(request, 'pets/pet-delete-page.html')


def details_pet(request, username, pet_slug):
    pet = get_pet_by_name_and_username(pet_slug, username)
    photos = [apply_likes_count(photo) for photo in pet.photo_set.all()]
    photos = [apply_likes_count(photo) for photo in photos]
    context = {
        'pet': pet,
        'photos_count': pet.photo_set.count(),
        'pet_photos': photos,
    }
    return render(request, 'pets/pet-details-page.html', context)


def edit_pet(request, username, pet_slug):
    return render(request, 'pets/pet-edit-page.html')
