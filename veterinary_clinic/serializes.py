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


class MakeRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    pet_name = serializers.CharField(max_length=100)
    service = serializers.ChoiceField([*Services.objects.all()])
