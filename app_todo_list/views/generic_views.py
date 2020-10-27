from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from django.http import Http404, HttpResponse
from rest_framework.settings import api_settings
# from django.contrib.auth.models import User
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView


class GenericList(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    def post(self, request, format=None):
        data = request.data.dict()
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class GenericDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    def get_object(self, pk):
        try:
            main_object = self.model.objects.get(pk=pk)
            return main_object
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        main_object = self.get_object(pk)
        serializer = self.serializer_class(main_object)
        return Response(serializer.data)

    def put(self, request, pk):
        main_object = self.get_object(pk)
        data = request.data.dict()
        serializer = self.serializer_class(main_object, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=HTTP_204_NO_CONTENT)
