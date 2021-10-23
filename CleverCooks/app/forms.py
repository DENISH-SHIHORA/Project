
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        first_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: First Name',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
        last_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: Last Name',
                               widget=(forms.TextInput(attrs={'class': 'form-control'})))
        model = User
        
        fields = UserCreationForm.Meta.fields + ('username','first_name','last_name','email','password1','password2')