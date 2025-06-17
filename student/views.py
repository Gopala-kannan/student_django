from django.shortcuts import render, redirect
from student.forms import StudentUserForms
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def register(request):
    form = StudentUserForms()
    if request.method == 'POST':
        form = StudentUserForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Use the name of your login URL pattern
        else:
            form = StudentUserForms()
    return render(request, 'student/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')  
        else:
            return render(request, 'student/login.html', {'error': 'Invalid credentials'})
    return render(request, 'student/login.html')


def logout_view(request):
    logout(request)
    return redirect('/login')

def home(request):
    if request.user.is_authenticated:
        return render(request, 'student/home.html')
    else:
        return redirect('login')