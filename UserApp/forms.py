from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        models = get_user_model()
        fields = ('email','username',)
        

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = get_user_model()
        fields = ('email','username')
        

