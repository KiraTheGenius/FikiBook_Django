from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, ProfileForm


def signup(response):
    form = SignUpForm()
    if response.method == "POST":
        form = SignUpForm(response.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if instance.is_publisher:
                instance.is_superuser = True
            instance.save()
            return redirect('home')
    else:
        form = SignUpForm()

    return render(response, "registration/signup.html", {"form": form})


@login_required(login_url='/login/')
def home(response):
    return render(response, "home.html")


@login_required(login_url='/login/')
def profile(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProfileForm(instance=request.user)

    return render(request, "registration/profile.html", {"form": form})