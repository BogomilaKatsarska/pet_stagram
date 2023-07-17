from django.urls import path, include

from pet_stagram.accounts.views import details_user, delete_user, edit_user, SignInView, SignUpView, SignOutView

urlpatterns = (
    path('register/', SignUpView.as_view(), name='register user'),
    path('login/', SignInView.as_view(), name='login user'),
    path('logout,', SignOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', details_user, name='details user'),
        path('delete/', delete_user, name='delete user'),
        path('edit/', edit_user, name='edit user'),
    ])),
)