from django.shortcuts import render
from .models import PostImage

# Create your views here.

def HomePageView(request):
    return render(request, "index.html", {"images": PostImage.objects.all()})

def ImageDetailView(request, pk):
    image = PostImage.objects.get(pk=pk)
    return render(request, "image_detail.html", {"image": image})
