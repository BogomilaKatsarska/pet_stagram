from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from pet_stagram.core.decorator import owner_required
from pet_stagram.core.photo_utils import apply_likes_count
from pet_stagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from pet_stagram.pets.models import Pet
from pet_stagram.pets.utils import get_pet_by_name_and_username
from pet_stagram.photos.models import Photo


@login_required
def add_pet(request):
    if request.method == 'GET':
        form = PetCreateForm()
    else:
        form = PetCreateForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('details user', pk=request.user.pk)

    context = {
        'form': form,
    }
    return redirect(request, 'pets/pet-add-page.html', context)


def delete_pet(request, username, pet_slug):
    pet = get_pet_by_name_and_username(pet_slug, username)
    if request.method == 'GET':
        form = PetDeleteForm(instance=pet)
    else:
        form = PetDeleteForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details user', pk=1)

    context = {
        'form': form,
        'pet_slug': pet_slug,
        'username': username,
    }
    return render(request, 'pets/pet-delete-page.html', context)


def details_pet(request, username, pet_slug):
    pet = get_pet_by_name_and_username(pet_slug, username)
    photos = [apply_likes_count(photo) for photo in pet.photo_set.all()]
    photos = [apply_likes_count(photo) for photo in photos]
    context = {
        'pet': pet,
        'photos_count': pet.photo_set.count(),
        'pet_photos': photos,
        'is_owner': pet.user == request.user,
    }
    return render(request, 'pets/pet-details-page.html', context)


@owner_required
def edit_pet(request, username, pet_slug):
    #TODO: use 'username' when auth
    pet = Pet.objects.filter(slug=pet_slug).get()
    if request.method == 'GET':
        form = PetEditForm(instance=pet)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details pet', username=username, pet_slug=pet_slug)

    context = {
        'form': form,
        'pet_slug': pet_slug,
        'username': username,
    }
    return render(request, 'pets/pet-edit-page.html', context)
