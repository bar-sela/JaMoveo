from django import forms
from django.contrib.auth.forms import UserCreationForm

from JaMoveo.models import CustomUser


class RegualUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('instrument','is_admin')



