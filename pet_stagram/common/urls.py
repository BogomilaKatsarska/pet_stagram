from django.urls import path

from pet_stagram.common.views import index

urlpatterns = (
    path('', index, name='index'),
)