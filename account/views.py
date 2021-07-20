from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from account.forms import UserLoginForm, UserRegistrationForm

def login_view(request):
    form = UserLoginForm(request.POST or None)
    _next = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request,user)
        _next = _next or '/'
        return redirect(_next)
    return render(request, 'account/login.html', {'form': form})

def logoute_view(request):
    logout(request)
    name = 'Главная страница сайта'
    return render(request, 'account/home.html', {'name': name})

def home_view(request):
    name = 'Главная страница сайта'
    return render(request, 'account/home.html', {'name': name})


def user_registration_view(request):
    if request.method == 'POST':
        form1 = UserRegistrationForm(request.POST)
        if form1.is_valid():
            new_user = form1.save(commit=False)
            new_user.set_password(form1.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})

        return render(request, 'account/register.html', {'form1': form1})

    else:
        form1 = UserRegistrationForm()
        context= {'form1': form1}
        return render(request, 'account/register.html', context)


def dashboard(request):
    if request.user.is_authenticated:
        name = 'Личный кабинет'
        return render(request, 'account/dashboard.html', {'name': name})
    else:
        form1 = UserRegistrationForm()
        context = {'form1': form1}
        return render(request, 'account/register.html', context)

































#from .forms import LoginForm

#__all__ = ('user_login',)

#def user_login(request):
    #if request.method == 'POST':
        #form = LoginForm(request.POST)
        #if form.is_valid():
            #cd = form.cleaned_data
            #user = authenticate(request, # проверяет данные в форме с данными в БД. Если такой пользователь аутентифицирован
                                         # то authenticate() вернет объект пользователя User. Если пользователь не
                                         # аутентифицирован, то переходим в блок else: return HttpResponse('Неверный логин или пароль!')
                                #username = cd['username'],
                                #password = cd['password'])
        #if user is not None:
            #if user.is_active:
                #login(request, user) # сохраняет текущего пользователя в сессии
                #return HttpResponse('Автризация прошла успешно!')
           # else:
                #return HttpResponse('Аккаунт отсутствует!')
        #else:
            #return HttpResponse('Неверный логин или пароль!')
    #else:
       # form = LoginForm()
    #return render(request, 'account/login.html', {'form':form})



