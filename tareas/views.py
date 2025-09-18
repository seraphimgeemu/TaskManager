from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import TareaForm
from .models import Tarea
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.
# def signup(request):
# return HttpResponse("<h1>Hello, this is the signup page.</h1>")

# Vista para registrar un nuevo usuario
def signup(request):
    # Si el metodo es GET, se muestra el formulario en blanco
    form = UserCreationForm()
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': form})
    else:
        # Si el metodo es POST, se procesa el formulario
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                # Se inicia la sesión del usuario y se redirige a la vista de tareas
                user.save()
                login(request, user)
                return redirect('tarea')
            except IntegrityError:
                return render(request, 'signup.html', {'form': form, 'error': 'Username already exists.'})

        return render(request, 'signup.html', {'form': form, 'error': 'Las contraseñas no coinciden.'})

# Vista para la página de inicio
def home(request):
    return render(request, 'home.html')

# Vista para mostrar las tareas del usuario autenticado @login_required es un decorador que verifica si el usuario está autenticado
@login_required
def tarea(request):
    tareas = Tarea.objects.filter(user=request.user, datecomplete__isnull=True)
    return render(request, 'tarea.html', {'tareas': tareas})

# Vista para mostrar los detalles de una tarea específica y permitir su edición
@login_required
def tarea_detalle(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id, user=request.user)
    if request.method == 'GET':
        form = TareaForm(instance=tarea)
        return render(request, 'tarea_detalle.html', {'tarea': tarea, 'form': form})
    else:
        try:
            form = TareaForm(request.POST, instance=tarea)
            form.save()
            return redirect('tarea')
        except Exception as e:
            print(e)
            return render(request, 'tarea_detalle.html', {'tarea': tarea, 'form': form})

# Vista para mostrar las tareas completadas del usuario autenticado
@login_required
def tareas_completadas(request):
    tareas = Tarea.objects.filter(
        user=request.user, datecomplete__isnull=False)
    return render(request, 'tareas_completas.html', {'tareas': tareas})

# Vista para marcar una tarea como completada
@login_required
def tarea_completada(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id, user=request.user)
    if request.method == 'POST':
        tarea.datecomplete = timezone.now()
        tarea.save()
        return redirect('tarea')

# Vista para eliminar una tarea
@login_required
def tarea_eliminar(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id, user=request.user)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tarea')

# Vista para crear una nueva tarea
@login_required
def create_tarea(request):
    if request.method == 'GET':
        return render(request, 'crear_tareas.html', {'form': TareaForm})

    else:
        try:
            form = TareaForm(request.POST)
            new_tarea = form.save(commit=False)
            new_tarea.user = request.user
            new_tarea.save()
            return redirect('tarea')
        except Exception as e:
            print(e)
            return render(request, 'crear_tareas.html', {'form': TareaForm})

# Vista para cerrar sesión
@login_required
def signout(request):
    logout(request)
    return redirect('home')

# Vista para iniciar sesión
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            return render(request, 'signin.html', {'form': AuthenticationForm, 'error': 'Username or password is incorrect.'})
        login(request, user)
        return redirect('tarea')

# Vista para renderizar el template de crear tarea
def crear_tarea(request):
    return render(request, 'crear_tareas.html')
