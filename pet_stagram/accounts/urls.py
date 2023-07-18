from django.urls import path, include

from pet_stagram.accounts.views import SignInView, SignUpView, SignOutView, UserDetailsView, \
    EditUserView, UserDeleteView

urlpatterns = (
    path('register/', SignUpView.as_view(), name='register user'),
    path('login/', SignInView.as_view(), name='login user'),
    path('logout,', SignOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
        path('edit/', EditUserView.as_view(), name='edit user'),
    ])),
)