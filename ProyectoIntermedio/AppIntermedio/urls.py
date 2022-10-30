from django.urls import path

from .views import form_lectores, form_libros, form_sectores, inicio, lectores, libros, muestra_lectores, muestra_libros, muestra_sectores, sectores

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('formulario-libros/', form_libros, name='FormularioLibros'),
    path('formulario-sectores/', form_sectores, name='FormularioSectores'),
    path('formulario-lectores/', form_lectores, name='FormularioLectores'),
    path('listado-libros/', muestra_libros, name='MuestraLibro'),
    path('listado-sectores/', muestra_sectores, name='MuestraSector'),
    path('listado-lectores/', muestra_lectores, name='MuestraLector'),
    path('vista-libros/', libros, name='ListadoLibros'),
    path('vista-sectores/', sectores, name='ListadoSectores'),
    path('vista-lectores/', lectores, name='ListadoLectores'),
]