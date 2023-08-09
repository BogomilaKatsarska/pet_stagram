from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from pet_stagram.accounts.forms import UserCreateForm
from pet_stagram.photos.models import Photo

UserModel = get_user_model()
# def login_user(request):
#     return render(request, 'accounts/login-page.html')


class SignInView(LoginView):
    template_name = 'accounts/login-page.html'

# def register_user(request):
#     return render(request, 'accounts/register-page.html')


class SignUpView(CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')


class SignOutView(LogoutView):
    next_page = reverse_lazy('index')


# def delete_user(request, pk):
#     return render(request, 'accounts/profile-delete-page.html')


class UserDeleteView(DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')


class UserDetailsView(DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        context['pets_count'] = self.object.pet_set.count()
        photos = self.object.photo_set.prefetch_related('photolike_set').select_realted('user')
        Photo.objects.select_related()
        Photo.objects.prefetch_related()
        context['photos_count'] = photos.count()
        context['likes_count'] = sum(x.photolike_set.count() for x in photos)

        return context


# def details_user(request, pk):
#     return render(request, 'accounts/profile-details-page.html')


class EditUserView(UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'gender', 'email',)

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })

# def edit_user(request, pk):
#     return render(request, 'accounts/profile-edit-page.html')
