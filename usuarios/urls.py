from django.urls import path
from usuarios import views

app_name = 'usuarios'
urlpatterns = [
    path('<int:usuarios_id>/', views.usuarios, name='usuarios'),
    path('', views.index, name='index'), 
]
