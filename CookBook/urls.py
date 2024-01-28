from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(
        title="CookBook",
        default_version="v1",
        description="Your API Description",
    ),
    public=True,
    permission_classes=(AllowAny,),
)


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Apps
    path('api/v1/recipe/', include('recipe.urls'))
]
