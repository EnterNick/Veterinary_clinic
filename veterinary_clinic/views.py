from django.shortcuts import render
from rest_framework.response import Response

from .models import Services, Person, Settings
from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets
from veterinary_clinic.serializes import GroupSerializer, UserSerializer, IndexSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView


# def index(request):
#     servises_list = Services.objects.order_by("-id")[:5]
#     context = {
#         "servises": servises_list,
#         'settings': Settings.objects.first()
#     }
#     return render(request, "veterinary_clinic/index.html", context)


class IndexView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'veterinary_clinic/index.html'

    def get(self, request):
        servises = Services.objects.all()[:5]
        settings = Settings.objects.first()
        return Response({'servisces': servises, 'settings': settings})


class UserViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
