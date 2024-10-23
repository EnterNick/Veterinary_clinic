import datetime

import rest_framework.permissions
from django.db.models import CharField
from django.shortcuts import redirect
from rest_framework.response import Response

from .models import Services, Person, Settings, Request
from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets, serializers
from veterinary_clinic.serializes import GroupSerializer, UserSerializer, MakeRequestSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView


class IndexView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'veterinary_clinic/index.html'

    def get(self, request):
        services = Services.objects.all()[:5]
        settings = Settings.objects.first()
        return Response({'services': services, 'settings': settings})


class UserViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class MakeRequestView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'veterinary_clinic/make_request_form.html'
    queryset = Request.objects.all()

    def get(self, request):
        serializer = MakeRequestSerializer(context={'request': request})
        settings = Settings.objects.first()
        return Response({'serializer': serializer, 'settings': settings})

    def post(self, request):
        serializer = MakeRequestSerializer(data=request.data, context={'request': request})
        settings = Settings.objects.first()
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'settings': settings})
        serializer.save()
        return redirect('/')
