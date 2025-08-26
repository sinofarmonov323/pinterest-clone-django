from django.urls import path
from .views import HomePageView, ImageDetailView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", HomePageView, name='index'),
    path("image/<int:pk>/", ImageDetailView, name='image_detail'),
] + static(settings.MEDIA_URL, document_root=".")
