"""
URL configuration for quezada_fabian_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from seminario_app.views import home, InscritoListView, institucion_list_view, inscripcion, InscritoDeleteView, institucion_create, InstitucionDeleteView


urlpatterns = [
    path('', home, name='home'),
    path('inscritos/', InscritoListView.as_view(), name='inscritos_list'),
    path('instituciones/', institucion_list_view, name='instituciones_list'),
    path('inscripcion/', inscripcion, name='inscripcion'),
    path('inscrito_delete/<int:pk>/', InscritoDeleteView.as_view(), name='inscrito_delete'),
    path('institucion_delete/<int:pk>/', InstitucionDeleteView.as_view(), name='institucion_delete'),
    path('inscripcion_institucion/', institucion_create, name='inscripcion_institucion'),
]