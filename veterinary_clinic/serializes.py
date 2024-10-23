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
    date = serializers.DateField(style={'template': 'custom_fields/input.html'})

    class Meta:
        model = Request
        fields = ['name', 'pet_name', 'service', 'email', 'time', 'date']

    def validate_date(self, val):
        if val < datetime.date.today():
            print('true')
            raise serializers.ValidationError
        return val

    def validate_time(self, val):
        if val < datetime.datetime.now().time():
            raise serializers.ValidationError
        return val
