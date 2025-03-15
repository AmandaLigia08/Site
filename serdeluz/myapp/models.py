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

# Create your models here.
class Carousel(models.Model):
    image       = models.ImageField(upload_to="pics/%y/%m/%d/")
    title       = models.CharField(max_length=150)
    action_name = models.CharField(max_length=50)
    link        = models.TextField(null=True, blank=True)
    sub_title   = models.CharField(max_length=100)
    is_active   = models.BooleanField(default=True)  # Adicionando campo de ativação

    def __str__(self):
        return self.title