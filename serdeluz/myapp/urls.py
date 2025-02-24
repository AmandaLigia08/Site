from django.urls import path 
from myapp import views


urlpatterns = [
    #paginas
    path('index/', views.site, name='index'), 
    path('sobre/', views.sobre, name='sobre'), 
    path('projeto/', views.projeto, name='projeto'),
    path('contato/', views.contato, name='contato'),
    path('chave/', views.chave, name='chave'),

    

]

