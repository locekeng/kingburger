
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(
    label="Email",
    widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )
    
    password1 = forms.CharField(
        label="mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
    )
    password2 = forms.CharField(
        label="confirmer mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
    )

    class Meta(UserCreationForm.Meta):
        
        fields = ('username', 'email')
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'})
    )