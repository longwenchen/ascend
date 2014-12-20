from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def login_view(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('accounts/login.html', c)


def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/accounts/loggedin/')
    else:
        return HttpResponseRedirect('/accounts/invalid/')


def invalid_view(request):
    pass


def logout_view(request):
    logout(request)
    return render_to_response('accounts/logout.html')


def loggedin_view(request):
    return render_to_response('accounts/loggedin.html', {'full_name': request.user.username})


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success/')

    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()

    return render_to_response('accounts/register.html', args)


def register_success(request):
    return render_to_response('accounts/register_success.html')
