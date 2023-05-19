from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('pet_stagram.accounts.urls')),
    path('', include('pet_stagram.common.urls')),
    path('photos/', include('pet_stagram.photos.urls')),
    path('pets/', include('pet_stagram.pets.urls')),
]
