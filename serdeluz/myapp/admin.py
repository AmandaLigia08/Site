from django.contrib import admin
from .models import Carousel, Conselho, Projeto

# Register your models here.
@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = [ 'image', 'title', 'sub_title', 'action_name', 'link']

@admin.register(Conselho)
class ConselhoAdmin(admin.ModelAdmin):
    list_display = ['name','funcao', 'instagra', 'foto', 'is_ativo']

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'subtitulo', 'descricao', 'fotoprojeto', 'is_ativo' ]





