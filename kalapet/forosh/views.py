from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from forosh.forms import SignUpForm
from django.utils import timezone
from django.views.generic import ListView
from .forms import *
from django.http import HttpResponse


@login_required
def home(request):
    time = timezone.now()
    return render(request, 'home.html', {'time': time})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

class AD(ListView):
    model = Advertisment
    template_name = 'AD.html'

def CreateAD(request):
    if request.method == 'POST':
        form = ADForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ADForm()
    return render(request, 'ADForm.html', {'form': form})

def success(request):
    return HttpResponse('successfuly uploaded')
