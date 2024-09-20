from django.shortcuts import render
from django.views.generic import(
    ListView
)
# Create your views here.
from .models import Empleado
from applications.department.models import Departamento

class ListAllEmpleados(ListView):
    template_name = 'person/list_all.html'
    model = Empleado

class ListByAreaEmpleado(ListView):
    ''' Lista empleados de un area '''
    template_name = 'person/list_by_area.html'
    queryset = Empleado.objects.filter(
        departamento__name ='Area de Soporte' 
    )
