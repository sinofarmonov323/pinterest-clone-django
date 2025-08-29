from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .models import PostImage

# Create your views here.

def HomePageView(request):
    return render(request, "index.html", {"images": PostImage.objects.all(), "user": request.user})

def ImageDetailView(request, pk):
    image = PostImage.objects.get(pk=pk)
    return render(request, "image_detail.html", {"image": image})

def RegisterView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after register
            return redirect("index")  # change 'home' to your desired URL name
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

def LogoutView(request):
    logout(request)
    return redirect("/")
