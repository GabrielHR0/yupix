from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from usuarios.models import UserRegister, ServerRegister
from usuarios.forms import RegisterFormServer, SearchForm


#from usuarios.models import 


def index(request):
    context = {
        'site_title':'Página principal',
        'header':'Yupix Brasil',
        'descripition':'Seja bem-vindo ao site da maior empresa de serviços terceirizados no mercado!',
    }

    return render(
        request,
        'usuarios/index.html',
        context,
        )

def contato(request):
    context = {
        'site_title':'Contato',
        'header':'Contato',
        'descripition':'Entre em contato conosco, oferecemos todo tipo de suporte aos nossos usuários, e se puder deixe seu comentário e avalie-nos.',
    }

    return render(
        request,
        'usuarios/contato.html',
        context,
    )

def login(request):

    return render(
        request,
        'usuarios/login.html',
    )

def create1(request):
    return render(
        request,
        'usuarios/register1.html',
    )

def create(request):
    return render(
        request,
        'usuarios/register2.html'
        )

@login_required(login_url='usuarios:login')
def profile(request):
    user_profile = UserRegister.objects.get(user=request.user)
    return render(request, 'usuarios/profile.html', {'user_profile': user_profile})

@login_required(login_url='usuarios:login')
def search(request):
    print("Entrou na view search")

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_service = form.cleaned_data.get('search_service', None)
            print("search_service:", search_service)  # Adicione esta linha para debug
            user_profiles = ServerRegister.objects.all()

            if search_service:
                user_profiles = user_profiles.filter(service=search_service)

            return render(request, 'usuarios/search.html', {'user_profiles': user_profiles, 'form': form})
    else:
        form = SearchForm()

    return render(request, 'usuarios/search.html', {'form': form})

def services(request):
    context = {
        'site_title':'Serviços',
        'header':'Serviços',
        'descripition':'Conheço abaixo os principais tipos de serviços que a Yupix oferece para seus usuários!',
    }

    return render(
        request,
        'usuarios/services.html',
        context,)

def aboutus(request):
     context = {
         'Site_title':'Sobre',
         'header':'Sobre nós',
         'descripition':'Conheça um pouco sobre nossa empresa, como funciona o aplicativo da Yupix e nossas parcerias mais importantes!'
     }

     return render(
         request,
         'usuarios/aboutus.html',
         context,
         )

def mobile(request):

    context = {
        'site_title':"Mobile",
        'header':"Serviços",
        'descripition':"Conheça abaixo os tipos de serviços que a Yupix oferece para seus usuários!",
    }

    return render(
        request, 
        'usuarios/mobile.html', 
        context)

def usuarios(request, contact_id):
    ...