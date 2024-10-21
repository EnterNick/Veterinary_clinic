import datetime

from django.contrib.auth.models import Group
from rest_framework import serializers

from veterinary_clinic.models import Person, Services, Request


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['url', 'username', 'email', 'groups', 'role']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class IndexSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Services
        fields = ['name', 'description', 'vet']


class MakeRequestSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(
        max_length=100,
        style={'template': 'custom_fields/input.html', 'placeholder': 'Ваше имя и фамилия'}
    )
    pet_name = serializers.CharField(max_length=100, style={'placeholder': 'Имя вашего любимца :)',
                                                            'template': 'custom_fields/input.html'})
    service = serializers.ChoiceField([*Services.objects.all()], style={'template': 'custom_fields/choice.html'})
    email = serializers.EmailField(max_length=100, style={'placeholder': 'Email',
                                                          'template': 'custom_fields/input.html'})
    time = serializers.TimeField(style={'template': 'custom_fields/input.html'})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.style)

    class Meta:
        model = Request
        fields = ['name', 'pet_name', 'service', 'email', 'time']
