from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import UserAdminCreationForm

def register(req):
    form = UserAdminCreationForm()   # UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        return redirect('login')
        if form.is_valid():
            form.save()
            return redirect('register')
    return render(req, 'register.html', {'form': form})