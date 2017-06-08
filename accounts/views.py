from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse
from .forms import SignUpForm
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return render(request, 'accounts/login.html', {'msj': 'Te has registrado con éxito, logueate!',})
        else:
            return render(request, 'accounts/reg_form.html', {'error': form.error_messages,})
    else:
        form = SignUpForm()
    return render(request, 'accounts/reg_form.html', {'form': form})
def login_user(request):
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/preguntas')
        return render(request, 'accounts/login.html', {'msj': 'Usuario o Contraseña Incorrectos',})
    return render(request, 'accounts/login.html')
def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(email__iexact=username).exists()
    }
    return JsonResponse(data)

class EmailBackend(object):
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if getattr(user, 'is_active', False) and  user.check_password(password):
                return user
        return None