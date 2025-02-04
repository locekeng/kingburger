from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import SignUpForm,LoginForm

def index (request):
    return render(request,'home/Site.html')

def login_view (request):
    return render(request,'home/Login.html')

# def login_signup(request):
#     if request.method == 'POST':
        
#         form_type = request.POST.get('form_type')

        
#         if form_type == 'login':
#             print(form_type),
#             login_form = AuthenticationForm(request, data=request.POST)
#             if login_form.is_valid():
#                 username = login_form.cleaned_data.get('username')
#                 password = login_form.cleaned_data.get('password')
#                 user = authenticate(username=username, password=password)
#                 if user is not None:
#                     login(request, user)
#                     return redirect('index')  

        
#         elif form_type == 'signup':
#             signup_form = UserCreationForm(request.POST)
#             if signup_form.is_valid():
#                 user = signup_form.save()
#                 login(request, user)  
#                 return redirect('index')  

#     else:
#         login_form = AuthenticationForm()
#         signup_form = UserCreationForm()

#     return render(request, 'login_signup.html', {
#         'login_form': login_form,
#         'signup_form': signup_form,
#     })

def login_signup(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'login':
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)  # Utiliser auth_login pour éviter le conflit
                    messages.success(request, 'Connexion réussie !')
                    return redirect('index')
                else:
                    messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
            else:
                messages.error(request, 'Formulaire invalide. Veuillez réessayer.')

        elif form_type == 'signup':
            signup_form = SignUpForm(request.POST)  # Utiliser ton formulaire personnalisé
            if signup_form.is_valid():
                user = signup_form.save()
                login(request, user)  # Utiliser auth_login pour éviter le conflit
                messages.success(request, 'Inscription réussie !')
                return redirect('index')
            else:
                messages.error(request, 'Formulaire invalide. Veuillez réessayer.')

    else:
        login_form = AuthenticationForm()
        signup_form = SignUpForm()  # Utiliser ton formulaire personnalisé

    return render(request, 'login_signup.html', {
        'login_form': login_form,
        'signup_form': signup_form,
    })