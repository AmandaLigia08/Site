from django.contrib import admin
from .models import Carousel, Conselho, Projeto

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'title', 'sub_title', 'action_name', 'link', 'is_active']
    list_filter = ['title', 'is_active']
    search_fields = ['title', 'sub_title']
    ordering = ['id']

    actions = ["ativar_carousel", "desativar_carousel"]

    @admin.action(description="Ativar itens selecionados")
    def ativar_carousel(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Desativar itens selecionados")
    def desativar_carousel(self, request, queryset):
        queryset.update(is_active=False)

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





