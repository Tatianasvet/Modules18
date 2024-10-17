from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
# Create your views here.
users = ['Anna', 'Nina', 'Mary', 'Roma', 'Yuriy']


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            try:
                age = int(form.cleaned_data['age'])
                if password != repeat_password:
                    info['error'] = 'Пароли не совпадают'
                elif age < 18:
                    info['error'] = 'Вы должны быть старше 18'
                elif username in users:
                    info['error'] = 'Пользователь уже существует'
                else:
                    info['message'] = f'Приветствуем, {username}!'
                    users.append(username)
            except TypeError:
                info['error'] = 'Возраст должен быть натуральным числом'
        else:
            info['error'] = 'Данные некорректны'
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        try:
            age = int(request.POST.get('age'))
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                info['message'] = f'Приветствуем, {username}!'
                users.append(username)
        except TypeError:
            info['error'] = 'Возраст должен быть натуральным числом'
    else:
        info['error'] = 'Данные некорректны'
    return render(request, 'registration_page.html', info)



