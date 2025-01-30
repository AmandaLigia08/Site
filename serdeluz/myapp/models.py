from django.db import models

# Create your models here.
class Conselho(models.Model):
    name = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    instagra = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='conselho', verbose_name='Logo',
        null=True, blank=True)
    is_ativo = models.BooleanField(default=False)
    
    def __str__(self):
        return "{}".format(self.name,)
    
    class Meta:
        verbose_name = 'Conselho'
        verbose_name_plural = 'Conselheiros'
        ordering = ['id']
        
class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    descricao = models.TextField()
    fotoprojeto = models.ImageField(upload_to='projeto', verbose_name='Logo',
        null=True, blank=True)
    is_ativo = models.BooleanField(default=False)
    
    def __str__(self):
        return "{}".format(self.titulo,)
    
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['id']