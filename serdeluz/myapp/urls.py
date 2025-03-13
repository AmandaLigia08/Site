from django.urls import path 
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
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

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Adicionar Isto
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Adicionar Isto

