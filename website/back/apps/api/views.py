from rest_framework import viewsets

from back.apps.api.serializers import CollaboratorSerializer, DepartamentSerializer
from back.apps.core.models import Collaborator, Departament
 
 
class DepartamentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartamentSerializer
    queryset = Departament.objects.all()

    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'put', 'delete']


class CollaboratorViewSet(viewsets.ModelViewSet):
    serializer_class = CollaboratorSerializer
    queryset = Collaborator.objects.all()

    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'put', 'delete']
