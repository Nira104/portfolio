from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .form import SignupForm, ProfileForm, EducationForm
from .models import Profile, Education

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # create empty profile
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    profile = Profile.objects.get(user=request.user)
    education = Education.objects.filter(user=request.user)
    return render(request, 'accounts/dashboard.html', {'profile': profile, 'education': education})

@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def add_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            edu = form.save(commit=False)
            edu.user = request.user
            edu.save()
            return redirect('dashboard')
    else:
        form = EducationForm()
    return render(request, 'accounts/add_education.html', {'form': form})
