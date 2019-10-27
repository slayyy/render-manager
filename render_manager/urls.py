from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"render", views.RenderViewSet)
router.register(r"group-render", views.GroupRenderViewSet)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        # My Urls
        path("", views.index, name="index"),
        path("api/", include(router.urls)),
        path("admin/", admin.site.urls),
        path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    ]
