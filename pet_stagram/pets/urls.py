from django.urls import path, include

from pet_stagram.pets.views import add_pet, delete_pet, details_pet, edit_pet

urlpatterns = (
    path('add/', add_pet, name='add pet'),
    path('<str:username>/pet/<slug:pet_name>/', include([
        path('', details_pet, name='details pet'),
        path('delete/', delete_pet, name='delete pet'),
        path('edit/', edit_pet, name='edit pet'),
    ])),
)