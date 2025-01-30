from django.urls import path 
from myapp import views


urlpatterns = [
    #paginas
    path('', views.site, name='index'), 
    path('sobre/', views.sobre, name='sobre'), 
    path('projeto/', views.projeto, name='projeto'),
    path('contato/', views.contato, name='contato'),

    

    #Cadastro
    #path('form-client/', views.form_client, name='client-create'),  

    #path('form-empreendimento/', views.form_empreendimento, name='empreendimento-create'),  
    
    #path('form-empreendimento-arq/<int:id>/', views.form_arquivo, name='empreendimento-arq'),
    
    #path('form-venda/<int:id>/', views.form_venda, name='venda-create'),
    

    #Listagens
    #path('list_quadra/<int:id>/', views.list_Quadra, name='list-quadras'), 

    #path('list_lote/<int:id>/', views.list_Lote, name='list-lote'), 

    #path('list_cliente/', views.list_Clientes, name='list-clientes'),
    
    #path('list_vendas/', views.list_Vendas, name='list-vendras'),
    
    
    #relatorios
    #path('reports/', views.reports, name='reports'),
]

