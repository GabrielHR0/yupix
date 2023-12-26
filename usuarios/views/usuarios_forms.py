from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render, redirect
from usuarios.forms import RegisterForm, RegisterFormServer
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth, messages
from django.db import IntegrityError
from usuarios.models import UserRegister, ServerRegister
from django.db.models import Q

def register2(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email', '')

            # Verifique se o e-mail já existe
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'Este e-mail já está em uso. Escolha outro.')
            else:
                try:
                    # Tente criar o usuário apenas se o e-mail for único
                    user = User.objects.create_user(
                        username=form.cleaned_data.get('email', ''),
                        email=form.cleaned_data.get('email', ''),
                        password=form.cleaned_data.get('password', ''),
                        first_name=form.cleaned_data.get('first_name', ''),  # Certifique-se de adicionar esta linha
                        last_name=form.cleaned_data.get('last_name', '')  # Certifique-se de adicionar esta linha
                    )
                    user_register = UserRegister(
                        user=user,
                        first_name=form.cleaned_data.get('first_name', ''),
                        last_name=form.cleaned_data.get('last_name', ''),
                        gender=form.cleaned_data.get('gender', ''),
                        birth_date=form.cleaned_data.get('birth_date', ''),
                        cpf=form.cleaned_data.get('cpf', ''),
                        address=form.cleaned_data.get('address', ''),
                        city=form.cleaned_data.get('city', ''),
                        state=form.cleaned_data.get('state', ''),
                        zip_code=form.cleaned_data.get('zip_code', ''),
                        email=form.cleaned_data.get('email', ''),
                        phone=form.cleaned_data.get('phone', ''),
                        password=form.cleaned_data.get('password', ''),
                        confirm_password=form.cleaned_data.get('confirm_password', ''),
                    )
                    user_register.save()
                    return redirect('usuarios:register2')  # ou redirecione para onde for apropriado
                except IntegrityError:
                    form.add_error(None, 'Erro ao criar o usuário. Tente novamente.')

    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'usuarios/register2.html', context)


def register1(request):
    if request.method == 'POST':
        form = RegisterFormServer(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email', '')

            # Verifique se o e-mail já existe
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'Este e-mail já está em uso. Escolha outro.')
            else:
                try:
                    # Tente criar o usuário apenas se o e-mail for único
                    user = User.objects.create_user(
                        username=form.cleaned_data.get('email', ''),
                        email=form.cleaned_data.get('email', ''),
                        password=form.cleaned_data.get('password', ''),
                        first_name=form.cleaned_data.get('first_name', ''),  # Certifique-se de adicionar esta linha
                        last_name=form.cleaned_data.get('last_name', '')  # Certifique-se de adicionar esta linha
                    )
                    user_register = ServerRegister(
                        user=user,
                        first_name=form.cleaned_data.get('first_name', ''),
                        last_name=form.cleaned_data.get('last_name', ''),
                        gender=form.cleaned_data.get('gender', ''),
                        birth_date=form.cleaned_data.get('birth_date', ''),
                        cpf=form.cleaned_data.get('cpf', ''),
                        address=form.cleaned_data.get('address', ''),
                        city=form.cleaned_data.get('city', ''),
                        state=form.cleaned_data.get('state', ''),
                        zip_code=form.cleaned_data.get('zip_code', ''),
                        email=form.cleaned_data.get('email', ''),
                        phone=form.cleaned_data.get('phone', ''),
                        password=form.cleaned_data.get('password', ''),
                        confirm_password=form.cleaned_data.get('confirm_password', ''),
                        document=form.cleaned_data.get('document', ''),
                        service=form.cleaned_data.get('service', ''),
                    )
                    user_register.save()
                    return redirect('usuarios:register1')  # ou redirecione para onde for apropriado
                except IntegrityError:
                    form.add_error(None, 'Erro ao criar o usuário. Tente novamente.')

    else:
        form = RegisterFormServer()

    context = {'form': form}
    return render(request, 'usuarios/register1.html', context)


def login(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.info(request, "Logado com sucesso.")
            return redirect('usuarios:index')


    return render(
        request,
        'usuarios/login.html',
        {
            'form':form
        }
    )


def logout(request):
    auth.logout(request)
    messages.info(request, "Desconectado com sucesso.")
    return redirect('usuarios:index')
