from django.db import models

# Create your models here.
class Conselho(models.Model):
    name = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    instagra = models.CharField(max_length=100)
    foto = models.FileField(upload_to='conselho', verbose_name='Foto',
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
    fotoprojeto = models.FileField(upload_to='projeto', verbose_name='fotoprojeto',
        null=True, blank=True)
    is_ativo = models.BooleanField(default=False)
    
    def __str__(self):
        return "{}".format(self.titulo,)
    
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['id']

class Carrocel(models.Model):
    discricao = models.CharField(max_length=100)
    fotocarrocel = models.FileField(upload_to='carrocel', verbose_name='fotocarrocel',
        null=True, blank=True)
    
    def __str__(self):
        return "{} - {}".format(self.discricao,self.fotocarrocel)