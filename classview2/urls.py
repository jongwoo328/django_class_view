from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


yasg_view = get_schema_view(
    openapi.Info(
        title="TEST API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="jongwoo328@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/signup/', include('rest_auth.registration.urls')),

    path('admin/', admin.site.urls),
    path('swagger/', yasg_view.with_ui('swagger', cache_timeout=0)),
    path('api/articles/', include('articles.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/images/', include('images.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
