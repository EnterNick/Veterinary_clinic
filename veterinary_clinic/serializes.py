from django.contrib.auth.models import Group
from rest_framework import serializers

from veterinary_clinic.models import Person, Services


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