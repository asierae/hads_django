from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label="Nombre",required=False,help_text='Optional.',widget=forms.TextInput(attrs={'placeholder':'Tu Nombre',}))
    last_name = forms.CharField(max_length=30, label="Apellido", required=False, help_text='Optional.',widget=forms.TextInput(attrs={'placeholder':'Tu Apellido',}))
    email = forms.EmailField(max_length=254, label="Email", help_text='Required. Inform a valid email address.',widget=forms.TextInput(attrs={'placeholder':'tuemail@email.com','onBlur':'prueba(this.value)',}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
