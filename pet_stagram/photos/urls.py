from django.urls import include, path

from pet_stagram.photos.views import add_photo, details_photo, edit_photo

urlpatterns = (
    path('add/', add_photo, name='add photo'),
    path('<int:pk>/', include([
        path('', details_photo, name='details photo'),
        path('edit/', edit_photo, name='edit photo'),
        ])),
)

