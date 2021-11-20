from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import coders
from .serializers import CodersSerializer, CodersDetailSerialiser
from django.http import Http404
from rest_framework import status, permissions

class CodersList(APIView):

    # for GET /coders
    def get(self, request):
        coder = coders.objects.all()
        serializer = CodersSerializer(coder, many=True)
        return Response(serializer.data)

    # for POST /coders
    def post(self, request):
        serializer = CodersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(student_ID=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status=status.HTTP_400_BAD_REQUEST
        )

class CodersDetail(APIView):
    
    def get_object(self, pk):
        try:
            coder = coders.objects.get(pk=pk)
            return coder
        except coders.DoesNotExist:
            raise Http404        

    def get(self, request, pk):
        coder = self.get_object(pk)
        serializer = CodersDetailSerialiser(coder)
        return Response(serializer.data)

    def put(self, request, pk):
        coder = self.get_object(pk)
        data = request.data
        serializer = CodersDetailSerialiser(
            instance=coder,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        coder = self.get_object(pk)
        coder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
