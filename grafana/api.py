from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from .models import DashboardDefaultTemplate
from .serializers import DashboardSerializer
import logging


logger = logging.getLogger(__name__)


@api_view(["GET"])
def dashboard_template(request, template_name):
    default_template = get_object_or_404(
        DashboardDefaultTemplate,
        name=template_name)
    serializer = DashboardSerializer(data={
        "model": default_template.data,
        "meta": {"slug": "", "isHome": template_name == "home"}
        })
    if serializer.is_valid():
        return Response(data=serializer.data)
    else:
        logger.warning(
            "Default template `%s` isn't valid. Errors - %s",
            template_name,
            serializer.errors)
        return Response(status=HTTP_400_BAD_REQUEST)
