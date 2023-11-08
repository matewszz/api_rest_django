from django.db import models


class Base(models.Model):
    publicacao = models.DateTimeField(auto_created=True)
    atualizacao = models.DateTimeField(auto_created=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Curso(Base):
    titulo = models.models.CharField(max_length=250)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

        def __str__(self):
            return self.titulo

class Avalia