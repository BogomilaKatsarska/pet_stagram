from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from pet_stagram.accounts.forms import UserCreateForm

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

def delete_user(request, pk):
    return render(request, 'accounts/profile-delete-page.html')


class UserDetailsView(DetailView):
def details_user(request, pk):
    return render(request, 'accounts/profile-details-page.html')

def edit_user(request, pk):
    return render(request, 'accounts/profile-edit-page.html')
