from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm

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


class UserEditForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'
        field_classes = {'username': UsernameField}
