from django.contrib import admin
from .models import Carousel, Conselho, Projeto

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'title', 'sub_title', 'action_name', 'link']
    list_filter = ['title']
    search_fields = ['title', 'sub_title']
    ordering = ['id']

@admin.register(Conselho)
class ConselhoAdmin(admin.ModelAdmin):
    list_display = ['name', 'funcao', 'instagra', 'foto', 'is_ativo']
    list_filter = ['funcao', 'is_ativo']
    search_fields = ['name', 'funcao']
    ordering = ['name']

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'subtitulo', 'descricao', 'fotoprojeto', 'is_ativo']
    list_filter = ['is_ativo']
    search_fields = ['titulo', 'subtitulo', 'descricao']
    ordering = ['titulo']





