from django.shortcuts import render
from .models import Services, Person, Settings
from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets
from veterinary_clinic.serializes import GroupSerializer, UserSerializer, IndexSerializer


def index(request):
    servises_list = Services.objects.order_by("-id")[:5]
    context = {
        "servises": servises_list,
        'settings': Settings.objects.first()
    }
    return render(request, "veterinary_clinic/index.html", context)


class UserViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
