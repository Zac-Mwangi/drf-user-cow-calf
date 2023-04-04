from .models import *
from rest_framework import serializers
from django.db.models import fields


class LoginSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('email', 'password')


class AllUsersSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('__all__')


class UsersCowsSerilizer(serializers.ModelSerializer):

    class Meta:
        model = UsersCows
        fields = ('__all__')


class UsersCowsCalvesSerilizer(serializers.ModelSerializer):

    class Meta:
        model = UsersCalves
        fields = ('__all__')