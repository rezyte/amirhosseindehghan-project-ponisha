from django import forms
from django.contrib.auth import get_user_model

from .models import Profile 

User = get_user_model()

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ("has_completed")