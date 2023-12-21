from django.urls import path
from usuarios import views

app_name = 'usuarios'
urlpatterns = [
    path('<int:usuarios_id>/', views.usuarios, name='usuarios'),
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato') ,
    path('login/', views.login, name='login'),
    path('register1/', views.register1, name='register1'),
    path('register2/', views.register2, name="register2"),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('services/', views.services, name='services'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('mobile/', views.mobile, name='mobile'),
    
    path('create/', views.register2, name="create"),
]
