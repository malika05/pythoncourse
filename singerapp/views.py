from singerapp.models import *
from singerapp.serializers import *
from rest_framework import generics
from rest_framework.response import Response
from django.http import Http404
import re

class LabelsView(generics.ListCreateAPIView):
    queryset = Labels.objects.all()
    serializer_class = LabelsSerializer
    def get(self, request):
        return Response('You cannot see this')

class LabelsDetailView(generics.ListAPIView):
    def get_object(self, pk):
        try:
            return Labels.objects.get(pk=pk)
        except Labels.DoesNoExist:
            raise Http404

    def get(self, request, pk, format = None):
        snippet = self.get_object(pk)
        serializer = LabelsSerializer(snippet)
        return Response(serializer.data)

class GroupsView(generics.ListCreateAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer

class GroupsDetailView(generics.ListAPIView):
    def get_object(self, pk):
        try:
            return Groups.objects.get(pk=pk)
        except Groups.DoesNoExist:
            raise Http404

    def get(self, request, pk, format = None):
        snippet = self.get_object(pk)
        serializer = GroupsSerializer(snippet)
        return Response(serializer.data)

class FeedbackView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackDetailView(generics.ListAPIView):
    def get_object(self, pk):
        try:
            return Feedback.objects.get(pk=pk)
        except Feedback.DoesNoExist:
            raise Http404

    def get(self, request, pk, format = None):
        snippet = self.get_object(pk)
        serializer = FeedbackSerializer(snippet)
        return Response(serializer.data)

class SingersView(generics.ListCreateAPIView):
    queryset = Singers.objects.all()
    serializer_class = SingersSerializer

class SingersDetailView(generics.ListAPIView):
    def get_object(self, pk):
        try:
            return Singers.objects.get(pk=pk)
        except Singers.DoesNoExist:
            raise Http404

    def get(self, request, pk, format = None):
        snippet = self.get_object(pk)
        serializer = SingersSerializer(snippet)
        return Response(serializer.data)

class Solo_singerView(generics.ListCreateAPIView):
    queryset = Solo_singer.objects.all()
    serializer_class = Solo_singerSerializer

class Solo_singerDetailView(generics.ListAPIView):
    def get_object(self, pk):
        try:
            return Solo_singer.objects.get(pk=pk)
        except Solo_singer.DoesNoExist:
            raise Http404

    def get(self, request, pk, format = None):
        snippet = self.get_object(pk)
        serializer = Solo_singerSerializer(snippet)
        return Response(serializer.data)

