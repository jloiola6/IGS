from django.urls import include, path
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from back.apps.api.views import CollaboratorViewSet, DepartamentViewSet

 
# Definindo o router
router = routers.DefaultRouter()

#
schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="Descrição da API",
    ),
    public=True,
    # permission_classes=[permissions.AllowAny],
)
 
# Definindo a caminho da rota e a viewset que será usada
router.register('collaborator', CollaboratorViewSet)
router.register('departament', DepartamentViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls), name='index'),
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='doc'),
]