from django.views.generic import ListView, View
from django.shortcuts import redirect, render, get_object_or_404
from .models import Inscrito, Institucion
from .forms import InscritoForm, InstitucionForm

def home(request):
    return render(request, 'index.html')

class InscritoDeleteView(View):
    def post(self, request, *args, **kwargs):
        inscrito = Inscrito.objects.get(pk=self.kwargs['pk'])
        inscrito.delete()
        return redirect('inscritos_list')

class InstitucionDeleteView(View):
    def post(self, request, *args, **kwargs):
        institucion = Institucion.objects.get(pk=self.kwargs['pk'])
        institucion.delete()
        return redirect('institucion_list')

class InscritoListView(ListView):
    model = Inscrito
    template_name = 'inscritos_list.html'

class InscritoListView(ListView):
    model = Inscrito
    template_name = 'inscritos_list.html'
    context_object_name = 'inscritos'

def inscritos_list(request):
    inscritos = Inscrito.objects.all()
    return render(request, 'inscritos_list.html', {'inscritos': inscritos})

def institucion_list_view(request):
    instituciones = Institucion.objects.all()
    return render(request, 'instituciones_list.html', {'instituciones': instituciones})

def institucion_detail_view(request, pk):
    institucion = get_object_or_404(Institucion, pk=pk)
    return render(request, 'instituciones_detail.html', {'institucion': institucion})

def inscripcion(request):
    if request.method == 'POST':
        form = InscritoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inscritos_list')
    else:
        form = InscritoForm()
    return render(request, 'inscripcion.html', {'form': form})

def institucion_create(request):
    if request.method == 'POST':
        form = InstitucionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instituciones_list')
    else:
        form = InstitucionForm()
    return render(request, 'inscripcion_institucion.html', {'form': form})