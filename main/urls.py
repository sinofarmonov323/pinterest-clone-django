from django.urls import path, include
from .views import HomePageView, ImageDetailView, RegisterView, LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", HomePageView, name='index'),
    path("accounts/logout/", LogoutView, name='logout'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", RegisterView, name='register'),
    path("image/<int:pk>/", ImageDetailView, name='image_detail'),
] + static(settings.MEDIA_URL, document_root=".")
