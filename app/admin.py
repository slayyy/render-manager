from django.contrib import admin

# Register your models here.

from .models import User, Render, GroupRender
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)

admin.site.register(Render)
admin.site.register(GroupRender)
