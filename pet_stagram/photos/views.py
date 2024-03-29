from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from pet_stagram.photos.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
from pet_stagram.photos.models import Photo


@login_required
def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            form.save_m2m()

            return redirect('details photo', pk=photo.pk)
    context = {
        'form': form,
    }
    return render(request, 'photos/photo-add-page.html', context)


def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    user_liked_photoes = Photo.objects.filter(pk=pk, user_id=request.user.pk)

    context = {
        'photo': photo,
        'has_user_liked_photo': user_liked_photoes,
        'is_owner': request.user == photo.user,
        'likes_count': photo.photolike_set.count(),
    }
    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PhotoEditForm(instance=photo)
    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save()
            return redirect('index')
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PhotoDeleteForm(instance=photo)
    else:
        form = PhotoDeleteForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save()
            return redirect('index')
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'photos/photo-delete-page.html', context)


