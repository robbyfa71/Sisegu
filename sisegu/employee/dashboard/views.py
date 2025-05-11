from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def login_view(request):
    error_message = None
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    if request.method == 'POST':
        authform = AuthenticationForm(request, data=request.POST)
        if authform.is_valid():
            login(request, authform.get_user())
            next_url = request.GET.get('next')
            return redirect(next_url)
        else:
            error_message = 'Username atau password yang anda masukkan salah!'
    else:
        authform = AuthenticationForm()
    return render(request,'employee/login.html',{'form':authform, 'error':error_message})


@login_required
def index_view(request):
    return render(request, 'employee/dashboard/index.html',{})


def logout_view(request):
    logout(request)
    return redirect('dashboard:login')
