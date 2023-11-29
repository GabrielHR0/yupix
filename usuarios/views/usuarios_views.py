from django.shortcuts import get_object_or_404, render

#from usuarios.models import 


def index(request):
    context = {
        'site_title':'Página principal',
    }

    return render(
        request,
        'usuarios/index.html',
        context,
        )

def usuarios(request, contact_id):
    ...