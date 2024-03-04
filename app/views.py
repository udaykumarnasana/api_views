from django.shortcuts import render

# Create your views here.

from app.models import *
from app.serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated



@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def schooljsondata(request):
    sod=School.objects.all()
    jod= SchoolModelSerializer(sod,many=True)
    jsondata=jod.data
    return Response(jsondata)
