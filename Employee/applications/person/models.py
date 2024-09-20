from django.db import models
from django_quill.fields import QuillField

#
from applications.department.models import Departamento

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'
    
    def __str__(self):
        return str(self.id) + '-' + self.habilidad 

# Create your models here.
class Empleado(models.Model):
    """ Modelo para tabla empleado """

    job_choices = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO')
    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    job = models.CharField('trabajos', max_length=1, choices=job_choices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = QuillField()

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
        ordering= ['-first_name', 'last_name']
        unique_together = ('first_name', 'departamento')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name #+ '-' + self.job + '-' + str(self.departamento)