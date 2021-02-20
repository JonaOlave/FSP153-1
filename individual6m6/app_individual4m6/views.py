from django.shortcuts import render, redirect
from .models import Asignatura, Departamento, Profesor
from .forms import AsignaturaForm

# Create your views here.



def asignatura(request):
    Departamento.objects.create(
                        nombre = 'Departamento de Ciencias',
                        descripcion = 'Este es el departamento de Ciencias',
                        )
    departamento_lista = Departamento.objects.all().values()

    Asignatura.objects.create(
                        nombre = 'Ciencias Sociales',
                        descripcion = 'Esta es la asignatura de Ciencias Sociales',
                        departamentos = Departamento.objects.filter(id=1)[0]
                        )
    asignatura_lista = Asignatura.objects.all().values()
   
    Profesor.objects.create(
                        nombre = 'Gilbert',
                        apellido = 'Lagos',
                        escuela = 'D822',
                        fecha_de_contratacion = '2021-01-02',
                        sueldo = 15000000
                       )
    profesor_lista = Profesor.objects.all().values()


    context =  {'asignatura_lista':asignatura_lista, 'profesor_lista':profesor_lista, 'departamento_lista':departamento_lista}
    return render(request, 'app_individual4m6/asignatura.html', context)

def eliminar_asignatura(request, pk):
    if request.method == 'GET':
        context = {'pk': pk}
        return render(request, 'app_individual4m6/eliminar_asignatura.html', context)

    if request.method == 'POST':
        Asignatura.objects.filter(id=pk).delete()
        return redirect('app_individual4m6:asignatura')

def agregar_asignatura(request):
    #if request.method == 'POST':
    
    formulario = AsignaturaForm()
    context = {'formulario': formulario}
    
    print(formulario)
    return render(request, "app_individual4m6/agregar_asignatura.html", context)

    