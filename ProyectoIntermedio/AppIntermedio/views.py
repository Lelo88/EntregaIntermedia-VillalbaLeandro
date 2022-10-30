from django.shortcuts import render, redirect
from .models import Sector, Lector, Libro
from django.http import HttpResponse
from .forms import Sectores, Lectores, Libros

# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def libros(request):
    
    libro = Libro.objects.all()
    
    return render(request, 'listado_libros.html',{'lista_libros': libro})

def sectores(request):
    
    sector = Sector.objects.all()

    return render(request, 'listado_sectores.html', {'lista_sectores': sector})

def lectores(request):
    
    lector = Lector.objects.all()
    
    return render(request, 'listado_lectores.html', {'lista_lectores': lector})

def form_libros(request):
    
    if request.method == "POST":
        libros = Libros(request.POST)
        
        if libros.is_valid():
            info_libros = libros.cleaned_data
            libro = Libro(titulo=info_libros['titulo'], sinopsis=info_libros['sinopsis'], autor=info_libros['autor'])
            libro.save()
            
            return redirect('ListadoLibros')
        
    else:
        libros = Libros()
    
    return render(request, 'formularioLibros.html', {'libros': libros})

def form_sectores(request):
    
    if request.method=='POST': 
        sectores = Sectores(request.POST)
        
        if sectores.is_valid():
            info_sectores = sectores.cleaned_data
            sector = Sector(color=info_sectores['color'], nombre=info_sectores['nombre'], cupo=info_sectores['cupo'])
            sector. save()
            
            return redirect('ListadoSectores')

    else:
        sectores = Sectores()
        
    return render(request, 'formularioSectores.html',{'sectores': sectores})

def form_lectores(request):
    
    if request.method == 'POST':
        lectores = Lectores(request.POST)
        
        if lectores.is_valid():
            info_lectores = lectores.cleaned_data
            lector = Lector(nombre=info_lectores['nombre'], apellido=info_lectores['apellido'], fecha_nac=info_lectores['fecha_nac'])
            lector.save()
            
            return redirect('ListadoLectores')
    
    else:
        lectores = Lectores()
        
    return render(request, 'formularioLectores.html', {'lectores': lectores})

def muestra_libros(request):
    
    libros = Libro.objects.all()
    
    return render(request, 'muestra_libros.html',{'listado_Libros': libros})

def muestra_sectores(request):
    
    sectores = Sector.objects.all()
    
    return render(request, 'muestra_sectores.html', {'listado_sectores': sectores})

def muestra_lectores(request):
    
    lectores = Lector.objects.all()
    
    return render(request, 'muestra_lectores.html', {'listado_lectores': lectores})