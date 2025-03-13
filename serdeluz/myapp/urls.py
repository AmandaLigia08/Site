from django.urls import path 
from myapp import views
from django.contrib.auth import views as auth_views
from .views import registrar_usuario

urlpatterns = [
    #paginas
    path('', views.site, name='index'), 
    path('index/', views.site, name='index'), 
    path('sobre/', views.sobre, name='sobre'), 
    path('projeto/', views.projeto, name='projeto'),
    path('contato/', views.contato, name='contato'),
    path('chave/', views.chave, name='chave'),
    path('portal/', views.portal, name='portal'),

    path("registro/", registrar_usuario, name="registro"),
    path("login/", auth_views.LoginView.as_view(template_name="usuarios/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

]

<<<<<<< HEAD
<<<<<<< HEAD
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Adicionar Isto
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Adicionar Isto
=======
=======
>>>>>>> parent of 3504ff4 (carrosel)
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "usuarios",  # Adicionamos nosso app aqui
]
<<<<<<< HEAD
>>>>>>> parent of 3504ff4 (carrosel)
=======
>>>>>>> parent of 3504ff4 (carrosel)

