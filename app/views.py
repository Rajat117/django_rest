from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer


@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def index(request):
    data = '''<html><h1>Django REST APIs<h1>
    <h1><a href = "https://github.com/Rajat117/django_rest/blob/master/Readme.md"> Go To Readme Page </a>
    </h1 ></html >'''
    return Response(data)
