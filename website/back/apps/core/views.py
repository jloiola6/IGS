from django.template.response import TemplateResponse

from back.apps.core.action import check_superuser
from back.apps.core.models import Collaborator


# Create your views here.


def index(request):
    template_name = 'index.html'
    
    user = check_superuser()
    
    queryset = Collaborator.objects.all()
    
    return TemplateResponse(request, template_name, locals())