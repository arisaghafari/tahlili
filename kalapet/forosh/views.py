from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from forosh.forms import SignUpForm
from django.utils import timezone
from django.views.generic import ListView, CreateView
from .models import Advertisment
from django.urls import reverse_lazy
from .forms import ADForm

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

class CreateADView(CreateView):
    model = Advertisment
    form_class = ADForm
    template_name = 'ADForm.html'
    success_url = reverse_lazy('advertisment')
