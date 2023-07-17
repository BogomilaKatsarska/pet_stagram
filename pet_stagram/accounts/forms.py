from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

UserModel = get_user_model()


class UserCreateForm(UserCreationForm):
    # placeholders = {
    #     'username': 'Username: '
    # }
    class Meta:
        model = UserModel
        fields = ("username", "email")
        #TODO:check what field_classes are
        field_classes = {'username': UsernameField}