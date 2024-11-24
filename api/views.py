from django.shortcuts import render
from .serializers import StatusSerializer
from .models import MNStatus
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .telegram_noti import check_alert
import asyncio, logging

logger = logging.getLogger('django')

# @api_view(['GET', 'PUT', 'DELETE'])
@api_view(['PUT'])
def status_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
   
    try:
        mnstatus = MNStatus.objects.get(id=pk)
    except MNStatus.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # if request.method == 'GET':
    #     # serializer = StatusSerializer(mnstatus)
    #     # return Response(serializer.data)

    # elif request.method == 'PUT':
    if request.method == 'PUT':

        serializer = StatusSerializer(mnstatus, data = request.data)

        if serializer.is_valid():
            serializer.save()
            
            # logger.info(serializer.data.get("Volt"))
            check_alert(serializer.data.get("id"),serializer.data.get("Temp"),serializer.data.get("Humi"),serializer.data.get("Volt"))

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     mnstatus.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
