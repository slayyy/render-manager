from django.shortcuts import render
from django.http import HttpResponse

from .models import User, Render, GroupRender


from django.contrib.auth.models import Group
from rest_framework import viewsets, permissions
from .serializers import (
    UserSerializer,
    GroupSerializer,
    RenderSerializer,
    GroupRenderSerializer,
)

# Create your views here.

def index(request):
    return render(request, "app/index.html")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = ([permissions.IsAdminUser])

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = ([permissions.IsAdminUser])


class RenderViewSet(viewsets.ModelViewSet):
    queryset = Render.objects.all()
    serializer_class = RenderSerializer


class GroupRenderViewSet(viewsets.ModelViewSet):
    queryset = GroupRender.objects.all()
    serializer_class = GroupRenderSerializer
