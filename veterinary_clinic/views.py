from django.shortcuts import render
from .models import Services


def index(request):
    servises_list = Services.objects.order_by("-id")[:5]
    context = {
        "servises": servises_list,
    }
    return render(request, "veterinary_clinic/index.html", context)
