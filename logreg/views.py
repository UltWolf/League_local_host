
from django.shortcuts import render_to_response, redirect,render
from django.contrib import auth
from django.contrib.auth.base_user import AbstractBaseUser
from django.template.context_processors import csrf
from .forms import UserCreationForm
from django.contrib.auth.models import User


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '') or request.POST.get('email','')
        password = request.POST.get('password', '')
        user =auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/articles/')
        else:
            args['login_error'] = "Пользователь не существует, либо пароль и логин неккоректные"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/articles/")

def register(request):
    args= {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate( username = newuser_form.cleaned_data["username"],email = newuser_form.cleaned_data['email'], password = newuser_form.cleaned_data['password2'])
            auth.login(request,newuser)
            return redirect('/auth/profile/')
        else:
            args['form'] = newuser_form
    return  render_to_response('registration.html', args)


def profile(request):
    return render_to_response('profile.html', {'username':auth.get_user(request).username})

