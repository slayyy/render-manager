from django.contrib.auth.models import User, Group
from .models import Render, GroupRender
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
        

class RenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Render
        fields = "__all__"


class GroupRenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupRender
        fields = "__all__"
