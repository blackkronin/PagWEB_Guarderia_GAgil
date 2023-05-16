from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate,login
from .forms import CustomUserCreationForm
from .models import Reserva

# Create your views here.

def home(request):
    return render(request, 'core/home.html')



@login_required
def reservar(request):
    reservas = Reserva.objects.all()
    return render(request, 'core/pag-reservar.html', {"reservas":reservas})

def registrarse(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data = request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    return render(request, 'registration/register.html',data)

def registrarReserva(request):
    codigo=request.POST['txtCodigo']
    nomhijo = request.POST['txtNombrehijo']
    rut_hijo = request.POST['numRuthijo']
    fecha_r = request.POST['fechaReserva']
    horas_reservadas = request.POST['horasReservadas']

    reserva = Reserva.objects.create(cod = codigo, nombrehijo = nomhijo, ruthijo = rut_hijo, fecha = fecha_r, horas_reserva = horas_reservadas)
    return redirect('/')