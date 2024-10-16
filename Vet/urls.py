from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("vet/", include("veterinary_clinic.urls")),
    path("admin/", admin.site.urls),
]
