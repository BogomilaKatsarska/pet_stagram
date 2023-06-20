from django.shortcuts import render, redirect, resolve_url
import pyperclip
from django.urls import reverse

from pet_stagram.common.forms import PhotoCommentForm, SearchPhotosForm
from pet_stagram.common.models import PhotoLike
from pet_stagram.core.photo_utils import apply_likes_count, apply_user_liked_photo
from pet_stagram.photos.models import Photo


def index(request):
    search_form = SearchPhotosForm(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['pet_name']
    #     print('Data:')
    #     print(search_form.cleaned_data)
    # else:
    #     print('Errors:')
    #    print(search_form.errors)

    photos = Photo.objects.all() 
    if search_pattern:
        photos = photos.filter(tagged_pets__name__icontains=search_pattern)
    photos = [apply_likes_count(photo) for photo in photos]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos,
        'comment_form': PhotoCommentForm(),
        'search_form': search_form,
    }
    return render(request, 'common/home-page.html', context)


def get_user_liked_photos(photo_id):
    #TODO: fix when auth available
    return PhotoLike.objects.filter(photo_id=photo_id)


def like_photo(request, photo_id):
    user_liked_photos = get_user_liked_photos(photo_id)
    if user_liked_photos:
        user_liked_photos.delete()
    else:
        photo_like = PhotoLike(
            photo_id=photo_id,
        )
        photo_like.save()
    # Option 2:
    # PhotoLike.objects.create(
    #     photo_id=photo_id,
    # )
    return redirect(request.META['HTTP_REFER'] + f'#photo-{photo_id}')

# pip install pyperclip


def share_photo(request, photo_id):
    photo_details_url = reverse('details photo', kwargs={
        'pk': photo_id})
    pyperclip.copy(photo_details_url)
    return redirect(request.META['HTTP_REFER'] + f'#photo-{photo_id}')


def comment_photo(request, photo_id):
    photo = Photo.objects.filter(pk=photo_id).get()
    form = PhotoCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False) #Does not persist to DB
        comment.photo = photo
        comment.save()

    return redirect('index')
